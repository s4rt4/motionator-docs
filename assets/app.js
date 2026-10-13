// Motionator user guide: language switch, theme, topic search, scroll spy, lightbox.
(() => {
  const root = document.documentElement;
  const store = {
    get: (k) => {
      try {
        return localStorage.getItem(k);
      } catch {
        return null;
      }
    },
    set: (k, v) => {
      try {
        localStorage.setItem(k, v);
      } catch {
        /* private mode: not remembered */
      }
    },
  };

  // ---- language ----
  const params = new URLSearchParams(location.search);
  const guess = (navigator.language || "en").toLowerCase().startsWith("id") ? "id" : "en";
  let lang = params.get("lang") || store.get("mguide.lang") || guess;
  const setLang = (l) => {
    lang = l === "id" ? "id" : "en";
    root.dataset.lang = lang;
    root.lang = lang;
    store.set("mguide.lang", lang);
    document.querySelectorAll("[data-set-lang]").forEach((b) => b.classList.toggle("on", b.dataset.setLang === lang));
    const input = document.getElementById("q");
    if (input) input.placeholder = lang === "id" ? "Cari topik… (tekan /)" : "Search topics… (press /)";
    document.title = lang === "id" ? "Panduan Motionator" : "Motionator User Guide";
    buildIndex();
    if (input && input.value) search(input.value);
  };
  document.querySelectorAll("[data-set-lang]").forEach((b) => b.addEventListener("click", () => setLang(b.dataset.setLang)));

  // ---- theme ----
  const themeBtn = document.getElementById("theme");
  const savedTheme = store.get("mguide.theme");
  if (savedTheme) root.dataset.theme = savedTheme;
  themeBtn?.addEventListener("click", () => {
    const dark = root.dataset.theme ? root.dataset.theme === "dark" : matchMedia("(prefers-color-scheme: dark)").matches;
    root.dataset.theme = dark ? "light" : "dark";
    store.set("mguide.theme", root.dataset.theme);
  });

  // ---- mobile nav ----
  document.getElementById("menu")?.addEventListener("click", () => document.body.classList.toggle("nav-open"));
  document.querySelectorAll(".sidebar a").forEach((a) => a.addEventListener("click", () => document.body.classList.remove("nav-open")));

  // ---- search ----
  // One entry per section and sub-heading, with the text of the current language under it.
  let index = [];
  const visibleText = (el) => {
    const clone = el.cloneNode(true);
    clone.querySelectorAll(`[lang]:not([lang="${lang}"])`).forEach((n) => n.remove());
    clone.querySelectorAll("svg, script, style, .anchor, .num").forEach((n) => n.remove());
    // Block elements end a word: keep table cells and list items apart in the snippet.
    clone.querySelectorAll("p, li, td, th, div, dt, dd, h3, h4, figcaption, .times span").forEach((n) => n.append(" "));
    return clone.textContent.replace(/\s+/g, " ").trim();
  };
  function buildIndex() {
    index = [];
    document.querySelectorAll("section.doc").forEach((sec) => {
      const h2 = sec.querySelector("h2");
      const secTitle = h2 ? visibleText(h2) : "";
      let current = { id: sec.id, title: secTitle, path: "", text: "" };
      index.push(current);
      for (const el of sec.children) {
        if (el.tagName === "H3" && el.id) {
          current = { id: el.id, title: visibleText(el), path: secTitle, text: "" };
          index.push(current);
        } else if (el.tagName !== "H2") {
          current.text += " " + visibleText(el);
        }
      }
    });
  }
  const norm = (s) => s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "");
  const esc = (s) => s.replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);
  const input = document.getElementById("q");
  const box = document.getElementById("results");
  let active = -1;
  function search(q) {
    const words = norm(q).split(/\s+/).filter((w) => w.length > 1);
    if (!words.length) {
      box.classList.remove("open");
      return;
    }
    const hits = [];
    for (const e of index) {
      const t = norm(e.title);
      const body = norm(e.text);
      let score = 0;
      for (const w of words) {
        if (t.includes(w)) score += 10;
        const c = body.split(w).length - 1;
        if (c) score += Math.min(c, 5);
        else if (!t.includes(w)) {
          score = 0;
          break;
        }
      }
      if (score) hits.push({ e, score });
    }
    hits.sort((a, b) => b.score - a.score);
    if (!hits.length) {
      box.innerHTML = `<div class="empty">${lang === "id" ? "Tidak ada hasil untuk" : "No results for"} “${esc(q)}”</div>`;
      box.classList.add("open");
      return;
    }
    const mark = (s) => {
      let out = esc(s);
      for (const w of words) out = out.replace(new RegExp(`(${w.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")})`, "gi"), "<mark>$1</mark>");
      return out;
    };
    box.innerHTML = hits
      .slice(0, 12)
      .map(({ e }) => {
        const body = e.text;
        const i = norm(body).indexOf(words[0]);
        const snip = i >= 0 ? (i > 50 ? "…" : "") + body.slice(Math.max(0, i - 50), i + 110) + "…" : body.slice(0, 140) + "…";
        return `<a href="#${e.id}"><div class="r-title">${mark(e.title)}</div>${e.path ? `<div class="r-path">${esc(e.path)}</div>` : ""}<div class="r-snip">${mark(snip)}</div></a>`;
      })
      .join("");
    active = -1;
    box.classList.add("open");
  }
  input?.addEventListener("input", () => search(input.value));
  input?.addEventListener("keydown", (ev) => {
    const links = [...box.querySelectorAll("a")];
    if (ev.key === "ArrowDown" || ev.key === "ArrowUp") {
      ev.preventDefault();
      active = (active + (ev.key === "ArrowDown" ? 1 : -1) + links.length) % links.length;
      links.forEach((l, i) => l.classList.toggle("active", i === active));
      links[active]?.scrollIntoView({ block: "nearest" });
    } else if (ev.key === "Enter") {
      (links[active] || links[0])?.click();
    } else if (ev.key === "Escape") {
      box.classList.remove("open");
      input.blur();
    }
  });
  box?.addEventListener("click", (ev) => {
    if (ev.target.closest("a")) {
      box.classList.remove("open");
      input.value = "";
    }
  });
  document.addEventListener("click", (ev) => {
    if (!ev.target.closest(".search")) box?.classList.remove("open");
  });
  document.addEventListener("keydown", (ev) => {
    if (ev.key === "/" && document.activeElement !== input) {
      ev.preventDefault();
      input?.focus();
    }
  });

  // ---- scroll spy ----
  const links = new Map([...document.querySelectorAll(".sidebar a[href^='#']")].map((a) => [a.getAttribute("href").slice(1), a]));
  const spy = new IntersectionObserver(
    (entries) => {
      for (const e of entries) {
        if (!e.isIntersecting) continue;
        links.forEach((a) => a.classList.remove("active"));
        links.get(e.target.id)?.classList.add("active");
      }
    },
    { rootMargin: "-20% 0px -70% 0px" },
  );
  document.querySelectorAll("section.doc").forEach((s) => spy.observe(s));

  // ---- lightbox ----
  const lb = document.getElementById("lightbox");
  const lbImg = lb?.querySelector("img");
  document.querySelectorAll("figure img, .strip img").forEach((img) =>
    img.addEventListener("click", () => {
      lbImg.src = img.currentSrc || img.src;
      lbImg.alt = img.alt;
      lb.classList.add("open");
    }),
  );
  lb?.addEventListener("click", () => lb.classList.remove("open"));
  document.addEventListener("keydown", (ev) => ev.key === "Escape" && lb?.classList.remove("open"));

  setLang(lang);
})();
