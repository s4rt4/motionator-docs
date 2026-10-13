"""Guide content, part 1: getting started and the interface. Every text is a pair (English,
Indonesian). Part 2 (animation, export, reference) is in content2.py."""
import content3
from build import B, CARDS, CODE, DIAGRAM, H3, H4, IMG, LEGEND, NOTE, P, RAW, STEPS, STRIP, TABLE, TIP, UL, WARN

G_START = B("Getting started", "Memulai")
G_UI = B("The interface", "Antarmuka")
G_ANIM = B("Animating", "Menganimasikan")
G_OUT = B("Export", "Ekspor")
G_REF = B("Guides & reference", "Panduan & referensi")

HERO = """<div class="hero"><img class="logo" src="img/logo.png" alt="">
<h1><span lang="en">Animate SVG without code</span><span lang="id">Animasikan SVG tanpa coding</span></h1>
<p><span lang="en">Motionator turns SVG artwork into motion graphics with presets and keyframes, then exports 4K video for stock sites, Lottie for apps and animated SVG for the web.</span><span lang="id">Motionator mengubah artwork SVG menjadi motion graphic dengan preset dan keyframe, lalu mengekspornya menjadi video 4K untuk situs stok, Lottie untuk aplikasi, dan SVG animasi untuk web.</span></p>
<div class="badges"><span>82 presets</span><span>4K · ProRes · H.264</span><span>Lottie</span><span>Animated SVG</span><span>EN / ID</span></div></div>"""


def svg_easing(lbl):
    """Four easing curves: progress over time."""
    curves = [
        ("Linear", "M0 100 L100 0"),
        ("Easy Ease", "M0 100 C33 100 67 0 100 0"),
        ("Ease In", "M0 100 C33 100 100 0 100 0"),
        ("Ease Out", "M0 100 C0 100 67 0 100 0"),
    ]
    g = ""
    for i, (name, d) in enumerate(curves):
        x = 20 + i * 175
        g += f'<g transform="translate({x},20)"><rect width="140" height="140" rx="10" fill="none" class="stroke" stroke-opacity=".2"/><g transform="translate(20,20)"><path d="{d}" fill="none" stroke="#e2381d" stroke-width="4" stroke-linecap="round"/></g><text x="70" y="165" text-anchor="middle" font-size="14" font-weight="600">{name}</text></g>'
    return f'<svg viewBox="0 0 720 200" width="720">{g}<text x="8" y="14" font-size="12" class="dim">{lbl}</text></svg>'


def svg_blend(t):
    return f"""<svg viewBox="0 0 720 230" width="720">
<text x="20" y="22" font-size="15" font-weight="700">{t[0]}</text>
<rect x="20" y="36" width="300" height="26" rx="6" fill="#16a34a" opacity=".85"/><text x="30" y="54" font-size="13" fill="#fff">Slide In ←</text>
<rect x="160" y="70" width="300" height="26" rx="6" fill="#16a34a" opacity=".85"/><text x="170" y="88" font-size="13" fill="#fff">Slide In ↑</text>
<text x="480" y="66" font-size="13" class="dim">{t[1]}</text>
<text x="20" y="132" font-size="15" font-weight="700">{t[2]}</text>
<rect x="20" y="146" width="460" height="26" rx="6" fill="#16a34a" opacity=".85"/><text x="30" y="164" font-size="13" fill="#fff">Fade In + Slide</text>
<rect x="20" y="180" width="660" height="26" rx="6" fill="#2563eb" opacity=".85"/><text x="30" y="198" font-size="13" fill="#fff">Float (loop)</text>
<text x="500" y="166" font-size="13" class="dim">{t[3]}</text>
</svg>"""


def svg_stagger(t):
    def row(y, label, starts):
        s = f'<text x="20" y="{y + 16}" font-size="13" font-weight="600">{label}</text>'
        for i, st in enumerate(starts):
            s += f'<rect x="{140 + st * 40}" y="{y + i * 0}" width="120" height="8" rx="4" fill="#e2381d" opacity="{0.45 + i * 0.12}" transform="translate(0,{i * 10})"/>'
        return s
    return f"""<svg viewBox="0 0 720 300" width="720">
{row(10, t[0], [0, 1, 2, 3, 4])}
{row(80, t[1], [4, 3, 2, 1, 0])}
{row(150, t[2], [2, 1, 0, 1, 2])}
{row(220, t[3], [3, 0, 4, 1, 2])}
</svg>"""


def svg_trim(t):
    return f"""<svg viewBox="0 0 720 210" width="720">
<path d="M40 150 C 140 20, 260 20, 360 110 S 580 200, 680 60" fill="none" stroke="#cbd5e1" stroke-width="14" stroke-linecap="round"/>
<path d="M40 150 C 140 20, 260 20, 360 110 S 580 200, 680 60" fill="none" stroke="#e2381d" stroke-width="14" stroke-linecap="round" stroke-dasharray="330 2000" stroke-dashoffset="-170"/>
<circle cx="181" cy="58" r="7" fill="#111827"/><text x="150" y="40" font-size="14" font-weight="600">{t[0]}</text>
<circle cx="452" cy="146" r="7" fill="#111827"/><text x="432" y="186" font-size="14" font-weight="600">{t[1]}</text>
<text x="40" y="190" font-size="13" class="dim">0%</text><text x="660" y="40" font-size="13" class="dim">100%</text>
<text x="250" y="200" font-size="13" class="dim">{t[2]}</text>
</svg>"""


def svg_loop(t):
    return f"""<svg viewBox="0 0 720 170" width="720">
<rect x="40" y="40" width="560" height="40" rx="8" fill="#2563eb" opacity=".18"/>
<path d="M40 60 Q 110 25 180 60 T 320 60 T 460 60 T 600 60" fill="none" stroke="#2563eb" stroke-width="4"/>
<circle cx="40" cy="60" r="8" fill="#16a34a"/><circle cx="600" cy="60" r="8" fill="#16a34a"/>
<path d="M600 60 C 660 60, 660 130, 320 130 C -20 130, -20 60, 40 60" fill="none" stroke="#16a34a" stroke-width="2.5" stroke-dasharray="6 6"/>
<text x="40" y="30" font-size="13" font-weight="600">0 s</text><text x="575" y="30" font-size="13" font-weight="600">{t[0]}</text>
<text x="210" y="155" font-size="13" class="dim">{t[1]}</text>
</svg>"""


def build(doc, presets, shortcuts):
    # ============================================================ welcome
    s = doc.section("welcome", G_START, B("Welcome", "Selamat datang"))
    s += [
        P(
            "This guide explains every part of Motionator, from the first import to a finished 4K clip, a Lottie file or an animated SVG for your website. Each chapter has real screenshots, and the tutorials use sample files you can download and follow step by step.",
            "Panduan ini menjelaskan setiap bagian Motionator, dari impor pertama sampai klip 4K jadi, file Lottie, atau SVG animasi untuk website Anda. Setiap bab berisi screenshot asli, dan tutorialnya memakai file contoh yang bisa diunduh lalu diikuti langkah demi langkah.",
        ),
        STRIP("logo", ["0.3 s", "0.9 s", "1.5 s", "2.6 s"], "A logo drawn on with Trim Paths, staggered letters and a wipe (sample: logo.motionator).", "Logo yang tergambar dengan Trim Paths, huruf yang muncul bergantian, dan wipe (contoh: logo.motionator)."),
        H3("what-you-can-make", "What you can make", "Apa yang bisa dibuat"),
        CARDS(
            ("🎞️", "Stock footage", "Footage stok", "Seamless 4K backgrounds in H.264 or ProRes, checked for loops and for the usual stock-site rules.", "Background 4K yang bisa diulang mulus, dalam H.264 atau ProRes, dicek loop-nya dan syarat umum situs stok."),
            ("✒️", "Logo animation", "Animasi logo", "Draw-on strokes, pops, wipes and colour flashes, with a soundtrack.", "Garis yang tergambar, pop, wipe, dan kilasan warna, lengkap dengan audio."),
            ("🌐", "Web animation", "Animasi web", "Lottie JSON for lottie-web and apps, or one self-contained animated SVG.", "Lottie JSON untuk lottie-web dan aplikasi, atau satu file SVG animasi yang berdiri sendiri."),
            ("🧩", "Your own presets", "Preset sendiri", "Turn any keyframed layer into a preset and reuse it in every project.", "Jadikan layer berkeyframe mana pun sebagai preset dan pakai ulang di semua proyek."),
        ),
        H3("how-it-works", "How Motionator works", "Cara kerja Motionator"),
        P(
            "You prepare artwork in Illustrator, Inkscape, Figma or any vector editor and save it as SVG. Every group or path with a name (an <code>id</code> in the SVG) becomes a <b>layer</b> you can animate. You then animate layers in two ways, which can be combined:",
            "Siapkan artwork di Illustrator, Inkscape, Figma, atau editor vektor lain lalu simpan sebagai SVG. Setiap grup atau path yang punya nama (<code>id</code> di SVG) menjadi <b>layer</b> yang bisa dianimasikan. Layer bisa dianimasikan dengan dua cara, dan keduanya bisa digabung:",
        ),
        UL(
            ("<b>Presets</b>: ready-made motions (Fade In, Bounce, Orbit, Draw On…) applied with a double-click. Ideal for fast, consistent results.", "<b>Preset</b>: gerakan siap pakai (Fade In, Bounce, Orbit, Draw On, dan lainnya) yang diterapkan dengan klik dua kali. Cocok untuk hasil cepat dan konsisten."),
            ("<b>Keyframes</b>: set values at points in time, with easing, a graph editor and curved motion paths, like in After Effects.", "<b>Keyframe</b>: tentukan nilai di titik waktu tertentu, dengan easing, graph editor, dan motion path melengkung, seperti di After Effects."),
        ),
        P(
            "The same renderer draws the preview and the exported video, so what you see is what you get. Lottie and animated SVG exports are checked against this renderer and each export shows a compatibility report before saving.",
            "Renderer yang sama dipakai untuk preview dan video hasil ekspor, jadi yang Anda lihat itulah hasilnya. Ekspor Lottie dan SVG animasi diuji terhadap renderer ini, dan setiap ekspor menampilkan laporan kompatibilitas sebelum disimpan.",
        ),
    ]

    # ============================================================ install
    s = doc.section("install", G_START, B("Installation", "Instalasi"), B("Install once, then open SVG files or projects straight from Explorer.", "Pasang sekali, lalu buka file SVG atau proyek langsung dari Explorer."))
    s += [
        H3("requirements", "Requirements", "Kebutuhan sistem"),
        TABLE(
            [B("Item", "Item"), B("Requirement", "Kebutuhan")],
            [
                [B("System", "Sistem"), B("Windows 10 or 11, 64-bit", "Windows 10 atau 11, 64-bit")],
                [B("Memory", "Memori"), B("8 GB RAM; 16 GB recommended for 4K export with motion blur", "RAM 8 GB; 16 GB disarankan untuk ekspor 4K dengan motion blur")],
                [B("Display", "Layar"), B("1600×900 or larger", "1600×900 atau lebih besar")],
                ["WebView2", B("Included in Windows 11; the installer adds it on Windows 10 if missing", "Sudah ada di Windows 11; installer memasangnya di Windows 10 bila belum ada")],
                ["FFmpeg", B("Bundled with the installer (used for video and audio export)", "Disertakan dalam installer (dipakai untuk ekspor video dan audio)")],
            ],
        ),
        H3("installing", "Installing", "Memasang"),
        STEPS(
            ("Run <code>Motionator_0.1.0_x64-setup.exe</code>. Choose <b>English</b> or <b>Bahasa Indonesia</b> for the installer.", "Jalankan <code>Motionator_0.1.0_x64-setup.exe</code>. Pilih <b>English</b> atau <b>Bahasa Indonesia</b> untuk installer."),
            ("Follow the pages and click <b>Install</b>. Motionator installs for your user account only, so no administrator rights are needed.", "Ikuti halamannya lalu klik <b>Install</b>. Motionator dipasang untuk akun Anda saja, jadi tidak perlu hak administrator."),
            ("Optionally create a desktop shortcut, then start Motionator from the last page or the Start menu.", "Bila perlu buat pintasan desktop, lalu jalankan Motionator dari halaman terakhir atau menu Start."),
        ),
        P(
            "The installer registers <code>.motionator</code> project files: double-clicking one in Explorer opens it in Motionator. You can also right-click an <code>.svg</code> file and choose <b>Open with ▸ Motionator</b> to import it straight away.",
            "Installer mendaftarkan file proyek <code>.motionator</code>: klik dua kali file itu di Explorer untuk membukanya di Motionator. Anda juga bisa klik kanan file <code>.svg</code> lalu pilih <b>Open with ▸ Motionator</b> untuk langsung mengimpornya.",
        ),
        H3("first-launch", "First launch and language", "Pertama kali dibuka dan bahasa"),
        P(
            "Motionator follows the Windows display language: Indonesian on an Indonesian Windows, English otherwise. Change it any time in <b>Edit ▸ Preferences</b> (<i>Bahasa / Language</i>); the whole interface switches at once, including preset descriptions and export reports.",
            "Motionator mengikuti bahasa tampilan Windows: Indonesia bila Windows berbahasa Indonesia, selain itu Inggris. Ganti kapan saja di <b>Edit ▸ Preferensi</b> (<i>Bahasa / Language</i>); seluruh antarmuka langsung berganti, termasuk deskripsi preset dan laporan ekspor.",
        ),
        IMG("dialog-prefs", "<b>Preferences</b>: language, theme (Dark or Darker) and auto-save interval.", "<b>Preferensi</b>: bahasa, tema (Dark atau Darker), dan interval auto-save.", "medium"),
        NOTE(
            "The status bar shows <b>FFmpeg</b> with a check mark when video export is ready. If it shows a warning, reinstall Motionator; video export needs FFmpeg, everything else works without it.",
            "Status bar menampilkan <b>FFmpeg</b> dengan tanda centang bila ekspor video siap. Bila muncul peringatan, pasang ulang Motionator; ekspor video butuh FFmpeg, fitur lain tetap jalan tanpanya.",
        ),
    ]

    # ============================================================ quick start
    s = doc.section("quick-start", G_START, B("Quick start: your first animation", "Mulai cepat: animasi pertama"), B("Five minutes from an SVG to a finished MP4.", "Lima menit dari SVG sampai MP4 jadi."))
    s += [
        STEPS(
            ("<b>Import an SVG.</b> Press [[Ctrl+I]], choose <b>File ▸ Import SVG…</b>, or simply drag an <code>.svg</code> file onto the window. Try <code>samples/logo.svg</code>.", "<b>Impor SVG.</b> Tekan [[Ctrl+I]], pilih <b>File ▸ Impor SVG…</b>, atau seret file <code>.svg</code> ke jendela. Coba <code>samples/logo.svg</code>."),
            ("<b>Select a layer.</b> Click it in the <b>Layers</b> panel or directly on the canvas with the Selection tool [[V]].", "<b>Pilih layer.</b> Klik di panel <b>Layers</b> atau langsung di canvas dengan Selection tool [[V]]."),
            ("<b>Apply a preset.</b> In the <b>Presets</b> panel, hover a preset to preview it, then <b>double-click</b> it. Enter presets start at the playhead (the blue line in the timeline).", "<b>Terapkan preset.</b> Di panel <b>Presets</b>, arahkan kursor ke preset untuk melihat preview-nya, lalu <b>klik dua kali</b>. Preset Enter dimulai di playhead (garis biru di timeline)."),
            ("<b>Play it.</b> Press [[Space]] or the round play button under the canvas. The green bar on the ruler shows frames already cached for smooth playback.", "<b>Putar.</b> Tekan [[Space]] atau tombol play bulat di bawah canvas. Bar hijau di ruler menunjukkan frame yang sudah di-cache agar pemutaran mulus."),
            ("<b>Adjust timing.</b> In the <b>Timeline</b>, drag a preset bar to move it and drag its right edge to change its duration.", "<b>Atur waktu.</b> Di <b>Timeline</b>, seret bar preset untuk memindahkannya dan seret tepi kanannya untuk mengubah durasi."),
            ("<b>Export.</b> Click the red <b>Export</b> button (or [[Ctrl+M]]), choose a format and size in the Render Queue, pick the output file, then press <b>Render</b>.", "<b>Ekspor.</b> Klik tombol merah <b>Export</b> (atau [[Ctrl+M]]), pilih format dan ukuran di Render Queue, tentukan file tujuan, lalu tekan <b>Render</b>."),
            ("<b>Save the project</b> with [[Ctrl+S]]. The <code>.motionator</code> file contains your SVG, so it can be moved and shared as one file.", "<b>Simpan proyek</b> dengan [[Ctrl+S]]. File <code>.motionator</code> sudah berisi SVG Anda, jadi bisa dipindah dan dibagikan sebagai satu file."),
        ),
        IMG("overview", "The logo sample at 1.5 s: layers on the left, the canvas in the middle, presets as bars in the timeline.", "Contoh logo di detik 1,5: layer di kiri, canvas di tengah, preset sebagai bar di timeline."),
        TIP("Everything you do can be undone with [[Ctrl+Z]] and redone with [[Ctrl+Shift+Z]]. A whole drag is one undo step.", "Semua tindakan bisa dibatalkan dengan [[Ctrl+Z]] dan diulang dengan [[Ctrl+Shift+Z]]. Satu kali seret dihitung satu langkah undo."),
    ]

    content3.concepts(doc, G_START)

    # ============================================================ preparing SVG
    s = doc.section("preparing-svg", G_START, B("Preparing SVG files", "Menyiapkan file SVG"), B("Good layer names in your design tool make animation easy.", "Nama layer yang baik di aplikasi desain memudahkan animasi."))
    s += [
        H3("ids-become-layers", "Named elements become layers", "Elemen bernama menjadi layer"),
        P(
            "Motionator makes a layer for every group and path that has an <code>id</code>. Elements without an id stay part of their parent layer, so they move together. Nesting is kept: a named group inside another named group becomes a child layer, and moving the parent moves the child.",
            "Motionator membuat layer untuk setiap grup dan path yang punya <code>id</code>. Elemen tanpa id tetap menjadi bagian layer induknya, jadi ikut bergerak bersama. Susunan bertingkat dipertahankan: grup bernama di dalam grup bernama lain menjadi layer anak, dan memindah induk ikut memindah anaknya.",
        ),
        TABLE(
            [B("Tool", "Aplikasi"), B("How to give elements ids", "Cara memberi id pada elemen")],
            [
                ["Adobe Illustrator", B("Name layers and sub-layers in the Layers panel. Export with <b>File ▸ Export ▸ Export As… ▸ SVG</b> and <i>Object IDs: Layer Names</i>. Illustrator writes spaces as <code>_x20_</code>; Motionator shows them as spaces again.", "Beri nama layer dan sub-layer di panel Layers. Ekspor lewat <b>File ▸ Export ▸ Export As… ▸ SVG</b> dengan <i>Object IDs: Layer Names</i>. Illustrator menulis spasi sebagai <code>_x20_</code>; Motionator menampilkannya lagi sebagai spasi.")],
                ["Inkscape", B("Set the <b>ID</b> in Object Properties ([[Ctrl+Shift+O]]), or rename layers. Save as <i>Plain SVG</i> or <i>Inkscape SVG</i>.", "Isi <b>ID</b> di Object Properties ([[Ctrl+Shift+O]]), atau ganti nama layer. Simpan sebagai <i>Plain SVG</i> atau <i>Inkscape SVG</i>.")],
                ["Figma", B("Layer names become ids when you export a frame as SVG with <i>Include \"id\" attribute</i> turned on.", "Nama layer menjadi id saat Anda mengekspor frame sebagai SVG dengan <i>Include \"id\" attribute</i> aktif.")],
                [B("Any editor", "Editor lain"), B("Add <code>id=\"Name\"</code> to the <code>&lt;g&gt;</code> or <code>&lt;path&gt;</code> elements in a text editor.", "Tambahkan <code>id=\"Nama\"</code> pada elemen <code>&lt;g&gt;</code> atau <code>&lt;path&gt;</code> lewat editor teks.")],
            ],
        ),
        H3("svg-checklist", "Checklist before importing", "Daftar periksa sebelum impor"),
        UL(
            ("<b>Outline text</b> (Create Outlines / Object to Path). Live text is not drawn.", "<b>Ubah teks menjadi outline</b> (Create Outlines / Object to Path). Teks yang masih bisa diedit tidak digambar."),
            ("<b>Use strokes for line art</b> you want to draw on with Trim Paths. Filled shapes cannot be drawn on.", "<b>Pakai stroke untuk line art</b> yang ingin tergambar dengan Trim Paths. Bentuk berisi (fill) tidak bisa tergambar."),
            ("<b>Group what moves together</b> and name the group, e.g. a wheel with its spokes.", "<b>Kelompokkan yang bergerak bersama</b> dan beri nama grupnya, misalnya roda beserta jari-jarinya."),
            ("<b>Avoid filters and raster images</b> if you also need Lottie: they render in video but cannot be exported to Lottie.", "<b>Hindari filter dan gambar raster</b> bila juga butuh Lottie: keduanya tampil di video tetapi tidak bisa diekspor ke Lottie."),
            ("<b>Keep ids unique.</b> Duplicate ids are reported; only the first becomes a layer.", "<b>Pastikan id unik.</b> Id ganda dilaporkan; hanya yang pertama menjadi layer."),
        ),
        H3("import-warnings", "Import warnings", "Peringatan impor"),
        P(
            "After an import the status bar shows how many layers were found. If something needs attention, a warning appears there; click it to see the list. Warnings never stop the import.",
            "Setelah impor, status bar menampilkan jumlah layer yang ditemukan. Bila ada yang perlu diperhatikan, peringatan muncul di sana; klik untuk melihat daftarnya. Peringatan tidak pernah menghentikan impor.",
        ),
        TABLE(
            [B("Warning", "Peringatan"), B("What to do", "Yang perlu dilakukan")],
            [
                [B("Text not outlined", "Teks belum di-outline"), B("Convert text to outlines and import again.", "Ubah teks menjadi outline lalu impor ulang.")],
                [B("Filters (blur, shadow…)", "Filter (blur, shadow, dll.)"), B("Fine for video; slows 4K rendering and is left out of Lottie.", "Aman untuk video; memperlambat render 4K dan tidak ikut ke Lottie.")],
                [B("Patterns / blend modes", "Pattern / blend mode"), B("Shown in video; Lottie support is limited.", "Tampil di video; dukungan Lottie terbatas.")],
                [B("Raster images", "Gambar raster"), B("Blurry when scaled up; makes Lottie files larger.", "Kabur bila diperbesar; memperbesar file Lottie.")],
                [B("Duplicate ids", "Id ganda"), B("Rename them in your editor so each part can be animated.", "Ganti namanya di editor supaya setiap bagian bisa dianimasikan.")],
                [B("No ids", "Tidak ada id"), B("The whole SVG becomes one layer; name your layers.", "Seluruh SVG menjadi satu layer; beri nama pada layer-layer Anda.")],
            ],
        ),
        P(
            "A newly imported SVG is centred in the composition at its own size, scaled down only if it is larger than the composition. Each layer's anchor point starts at the centre of its box.",
            "SVG yang baru diimpor diletakkan di tengah komposisi dengan ukuran aslinya, dan hanya diperkecil bila lebih besar dari komposisi. Anchor point setiap layer awalnya ada di tengah kotaknya.",
        ),
    ]

    s += content3.svg_prep_extra()

    # ============================================================ interface
    s = doc.section("interface", G_UI, B("The workspace at a glance", "Sekilas ruang kerja"), B("An After Effects–style layout: panels around a central canvas.", "Tata letak gaya After Effects: panel-panel di sekeliling canvas utama."))
    s += [
        IMG(
            "overview",
            "The main window in the Advanced workspace.",
            "Jendela utama di workspace Advanced.",
            pins=[(1, 2.5, 4.4), (2, 13, 8.6), (3, 86, 8.6), (4, 97, 8.6), (5, 8, 30), (6, 48, 22), (7, 47, 50.7), (8, 89, 25), (9, 30, 75), (10, 89, 64), (11, 89, 87), (12, 18, 98.6)],
        ),
        LEGEND(
            (1, "<b>Menu bar</b>: every command, with its shortcut.", "<b>Menu bar</b>: semua perintah, lengkap dengan shortcut."),
            (2, "<b>Toolbar</b>: Selection, Hand, Zoom, Rotation, Anchor Point and Pen tools, and Snapping.", "<b>Toolbar</b>: tool Selection, Hand, Zoom, Rotation, Anchor Point, Pen, dan Snapping."),
            (3, "<b>Workspaces</b>: Simple, Advanced and Minimal.", "<b>Workspace</b>: Simple, Advanced, dan Minimal."),
            (4, "<b>Export</b>: adds the composition to the Render Queue.", "<b>Export</b>: menambahkan komposisi ke Render Queue."),
            (5, "<b>Layers</b>: the layer tree of your SVGs.", "<b>Layers</b>: pohon layer dari SVG Anda."),
            (6, "<b>Composition</b>: the canvas, where you select and move layers.", "<b>Composition</b>: canvas, tempat memilih dan memindah layer."),
            (7, "<b>Transport</b>: play, step, loop, current time and cache.", "<b>Transport</b>: putar, maju/mundur per frame, loop, waktu saat ini, dan cache."),
            (8, "<b>Properties</b>: transform, effects, Trim Paths and presets of the selected layer.", "<b>Properties</b>: transform, efek, Trim Paths, dan preset dari layer terpilih."),
            (9, "<b>Timeline</b>: preset bars, keyframes and the Graph Editor; the Render Queue is its neighbour tab.", "<b>Timeline</b>: bar preset, keyframe, dan Graph Editor; Render Queue ada di tab sebelahnya."),
            (10, "<b>Presets</b>: the preset library with search and live previews.", "<b>Presets</b>: pustaka preset dengan pencarian dan preview langsung."),
            (11, "<b>Align</b>: align the selected layer to the composition.", "<b>Align</b>: ratakan layer terpilih terhadap komposisi."),
            (12, "<b>Status bar</b>: messages, import warnings and the FFmpeg check.", "<b>Status bar</b>: pesan, peringatan impor, dan cek FFmpeg."),
        ),
        H3("menus", "Menus", "Menu"),
        P(
            "The menus list every command with its keyboard shortcut. The File menu holds projects, imports and the web exports; Animation holds preset and keyframe commands; Window shows and arranges panels.",
            "Menu berisi semua perintah beserta shortcut-nya. Menu File berisi proyek, impor, dan ekspor web; Animation berisi perintah preset dan keyframe; Window menampilkan dan menata panel.",
        ),
        RAW('<div class="cards" style="grid-template-columns:repeat(auto-fill,minmax(300px,1fr))">'),
        IMG("menu-file", "File menu", "Menu File"),
        IMG("menu-animation", "Animation menu", "Menu Animation"),
        RAW("</div>"),
        H3("toolbar", "Toolbar and tools", "Toolbar dan tool"),
        IMG("toolbar", "The toolbar: logo, tools, Snapping, workspaces and Export.", "Toolbar: logo, tool, Snapping, workspace, dan Export."),
        TABLE(
            [B("Tool", "Tool"), B("Key", "Tombol"), B("Use", "Kegunaan")],
            [
                ["Selection", "[[V]]", B("Click a layer on the canvas to select it; drag to move it. Hold [[Shift]] to move only horizontally or vertically.", "Klik layer di canvas untuk memilihnya; seret untuk memindahkannya. Tahan [[Shift]] agar hanya bergerak horizontal atau vertikal.")],
                ["Hand", "[[H]]", B("Drag to pan the canvas. Holding [[Space]] gives the Hand tool temporarily.", "Seret untuk menggeser tampilan canvas. Menahan [[Space]] memberi tool Hand sementara.")],
                ["Zoom", "[[Z]]", B("Click to zoom in at that point; [[Alt]]-click zooms out.", "Klik untuk memperbesar di titik itu; [[Alt]]+klik untuk memperkecil.")],
                ["Rotation", "[[W]]", B("Drag around the selected layer to rotate it about its anchor point; [[Shift]] snaps to 45°.", "Seret di sekitar layer terpilih untuk memutarnya pada anchor point; [[Shift]] mengunci ke 45°.")],
                ["Anchor Point", "[[Y]]", B("Drag to move the anchor point (the pivot for rotation and scale) without moving the layer.", "Seret untuk memindah anchor point (poros rotasi dan skala) tanpa memindah layer.")],
                ["Pen", "[[G]]", B("Shows the motion path; click a position keyframe to switch it between a smooth curve and a sharp corner.", "Menampilkan motion path; klik keyframe posisi untuk mengubahnya antara kurva halus dan sudut tajam.")],
            ],
        ),
        P(
            "With the mouse wheel over the canvas: scroll pans, [[Shift]]+scroll pans sideways, and [[Ctrl]]+scroll or [[Alt]]+scroll zooms around the pointer.",
            "Dengan roda mouse di atas canvas: scroll menggeser tampilan, [[Shift]]+scroll menggeser ke samping, dan [[Ctrl]]+scroll atau [[Alt]]+scroll memperbesar di sekitar kursor.",
        ),
    ]

    content3.menu_reference(doc, G_UI)

    # ============================================================ workspaces & docking
    s = doc.section("workspaces", G_UI, B("Workspaces and docking panels", "Workspace dan panel docking"), B("Arrange panels the way you work, and keep several layouts.", "Tata panel sesuai cara kerja Anda, dan simpan beberapa tata letak."))
    s += [
        H3("three-workspaces", "Simple, Advanced and Minimal", "Simple, Advanced, dan Minimal"),
        TABLE(
            [B("Workspace", "Workspace"), B("Key", "Tombol"), B("For", "Untuk")],
            [
                ["Simple", "[[Shift+F10]]", B("Working with presets: the timeline shows one row per layer with preset bars.", "Bekerja dengan preset: timeline menampilkan satu baris per layer dengan bar preset.")],
                ["Advanced", "[[Shift+F11]]", B("Keyframes: layers twirl open to show every property, keyframes and the Graph Editor.", "Keyframe: layer bisa dibuka untuk menampilkan semua properti, keyframe, dan Graph Editor.")],
                ["Minimal", "[[Shift+F12]]", B("Reviewing: just the canvas and the timeline.", "Meninjau: hanya canvas dan timeline.")],
            ],
        ),
        IMG("workspace-minimal", "The Minimal workspace: more room for the canvas.", "Workspace Minimal: ruang lebih luas untuk canvas."),
        H3("docking", "Moving panels", "Memindah panel"),
        P(
            "Drag a panel by its tab. A blue overlay shows where it will land: the outer quarter of a panel group docks it on that side, the middle adds it as a tab. Release to drop it there, or press [[Esc]] to cancel. Drag the gaps between panels to resize them.",
            "Seret panel lewat tab-nya. Overlay biru menunjukkan tempat panel akan diletakkan: seperempat bagian tepi suatu grup panel menempelkannya di sisi itu, bagian tengah menambahkannya sebagai tab. Lepas untuk meletakkannya, atau tekan [[Esc]] untuk batal. Seret celah antar panel untuk mengubah ukurannya.",
        ),
        IMG("dock-drag", "Dragging the Presets tab: the blue overlay marks the drop zone (here the middle of the Composition group, so it would become a tab).", "Menyeret tab Presets: overlay biru menandai zona drop (di sini bagian tengah grup Composition, jadi akan menjadi tab)."),
        P(
            "Close a panel with the × on its tab and bring it back from the <b>Window</b> menu. Each workspace remembers its own arrangement. <b>Window ▸ Reset Layout</b> restores the default, and <b>Window ▸ Saved Layouts…</b> keeps arrangements under a name.",
            "Tutup panel dengan × di tab-nya dan buka lagi dari menu <b>Window</b>. Setiap workspace mengingat susunannya sendiri. <b>Window ▸ Reset Tata Letak</b> mengembalikan susunan default, dan <b>Window ▸ Tata Letak Tersimpan…</b> menyimpan susunan dengan nama.",
        ),
        RAW('<div class="cards" style="grid-template-columns:repeat(auto-fill,minmax(320px,1fr))">'),
        IMG("menu-window", "The Window menu: workspaces, themes, panels and layouts.", "Menu Window: workspace, tema, panel, dan tata letak."),
        IMG("dialog-layouts", "Saved Layouts: save the current arrangement, apply or delete saved ones.", "Tata Letak Tersimpan: simpan susunan saat ini, pakai atau hapus yang tersimpan."),
        RAW("</div>"),
        TIP("Themes: <b>Window ▸ Dark Theme</b> or <b>Darker Theme</b>. The choice is remembered.", "Tema: <b>Window ▸ Tema Dark</b> atau <b>Tema Darker</b>. Pilihan Anda diingat."),
    ]

    # ============================================================ layers panel
    s = doc.section("layers", G_UI, B("Layers panel", "Panel Layers"))
    s += [
        IMG("panel-layers", "Layers panel with the logo sample: SVG root, groups and paths. A dot marks animated layers.", "Panel Layers dengan contoh logo: root SVG, grup, dan path. Titik menandai layer yang beranimasi.", "small"),
        UL(
            ("<b>Header</b>: the selected layer's name, kind, size and SVG id.", "<b>Header</b>: nama, jenis, ukuran, dan id SVG dari layer terpilih."),
            ("<b>Search</b>: type to filter layers by name.", "<b>Cari</b>: ketik untuk menyaring layer berdasarkan nama."),
            ("<b>Kinds</b>: <i>SVG</i> is the imported file (the root layer), <i>Group</i> and <i>Path</i> are named elements inside it. Arrows fold groups.", "<b>Jenis</b>: <i>SVG</i> adalah file yang diimpor (layer root), <i>Grup</i> dan <i>Path</i> adalah elemen bernama di dalamnya. Panah melipat grup."),
            ("<b>Blue dot</b>: the layer has presets or keyframes.", "<b>Titik biru</b>: layer punya preset atau keyframe."),
            ("<b>Buttons</b>: import another SVG, and delete the selected SVG (only whole SVG files can be deleted; their parts belong to the file).", "<b>Tombol</b>: impor SVG lain, dan hapus SVG terpilih (hanya file SVG utuh yang bisa dihapus; bagian di dalamnya milik file itu)."),
        ),
        P(
            "A composition can hold several SVG files; each becomes its own root layer. Later imports appear on top.",
            "Satu komposisi bisa berisi beberapa file SVG; masing-masing menjadi layer root sendiri. Impor terakhir tampil paling atas.",
        ),
    ]

    # ============================================================ composition panel
    s = doc.section("composition", G_UI, B("Composition panel", "Panel Composition"))
    s += [
        IMG("panel-composition", "The canvas with the selection box, anchor point (crosshair) and the bar of controls under it.", "Canvas dengan kotak seleksi, anchor point (tanda silang), dan bar kontrol di bawahnya."),
        H3("canvas", "Canvas", "Canvas"),
        P(
            "The composition is the white (or chequered, when transparent) rectangle; the dark area around it is the pasteboard. The selected layer shows a red box that follows its rotation, eight handles and its anchor point. Hovering a layer outlines it in blue.",
            "Komposisi adalah persegi putih (atau kotak-kotak bila transparan); area gelap di sekitarnya adalah pasteboard. Layer terpilih menampilkan kotak merah yang ikut berputar, delapan handle, dan anchor point-nya. Mengarahkan kursor ke layer memberinya garis biru.",
        ),
        H3("transport", "Playback controls", "Kontrol pemutaran"),
        TABLE(
            [B("Control", "Kontrol"), B("Key", "Tombol"), B("Action", "Fungsi")],
            [
                [B("Current time / duration", "Waktu saat ini / durasi"), "", B("Timecode in hours:minutes:seconds:frames.", "Timecode dalam jam:menit:detik:frame.")],
                [B("Go to start / end", "Ke awal / akhir"), "[[Home]] [[End]]", ""],
                [B("Previous / next frame", "Frame sebelumnya / berikutnya"), "[[PageUp]] [[PageDown]]", B("Also the arrow keys; with [[Shift]] they move 10 frames.", "Juga tombol panah; dengan [[Shift]] bergerak 10 frame.")],
                [B("Play / Pause", "Putar / Jeda"), "[[Space]]", B("Plays in real time with sound (if the project has audio).", "Memutar secara real time dengan suara (bila proyek punya audio).")],
                [B("Loop", "Loop"), "", B("Repeat playback from the start.", "Ulangi pemutaran dari awal.")],
                [B("Cache", "Cache"), "", B("How many frames are ready; cached frames play smoothly.", "Jumlah frame yang siap; frame yang sudah di-cache diputar dengan mulus.")],
            ],
        ),
        H3("viewer-options", "Viewer options", "Opsi tampilan"),
        UL(
            ("<b>Zoom</b>: Fit, or a fixed percentage. Keys: [[.]] zoom in, [[,]] zoom out, [[/]] 100 %, [[Shift+/]] fit.", "<b>Zoom</b>: Fit, atau persentase tetap. Tombol: [[.]] perbesar, [[,]] perkecil, [[/]] 100 %, [[Shift+/]] sesuaikan."),
            ("<b>Resolution</b>: Full, Half, Third, Quarter. Lower resolutions preview faster on large compositions.", "<b>Resolusi</b>: Full, Half, Third, Quarter. Resolusi rendah mempercepat preview pada komposisi besar."),
            ("<b>Grid</b> [[Ctrl+']], <b>transparency grid</b> and <b>safe areas</b> (action and title safe).", "<b>Grid</b> [[Ctrl+']], <b>grid transparansi</b>, dan <b>safe area</b> (action dan title safe)."),
            ("<b>Frame Render Time</b>: how long the last frame took to draw.", "<b>Frame Render Time</b>: berapa lama frame terakhir digambar."),
        ),
    ]

    # ============================================================ properties panel
    s = doc.section("properties", G_UI, B("Properties panel", "Panel Properties"), B("Exact values for the selected layer, or the composition settings when nothing is selected.", "Nilai pasti untuk layer terpilih, atau pengaturan komposisi bila tidak ada yang dipilih."))
    s += [
        RAW('<div class="cards" style="grid-template-columns:repeat(auto-fill,minmax(260px,1fr))">'),
        IMG("panel-properties", "Layer Transform and Effects.", "Layer Transform dan Efek."),
        IMG("panel-properties-trim", "Further down: Trim Paths and the presets on this layer.", "Di bawahnya: Trim Paths dan preset pada layer ini."),
        IMG("panel-properties-comp", "With nothing selected: the composition settings.", "Tanpa seleksi: pengaturan komposisi."),
        RAW("</div>"),
        H3("editing-values", "Editing values", "Mengubah nilai"),
        P(
            "Blue numbers can be <b>dragged</b> left and right to scrub the value, or <b>clicked</b> to type a number (press [[Enter]] to confirm, [[Esc]] to cancel). The clock icon is the <b>stopwatch</b>: turn it on to animate the property with keyframes (see Keyframes).",
            "Angka biru bisa <b>diseret</b> ke kiri dan kanan untuk mengubah nilai, atau <b>diklik</b> untuk mengetik angka (tekan [[Enter]] untuk konfirmasi, [[Esc]] untuk batal). Ikon jam adalah <b>stopwatch</b>: nyalakan untuk menganimasikan properti dengan keyframe (lihat Keyframe).",
        ),
        H3("transform-props", "Layer Transform", "Layer Transform"),
        TABLE(
            [B("Property", "Properti"), B("Meaning", "Arti")],
            [
                ["Anchor Point", B("The pivot for rotation, scale and skew, in the parent's coordinates. The crosshair button centres it on the layer.", "Poros untuk rotasi, skala, dan skew, dalam koordinat induk. Tombol tanda silang menaruhnya di tengah layer.")],
                ["Position", B("Where the anchor point sits (x, y).", "Letak anchor point (x, y).")],
                ["Scale", B("Width and height in percent. The chain button keeps the proportions.", "Lebar dan tinggi dalam persen. Tombol rantai menjaga proporsi.")],
                ["Rotation", B("Degrees, clockwise.", "Derajat, searah jarum jam.")],
                ["Opacity", B("0–100 %.", "0–100 %.")],
                ["Skew / Skew Axis", B("Slants the layer along an axis (degrees), like in After Effects.", "Memiringkan layer di sepanjang sumbu tertentu (derajat), seperti di After Effects.")],
            ],
        ),
        P(
            "<b>Reset</b> returns the transform to the rest pose of the SVG (effects are kept). <b>Layer ▸ Center Anchor Point</b> [[Ctrl+Alt+Home]] and <b>Layer ▸ Reset Transform</b> do the same from the menu.",
            "<b>Reset</b> mengembalikan transform ke pose diam SVG (efek tetap). <b>Layer ▸ Pusatkan Anchor Point</b> [[Ctrl+Alt+Home]] dan <b>Layer ▸ Reset Transform</b> melakukan hal yang sama dari menu.",
        ),
        H3("effects-props", "Effects", "Efek"),
        TABLE(
            [B("Effect", "Efek"), B("Meaning", "Arti")],
            [
                ["Blur", B("Gaussian blur radius in the layer's own pixels (it grows with the layer's scale).", "Radius gaussian blur dalam piksel layer itu sendiri (ikut membesar dengan skala layer).")],
                ["Tint", B("How much of the tint colour replaces the layer's colours (0–100 %). Pick the colour with <b>Tint colour</b>.", "Seberapa banyak warna tint menggantikan warna layer (0–100 %). Pilih warnanya di <b>Warna tint</b>.")],
                ["Reveal", B("The visible part of the layer's box (100 % = all), wiping in from the side chosen in <b>Reveal from</b>: left, right, top, bottom, iris (circle) or centre.", "Bagian kotak layer yang terlihat (100 % = semua), tersapu dari sisi yang dipilih di <b>Reveal dari</b>: kiri, kanan, atas, bawah, iris (lingkaran), atau tengah.")],
            ],
        ),
        H3("comp-settings", "Composition settings", "Pengaturan komposisi"),
        P(
            "Click an empty part of the canvas (or press [[Ctrl+K]]) to edit the composition: <b>name</b>, <b>size</b> in pixels, <b>frame rate</b> (23.976 to 60 fps), <b>duration</b> in seconds and the <b>background</b> colour. Tick <b>Transparent</b> for a transparent background, needed for ProRes 4444 or VP9 with alpha.",
            "Klik bagian kosong canvas (atau tekan [[Ctrl+K]]) untuk mengubah komposisi: <b>nama</b>, <b>ukuran</b> dalam piksel, <b>frame rate</b> (23,976 sampai 60 fps), <b>durasi</b> dalam detik, dan warna <b>background</b>. Centang <b>Transparan</b> untuk background transparan, yang dibutuhkan ProRes 4444 atau VP9 dengan alpha.",
        ),
        H3("align-panel", "Align panel", "Panel Align"),
        P(
            "The six buttons align the selected layer's box to the left, centre or right and to the top, middle or bottom of the composition. If Position is keyframed, the change is keyed at the playhead.",
            "Keenam tombol meratakan kotak layer terpilih ke kiri, tengah, atau kanan, dan ke atas, tengah, atau bawah komposisi. Bila Position berkeyframe, perubahan dicatat sebagai keyframe di playhead.",
        ),
    ]

    import content2

    content2.build(doc, presets, shortcuts)
    return doc
