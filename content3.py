"""Guide content, part 3: concepts, references (menus, presets, easing), animation principles,
web integration, microstock, extra tutorials and the glossary."""
import io
import json
import os
import re

from build import APP, B, CARDS, CODE, DIAGRAM, H3, H4, IMG, NOTE, P, RAW, STEPS, STRIP, TABLE, TIP, UL, WARN, kbd

HERE = os.path.dirname(os.path.abspath(__file__))


def bi(en, idn, tag="span", attrs=""):
    return f'<{tag} lang="en"{attrs}>{en}</{tag}><{tag} lang="id"{attrs}>{idn}</{tag}>'


# ---------------------------------------------------------------- concepts


def svg_anchor(t):
    return f"""<svg viewBox="0 0 720 230" width="720">
<g transform="translate(60,30)">
<rect x="40" y="40" width="100" height="100" rx="14" fill="none" stroke="#9aa3b8" stroke-width="2" stroke-dasharray="7 6"/>
<rect x="40" y="40" width="100" height="100" rx="14" fill="#2563eb" opacity=".85" transform="rotate(30 90 90)"/>
<circle cx="90" cy="90" r="6" fill="#e2381d"/><path d="M90 30 A60 60 0 0 1 142 60" fill="none" stroke="#e2381d" stroke-width="2.5" marker-end="url(#ar)"/>
<text x="90" y="185" text-anchor="middle" font-size="14" font-weight="600">{t[0]}</text></g>
<g transform="translate(400,30)">
<rect x="40" y="40" width="100" height="100" rx="14" fill="none" stroke="#9aa3b8" stroke-width="2" stroke-dasharray="7 6"/>
<rect x="40" y="40" width="100" height="100" rx="14" fill="#2563eb" opacity=".85" transform="rotate(30 40 140)"/>
<circle cx="40" cy="140" r="6" fill="#e2381d"/>
<text x="110" y="185" text-anchor="middle" font-size="14" font-weight="600">{t[1]}</text></g>
<defs><marker id="ar" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10z" fill="#e2381d"/></marker></defs>
</svg>"""


def svg_tree(t):
    def box(x, y, label, kind, fill):
        return f'<rect x="{x}" y="{y}" width="150" height="40" rx="9" fill="{fill}" opacity=".16"/><rect x="{x}" y="{y}" width="150" height="40" rx="9" fill="none" stroke="{fill}" stroke-width="1.5"/><text x="{x + 12}" y="{y + 25}" font-size="14" font-weight="600">{label}</text><text x="{x + 140}" y="{y + 25}" font-size="11" text-anchor="end" class="dim">{kind}</text>'

    lines = "".join(f'<path d="M{a} {b} V{c} H{d}" fill="none" class="stroke" stroke-opacity=".35" stroke-width="1.5"/>' for a, b, c, d in [(95, 60, 100, 130), (95, 60, 220, 130), (95, 60, 160, 130), (225, 140, 180, 280), (225, 140, 230, 280)])
    return f"""<svg viewBox="0 0 720 270" width="720">{lines}
{box(20, 20, "logo.svg", "SVG", "#e2381d")}
{box(130, 80, "Mark", "Group", "#2563eb")}{box(130, 140, "Wordmark", "Group", "#2563eb")}{box(130, 200, "Underline", "Path", "#16a34a")}
{box(280, 160, "Letter_M", "Path", "#16a34a")}{box(280, 210, "Letter_O …", "Path", "#16a34a")}
<text x="470" y="100" font-size="13" class="dim">{t[0]}</text><text x="470" y="122" font-size="13" class="dim">{t[1]}</text><text x="470" y="144" font-size="13" class="dim">{t[2]}</text>
</svg>"""


def svg_order(t):
    steps = t
    g = ""
    for i, s in enumerate(steps):
        x = 10 + i * 142
        g += f'<rect x="{x}" y="30" width="126" height="54" rx="10" fill="#2563eb" opacity=".12"/><rect x="{x}" y="30" width="126" height="54" rx="10" fill="none" stroke="#2563eb"/><text x="{x + 63}" y="62" text-anchor="middle" font-size="13" font-weight="600">{s}</text>'
        if i < len(steps) - 1:
            g += f'<path d="M{x + 128} 57 h12" stroke="#2563eb" stroke-width="2" marker-end="url(#ar2)"/>'
    return f'<svg viewBox="0 0 720 110" width="720"><defs><marker id="ar2" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10z" fill="#2563eb"/></marker></defs>{g}</svg>'


def svg_stack(t):
    rows = [(t[0], "#64748b", 0, 700), (t[1], "#16a34a", 0, 260), (t[2], "#dc2626", 520, 180), (t[3], "#2563eb", 0, 700), (t[4], "#d97706", 330, 120)]
    g = ""
    for i, (label, col, x, w) in enumerate(rows):
        y = 18 + i * 38
        g += f'<text x="10" y="{y + 18}" font-size="13" font-weight="600">{label}</text><rect x="{190 + x * 0.73}" y="{y + 2}" width="{w * 0.73}" height="24" rx="6" fill="{col}" opacity=".8"/>'
    return f'<svg viewBox="0 0 720 220" width="720">{g}</svg>'


def concepts(doc, G):
    s = doc.section("concepts", G, B("Core concepts", "Konsep dasar"), B("Six ideas that explain how everything in Motionator behaves.", "Enam gagasan yang menjelaskan perilaku semua bagian Motionator."))
    s += [
        H3("composition-concept", "1. The composition", "1. Komposisi"),
        P(
            "A composition is the frame you animate in: a size in pixels, a frame rate, a duration and a background. Everything you export is a render of the composition. A project has one composition; you can import several SVG files into it.",
            "Komposisi adalah bingkai tempat Anda menganimasikan: ukuran dalam piksel, frame rate, durasi, dan background. Semua yang diekspor adalah hasil render komposisi. Satu proyek punya satu komposisi; Anda bisa mengimpor beberapa file SVG ke dalamnya.",
        ),
        TABLE(
            [B("Frame rate", "Frame rate"), B("Typical use", "Penggunaan umum")],
            [
                ["23.976 / 24 fps", B("Cinematic footage; matches film and most stock clips shot on cameras.", "Footage sinematik; cocok dengan film dan kebanyakan klip stok dari kamera.")],
                ["25 / 50 fps", B("PAL regions (Europe, Indonesia broadcast).", "Wilayah PAL (Eropa, siaran Indonesia).")],
                ["29.97 / 30 fps", B("Web video, social media, NTSC regions. A safe default.", "Video web, media sosial, wilayah NTSC. Default yang aman.")],
                ["59.94 / 60 fps", B("Very smooth motion, UI demos, fast-moving graphics.", "Gerakan sangat halus, demo UI, grafis yang bergerak cepat.")],
            ],
        ),
        P(
            "Time is shown as a <b>timecode</b> <code>0:00:02:15</code> = hours : minutes : seconds : frames, so at 30 fps <code>0:00:02:15</code> is 2.5 seconds. Below it the timeline shows the absolute frame number. Internally Motionator counts time in very fine ticks, so changing the frame rate never shifts your animation.",
            "Waktu ditampilkan sebagai <b>timecode</b> <code>0:00:02:15</code> = jam : menit : detik : frame, jadi pada 30 fps <code>0:00:02:15</code> adalah 2,5 detik. Di bawahnya timeline menampilkan nomor frame absolut. Di dalamnya Motionator menghitung waktu dalam satuan tick yang sangat halus, jadi mengubah frame rate tidak menggeser animasi Anda.",
        ),
        H3("hierarchy", "2. Layers and the hierarchy", "2. Layer dan hierarki"),
        DIAGRAM(svg_tree(["Children inherit the parent's transform:", "move, rotate or fade Mark and Ring,", "Wave and Dot follow."]), svg_tree(["Anak mewarisi transform induknya:", "geser, putar, atau pudarkan Mark, maka Ring,", "Wave, dan Dot ikut."])),
        P(
            "Layers form a tree that mirrors the groups in your SVG. A child's transform is relative to its parent: if <code>Wordmark</code> moves 100 px right, every letter inside moves with it, and each letter can still have its own animation on top. This is why good grouping in your design tool matters so much: animate a group to move parts together, animate the children for detail.",
            "Layer membentuk pohon yang mencerminkan grup di SVG Anda. Transform anak relatif terhadap induknya: bila <code>Wordmark</code> bergeser 100 px ke kanan, setiap huruf di dalamnya ikut bergeser, dan setiap huruf tetap bisa punya animasinya sendiri di atasnya. Itulah sebabnya pengelompokan yang baik di aplikasi desain sangat penting: animasikan grup untuk menggerakkan bagian-bagian bersama, animasikan anaknya untuk detail.",
        ),
        P(
            "Opacity multiplies down the tree (a child at 50 % inside a parent at 50 % shows at 25 %). Effects such as Blur, Tint and Reveal apply to the layer and everything inside it.",
            "Opacity dikalikan ke bawah pohon (anak 50 % di dalam induk 50 % tampil 25 %). Efek seperti Blur, Tint, dan Reveal berlaku untuk layer beserta semua isinya.",
        ),
        H3("anchor-concept", "3. The anchor point", "3. Anchor point"),
        DIAGRAM(svg_anchor(["anchor in the centre", "anchor on the corner"]), svg_anchor(["anchor di tengah", "anchor di sudut"])),
        P(
            "Rotation, scale and skew happen around the anchor point (the red crosshair on the canvas). The same 30° rotation looks completely different with the anchor in the centre or on a corner. Position moves the anchor point, so a layer's Position is where its anchor sits in the parent.",
            "Rotasi, skala, dan skew terjadi di sekitar anchor point (tanda silang merah di canvas). Rotasi 30° yang sama terlihat sangat berbeda bila anchor ada di tengah atau di sudut. Position memindah anchor point, jadi Position sebuah layer adalah letak anchor-nya di dalam induk.",
        ),
        UL(
            ("A door or a pendulum (Swing): anchor on the hinge or the top.", "Pintu atau bandul (Swing): anchor di engsel atau di atas."),
            ("A clock hand (Tick, Spin): anchor at the end that stays fixed.", "Jarum jam (Tick, Spin): anchor di ujung yang diam."),
            ("A bouncing ball with squash: anchor at the bottom so it squashes onto the ground.", "Bola memantul dengan squash: anchor di bawah agar memipih ke lantai."),
            ("A logo popping in: anchor in the centre.", "Logo yang muncul membesar: anchor di tengah."),
        ),
        H3("transform-order", "4. Transform order", "4. Urutan transform"),
        DIAGRAM(svg_order(["Anchor", "Scale", "Skew", "Rotation", "Position"]), svg_order(["Anchor", "Skala", "Skew", "Rotasi", "Posisi"])),
        P(
            "Every frame, each layer is placed in this order: the shape is offset so its anchor point is at the origin, then scaled, skewed and rotated around it, then moved to Position, and finally put inside its parent. You never have to think about this while working, but it explains why scaling never moves the anchor point and why rotating a parent swings its children around the parent's anchor.",
            "Di setiap frame, setiap layer ditempatkan dengan urutan ini: bentuk digeser agar anchor point-nya di titik asal, lalu diskala, dimiringkan, dan diputar di sekitarnya, lalu dipindah ke Position, dan akhirnya dimasukkan ke induknya. Anda tidak perlu memikirkannya saat bekerja, tetapi ini menjelaskan kenapa skala tidak pernah memindah anchor point dan kenapa memutar induk membuat anaknya berayun di sekitar anchor induk.",
        ),
        H3("rest-pose", "5. The rest pose", "5. Pose diam"),
        P(
            "The <b>rest pose</b> is how the layer looks in your SVG file: its original position, size and rotation. Presets are relative to it: <i>Slide In ←</i> always ends exactly at the rest pose, wherever that is. <b>Reset Transform</b> brings a layer back to it, and <b>Save as Preset</b> stores motion as changes from it, which is why your presets work on other layers.",
            "<b>Pose diam</b> adalah tampilan layer di file SVG Anda: posisi, ukuran, dan rotasi aslinya. Preset bersifat relatif terhadapnya: <i>Slide In ←</i> selalu berakhir tepat di pose diam, di mana pun letaknya. <b>Reset Transform</b> mengembalikan layer ke pose ini, dan <b>Simpan sebagai Preset</b> menyimpan gerakan sebagai perubahan dari pose ini, itulah sebabnya preset Anda bisa dipakai di layer lain.",
        ),
        H3("evaluation", "6. How a frame is calculated", "6. Cara sebuah frame dihitung"),
        DIAGRAM(
            svg_stack(["Rest pose", "Keyframes", "Enter / Exit", "Loop", "Emphasis"]),
            svg_stack(["Pose diam", "Keyframe", "Enter / Exit", "Loop", "Emphasis"]),
        ),
        STEPS(
            ("Start from the rest pose (or the keyframed value, if the property has keyframes).", "Mulai dari pose diam (atau nilai keyframe, bila properti punya keyframe)."),
            ("Enter and Exit presets that are active at this time replace the value; the one that starts last wins.", "Preset Enter dan Exit yang aktif pada waktu ini menggantikan nilainya; yang mulai paling akhir yang menang."),
            ("Loop and Emphasis presets add their motion on top.", "Preset Loop dan Emphasis menambahkan gerakannya di atasnya."),
            ("The parent's result is applied, then the layer is drawn with its effects.", "Hasil induk diterapkan, lalu layer digambar dengan efeknya."),
        ),
        P(
            "Because of this order you can freely mix methods: keyframe a logo's position across the screen, add <i>Fade In</i> at the start and <i>Float</i> for the whole clip, and all three work together.",
            "Karena urutan ini Anda bebas mencampur cara: beri keyframe pada posisi logo melintasi layar, tambahkan <i>Fade In</i> di awal dan <i>Float</i> sepanjang klip, dan ketiganya bekerja bersama.",
        ),
        TIP(
            "Everything is non-destructive: presets are calculated live and never baked into your project unless you choose Bake to Keyframes. Delete a preset and the layer is exactly as before.",
            "Semuanya non-destruktif: preset dihitung langsung dan tidak pernah di-bake ke proyek kecuali Anda memilih Bake ke Keyframe. Hapus preset dan layer kembali persis seperti sebelumnya.",
        ),
    ]


# ---------------------------------------------------------------- preparing SVG, in more depth


def svg_prep_extra():
    return [
        H3("good-structure", "A well-structured SVG", "SVG yang tersusun baik"),
        P(
            "This is the structure of <code>samples/logo.svg</code>. Groups with ids become layers that can move as a unit; paths with ids inside them can be animated on their own. Strokes are used where the line should draw on.",
            "Ini struktur <code>samples/logo.svg</code>. Grup ber-id menjadi layer yang bisa bergerak sebagai satu kesatuan; path ber-id di dalamnya bisa dianimasikan sendiri. Stroke dipakai pada garis yang akan tergambar.",
        ),
        CODE("""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 220">
  <g id="Mark">                     <!-- layer: the symbol -->
    <circle id="Ring" … fill="none" stroke="#e2381d" stroke-width="14"/>
    <path   id="Wave" … fill="none" stroke="#7c3aed" stroke-width="12"/>
    <circle id="Dot"  … fill="#111827"/>
  </g>
  <g id="Wordmark">                 <!-- layer: the name -->
    <path id="Letter_M" …/>  <path id="Letter_O" …/>
    <path id="Letter_V" …/>  <path id="Letter_E" …/>
  </g>
  <path id="Underline" … stroke="#e2381d"/>
</svg>"""),
        H3("illustrator-steps", "Step by step: Adobe Illustrator", "Langkah demi langkah: Adobe Illustrator"),
        STEPS(
            ("Put each part you want to animate on its own layer or sub-layer, and name it in the Layers panel (double-click the name).", "Taruh setiap bagian yang ingin dianimasikan di layer atau sub-layer sendiri, dan beri nama di panel Layers (klik dua kali namanya)."),
            ("Select text and choose <b>Type ▸ Create Outlines</b> [[Ctrl+Shift+O]]. Keep a copy of the editable file.", "Pilih teks lalu <b>Type ▸ Create Outlines</b> [[Ctrl+Shift+O]]. Simpan salinan file yang masih bisa diedit."),
            ("Expand appearances and brushes you want as plain shapes (<b>Object ▸ Expand Appearance</b>), but keep strokes as strokes for Trim Paths.", "Expand appearance dan brush yang ingin dijadikan bentuk biasa (<b>Object ▸ Expand Appearance</b>), tetapi biarkan stroke tetap stroke untuk Trim Paths."),
            ("Set the artboard to the area of the artwork (<b>Object ▸ Artboards ▸ Fit to Artwork Bounds</b>).", "Atur artboard sesuai area artwork (<b>Object ▸ Artboards ▸ Fit to Artwork Bounds</b>)."),
            ("<b>File ▸ Export ▸ Export As…</b>, format SVG, tick <i>Use Artboards</i>. In the options: Styling <i>Presentation Attributes</i>, Font <i>Convert to Outlines</i>, Images <i>Embed</i>, Object IDs <i>Layer Names</i>, Decimal <i>2</i>, untick <i>Minify</i>.", "<b>File ▸ Export ▸ Export As…</b>, format SVG, centang <i>Use Artboards</i>. Di opsinya: Styling <i>Presentation Attributes</i>, Font <i>Convert to Outlines</i>, Images <i>Embed</i>, Object IDs <i>Layer Names</i>, Decimal <i>2</i>, jangan centang <i>Minify</i>."),
        ),
        H3("figma-steps", "Step by step: Figma", "Langkah demi langkah: Figma"),
        STEPS(
            ("Build the artwork inside a frame. Name layers and groups in the layers list.", "Buat artwork di dalam frame. Beri nama layer dan grup di daftar layer."),
            ("Select text and use <b>Outline stroke</b>/<b>Flatten</b> only where needed; Figma exports text as paths when <i>Outline text</i> is on.", "Pilih teks dan pakai <b>Outline stroke</b>/<b>Flatten</b> hanya bila perlu; Figma mengekspor teks sebagai path bila <i>Outline text</i> aktif."),
            ("Select the frame, add an export setting <b>SVG</b>, open its options and tick <i>Include \"id\" attribute</i> and <i>Outline text</i>.", "Pilih frame, tambahkan export setting <b>SVG</b>, buka opsinya lalu centang <i>Include \"id\" attribute</i> dan <i>Outline text</i>."),
            ("Export. Auto-layout frames become plain groups, which is fine.", "Ekspor. Frame auto-layout menjadi grup biasa, dan itu tidak masalah."),
        ),
        H3("inkscape-steps", "Step by step: Inkscape", "Langkah demi langkah: Inkscape"),
        STEPS(
            ("Group parts with [[Ctrl+G]] and set each group's <b>ID</b> in <b>Object ▸ Object Properties</b>, then click <i>Set</i>.", "Kelompokkan bagian dengan [[Ctrl+G]] dan isi <b>ID</b> tiap grup di <b>Object ▸ Object Properties</b>, lalu klik <i>Set</i>."),
            ("Convert text with <b>Path ▸ Object to Path</b> [[Shift+Ctrl+C]].", "Ubah teks dengan <b>Path ▸ Object to Path</b> [[Shift+Ctrl+C]]."),
            ("<b>Document Properties</b> ▸ <i>Resize to content</i>, then <b>Save As ▸ Plain SVG</b>.", "<b>Document Properties</b> ▸ <i>Resize to content</i>, lalu <b>Save As ▸ Plain SVG</b>."),
        ),
        H3("svg-size", "Size and resolution", "Ukuran dan resolusi"),
        P(
            "SVG is resolution-independent: a 600 px wide logo renders razor-sharp in a 4K composition, because every frame is drawn from the vectors. The <code>viewBox</code> of the file only sets the starting size. Scale the SVG root layer up in Motionator rather than exporting a bigger SVG.",
            "SVG tidak bergantung resolusi: logo selebar 600 px tetap tajam di komposisi 4K, karena setiap frame digambar dari vektornya. <code>viewBox</code> file hanya menentukan ukuran awal. Perbesar layer root SVG di Motionator daripada mengekspor SVG yang lebih besar.",
        ),
        WARN(
            "Very complex files (tens of thousands of paths, heavy blur filters, large embedded photos) render slowly at 4K. Simplify paths (Illustrator: <i>Object ▸ Path ▸ Simplify</i>) and avoid unnecessary filters.",
            "File yang sangat rumit (puluhan ribu path, filter blur berat, foto besar yang di-embed) dirender lambat di 4K. Sederhanakan path (Illustrator: <i>Object ▸ Path ▸ Simplify</i>) dan hindari filter yang tidak perlu.",
        ),
    ]


# ---------------------------------------------------------------- menu reference


def menu_reference(doc, G):
    s = doc.section("menu-reference", G, B("Menu reference", "Referensi menu"), B("Every command in every menu, what it does and its shortcut.", "Semua perintah di setiap menu, fungsinya, dan shortcut-nya."))

    def k(*keys):
        return " ".join(kbd(x) for x in keys)

    menus = [
        ("File", "menu-file", [
            (B("New Project", "Proyek Baru"), k("Ctrl+Alt+N"), B("Starts an empty project (asks to save changes first).", "Memulai proyek kosong (bertanya dulu untuk menyimpan perubahan).")),
            (B("Open Project…", "Buka Proyek…"), k("Ctrl+O"), B("Opens a <code>.motionator</code> file.", "Membuka file <code>.motionator</code>.")),
            (B("Save / Save As…", "Simpan / Simpan Sebagai…"), k("Ctrl+S") + " " + k("Ctrl+Shift+S"), B("Saves the project; Save As picks a new name.", "Menyimpan proyek; Simpan Sebagai memilih nama baru.")),
            (B("Import SVG…", "Impor SVG…"), k("Ctrl+I"), B("Adds an SVG file to the composition as a new root layer.", "Menambahkan file SVG ke komposisi sebagai layer root baru.")),
            (B("Import Audio…", "Impor Audio…"), k("Ctrl+Alt+I"), B("Sets the project's soundtrack (replaces the current one).", "Mengatur trek audio proyek (menggantikan yang ada).")),
            (B("Export Animated SVG…", "Ekspor SVG Animasi…"), k("Ctrl+Alt+G"), B("Opens the animated SVG export dialog.", "Membuka dialog ekspor SVG animasi.")),
            (B("Export Lottie…", "Ekspor Lottie…"), k("Ctrl+Alt+L"), B("Opens the Lottie export dialog.", "Membuka dialog ekspor Lottie.")),
            (B("Exit", "Keluar"), k("Ctrl+Q"), B("Closes Motionator (asks to save changes).", "Menutup Motionator (bertanya untuk menyimpan perubahan).")),
        ]),
        ("Edit", "menu-edit", [
            ("Undo / Redo", k("Ctrl+Z") + " " + k("Ctrl+Shift+Z") + " " + k("Ctrl+Y"), B("Steps back and forward through every change, including preset and keyframe edits.", "Mundur dan maju di setiap perubahan, termasuk edit preset dan keyframe.")),
            (B("Delete", "Hapus"), k("Delete"), B("Deletes what is selected: keyframes, a preset bar, the audio track or a whole SVG.", "Menghapus yang terpilih: keyframe, bar preset, trek audio, atau seluruh SVG.")),
            (B("Deselect All", "Batalkan Semua Pilihan"), k("Ctrl+Shift+A"), B("Clears the selection; the Properties panel then shows the composition.", "Mengosongkan seleksi; panel Properties lalu menampilkan komposisi.")),
            (B("Preferences…", "Preferensi…"), k("Ctrl+Alt+;"), B("Language, theme and auto-save.", "Bahasa, tema, dan auto-save.")),
        ]),
        ("Composition", None, [
            (B("Composition Settings…", "Pengaturan Komposisi…"), k("Ctrl+K"), B("Shows the composition settings in the Properties panel.", "Menampilkan pengaturan komposisi di panel Properties.")),
            (B("Add to Render Queue", "Tambah ke Render Queue"), k("Ctrl+M"), B("Adds the composition to the Render Queue and shows it.", "Menambahkan komposisi ke Render Queue dan menampilkannya.")),
        ]),
        ("Layer", None, [
            (B("Center Anchor Point", "Pusatkan Anchor Point"), k("Ctrl+Alt+Home"), B("Moves the anchor to the centre of the layer without moving the layer.", "Memindah anchor ke tengah layer tanpa memindah layer.")),
            ("Reset Transform", "", B("Returns the selected layer to its rest pose.", "Mengembalikan layer terpilih ke pose diamnya.")),
        ]),
        ("Animation", "menu-animation", [
            (B("Apply Preset…", "Terapkan Preset…"), "", B("Shows the Presets panel; double-click a preset there.", "Menampilkan panel Presets; klik dua kali preset di sana.")),
            (B("Bake to Keyframes", "Bake ke Keyframe"), "", B("Turns the layer's presets into keyframes.", "Mengubah preset layer menjadi keyframe.")),
            (B("Save as Preset…", "Simpan sebagai Preset…"), "", B("Saves the layer's keyframes as your own preset.", "Menyimpan keyframe layer sebagai preset sendiri.")),
            ("Easy Ease / In / Out", k("F9") + " " + k("Shift+F9") + " " + k("Ctrl+Shift+F9"), B("Eases the selected keyframes.", "Memberi easing pada keyframe terpilih.")),
            (B("Previous / Next Keyframe", "Keyframe sebelumnya / berikutnya"), k("J") + " " + k("K"), B("Moves the playhead to the nearest keyframe of the selected layer.", "Memindah playhead ke keyframe terdekat pada layer terpilih.")),
            (B("Reveal Animated Properties", "Tampilkan properti beranimasi"), k("U"), B("Opens all layers that have keyframes, showing only animated properties.", "Membuka semua layer yang punya keyframe, hanya menampilkan properti yang beranimasi.")),
            ("Graph Editor", k("Shift+F3"), B("Toggles the Graph Editor in the timeline.", "Menyalakan/mematikan Graph Editor di timeline.")),
        ]),
        ("View", None, [
            ("Grid", k("Ctrl+'"), B("Shows a grid over the composition.", "Menampilkan grid di atas komposisi.")),
            (B("Transparency Grid", "Grid Transparansi"), "", B("Shows a chequerboard behind transparent compositions.", "Menampilkan kotak-kotak di belakang komposisi transparan.")),
            ("Safe Area", "", B("Shows action-safe and title-safe margins for video.", "Menampilkan margin action-safe dan title-safe untuk video.")),
            ("Snapping", k("Ctrl+Shift+;"), B("The snapping switch (also in the toolbar). In this version dragging does not snap yet; the setting is kept for when it does.", "Sakelar snapping (juga ada di toolbar). Di versi ini menyeret belum menempel; pengaturannya disimpan untuk saat fitur itu hadir.")),
            (B("Zoom In / Out", "Perbesar / Perkecil"), k(".") + " " + k(","), B("Zooms the canvas.", "Memperbesar/memperkecil canvas.")),
            (B("Actual Size / Fit", "Ukuran Asli / Sesuaikan"), k("/") + " " + k("Shift+/"), B("100 % zoom, or fit the composition to the panel.", "Zoom 100 %, atau sesuaikan komposisi dengan panel.")),
        ]),
        ("Window", "menu-window", [
            ("Workspace: Simple / Advanced / Minimal", k("Shift+F10") + " " + k("Shift+F11") + " " + k("Shift+F12"), B("Switches workspace.", "Berganti workspace.")),
            (B("Dark / Darker Theme", "Tema Dark / Darker"), "", B("Changes the colour theme.", "Mengubah tema warna.")),
            (B("Panels", "Panel"), "", B("Composition, Layers, Timeline, Render Queue, Properties, Presets, Align: shows the panel (opening it again if it was closed).", "Composition, Layers, Timeline, Render Queue, Properties, Presets, Align: menampilkan panel (membukanya lagi bila tertutup).")),
            (B("Reset Layout", "Reset Tata Letak"), "", B("Restores the default arrangement of the current workspace.", "Mengembalikan susunan default workspace saat ini.")),
            (B("Saved Layouts…", "Tata Letak Tersimpan…"), "", B("Saves, applies and deletes named arrangements.", "Menyimpan, memakai, dan menghapus susunan bernama.")),
        ]),
        ("Help", None, [
            (B("About Motionator", "Tentang Motionator"), "", B("Version, licences and the open-source components.", "Versi, lisensi, dan komponen open-source.")),
        ]),
    ]
    for name, shot, rows in menus:
        s.append(H3(f"menu-{name.lower()}", f"{name} menu", f"Menu {name}"))
        if shot == "menu-edit":
            s.append(IMG(shot, "The Edit menu.", "Menu Edit.", "medium"))
        s.append(TABLE([B("Command", "Perintah"), B("Shortcut", "Shortcut"), B("What it does", "Fungsinya")], [list(r) for r in rows]))
    s.append(NOTE("Greyed-out items need a selection first (for example a layer for Bake to Keyframes, or keyframes for Easy Ease).", "Item yang abu-abu butuh seleksi dulu (misalnya layer untuk Bake ke Keyframe, atau keyframe untuk Easy Ease)."))


# ---------------------------------------------------------------- preset reference

TIPS = {
    "enter.fade": ("The safest entrance: combine it with any move for a softer start. Use 0.3–0.6 s for UI, up to 1.5 s for calm backgrounds.", "Masuk paling aman: gabungkan dengan gerakan apa pun agar awalnya lebih lembut. Pakai 0,3–0,6 s untuk UI, sampai 1,5 s untuk background yang tenang."),
    "enter.slide_left": ("Good for text and cards entering in reading order. Keep the distance small (40–120 px) for elegance, large for drama.", "Cocok untuk teks dan kartu yang masuk sesuai arah baca. Jarak kecil (40–120 px) terkesan elegan, jarak besar terkesan dramatis."),
    "enter.slide_right": ("Use for elements on the right side of the frame so they arrive from the nearest edge.", "Pakai untuk elemen di sisi kanan bingkai agar datang dari tepi terdekat."),
    "enter.slide_up": ("The classic title move. With stagger on lines of text it reads naturally top to bottom.", "Gerakan judul klasik. Dengan stagger pada baris teks, urutannya terbaca alami dari atas ke bawah."),
    "enter.slide_down": ("Works for things that hang or drop into place: banners, labels, price tags.", "Cocok untuk benda yang menggantung atau turun ke tempatnya: banner, label, label harga."),
    "enter.scale_pop": ("The go-to for icons, buttons and badges. The slight overshoot makes it feel alive; keep the anchor in the centre.", "Pilihan utama untuk ikon, tombol, dan badge. Sedikit overshoot membuatnya terasa hidup; biarkan anchor di tengah."),
    "enter.rotate_in": ("Adds energy to logos and stickers. Combine with a centred anchor so it does not swing.", "Menambah energi pada logo dan stiker. Pakai anchor di tengah agar tidak berayun."),
    "enter.bounce_in": ("Playful: cartoon objects, kids content, fun call-outs. Too much bounce feels cheap in corporate work.", "Ceria: objek kartun, konten anak, ajakan yang lucu. Pantulan berlebihan terasa murahan untuk pekerjaan korporat."),
    "enter.elastic_pop": ("A springier Scale Pop. Great for a logo dot, a notification badge or a like icon.", "Scale Pop yang lebih kenyal. Bagus untuk titik logo, badge notifikasi, atau ikon like."),
    "enter.drop": ("Feels heavy, like gravity. Pair it with a Squash emphasis on landing.", "Terasa berat seperti gravitasi. Pasangkan dengan emphasis Squash saat mendarat."),
    "enter.zoom_in": ("Cinematic for big titles: the element settles into place from the camera's side.", "Sinematik untuk judul besar: elemen turun ke tempatnya seolah dari arah kamera."),
    "enter.fly_in": ("For dynamic compositions where elements come from a corner; choose the corner in the parameters.", "Untuk komposisi dinamis dengan elemen yang datang dari sudut; pilih sudutnya di parameter."),
    "enter.spiral_in": ("Eye-catching for stickers and badges. Use sparingly: one spiral per scene is plenty.", "Menarik perhatian untuk stiker dan badge. Pakai seperlunya: satu spiral per adegan sudah cukup."),
    "enter.roll_in": ("For round things: wheels, coins, balls. The rotation matches the distance travelled.", "Untuk benda bulat: roda, koin, bola. Rotasinya sesuai jarak tempuh."),
    "enter.flip_in_x": ("Card and tile reveals. Looks 3D without any 3D setup.", "Membuka kartu dan ubin. Terlihat 3D tanpa perlu pengaturan 3D."),
    "enter.flip_in_y": ("Like Flip In X but vertical: good for counters and rows of tiles.", "Seperti Flip In X tetapi vertikal: bagus untuk penghitung dan deretan ubin."),
    "enter.pop_up": ("Ideal for letters and list items with stagger: each rises and overshoots slightly.", "Ideal untuk huruf dan item daftar dengan stagger: masing-masing naik dan sedikit overshoot."),
    "enter.swing_in": ("Hanging signs and pendants. Put the anchor on the hinge with the Anchor Point tool first.", "Papan gantung dan liontin. Taruh anchor di engsel dengan tool Anchor Point terlebih dulu."),
    "enter.stretch_in": ("Gives cartoon squash-and-stretch energy to simple shapes.", "Memberi energi squash-and-stretch kartun pada bentuk sederhana."),
    "enter.draw_on": ("The signature logo reveal: strokes draw from start to end. Path direction in your SVG decides where it starts.", "Logo reveal khas: stroke tergambar dari awal ke akhir. Arah path di SVG menentukan titik mulainya."),
    "enter.draw_center": ("Symmetric reveals: underlines, frames and dividers growing from the middle.", "Reveal simetris: garis bawah, bingkai, dan pembatas yang tumbuh dari tengah."),
    "enter.blur_in": ("Soft and modern, good for backgrounds and quotes. Blur is not in Lottie; use it for video and SVG.", "Lembut dan modern, cocok untuk background dan kutipan. Blur tidak ada di Lottie; pakai untuk video dan SVG."),
    "enter.shear_in": ("Fast, sporty feel for headlines and sale banners.", "Kesan cepat dan sporty untuk headline dan banner diskon."),
    "enter.wipe": ("Reveals filled shapes cleanly: bars, underlines, panels. Choose the side in <i>From</i>.", "Memunculkan bentuk berisi dengan rapi: bar, garis bawah, panel. Pilih sisinya di <i>Dari</i>."),
    "enter.iris": ("A circular reveal: photos in circles, avatars, spotlight effects.", "Reveal melingkar: foto dalam lingkaran, avatar, efek sorotan."),
    "enter.split": ("Opens a panel from the centre line, like doors opening.", "Membuka panel dari garis tengah, seperti pintu yang terbuka."),
    "exit.fade": ("The neutral exit. Placed at the end of the composition automatically.", "Keluar yang netral. Otomatis diletakkan di akhir komposisi."),
    "exit.scale": ("A tidy exit for icons and badges; the reverse of Scale Pop.", "Keluar yang rapi untuk ikon dan badge; kebalikan Scale Pop."),
    "exit.slide_left": ("Pairs with Slide In → for elements that pass through the frame.", "Berpasangan dengan Slide In → untuk elemen yang melintasi bingkai."),
    "exit.slide_right": ("Pairs with Slide In ← for continuous left-to-right motion.", "Berpasangan dengan Slide In ← untuk gerakan kiri-ke-kanan yang berkesinambungan."),
    "exit.slide_up": ("Clears titles upwards, like credits rolling.", "Menghapus judul ke atas, seperti kredit film."),
    "exit.slide_down": ("Drops elements out of the frame; feels like letting go.", "Menjatuhkan elemen keluar bingkai; terasa seperti dilepaskan."),
    "exit.rotate_out": ("The reverse of Rotate In.", "Kebalikan Rotate In."),
    "exit.bounce_out": ("A playful goodbye: a small hop, then a fall.", "Perpisahan yang ceria: lompatan kecil, lalu jatuh."),
    "exit.zoom_out": ("Feels like the element flies towards the camera.", "Terasa seperti elemen terbang ke arah kamera."),
    "exit.fly_out": ("Diagonal exit; choose the corner.", "Keluar diagonal; pilih sudutnya."),
    "exit.spiral_out": ("The reverse of Spiral In: a whirl away.", "Kebalikan Spiral In: berputar menghilang."),
    "exit.roll_out": ("Round objects rolling off to the right.", "Benda bulat yang menggelinding ke kanan."),
    "exit.flip_out_x": ("Card flip away; pairs with Flip In X on the next card.", "Kartu yang berbalik pergi; berpasangan dengan Flip In X pada kartu berikutnya."),
    "exit.flip_out_y": ("Vertical flip away.", "Berbalik pergi secara vertikal."),
    "exit.sink": ("A gentle, quiet exit for secondary elements.", "Keluar yang lembut dan tenang untuk elemen pendukung."),
    "exit.collapse": ("Like a TV switching off: good for ends of scenes.", "Seperti TV dimatikan: bagus untuk akhir adegan."),
    "exit.draw_off": ("Strokes erase themselves; the mirror of Draw On.", "Stroke menghapus dirinya; cermin dari Draw On."),
    "exit.blur_out": ("Dreamy exit; video and SVG only (no blur in Lottie).", "Keluar yang lembut; hanya video dan SVG (tidak ada blur di Lottie)."),
    "exit.wipe": ("Hides bars and panels towards a side.", "Menyembunyikan bar dan panel ke arah satu sisi."),
    "exit.iris": ("Closes to a circle, like the classic cartoon ending.", "Menutup menjadi lingkaran, seperti akhir film kartun klasik."),
    "loop.float": ("Makes still elements feel alive. For seamless clips make the period divide the duration (2 s in a 10 s clip).", "Membuat elemen diam terasa hidup. Untuk klip mulus, buat periode habis membagi durasi (2 s pada klip 10 s)."),
    "loop.pulse": ("Draws attention to a button or a dot. Small amounts (4–8 %) look premium.", "Menarik perhatian ke tombol atau titik. Nilai kecil (4–8 %) terlihat premium."),
    "loop.spin": ("Loaders, gears, suns. A symmetric shape loops seamlessly even when the period is longer than the clip.", "Loader, roda gigi, matahari. Bentuk simetris tetap mulus meskipun periodenya lebih panjang dari klip."),
    "loop.swing": ("Pendulums, hanging signs, leaves. Anchor = pivot.", "Bandul, papan gantung, daun. Anchor = poros."),
    "loop.breathe": ("Slow, calm motion for meditation, wellness and ambient backgrounds.", "Gerakan pelan dan tenang untuk meditasi, wellness, dan background ambient."),
    "loop.blink": ("Eyes, cursors and indicator lights.", "Mata, kursor, dan lampu indikator."),
    "loop.orbit": ("Planets, particles, decorative dots circling their spot.", "Planet, partikel, titik dekoratif yang mengitari tempatnya."),
    "loop.figure8": ("An organic, wandering path for insects, sparks and floating particles.", "Lintasan organik yang mengembara untuk serangga, percikan, dan partikel melayang."),
    "loop.bounce": ("A ball or character hopping in place. Anchor at the bottom for a nice squash.", "Bola atau karakter melompat di tempat. Anchor di bawah agar squash-nya bagus."),
    "loop.wobble": ("Jelly-like idle motion for mascots and blobs.", "Gerakan diam seperti jeli untuk maskot dan bentuk blob."),
    "loop.glow": ("Lights, stars, neon signs. Lower <i>min</i> for a stronger flicker.", "Lampu, bintang, papan neon. Turunkan <i>min</i> untuk kedip yang lebih kuat."),
    "loop.drift": ("Bubbles, dust, clouds. Give each item a different period for natural variety.", "Gelembung, debu, awan. Beri periode berbeda pada setiap item agar variasinya alami."),
    "loop.hover": ("Floating objects with a gentle tilt: drones, balloons, product shots.", "Benda melayang dengan sedikit miring: drone, balon, foto produk."),
    "loop.tick": ("Clock hands and step-by-step rotation. Set steps to 60 for a seconds hand.", "Jarum jam dan rotasi bertahap. Atur steps ke 60 untuk jarum detik."),
    "loop.trace": ("A light running along a line: circuits, routes on a map, neon outlines.", "Cahaya yang berjalan di sepanjang garis: sirkuit, rute di peta, garis neon."),
    "loop.sway": ("Plants, grass, flags and waves moving in the wind.", "Tanaman, rumput, bendera, dan ombak yang bergerak tertiup angin."),
    "loop.tint_pulse": ("Colour breathing: alerts, highlights, mood changes.", "Warna yang bernapas: peringatan, sorotan, perubahan suasana."),
    "emphasis.shake": ("Errors, wrong answers, impact moments.", "Kesalahan, jawaban salah, momen benturan."),
    "emphasis.heartbeat": ("Likes, love, health topics, “buy now” moments.", "Like, cinta, topik kesehatan, momen “beli sekarang”."),
    "emphasis.tada": ("Celebrations and achievements.", "Perayaan dan pencapaian."),
    "emphasis.jello": ("Playful attention grabber for mascots and buttons.", "Penarik perhatian yang ceria untuk maskot dan tombol."),
    "emphasis.wiggle": ("Hand-made, nervous or electric motion. Change the seed for a different pattern.", "Gerakan buatan tangan, gugup, atau bertenaga listrik. Ganti seed untuk pola berbeda."),
    "emphasis.flash": ("Blinks a few times: notifications, “new”, alerts.", "Berkedip beberapa kali: notifikasi, “baru”, peringatan."),
    "emphasis.rubber_band": ("Stretchy squish for cartoon buttons and icons.", "Pipih kenyal untuk tombol dan ikon kartun."),
    "emphasis.head_shake": ("Saying “no”: wrong answers, rejected actions.", "Mengatakan “tidak”: jawaban salah, aksi yang ditolak."),
    "emphasis.nod": ("Saying “yes”: confirmations and agreement.", "Mengatakan “ya”: konfirmasi dan persetujuan."),
    "emphasis.spin": ("A full turn to celebrate or to switch state (refresh icons).", "Satu putaran penuh untuk merayakan atau berganti keadaan (ikon refresh)."),
    "emphasis.flip": ("Turn a card or coin over once.", "Membalik kartu atau koin satu kali."),
    "emphasis.pop": ("A quick “look here” for logos and prices. Used at 3 s on the logo sample.", "“Lihat ke sini” yang cepat untuk logo dan harga. Dipakai di detik 3 pada contoh logo."),
    "emphasis.squash": ("Landing impact after a Drop or Bounce In. Anchor at the bottom.", "Benturan mendarat setelah Drop atau Bounce In. Anchor di bawah."),
    "emphasis.nudge": ("A small push to suggest direction: arrows, “swipe” hints.", "Dorongan kecil untuk menunjukkan arah: panah, petunjuk “geser”."),
    "emphasis.swing": ("A sign swinging after being hit; anchor = pivot.", "Papan yang berayun setelah tersenggol; anchor = poros."),
    "emphasis.focus": ("Briefly out of focus, then sharp: rack-focus feel.", "Sesaat tidak fokus, lalu tajam: kesan rack focus kamera."),
    "emphasis.lean": ("Leans and springs back: excitement, a gust of wind.", "Miring lalu kembali memantul: antusiasme, embusan angin."),
    "emphasis.color_flash": ("Flashes a colour: hits, highlights, “on sale” moments.", "Kilatan warna: benturan, sorotan, momen “diskon”."),
    "emphasis.jump": ("A happy double jump for characters and icons.", "Lompatan ganda yang ceria untuk karakter dan ikon."),
}

CAT = {"enter": ("Enter", B("Enter presets", "Preset Enter")), "exit": ("Exit", B("Exit presets", "Preset Exit")), "loop": ("Loop", B("Loop presets", "Preset Loop")), "emphasis": ("Emphasis", B("Emphasis presets", "Preset Emphasis"))}


def num(v):
    return f"{v:g}"


def preset_reference(doc, G, names):
    data = json.load(io.open(os.path.join(HERE, "data", "presets.json"), encoding="utf-8"))
    s = doc.section("preset-reference", G, B("Preset reference", "Referensi preset"), B("Every preset with frames rendered by Motionator, its default length, its parameters and when to use it.", "Setiap preset dengan frame yang dirender Motionator, durasi default, parameter, dan kapan memakainya."))
    s += [
        P(
            "Each strip shows five moments of the preset on a demo tile, from the start (left) to the end (right). The dashed outline marks the layer's rest pose. Loops show two seconds. Every parameter can be changed after applying, in the Properties panel.",
            "Setiap strip menampilkan lima momen preset pada ubin contoh, dari awal (kiri) sampai akhir (kanan). Garis putus-putus menandai pose diam layer. Loop menampilkan dua detik. Setiap parameter bisa diubah setelah diterapkan, di panel Properties.",
        ),
    ]
    order = ["enter", "exit", "loop", "emphasis"]
    for cat in order:
        tagname, title = CAT[cat]
        s.append(RAW(f'<h3 id="ref-{cat}">{bi(title["en"], title["id"])}<a class="anchor" href="#ref-{cat}">#</a></h3>'))
        for p in [x for x in data if x["category"] == cat]:
            pid = "p-" + p["id"].replace(".", "-").replace("_", "-")
            if p["duration"]:
                dur = bi(f"Default length {num(p['duration'])} s", f"Durasi default {num(p['duration'])} s")
            else:
                dur = bi("Runs for the whole composition", "Berjalan sepanjang komposisi")
            times = "".join(f"<span>{t:.2f} s</span>" for t in p["times"])
            rows = ""
            for q in p["params"]:
                if q["kind"] == "number":
                    unit = f" {q['unit']}" if q["unit"] else ""
                    rng = f"{num(q['min'])} – {num(q['max'])}{unit}"
                    dflt = f"{num(q['default'])}{unit}"
                elif q["kind"] == "choice":
                    rng = ", ".join(bi(o["label"]["en"], o["label"]["id"]) for o in q["options"])
                    d = next((o for o in q["options"] if o["value"] == q["default"]), None)
                    dflt = bi(d["label"]["en"], d["label"]["id"]) if d else q["default"]
                elif q["kind"] == "ease":
                    rng = bi("any easing curve (see Easing reference)", "kurva easing apa pun (lihat Referensi easing)")
                    dflt = names.get(q["default"], q["default"])
                else:
                    rng = bi("any colour", "warna apa pun")
                    dflt = f'<span style="display:inline-block;width:12px;height:12px;border-radius:3px;border:1px solid #999;background:{q["default"]};vertical-align:-1px"></span> <code>{q["default"]}</code>'
                rows += f"<tr><td>{bi(q['label']['en'], q['label']['id'])}</td><td>{rng}</td><td>{dflt}</td></tr>"
            table = (
                f'<div class="table-wrap"><table><thead><tr><th>{bi("Parameter", "Parameter")}</th><th>{bi("Range / options", "Rentang / pilihan")}</th><th>{bi("Default", "Default")}</th></tr></thead><tbody>{rows}</tbody></table></div>'
                if rows
                else f'<p class="meta">{bi("No parameters: only Start and Duration.", "Tanpa parameter: hanya Mulai dan Durasi.")}</p>'
            )
            tip = TIPS.get(p["id"])
            tip_html = f"<p>💡 {bi(tip[0], tip[1])}</p>" if tip else ""
            s.append(RAW(f'<h3 id="{pid}" class="preset-title">{p["name"]} <span class="tag {cat}">{tagname}</span><a class="anchor" href="#{pid}">#</a></h3>'))
            s.append(
                RAW(
                    f'<div class="preset"><p class="meta">{bi(p["description"]["en"], p["description"]["id"])} · {dur} · <code>{p["id"]}</code></p>'
                    f'<div class="frames"><img src="img/presets/{p["id"]}.png" alt="{p["name"]}" loading="lazy"></div><div class="times">{times}</div>'
                    f"{tip_html}{table}</div>"
                )
            )


# ---------------------------------------------------------------- easing reference


def easing_names():
    src = io.open(os.path.join(APP, "crates", "motion_core", "src", "easing.rs"), encoding="utf-8").read()
    return [(n, [float(x) for x in p.split(",")]) for n, p in re.findall(r'\("(\w+)", \[([-\d., ]+)\]\)', src)]


PRETTY = {"linear": "Linear", "easyEase": "Easy Ease"}


def pretty(n):
    if n in PRETTY:
        return PRETTY[n]
    return re.sub(r"([A-Z])", r" \1", n).strip().title().replace("In Out", "In-Out")


def curve_svg(p):
    x1, y1, x2, y2 = p
    lo, hi = min(0, y1, y2), max(1, y1, y2)
    span = hi - lo
    Y = lambda y: 10 + (hi - y) / span * 100
    X = lambda x: 10 + x * 100
    return (
        f'<svg viewBox="0 0 120 120"><rect x="10" y="{Y(1):.1f}" width="100" height="{Y(0) - Y(1):.1f}" fill="none" stroke="currentColor" stroke-opacity=".15"/>'
        f'<path d="M{X(0)} {Y(0):.1f} L{X(x1):.1f} {Y(y1):.1f} M{X(1)} {Y(1):.1f} L{X(x2):.1f} {Y(y2):.1f}" stroke="#94a3b8" stroke-width="1.2"/>'
        f'<path d="M{X(0)} {Y(0):.1f} C{X(x1):.1f} {Y(y1):.1f} {X(x2):.1f} {Y(y2):.1f} {X(1)} {Y(1):.1f}" fill="none" stroke="#e2381d" stroke-width="3" stroke-linecap="round"/>'
        f'<circle cx="{X(x1):.1f}" cy="{Y(y1):.1f}" r="3" fill="#2563eb"/><circle cx="{X(x2):.1f}" cy="{Y(y2):.1f}" r="3" fill="#2563eb"/></svg>'
    )


def easing_reference(doc, G):
    curves = easing_names()
    s = doc.section("easing-reference", G, B("Easing reference", "Referensi easing"), B(f"The {len(curves)} named curves you can pick for a preset's Easing parameter.", f"{len(curves)} kurva bernama yang bisa dipilih untuk parameter Easing preset."))
    s += [
        P(
            "Each curve shows progress (up) over time (right). The blue dots are the bezier handles; the numbers are the CSS <code>cubic-bezier()</code> values, so you can reuse them in web projects. Curves that go above the box overshoot (Back) and give a springy feel.",
            "Setiap kurva menunjukkan progres (atas) terhadap waktu (kanan). Titik biru adalah handle bezier; angkanya adalah nilai CSS <code>cubic-bezier()</code>, jadi bisa dipakai ulang di proyek web. Kurva yang keluar dari kotak berarti overshoot (Back) dan memberi kesan memantul.",
        ),
        RAW('<div class="ease-grid">' + "".join(f"<div>{curve_svg(p)}<b>{pretty(n)}</b><code>{', '.join(f'{v:g}' for v in p)}</code></div>" for n, p in curves) + "</div>"),
        H3("choosing-easing", "Choosing an easing", "Memilih easing"),
        TABLE(
            [B("Family", "Keluarga"), B("Character", "Karakter"), B("Use for", "Dipakai untuk")],
            [
                ["Sine", B("Very gentle", "Sangat lembut"), B("Slow ambient loops, backgrounds", "Loop ambient yang pelan, background")],
                ["Quad / Cubic", B("Natural, balanced", "Alami, seimbang"), B("Most UI and text motion (Cubic is the default of many presets)", "Kebanyakan gerakan UI dan teks (Cubic adalah default banyak preset)")],
                ["Quart / Expo", B("Snappy, decisive", "Tegas, cepat"), B("Fast reveals, modern tech look", "Reveal cepat, kesan teknologi modern")],
                ["Circ", B("Sudden start or stop", "Mulai atau berhenti mendadak"), B("Mechanical, physical motion", "Gerakan mekanis dan fisik")],
                ["Back", B("Overshoots and settles", "Melewati lalu kembali"), B("Pops, icons, playful entrances", "Pop, ikon, kemunculan yang ceria")],
            ],
        ),
        UL(
            ("<b>Ease Out</b> curves (fast start, slow end) for things <i>entering</i>: they arrive and settle.", "Kurva <b>Ease Out</b> (awal cepat, akhir lambat) untuk benda yang <i>masuk</i>: datang lalu tenang."),
            ("<b>Ease In</b> curves (slow start, fast end) for things <i>leaving</i>: they gather speed and go.", "Kurva <b>Ease In</b> (awal lambat, akhir cepat) untuk benda yang <i>keluar</i>: mengumpulkan kecepatan lalu pergi."),
            ("<b>Ease In-Out</b> for things moving from one place to another on screen.", "<b>Ease In-Out</b> untuk benda yang berpindah dari satu tempat ke tempat lain di layar."),
            ("<b>Linear</b> only for constant motion: spinning loaders, scrolling tickers, Trace.", "<b>Linear</b> hanya untuk gerakan konstan: loader berputar, teks berjalan, Trace."),
        ),
    ]


# ---------------------------------------------------------------- animation principles


def svg_spacing(t):
    def row(y, label, xs, col):
        g = f'<text x="10" y="{y + 5}" font-size="13" font-weight="600">{label}</text><line x1="150" y1="{y}" x2="700" y2="{y}" class="stroke" stroke-opacity=".15"/>'
        for x in xs:
            g += f'<circle cx="{150 + x * 550:.1f}" cy="{y}" r="9" fill="{col}" opacity=".85"/>'
        return g

    lin = [i / 10 for i in range(11)]
    import math

    ease = [(1 - math.cos(math.pi * i / 10)) / 2 for i in range(11)]
    out = [1 - (1 - i / 10) ** 3 for i in range(11)]
    return f'<svg viewBox="0 0 720 170" width="720">{row(30, t[0], lin, "#64748b")}{row(85, t[1], ease, "#2563eb")}{row(140, t[2], out, "#16a34a")}</svg>'


def svg_overlap(t):
    bars = ""
    for i, (x, w, c) in enumerate([(0, 300, "#2563eb"), (110, 300, "#7c3aed"), (220, 300, "#e2381d")]):
        bars += f'<rect x="{150 + x}" y="{20 + i * 34}" width="{w}" height="24" rx="6" fill="{c}" opacity=".85"/>'
    for i, (x, w, c) in enumerate([(0, 180, "#94a3b8"), (180, 180, "#94a3b8"), (360, 180, "#94a3b8")]):
        bars += f'<rect x="{150 + x}" y="{150 + i * 34}" width="{w}" height="24" rx="6" fill="{c}" opacity=".85"/>'
    return f'<svg viewBox="0 0 720 260" width="720"><text x="10" y="70" font-size="13" font-weight="600">{t[0]}</text><text x="10" y="200" font-size="13" font-weight="600">{t[1]}</text>{bars}</svg>'


def principles(doc, G):
    s = doc.section("principles", G, B("Animation principles for motion design", "Prinsip animasi untuk motion design"), B("The classic rules of animation, and the Motionator feature for each.", "Aturan klasik animasi, dan fitur Motionator untuk masing-masing."))
    s += [
        H3("timing", "Timing", "Timing"),
        P(
            "How long a motion lasts sets its mood: short is energetic, long is calm. Typical durations:",
            "Lama sebuah gerakan menentukan suasananya: singkat terasa enerjik, panjang terasa tenang. Durasi umum:",
        ),
        TABLE(
            [B("Content", "Konten"), B("Typical duration", "Durasi umum")],
            [
                [B("Button and icon feedback (web/app)", "Umpan balik tombol dan ikon (web/aplikasi)"), "0.15 – 0.3 s"],
                [B("UI elements entering, cards, menus", "Elemen UI masuk, kartu, menu"), "0.3 – 0.6 s"],
                [B("Titles and text lines", "Judul dan baris teks"), "0.5 – 1 s"],
                [B("Logo reveal (whole)", "Logo reveal (keseluruhan)"), "2 – 5 s"],
                [B("Social media post", "Postingan media sosial"), "5 – 15 s"],
                [B("Stock background loop", "Loop background stok"), "10 – 30 s"],
            ],
        ),
        H3("spacing", "Spacing and easing", "Spacing dan easing"),
        DIAGRAM(svg_spacing(["Linear", "Ease In-Out", "Ease Out"])),
        P(
            "The dots show where an object is on equally spaced frames. Linear motion has equal steps and looks robotic. Eased motion bunches frames at the ends, so the object speeds up and slows down like a real object with weight. Press [[F9]] on keyframes, or pick an easing for a preset.",
            "Titik-titik menunjukkan letak benda pada frame yang berjarak sama. Gerakan linear punya langkah sama dan terlihat seperti robot. Gerakan dengan easing merapatkan frame di ujung-ujungnya, sehingga benda mempercepat dan melambat seperti benda nyata yang punya berat. Tekan [[F9]] pada keyframe, atau pilih easing untuk preset.",
        ),
        H3("anticipation", "Anticipation", "Antisipasi"),
        P(
            "A small move in the opposite direction before the main action prepares the eye: a character crouches before jumping, a button shrinks slightly before popping. In Motionator, keyframe a small opposite value just before the motion, or use curves with a negative handle such as <i>Ease In Back</i>.",
            "Gerakan kecil ke arah berlawanan sebelum aksi utama mempersiapkan mata: karakter berjongkok sebelum melompat, tombol sedikit mengecil sebelum membesar. Di Motionator, beri keyframe nilai berlawanan kecil tepat sebelum gerakan, atau pakai kurva dengan handle negatif seperti <i>Ease In Back</i>.",
        ),
        H3("follow-through", "Follow-through and overshoot", "Follow-through dan overshoot"),
        P(
            "Real objects do not stop dead; they go a little too far and settle. <i>Scale Pop</i>, <i>Pop Up</i> and <i>Elastic Pop</i> do this built in, and any preset can use <i>Ease Out Back</i>. In keyframes, add a key slightly past the final value a few frames before the end.",
            "Benda nyata tidak berhenti mendadak; benda bergerak sedikit terlalu jauh lalu tenang. <i>Scale Pop</i>, <i>Pop Up</i>, dan <i>Elastic Pop</i> sudah melakukannya, dan preset apa pun bisa memakai <i>Ease Out Back</i>. Dengan keyframe, tambahkan key sedikit melewati nilai akhir beberapa frame sebelum akhir.",
        ),
        H3("overlap", "Overlapping action and stagger", "Overlapping action dan stagger"),
        DIAGRAM(svg_overlap(["Overlapping", "One after another"]), svg_overlap(["Tumpang tindih", "Satu per satu"])),
        P(
            "When parts start at slightly different times and overlap, motion feels fluid and organic. Waiting for each part to finish feels slow and mechanical. Use <b>Stagger</b> with a step shorter than the preset's duration (e.g. 0.08 s for 0.6 s Pop Up) for overlap.",
            "Bila bagian-bagian mulai pada waktu yang sedikit berbeda dan tumpang tindih, gerakan terasa luwes dan organik. Menunggu setiap bagian selesai terasa lambat dan mekanis. Pakai <b>Stagger</b> dengan jeda lebih pendek dari durasi preset (misalnya 0,08 s untuk Pop Up 0,6 s) agar tumpang tindih.",
        ),
        H3("arcs", "Arcs", "Lengkungan (arcs)"),
        P(
            "Living things move along curves, not straight lines. Curve your motion paths with the handles on the canvas; the plane in the icon sample swoops instead of sliding.",
            "Makhluk hidup bergerak di sepanjang kurva, bukan garis lurus. Lengkungkan motion path dengan handle di canvas; pesawat pada contoh ikon meliuk alih-alih meluncur lurus.",
        ),
        H3("secondary", "Secondary action", "Aksi sekunder"),
        P(
            "A small extra motion supports the main one: the badge hovers while the plane flies, a glow pulses while the logo sits. Add a Loop preset with a small amount on top of the main animation.",
            "Gerakan tambahan kecil mendukung gerakan utama: badge melayang saat pesawat terbang, cahaya berdenyut saat logo diam. Tambahkan preset Loop dengan nilai kecil di atas animasi utama.",
        ),
        H3("squash-stretch", "Squash and stretch", "Squash dan stretch"),
        P(
            "Squashing on impact and stretching in fast motion gives flexibility and weight. <i>Squash</i>, <i>Stretch In</i>, <i>Rubber Band</i> and the <i>Bounce</i> loop do this; keep the anchor at the contact point.",
            "Memipih saat benturan dan meregang saat bergerak cepat memberi kesan lentur dan berat. <i>Squash</i>, <i>Stretch In</i>, <i>Rubber Band</i>, dan loop <i>Bounce</i> melakukannya; letakkan anchor di titik sentuh.",
        ),
        H3("hierarchy-motion", "Hierarchy and restraint", "Hierarki dan pengendalian diri"),
        UL(
            ("Animate the most important thing first and most clearly; let secondary items follow.", "Animasikan hal terpenting lebih dulu dan paling jelas; biarkan elemen pendukung menyusul."),
            ("Use one or two kinds of motion per scene. Ten different presets at once looks busy.", "Pakai satu atau dua jenis gerakan per adegan. Sepuluh preset berbeda sekaligus terlihat ramai."),
            ("Leave moments of stillness so the viewer can read.", "Sisakan momen diam agar penonton bisa membaca."),
            ("Match motion to the brand: soft eases for calm brands, snappy Expo and Back for energetic ones.", "Sesuaikan gerakan dengan merek: easing lembut untuk merek tenang, Expo dan Back yang tegas untuk merek enerjik."),
        ),
    ]


# ---------------------------------------------------------------- web integration


def web_integration(doc, G):
    s = doc.section("web-integration", G, B("Using animations on websites and in apps", "Memakai animasi di website dan aplikasi"), B("Practical code for lottie-web, React and animated SVG.", "Kode praktis untuk lottie-web, React, dan SVG animasi."))
    s += [
        H3("lottie-control", "Controlling a Lottie with JavaScript", "Mengendalikan Lottie dengan JavaScript"),
        P("<code>loadAnimation</code> returns an object with methods to control playback:", "<code>loadAnimation</code> mengembalikan objek dengan method untuk mengatur pemutaran:"),
        CODE("""const anim = lottie.loadAnimation({
  container: document.getElementById("icon"),
  renderer: "svg", loop: false, autoplay: false,
  path: "icon.json"
});

anim.play();                    // play from the current frame
anim.pause();
anim.stop();                    // back to frame 0
anim.setSpeed(1.5);             // 1 = normal
anim.setDirection(-1);          // play backwards
anim.goToAndStop(45, true);     // jump to frame 45
anim.playSegments([0, 30], true);
anim.addEventListener("complete", () => console.log("done"));"""),
        H4("Play on hover", "Putar saat hover"),
        CODE("""const box = document.getElementById("icon");
box.addEventListener("mouseenter", () => { anim.setDirection(1); anim.play(); });
box.addEventListener("mouseleave", () => { anim.setDirection(-1); anim.play(); });"""),
        H4("Play when scrolled into view", "Putar saat terlihat di layar"),
        CODE("""new IntersectionObserver(([e]) => e.isIntersecting ? anim.play() : anim.pause(),
  { threshold: 0.4 }).observe(document.getElementById("icon"));"""),
        H3("lottie-react", "Lottie in React", "Lottie di React"),
        CODE("""// npm install lottie-react
import Lottie from "lottie-react";
import spinner from "./spinner.json";

export function Loader() {
  return <Lottie animationData={spinner} loop style={{ width: 96, height: 96 }} />;
}"""),
        P(
            "Other platforms: <b>lottie-android</b> and <b>lottie-ios</b> (Airbnb), <b>lottie</b> for Flutter, <b>lottie-react-native</b>. They all read the same JSON.",
            "Platform lain: <b>lottie-android</b> dan <b>lottie-ios</b> (Airbnb), <b>lottie</b> untuk Flutter, <b>lottie-react-native</b>. Semuanya membaca JSON yang sama.",
        ),
        H3("lottie-size", "Keeping Lottie files small", "Menjaga file Lottie tetap kecil"),
        UL(
            ("Lower <b>Number precision</b> in the export dialog (2 decimals is usually invisible).", "Turunkan <b>Presisi angka</b> di dialog ekspor (2 desimal biasanya tidak terlihat bedanya)."),
            ("Prefer keyframes over presets where file size matters: keyframes export as a few bezier keys, presets as sampled keys.", "Utamakan keyframe daripada preset bila ukuran file penting: keyframe diekspor sebagai sedikit key bezier, preset sebagai key sampel."),
            ("Simplify paths in your design tool; every point is stored.", "Sederhanakan path di aplikasi desain; setiap titik disimpan."),
            ("Leave out the background if the page already has one.", "Jangan sertakan background bila halamannya sudah punya."),
            ("Serve the JSON with gzip/brotli compression (most hosts do this automatically); JSON compresses very well.", "Sajikan JSON dengan kompresi gzip/brotli (kebanyakan hosting otomatis melakukannya); JSON terkompresi sangat baik."),
        ),
        H3("svg-a11y", "Accessible animated SVG", "SVG animasi yang aksesibel"),
        CODE("""<!-- decorative: hide it from screen readers -->
<img src="wave.svg" alt="" aria-hidden="true">

<!-- meaningful: describe it -->
<img src="logo.svg" alt="Motionator logo">

<!-- respect users who prefer less motion (inline SVG) -->
<style>
  @media (prefers-reduced-motion: reduce) {
    .hero-icon svg * { animation: none !important; }
  }
</style>"""),
        TIP(
            "With <code>&lt;img&gt;</code> the animation cannot be paused by page CSS. If you need reduced-motion support, either inline the SVG and use the CSS above, or swap the source with <code>&lt;picture&gt;</code> and <code>media=\"(prefers-reduced-motion: reduce)\"</code> pointing to a static SVG.",
            "Dengan <code>&lt;img&gt;</code> animasi tidak bisa dijeda oleh CSS halaman. Bila butuh dukungan pengurangan gerak, sisipkan SVG secara inline dan pakai CSS di atas, atau ganti sumbernya dengan <code>&lt;picture&gt;</code> dan <code>media=\"(prefers-reduced-motion: reduce)\"</code> yang menunjuk ke SVG statis.",
        ),
        H3("video-web", "Transparent video on the web", "Video transparan di web"),
        CODE("""<video autoplay loop muted playsinline width="640">
  <source src="badge.webm" type="video/webm">   <!-- VP9 + alpha -->
  <source src="badge.mp4"  type="video/mp4">    <!-- fallback, no alpha -->
</video>"""),
        P(
            "VP9 with alpha plays with transparency in Chrome, Edge and Firefox. Safari needs HEVC with alpha, which Motionator does not export; the MP4 fallback shows there on the composition background. For simple vector graphics, Lottie or animated SVG are lighter and sharper.",
            "VP9 dengan alpha tampil transparan di Chrome, Edge, dan Firefox. Safari butuh HEVC dengan alpha, yang tidak diekspor Motionator; di sana tampil fallback MP4 dengan background komposisi. Untuk grafis vektor sederhana, Lottie atau SVG animasi lebih ringan dan tajam.",
        ),
        H3("format-sizes", "Which format is lightest?", "Format mana yang paling ringan?"),
        P(
            "For the logo sample (3 s, 9 animated layers) the export dialogs report about <b>27.7 KB</b> for Lottie (3 decimals) and <b>26.4 KB</b> for the animated SVG, before gzip compression. A video of the same clip is many times larger and is fixed to one resolution. The dialogs always show the size before you save, so compare for your own project.",
            "Untuk contoh logo (3 s, 9 layer beranimasi) dialog ekspor melaporkan sekitar <b>27,7 KB</b> untuk Lottie (3 desimal) dan <b>26,4 KB</b> untuk SVG animasi, sebelum kompresi gzip. Video dari klip yang sama berukuran berkali-kali lipat dan terkunci pada satu resolusi. Dialog selalu menampilkan ukurannya sebelum disimpan, jadi bandingkan untuk proyek Anda sendiri.",
        ),
        P(
            "Vector formats stay sharp at any size and on high-DPI screens; choose video only when the scene needs effects the vector formats cannot show.",
            "Format vektor tetap tajam di ukuran berapa pun dan di layar high-DPI; pilih video hanya bila adegannya butuh efek yang tidak bisa ditampilkan format vektor.",
        ),
    ]


# ---------------------------------------------------------------- microstock


def microstock(doc, G):
    s = doc.section("microstock", G, B("Making motion backgrounds for microstock", "Membuat background motion untuk microstock"), B("A practical workflow from idea to upload.", "Alur kerja praktis dari ide sampai unggah."))
    s += [
        NOTE(
            "Stock agencies change their requirements from time to time. The values below are common across major sites; always check the current contributor guidelines of the site you upload to.",
            "Agensi stok mengubah syaratnya dari waktu ke waktu. Nilai di bawah ini umum di situs-situs besar; selalu cek panduan kontributor terbaru di situs tujuan.",
        ),
        H3("stock-specs", "Technical checklist", "Daftar periksa teknis"),
        TABLE(
            [B("Item", "Item"), B("Common requirement", "Syarat umum"), B("In Motionator", "Di Motionator")],
            [
                [B("Resolution", "Resolusi"), B("At least 1920×1080; 3840×2160 (4K) sells better", "Minimal 1920×1080; 3840×2160 (4K) lebih laku"), B("Size 2160p in the Render Queue", "Ukuran 2160p di Render Queue")],
                [B("Length", "Durasi"), "5 – 60 s", B("Composition duration; warning if outside", "Durasi komposisi; peringatan bila di luar batas")],
                [B("Frame rate", "Frame rate"), B("Standard rates (23.976–60)", "Frame rate standar (23,976–60)"), B("Composition settings", "Pengaturan komposisi")],
                [B("Codec", "Codec"), B("H.264 high quality or ProRes", "H.264 kualitas tinggi atau ProRes"), B("Stock presets", "Preset stok")],
                [B("Audio", "Audio"), B("Usually none for backgrounds", "Biasanya tanpa audio untuk background"), B("Mute the track or leave it out", "Bisukan trek atau jangan dipakai")],
                [B("Seamless loop", "Loop mulus"), B("A strong selling point (mention it)", "Nilai jual yang kuat (sebutkan)"), B("Check loop", "Cek loop")],
                [B("Content", "Konten"), B("No logos, brands or text you do not own", "Tanpa logo, merek, atau teks milik orang lain"), B("Use your own artwork", "Pakai artwork sendiri")],
            ],
        ),
        H3("stock-ideas", "What sells: ideas that suit Motionator", "Yang laku: ide yang cocok untuk Motionator"),
        CARDS(
            ("🌊", "Abstract waves", "Gelombang abstrak", "Layered waves with Sway and Float, gradients, slow motion. Classic presentation backgrounds.", "Gelombang berlapis dengan Sway dan Float, gradien, gerakan pelan. Background presentasi klasik."),
            ("✨", "Particles and bokeh", "Partikel dan bokeh", "Many small circles with Drift and Glow at different periods; blur some for depth.", "Banyak lingkaran kecil dengan Drift dan Glow berperiode berbeda; beri blur pada sebagian untuk kedalaman."),
            ("🔷", "Geometric patterns", "Pola geometris", "Grids of shapes with Spin, Pulse and stagger; perfect loops by design.", "Grid bentuk dengan Spin, Pulse, dan stagger; loop sempurna karena desainnya."),
            ("💡", "Tech and circuits", "Teknologi dan sirkuit", "Line art with Trace running along paths, Glow on nodes.", "Line art dengan Trace yang berjalan di sepanjang path, Glow pada titik simpul."),
            ("🎉", "Seasonal", "Musiman", "Snow, confetti, lanterns, Ramadan and Christmas themes, released a few months early.", "Salju, konfeti, lampion, tema Ramadan dan Natal, dirilis beberapa bulan lebih awal."),
            ("📊", "Lower thirds and overlays", "Lower third dan overlay", "Transparent ProRes 4444 elements editors can drop onto their video.", "Elemen ProRes 4444 transparan yang bisa langsung ditaruh editor di video mereka."),
        ),
        H3("perfect-loops", "Designing perfect loops", "Merancang loop sempurna"),
        STEPS(
            ("Pick the clip length first (for example 10 s).", "Tentukan panjang klip terlebih dulu (misalnya 10 s)."),
            ("Give every Loop preset a period that divides it: 10, 5, 2.5, 2 or 1 s. Different periods (5 and 2.5) create variety and still meet at the end.", "Beri setiap preset Loop periode yang habis membaginya: 10, 5, 2,5, 2, atau 1 s. Periode berbeda (5 dan 2,5) menciptakan variasi dan tetap bertemu di akhir."),
            ("For Spin, a full turn must fit, or the shape must be symmetric: a 16-point star repeats every 22.5°.", "Untuk Spin, satu putaran penuh harus muat, atau bentuknya harus simetris: bintang 16 sudut berulang setiap 22,5°."),
            ("Do not use Enter/Exit presets in a loop: the start and end would differ.", "Jangan pakai preset Enter/Exit di loop: awal dan akhirnya akan berbeda."),
            ("For keyframes, make the last key equal to the first (the Check loop fix does this for you).", "Untuk keyframe, buat key terakhir sama dengan yang pertama (perbaikan Cek loop melakukannya untuk Anda)."),
            ("Run <b>Check loop</b>, then watch the clip with loop playback on: the jump from last to first frame should be invisible.", "Jalankan <b>Cek loop</b>, lalu tonton klip dengan loop aktif: lompatan dari frame terakhir ke pertama tidak boleh terlihat."),
        ),
        H3("variations", "One project, many clips", "Satu proyek, banyak klip"),
        P(
            "Stock buyers search by colour and mood. After finishing one background, save copies of the project with different colours (use <b>Tint</b> on the root layer, or recolour the SVG), different speeds (change the periods) or a different crop (scale the root layer), and render each. Queue them all in the Render Queue overnight.",
            "Pembeli stok mencari berdasarkan warna dan suasana. Setelah satu background selesai, simpan salinan proyek dengan warna berbeda (pakai <b>Tint</b> pada layer root, atau warnai ulang SVG-nya), kecepatan berbeda (ubah periodenya), atau potongan berbeda (skala layer root), lalu render masing-masing. Antrekan semuanya di Render Queue untuk dirender semalaman.",
        ),
        H3("metadata", "Titles and keywords", "Judul dan kata kunci"),
        UL(
            ("Title: what it is, the style and the use. <i>“Abstract purple waves seamless loop background 4K”</i>.", "Judul: apa isinya, gayanya, dan kegunaannya. <i>“Abstract purple waves seamless loop background 4K”</i>."),
            ("Keywords: subject (waves, particles), colours, mood (calm, corporate, festive), technique (loop, motion graphics, animation), use (presentation, intro, backdrop).", "Kata kunci: subjek (waves, particles), warna, suasana (calm, corporate, festive), teknik (loop, motion graphics, animation), kegunaan (presentation, intro, backdrop)."),
            ("Most sites need English metadata; write it in English even if your audience is local.", "Kebanyakan situs butuh metadata berbahasa Inggris; tulis dalam bahasa Inggris meskipun pasar Anda lokal."),
            ("Abstract graphics made entirely by you need no model or property release.", "Grafis abstrak yang sepenuhnya Anda buat tidak memerlukan model atau property release."),
        ),
    ]


# ---------------------------------------------------------------- new tutorials


def tutorials_extra(doc, G):
    s = doc.section("tutorial-spinner", G, B("Tutorial: loading spinner for Lottie", "Tutorial: loading spinner untuk Lottie"), B("Uses samples/spinner.svg. Result: samples/spinner.motionator.", "Memakai samples/spinner.svg. Hasil: samples/spinner.motionator."))
    s += [
        STRIP("spinner", ["0 s", "0.125 s", "0.25 s", "0.375 s"]),
        P(
            "A spinner must loop perfectly and stay tiny. The sample has a grey <code>Track</code>, a group <code>Arcs</code> with two opposite arcs, and a <code>Core</code> dot.",
            "Spinner harus berulang sempurna dan tetap kecil. Contoh ini punya <code>Track</code> abu-abu, grup <code>Arcs</code> berisi dua busur berlawanan, dan titik <code>Core</code>.",
        ),
        STEPS(
            ("<b>Composition</b> 512×512, 30 fps, <b>2 s</b>, Transparent.", "<b>Komposisi</b> 512×512, 30 fps, <b>2 s</b>, Transparan."),
            ("<b>Import</b> <code>spinner.svg</code>.", "<b>Impor</b> <code>spinner.svg</code>."),
            ("Select <code>Arcs</code> and apply <i>Spin</i> (Loop). Set <i>Period</i> to 1 s: two full turns in the 2 s clip.", "Pilih <code>Arcs</code> lalu terapkan <i>Spin</i> (Loop). Atur <i>Periode</i> ke 1 s: dua putaran penuh dalam klip 2 s."),
            ("Select <code>Core</code> and apply <i>Pulse</i> with Amount 10 % and Period 1 s.", "Pilih <code>Core</code> lalu terapkan <i>Pulse</i> dengan Amount 10 % dan Periode 1 s."),
            ("<b>Check loop</b> in the Render Queue: it should be seamless.", "<b>Cek loop</b> di Render Queue: hasilnya harus mulus."),
            ("<b>Export Lottie</b> with 2 decimals. Use it with <code>loop: true</code>.", "<b>Ekspor Lottie</b> dengan 2 desimal. Pakai dengan <code>loop: true</code>."),
        ),
        TIP(
            "Why two arcs in a group? A layer spins around its anchor point, which starts at the centre of its box. One arc alone has its box off-centre and would wobble; two opposite arcs make the box centred on the circle. With a single arc, move the anchor to the circle's centre with the Anchor Point tool [[Y]].",
            "Kenapa dua busur dalam satu grup? Layer berputar di sekitar anchor point-nya, yang awalnya ada di tengah kotaknya. Satu busur saja kotaknya tidak di tengah lingkaran sehingga akan bergoyang; dua busur berlawanan membuat kotaknya tepat di tengah lingkaran. Bila hanya satu busur, pindahkan anchor ke tengah lingkaran dengan tool Anchor Point [[Y]].",
        ),
    ]

    s = doc.section("tutorial-lower-third", G, B("Tutorial: lower third with transparency", "Tutorial: lower third transparan"), B("Uses samples/lowerthird.svg. Result: samples/lowerthird.motionator.", "Memakai samples/lowerthird.svg. Hasil: samples/lowerthird.motionator."))
    s += [
        STRIP("lowerthird", ["0.2 s", "0.5 s", "1.4 s", "4.7 s"]),
        P(
            "A lower third is the name caption at the bottom of interviews and vlogs. It is delivered with transparency so editors can place it over any footage.",
            "Lower third adalah keterangan nama di bagian bawah wawancara dan vlog. Diserahkan dalam bentuk transparan agar editor bisa menaruhnya di atas footage apa pun.",
        ),
        STEPS(
            ("<b>Composition</b> 1920×1080, 30 fps, 5 s, <b>Transparent</b>. Turn on <b>View ▸ Safe Area</b> to keep the text inside title-safe.", "<b>Komposisi</b> 1920×1080, 30 fps, 5 s, <b>Transparan</b>. Nyalakan <b>View ▸ Safe Area</b> agar teks tetap di dalam title-safe."),
            ("<b>Import</b> <code>lowerthird.svg</code>: group <code>Lower_Third</code> with <code>Bar</code>, <code>Accent</code>, <code>Title</code> and <code>Subtitle</code> (text already outlined).", "<b>Impor</b> <code>lowerthird.svg</code>: grup <code>Lower_Third</code> berisi <code>Bar</code>, <code>Accent</code>, <code>Title</code>, dan <code>Subtitle</code> (teks sudah di-outline)."),
            ("At 0 s: <i>Scale Pop</i> on <code>Accent</code>.", "Di 0 s: <i>Scale Pop</i> pada <code>Accent</code>."),
            ("At 0.15 s: <i>Wipe In</i> on <code>Bar</code>, from the left.", "Di 0,15 s: <i>Wipe In</i> pada <code>Bar</code>, dari kiri."),
            ("At 0.45 s: <i>Slide In ←</i> on <code>Title</code> with Distance 80 px.", "Di 0,45 s: <i>Slide In ←</i> pada <code>Title</code> dengan Jarak 80 px."),
            ("At 0.7 s: <i>Fade In</i> on <code>Subtitle</code>.", "Di 0,7 s: <i>Fade In</i> pada <code>Subtitle</code>."),
            ("Select <code>Lower_Third</code> and apply <i>Fade Out</i>: as an Exit preset it is placed at the end automatically.", "Pilih <code>Lower_Third</code> lalu terapkan <i>Fade Out</i>: sebagai preset Exit, otomatis diletakkan di akhir."),
            ("<b>Render</b> as <b>ProRes 4444 + alpha</b> (for Premiere, Resolve, Final Cut) or <b>VP9 + alpha</b> (for the web).", "<b>Render</b> sebagai <b>ProRes 4444 + alpha</b> (untuk Premiere, Resolve, Final Cut) atau <b>VP9 + alpha</b> (untuk web)."),
        ),
        NOTE(
            "Exit presets count from the end of the composition: in the Properties panel their first field is <i>Ends before the end</i> (0 s = ends exactly with the composition). If you lengthen the composition, the exit moves with the end, which is usually what you want for captions.",
            "Preset Exit dihitung dari akhir komposisi: di panel Properties field pertamanya adalah <i>Selesai sebelum akhir</i> (0 s = berakhir tepat bersama komposisi). Bila komposisi diperpanjang, exit ikut bergeser bersama akhir komposisi, yang biasanya memang diinginkan untuk keterangan.",
        ),
        TIP(
            "To reuse it for another person, duplicate the SVG in your design tool, change the text, outline it and import the new file into a copy of the project; the presets are on layers with the same names.",
            "Untuk dipakai orang lain, duplikat SVG di aplikasi desain, ubah teksnya, outline, lalu impor file baru itu ke salinan proyek; preset ada di layer dengan nama yang sama.",
        ),
    ]

    s = doc.section("tutorial-social", G, B("Tutorial: square social media post", "Tutorial: postingan media sosial persegi"), B("Uses samples/social.svg. Result: samples/social.motionator.", "Memakai samples/social.svg. Hasil: samples/social.motionator."))
    s += [
        STRIP("social", ["0.25 s", "0.6 s", "1.3 s", "3.2 s"]),
        STEPS(
            ("<b>Composition</b> 1080×1080 (Instagram feed), 30 fps, 6 s.", "<b>Komposisi</b> 1080×1080 (feed Instagram), 30 fps, 6 s."),
            ("<b>Import</b> <code>social.svg</code>: <code>Backdrop</code>, <code>Burst</code>, group <code>Headline</code> with <code>Letter_S/A/L/E</code>, group <code>Price_Tag</code>.", "<b>Impor</b> <code>social.svg</code>: <code>Backdrop</code>, <code>Burst</code>, grup <code>Headline</code> berisi <code>Letter_S/A/L/E</code>, grup <code>Price_Tag</code>."),
            ("<code>Burst</code>: <i>Scale Pop</i> at 0 s, then <i>Spin</i> (Loop) with Period 12 s for a slow turn.", "<code>Burst</code>: <i>Scale Pop</i> di 0 s, lalu <i>Spin</i> (Loop) dengan Periode 12 s untuk putaran pelan."),
            ("Tick <i>Stagger to child layers</i> (0.1 s, In order), select <code>Headline</code> at 0.4 s and apply <i>Pop Up</i>.", "Centang <i>Stagger ke anak layer</i> (0,1 s, Berurutan), pilih <code>Headline</code> di 0,4 s lalu terapkan <i>Pop Up</i>."),
            ("Untick stagger. At 1.1 s apply <i>Slide In ↑</i> to <code>Price_Tag</code> with Distance 120 px.", "Matikan stagger. Di 1,1 s terapkan <i>Slide In ↑</i> pada <code>Price_Tag</code> dengan Jarak 120 px."),
            ("At 3 s apply <i>Heartbeat</i> to <code>Headline</code> to re-catch the eye.", "Di 3 s terapkan <i>Heartbeat</i> pada <code>Headline</code> untuk menarik perhatian lagi."),
            ("<b>Render</b> H.264 at composition size; add music with Import Audio if the platform plays sound.", "<b>Render</b> H.264 dengan ukuran komposisi; tambahkan musik lewat Impor Audio bila platformnya memutar suara."),
        ),
        TABLE(
            [B("Platform", "Platform"), B("Size", "Ukuran"), B("Notes", "Catatan")],
            [
                [B("Instagram / Facebook feed", "Feed Instagram / Facebook"), "1080×1080, 1080×1350", B("Square or 4:5 portrait", "Persegi atau potret 4:5")],
                [B("Reels, Stories, TikTok, Shorts", "Reels, Stories, TikTok, Shorts"), "1080×1920", B("Keep text away from the top and bottom 250 px (UI overlays)", "Jauhkan teks dari 250 px atas dan bawah (tertutup UI)")],
                ["YouTube, LinkedIn", "1920×1080", B("Landscape 16:9", "Lanskap 16:9")],
            ],
        ),
        TIP(
            "Make a vertical version by changing the composition to 1080×1920 and moving the root layer: presets stay relative to each layer, so the animation adapts.",
            "Buat versi vertikal dengan mengubah komposisi ke 1080×1920 dan menggeser layer root: preset tetap relatif terhadap setiap layer, jadi animasinya menyesuaikan.",
        ),
    ]


# ---------------------------------------------------------------- glossary

GLOSSARY = [
    ("Additive (blend)", "Aditif (blend)", "How Loop and Emphasis presets combine: their motion is added on top of everything else.", "Cara preset Loop dan Emphasis digabungkan: gerakannya ditambahkan di atas yang lain."),
    ("Alpha", "Alpha", "Transparency information in a video or image. ProRes 4444 and VP9 can carry it.", "Informasi transparansi pada video atau gambar. ProRes 4444 dan VP9 bisa membawanya."),
    ("Anchor point", "Anchor point", "The pivot of a layer for rotation, scale and skew.", "Poros layer untuk rotasi, skala, dan skew."),
    ("Bake", "Bake", "Turning presets into ordinary keyframes.", "Mengubah preset menjadi keyframe biasa."),
    ("Bezier handle", "Handle bezier", "The control points that shape a curve, in motion paths and easing curves.", "Titik kendali yang membentuk kurva, pada motion path dan kurva easing."),
    ("Cache", "Cache", "Frames already rendered and kept in memory for smooth playback (green bar on the ruler).", "Frame yang sudah dirender dan disimpan di memori agar pemutaran mulus (bar hijau di ruler)."),
    ("Codec", "Codec", "The method used to compress video: H.264, ProRes, VP9.", "Metode untuk mengompresi video: H.264, ProRes, VP9."),
    ("Composition", "Komposisi", "The frame you animate in: size, frame rate, duration, background.", "Bingkai tempat Anda menganimasikan: ukuran, frame rate, durasi, background."),
    ("CRF", "CRF", "Constant Rate Factor: H.264/VP9 quality setting; lower is better quality and larger files.", "Constant Rate Factor: pengaturan kualitas H.264/VP9; makin rendah makin bagus kualitasnya dan makin besar file-nya."),
    ("CTI / playhead", "CTI / playhead", "The current time indicator, the blue line in the timeline.", "Penanda waktu saat ini, garis biru di timeline."),
    ("Easing", "Easing", "How speed changes between two values: linear, ease in, ease out…", "Cara kecepatan berubah di antara dua nilai: linear, ease in, ease out, dan lainnya."),
    ("Easy Ease", "Easy Ease", "After Effects' standard ease: slows into and out of a keyframe.", "Easing standar After Effects: melambat saat masuk dan keluar dari keyframe."),
    ("FFmpeg", "FFmpeg", "The open-source program Motionator uses to encode video and audio.", "Program open-source yang dipakai Motionator untuk meng-encode video dan audio."),
    ("Frame rate (fps)", "Frame rate (fps)", "Frames per second.", "Jumlah frame per detik."),
    ("Graph Editor", "Graph Editor", "The timeline view that shows animation as value or speed curves.", "Tampilan timeline yang menunjukkan animasi sebagai kurva nilai atau kecepatan."),
    ("Keyframe", "Keyframe", "A value at a point in time; Motionator fills in the frames between keyframes.", "Nilai pada satu titik waktu; Motionator mengisi frame di antara keyframe."),
    ("Layer", "Layer", "An element of the SVG that can be animated: the root SVG, a group or a path with an id.", "Elemen SVG yang bisa dianimasikan: root SVG, grup, atau path ber-id."),
    ("Lottie", "Lottie", "A JSON format for vector animation, played by lottie-web and native libraries.", "Format JSON untuk animasi vektor, diputar oleh lottie-web dan library native."),
    ("Loop (seamless)", "Loop (mulus)", "A clip whose last frame flows into its first without a visible jump.", "Klip yang frame terakhirnya menyambung ke frame pertama tanpa lompatan yang terlihat."),
    ("Motion blur", "Motion blur", "Blur along the direction of fast movement, as a camera would capture it.", "Blur searah gerakan cepat, seperti yang ditangkap kamera."),
    ("Motion path", "Motion path", "The path a layer follows between Position keyframes.", "Lintasan yang diikuti layer di antara keyframe Position."),
    ("Override (blend)", "Override (blend)", "How Enter and Exit presets combine: the later one replaces the value.", "Cara preset Enter dan Exit digabungkan: yang belakangan menggantikan nilainya."),
    ("Overshoot", "Overshoot", "Going slightly past the final value before settling.", "Melewati sedikit nilai akhir sebelum tenang."),
    ("Parent / child", "Induk / anak", "Layers inside a group are its children and follow its transform.", "Layer di dalam grup adalah anaknya dan mengikuti transform-nya."),
    ("Period", "Periode", "The time one cycle of a Loop preset takes.", "Waktu yang dibutuhkan satu siklus preset Loop."),
    ("Preset", "Preset", "A ready-made motion applied to a layer as a bar in the timeline.", "Gerakan siap pakai yang diterapkan ke layer sebagai bar di timeline."),
    ("ProRes", "ProRes", "Apple's high-quality editing codec; 422 HQ for masters, 4444 with alpha.", "Codec editing berkualitas tinggi dari Apple; 422 HQ untuk master, 4444 dengan alpha."),
    ("Render Queue", "Render Queue", "The list of video exports, rendered one after another.", "Daftar ekspor video yang dirender satu per satu."),
    ("Rest pose", "Pose diam", "How a layer looks in the original SVG.", "Tampilan layer di SVG aslinya."),
    ("Reveal", "Reveal", "An effect that shows part of a layer, wiping from a side or as an iris.", "Efek yang menampilkan sebagian layer, tersapu dari satu sisi atau seperti iris."),
    ("Safe area", "Safe area", "Margins inside which text and action stay visible on all screens.", "Margin yang menjamin teks dan aksi tetap terlihat di semua layar."),
    ("Stagger", "Stagger", "Applying a preset to several layers with a delay between them.", "Menerapkan preset ke beberapa layer dengan jeda di antaranya."),
    ("Stopwatch", "Stopwatch", "The clock icon that turns keyframes on for a property.", "Ikon jam yang mengaktifkan keyframe untuk suatu properti."),
    ("Tint", "Tint", "An effect that recolours a layer towards a chosen colour.", "Efek yang mewarnai ulang layer ke arah warna yang dipilih."),
    ("Timecode", "Timecode", "Time written as hours:minutes:seconds:frames.", "Waktu yang ditulis sebagai jam:menit:detik:frame."),
    ("Trim Paths", "Trim Paths", "Shows only part of each stroke: Start, End and Offset.", "Menampilkan hanya sebagian setiap stroke: Start, End, dan Offset."),
    ("viewBox", "viewBox", "The SVG attribute that sets the coordinate area of the drawing.", "Atribut SVG yang menentukan area koordinat gambar."),
    ("Workspace", "Workspace", "A saved arrangement of panels: Simple, Advanced, Minimal.", "Susunan panel yang tersimpan: Simple, Advanced, Minimal."),
]


def glossary(doc, G):
    s = doc.section("glossary", G, B("Glossary", "Glosarium"))
    items = "".join(f"<dt>{bi(te, ti)}</dt><dd>{bi(de, di)}</dd>" for te, ti, de, di in GLOSSARY)
    s.append(RAW(f'<dl class="glossary">{items}</dl>'))


FAQ_EXTRA = [
    ("Can I animate text without outlining it?", "Bisakah teks dianimasikan tanpa di-outline?", "Not yet: outline it in your design tool. Keep the editable original so you can change the wording later.", "Belum: outline teks di aplikasi desain. Simpan file asli yang masih bisa diedit agar kata-katanya bisa diubah nanti."),
    ("How do I animate each letter separately?", "Bagaimana menganimasikan setiap huruf terpisah?", "Give each letter its own id inside a named group (the social sample shows this), then apply a preset to the group with Stagger to child layers.", "Beri setiap huruf id sendiri di dalam grup bernama (contoh social menunjukkannya), lalu terapkan preset ke grup dengan Stagger ke anak layer."),
    ("My Exit preset appears at the start.", "Preset Exit saya muncul di awal.", "Exit presets are placed from the end of the composition. Check the composition duration and <i>Ends before the end</i> in the Properties panel (0 s = at the very end).", "Preset Exit diletakkan dari akhir komposisi. Periksa durasi komposisi dan <i>Selesai sebelum akhir</i> di panel Properties (0 s = tepat di akhir)."),
    ("The layer spins around the wrong point in the export too.", "Layer berputar di titik yang salah juga pada hasil ekspor.", "The export uses the same anchor point as the preview. Fix the anchor with [[Y]] or Center Anchor Point.", "Ekspor memakai anchor point yang sama dengan preview. Perbaiki anchor dengan [[Y]] atau Pusatkan Anchor Point."),
    ("Can I change the composition size after animating?", "Bisakah ukuran komposisi diubah setelah dianimasikan?", "Yes. Layers keep their positions in pixels from the top-left, so move or scale the root layer to re-centre. Presets adapt because they are relative.", "Bisa. Layer mempertahankan posisinya dalam piksel dari kiri atas, jadi geser atau skala layer root untuk menengahkan lagi. Preset menyesuaikan karena sifatnya relatif."),
    ("Rendering 4K is slow.", "Render 4K lambat.", "Motion blur multiplies render time by about 8. Blur effects and SVG filters are the most expensive; remove them where they do not show. Rendering runs in the background, so you can queue several items.", "Motion blur melipatgandakan waktu render sekitar 8 kali. Efek blur dan filter SVG paling berat; buang bila tidak terlihat. Render berjalan di latar belakang, jadi Anda bisa mengantrekan beberapa item."),
    ("The colours in my video look washed out.", "Warna video saya terlihat pucat.", "Some players show H.264 with limited colour range. Compare in a different player (VLC, a browser); for colour-critical work deliver ProRes.", "Beberapa player menampilkan H.264 dengan rentang warna terbatas. Bandingkan di player lain (VLC, browser); untuk pekerjaan yang warnanya kritis, serahkan ProRes."),
    ("Where are my own presets stored?", "Di mana preset buatan saya disimpan?", "In Motionator's settings folder on this computer, and as a copy inside every project that uses them.", "Di folder pengaturan Motionator di komputer ini, dan sebagai salinan di dalam setiap proyek yang memakainya."),
    ("Can I open a project on another computer?", "Bisakah proyek dibuka di komputer lain?", "Yes: the .motionator file contains the SVGs and presets. Copy the audio file next to it if the project has sound.", "Bisa: file .motionator berisi SVG dan preset. Salin juga file audio di sampingnya bila proyek punya suara."),
]
