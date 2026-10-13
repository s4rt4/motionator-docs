"""Build the Motionator user guide.

    python build.py [path/to/motionator]

Writes index.html (bilingual, with search) and print-en.html / print-id.html (one language each,
for the PDFs). Preset and shortcut tables are read from the app's source, so they stay accurate.
"""
import html
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
APP = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "motionator")
VERSION = "0.1.0"


# ---------------------------------------------------------------- data from the app source


def read(rel):
    return io.open(os.path.join(APP, rel), encoding="utf-8").read()


def presets():
    s = read("crates/motion_core/src/presets.rs")
    body = s[s.index("fn build()") : s.index("fn slide_out")]
    pat = re.compile(r'(def|slide|slide_out)\(\s*"([a-z_.0-9]+)",\s*"([^"]+)",\s*(?:Category::(\w+),\s*)?t\("([^"]*)",\s*"([^"]*)"\)', re.S)
    out = []
    for kind, pid, name, cat, d_id, d_en in pat.findall(body):
        cat = cat or ("Enter" if kind == "slide" else "Exit")
        out.append({"id": pid, "name": name, "cat": cat.lower(), "en": d_en, "idn": d_id})
    order = {"enter": 0, "exit": 1, "loop": 2, "emphasis": 3}
    out.sort(key=lambda p: order[p["cat"]])
    return out


def shortcuts():
    r = read("src/commands/registry.ts")
    r = r[r.index("export const COMMANDS") : r.index("function withLayer")]
    ents = re.findall(r'id: "([\w.]+)",\s*label: \["([^"]+)", "([^"]+)"\](.*?)(?=\n  \{|\n  tool\(|\n  \.\.\.|\n\];|\n  //)', r, re.S)
    out = []
    for cid, l_id, l_en, rest in ents:
        if "later(" in rest:
            continue
        m = re.search(r"shortcuts: \[(.*?)\]", rest)
        if not m:
            continue
        keys = re.findall(r'"([^"]*)"', m.group(1))
        out.append((cid, l_en, l_id, keys))
    for tid, name, key in re.findall(r'tool\("(\w+)", "([^"]+)", "([^"]+)"', r):
        out.append((f"tool.{tid}", name, name, [key]))
    return out


# ---------------------------------------------------------------- content blocks


def B(en, idn):
    return {"en": en, "id": idn}


class Doc:
    def __init__(self):
        self.sections = []

    def section(self, sid, group, title, lead=None):
        s = {"id": sid, "group": group, "title": title, "lead": lead, "blocks": []}
        self.sections.append(s)
        return s["blocks"]


def kbd(s):
    """'Ctrl+Shift+Z' → <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Z</kbd>"""
    names = {"ArrowLeft": "←", "ArrowRight": "→", "PageUp": "Page Up", "PageDown": "Page Down"}
    if s == "+":
        return "<kbd>+</kbd>"
    parts = s.split("+") if s != "Shift+/" else ["Shift", "/"]
    return "+".join(f"<kbd>{html.escape(names.get(p, p))}</kbd>" for p in parts if p)


def inline(text):
    """Light markup: [[Ctrl+S]] → keys."""
    return re.sub(r"\[\[([^\]]+)\]\]", lambda m: " / ".join(kbd(k.strip()) for k in m.group(1).split("|")), text)


def both(pair, tag="span", attrs=""):
    return f'<{tag} lang="en"{attrs}>{inline(pair["en"])}</{tag}><{tag} lang="id"{attrs}>{inline(pair["id"])}</{tag}>'


def one(pair, lang):
    return inline(pair[lang])


class Renderer:
    """Renders blocks for 'both' (the web page) or one language (print)."""

    def __init__(self, lang=None):
        self.lang = lang

    def t(self, pair, tag="span", attrs=""):
        if self.lang:
            return f"<{tag}{attrs}>{one(pair, self.lang)}</{tag}>" if tag != "span" or attrs else one(pair, self.lang)
        return both(pair, tag, attrs)

    def img_src(self, name, lang):
        return f"img/{lang}/{name}.png"

    def block(self, b):
        k = b["k"]
        if k == "p":
            return self.t(b["v"], "p")
        if k == "h3":
            return f'<h3 id="{b["id"]}">{self.t(b["v"])}<a class="anchor" href="#{b["id"]}">#</a></h3>'
        if k == "h4":
            return f"<h4>{self.t(b['v'])}</h4>"
        if k == "list":
            items = "".join(self.t(i, "li") for i in b["items"])
            return f"<ul>{items}</ul>"
        if k == "steps":
            items = "".join(f"<li>{self.t(i, 'div')}</li>" for i in b["items"])
            return f'<ol class="steps">{items}</ol>'
        if k == "callout":
            label = {"tip": B("Tip", "Tips"), "note": B("Note", "Catatan"), "warn": B("Important", "Penting")}[b["kind"]]
            return f'<div class="callout {b["kind"]}">{self.t(label, "span", " class=\"t\"")}{self.t(b["v"], "p")}</div>'
        if k == "img":
            cls = f' class="{b["size"]}"' if b.get("size") else ""
            pins = "".join(f'<span class="pin" style="left:{x}%;top:{y}%">{n}</span>' for n, x, y in b.get("pins", []))
            langs = [self.lang] if self.lang else ["en", "id"]
            if b.get("shared"):
                imgs = f'<img src="img/{b["name"]}.png" alt="" loading="{self.loading()}">'
                return f'<figure{cls}><div class="shot">{imgs}{pins}</div><figcaption>{self.t(b["cap"])}</figcaption></figure>'
            figs = []
            for lg in langs:
                alt = html.escape(re.sub("<[^>]+>", "", b["cap"][lg]))
                lattr = "" if self.lang else f' lang="{lg}"'
                figs.append(f'<figure{cls}{lattr}><div class="shot"><img src="{self.img_src(b["name"], lg)}" alt="{alt}" loading="{self.loading()}">{pins}</div><figcaption>{inline(b["cap"][lg])}</figcaption></figure>')
            return "".join(figs)
        if k == "legend":
            items = "".join(f'<li><b class="n">{n}</b><span>{self.t(v)}</span></li>' for n, v in b["items"])
            return f'<ul class="legend">{items}</ul>'
        if k == "strip":
            cells = "".join(f'<div><img src="img/anim/{b["name"]}-{i}.png" alt="" loading="{self.loading()}"><span>{t}</span></div>' for i, t in enumerate(b["times"]))
            return f'<div class="strip">{cells}</div>' + (self.t(b["cap"], "p", ' class="lead" style="font-size:14px"') if b.get("cap") else "")
        if k == "table":
            head = "".join(f"<th>{self.t(h) if isinstance(h, dict) else h}</th>" for h in b["head"])
            rows = ""
            for r in b["rows"]:
                rows += "<tr>" + "".join(f"<td>{self.t(c) if isinstance(c, dict) else inline(c)}</td>" for c in r) + "</tr>"
            return f'<div class="table-wrap"><table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>'
        if k == "cards":
            cards = "".join(f'<div class="card"><span class="ico">{ico}</span><h4>{self.t(t)}</h4>{self.t(d, "p")}</div>' for ico, t, d in b["items"])
            return f'<div class="cards">{cards}</div>'
        if k == "code":
            return f"<pre><code>{html.escape(b['v'])}</code></pre>"
        if k == "diagram":
            if self.lang:
                return f'<div class="diagram">{b["v"][self.lang]}</div>'
            return f'<div class="diagram" lang="en">{b["v"]["en"]}</div><div class="diagram" lang="id">{b["v"]["id"]}</div>'
        if k == "raw":
            return b["v"]
        raise ValueError(k)

    def loading(self):
        return "eager" if self.lang else "lazy"


# block constructors used by content.py
def P(en, idn):
    return {"k": "p", "v": B(en, idn)}


def H3(hid, en, idn):
    return {"k": "h3", "id": hid, "v": B(en, idn)}


def H4(en, idn):
    return {"k": "h4", "v": B(en, idn)}


def UL(*items):
    return {"k": "list", "items": [B(e, i) for e, i in items]}


def STEPS(*items):
    return {"k": "steps", "items": [B(e, i) for e, i in items]}


def TIP(en, idn):
    return {"k": "callout", "kind": "tip", "v": B(en, idn)}


def NOTE(en, idn):
    return {"k": "callout", "kind": "note", "v": B(en, idn)}


def WARN(en, idn):
    return {"k": "callout", "kind": "warn", "v": B(en, idn)}


def IMG(name, en, idn, size=None, pins=None, shared=False):
    return {"k": "img", "name": name, "cap": B(en, idn), "size": size, "pins": pins or [], "shared": shared}


def LEGEND(*items):
    return {"k": "legend", "items": [(n, B(e, i)) for n, e, i in items]}


def STRIP(name, times, en=None, idn=None):
    return {"k": "strip", "name": name, "times": times, "cap": B(en, idn) if en else None}


def TABLE(head, rows):
    return {"k": "table", "head": head, "rows": rows}


def CARDS(*items):
    return {"k": "cards", "items": [(ico, B(te, ti), B(de, di)) for ico, te, ti, de, di in items]}


def CODE(v):
    return {"k": "code", "v": v}


def DIAGRAM(en, idn=None):
    return {"k": "diagram", "v": B(en, idn if idn is not None else en)}


def RAW(v):
    return {"k": "raw", "v": v}


# ---------------------------------------------------------------- page assembly

ICON_SEARCH = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>'
ICON_THEME = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/></svg>'
ICON_MENU = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 6h16M4 12h16M4 18h16"/></svg>'


def head(title, extra=""):
    return f"""<!doctype html>
<html lang="en" data-lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="Motionator user guide: animate SVG without code, export 4K video, Lottie and animated SVG. Panduan lengkap Motionator dalam bahasa Inggris dan Indonesia.">
<link rel="icon" href="img/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
{extra}
</head>
"""


def build_web(doc):
    r = Renderer()
    nav, groups, body = [], None, []
    for n, s in enumerate(doc.sections):
        if s["group"] and s["group"] != groups:
            groups = s["group"]
            nav.append(f'<div class="group">{both(s["group"])}</div>')
        nav.append(f'<a href="#{s["id"]}">{both(s["title"])}</a>')
        blocks = "".join(r.block(b) for b in s["blocks"])
        lead = r.t(s["lead"], "p", ' class="lead"') if s["lead"] else ""
        num = f'<span class="num">{n:02d}</span>' if s["id"] != "welcome" else ""
        hero = HERO if s["id"] == "welcome" else ""
        title = "" if s["id"] == "welcome" else f'<h2>{num}{both(s["title"])}<a class="anchor" href="#{s["id"]}">#</a></h2>'
        body.append(f'<section class="doc" id="{s["id"]}">{hero}{title}{lead}{blocks}</section>')
    downloads = f"""<div class="downloads">
<b>{both(B("Downloads", "Unduhan"))}</b>
<a href="pdf/Motionator-User-Guide-EN.pdf">📄 {both(B("User guide (PDF, English)", "Panduan (PDF, English)"))}</a>
<a href="pdf/Motionator-Panduan-ID.pdf">📄 {both(B("Panduan (PDF, Indonesian)", "Panduan (PDF, Indonesia)"))}</a>
<a href="samples/">🗂️ {both(B("Sample files", "File contoh"))}</a>
</div>"""
    page = head("Motionator User Guide") + f"""<body>
<header class="topbar">
  <button class="icon-btn menu-btn" id="menu" aria-label="Menu">{ICON_MENU}</button>
  <a class="brand" href="#welcome"><img src="img/logo.png" alt=""><span>Motionator <small>{both(B("User Guide", "Panduan"))} · v{VERSION}</small></span></a>
  <div class="search">{ICON_SEARCH}<input id="q" type="search" autocomplete="off" placeholder="Search topics… (press /)"><span class="hint"><kbd>/</kbd></span><div class="results" id="results"></div></div>
  <div class="tools">
    <div class="seg" role="group" aria-label="Language"><button data-set-lang="en">EN</button><button data-set-lang="id">ID</button></div>
    <button class="icon-btn" id="theme" aria-label="Theme">{ICON_THEME}</button>
  </div>
</header>
<nav class="sidebar">{''.join(nav)}{downloads}</nav>
<main><div class="content">
{''.join(body)}
<div class="footer">{both(B(FOOTER_EN, FOOTER_ID))}</div>
</div></main>
<div class="lightbox" id="lightbox"><img alt=""></div>
<script src="assets/app.js"></script>
</body></html>"""
    io.open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)


def build_print(doc, lang):
    r = Renderer(lang)
    t = lambda p: one(p, lang)
    title = t(B("User Guide", "Panduan Pengguna"))
    cover = f"""<div class="cover"><img src="img/logo.png" alt=""><div class="band"></div><h1>Motionator</h1><p>{title}</p>
<p style="margin-top:10px">{t(B("Animate SVG without code — 4K video, Lottie and animated SVG", "Animasikan SVG tanpa coding — video 4K, Lottie, dan SVG animasi"))}</p>
<div class="meta">{t(B("Version", "Versi"))} {VERSION} · {t(B("Online version", "Versi online"))}: s4rt4.github.io/motionator-docs</div></div>"""
    toc = "".join(f"<li>{t(s['title'])}</li>" for s in doc.sections if s["id"] != "welcome")
    body = []
    for n, s in enumerate(doc.sections):
        if s["id"] == "welcome":
            blocks = "".join(r.block(b) for b in s["blocks"])
            body.append(f'<section class="doc" id="{s["id"]}"><h2>{t(B("Welcome", "Selamat datang"))}</h2>{blocks}</section>')
            continue
        blocks = "".join(r.block(b) for b in s["blocks"])
        lead = r.t(s["lead"], "p", ' class="lead"') if s["lead"] else ""
        body.append(f'<section class="doc" id="{s["id"]}"><h2><span class="num">{n:02d}</span>{t(s["title"])}</h2>{lead}{blocks}</section>')
    page = head(f"Motionator — {title}").replace('data-lang="en"', f'data-lang="{lang}"').replace('lang="en"', f'lang="{lang}"', 1) + f"""<body>
<main><div class="content">{cover}<div class="print-toc"><h2>{t(B("Contents", "Daftar isi"))}</h2><ol>{toc}</ol></div>{''.join(body)}
<div class="footer">{t(B(FOOTER_EN, FOOTER_ID))}</div></div></main></body></html>"""
    io.open(os.path.join(HERE, f"print-{lang}.html"), "w", encoding="utf-8").write(page)


FOOTER_EN = f"Motionator {VERSION} · This guide uses screenshots of the real app and the sample files in <code>samples/</code>. FFmpeg (GPL v3) ships with the installer as a separate program."
FOOTER_ID = f"Motionator {VERSION} · Panduan ini memakai screenshot aplikasi asli dan file contoh di <code>samples/</code>. FFmpeg (GPL v3) disertakan installer sebagai program terpisah."

HERO = ""

if __name__ == "__main__":
    sys.path.insert(0, HERE)
    import content

    HERO = content.HERO
    doc = content.build(Doc(), presets(), shortcuts())
    build_web(doc)
    build_print(doc, "en")
    build_print(doc, "id")
    print(f"{len(doc.sections)} sections written")
