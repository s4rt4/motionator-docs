"""Guide content, part 2: animating, export, guides and reference."""
from build import B, CARDS, CODE, DIAGRAM, H3, H4, IMG, LEGEND, NOTE, P, RAW, STEPS, STRIP, TABLE, TIP, UL, WARN, kbd
import content3
from content import G_ANIM, G_OUT, G_REF, svg_blend, svg_easing, svg_loop, svg_stagger, svg_trim

YES = '<span class="tag yes">✓</span>'
NO = '<span class="tag no">✗</span>'


def part(en, idn):
    return B(f'<span class="tag part">~</span> {en}', f'<span class="tag part">~</span> {idn}')


def keys(ks):
    return " ".join(kbd(k) for k in ks)


def build(doc, presets, shortcuts):
    # ============================================================ presets
    s = doc.section("presets", G_ANIM, B("Presets", "Preset"), B("82 ready-made motions in four categories, applied with a double-click.", "82 gerakan siap pakai dalam empat kategori, diterapkan dengan klik dua kali."))
    s += [
        H3("preset-categories", "The four categories", "Empat kategori"),
        TABLE(
            [B("Category", "Kategori"), B("What it does", "Fungsinya"), B("Where it is placed", "Posisinya di timeline")],
            [
                ['<span class="tag enter">Enter</span>', B("Brings the layer in: it ends in the layer's rest pose.", "Memunculkan layer: berakhir di pose diam layer."), B("Starts at the playhead.", "Mulai di playhead.")],
                ['<span class="tag exit">Exit</span>', B("Takes the layer out: it starts from the rest pose.", "Menghilangkan layer: mulai dari pose diam."), B("Ends at the end of the composition.", "Berakhir di akhir komposisi.")],
                ['<span class="tag loop">Loop</span>', B("Repeats for as long as the bar lasts and loops seamlessly.", "Berulang selama bar berlangsung dan bisa di-loop mulus."), B("Covers the whole composition.", "Menutupi seluruh komposisi.")],
                ['<span class="tag emphasis">Emphasis</span>', B("A short accent that returns to where it started.", "Aksen singkat yang kembali ke posisi awal."), B("Starts at the playhead.", "Mulai di playhead.")],
            ],
        ),
        H3("applying-presets", "Applying a preset", "Menerapkan preset"),
        IMG("presets-hover", "Hovering a preset plays a live preview of it on a sample shape.", "Mengarahkan kursor ke preset memutar preview langsung pada bentuk contoh.", "medium"),
        STEPS(
            ("Select a layer (in the Layers panel, the timeline or on the canvas).", "Pilih layer (di panel Layers, timeline, atau canvas)."),
            ("For Enter and Emphasis presets, move the playhead to where the motion should start.", "Untuk preset Enter dan Emphasis, pindahkan playhead ke titik mulai gerakan."),
            ("Find the preset: type in <b>Search presets</b> or open a category. Hover to preview.", "Cari preset: ketik di <b>Cari preset</b> atau buka kategori. Arahkan kursor untuk preview."),
            ("Double-click the preset. It appears as a bar in the timeline and in the <b>Preset</b> section of the Properties panel.", "Klik dua kali preset. Preset tampil sebagai bar di timeline dan di bagian <b>Preset</b> panel Properties."),
        ),
        P(
            "A layer can have any number of presets. Select a bar in the timeline to edit its <b>Start</b>, <b>Duration</b> and parameters (distance, amount, period, direction…) in the Properties panel, or delete it with the trash icon or [[Delete]].",
            "Satu layer bisa punya preset sebanyak apa pun. Pilih bar di timeline untuk mengubah <b>Mulai</b>, <b>Durasi</b>, dan parameternya (jarak, besar, periode, arah, dan lainnya) di panel Properties, atau hapus dengan ikon tempat sampah atau [[Delete]].",
        ),
        IMG("timeline-simple", "The Simple timeline: one row per layer, presets as coloured bars. Drag a bar to move it, drag its edges to change its length.", "Timeline Simple: satu baris per layer, preset sebagai bar berwarna. Seret bar untuk memindahkannya, seret tepinya untuk mengubah panjangnya."),
        H3("stagger", "Stagger: animate children one after another", "Stagger: animasikan anak layer bergantian"),
        P(
            "Tick <b>Stagger to child layers</b> at the top of the Presets panel, select a group and double-click a preset. Instead of the group, each child layer gets the preset, each starting a little later. Set the delay between them (seconds) and the order:",
            "Centang <b>Stagger ke anak layer</b> di atas panel Presets, pilih grup lalu klik dua kali preset. Bukan grupnya, melainkan setiap anak layer yang mendapat preset, masing-masing mulai sedikit lebih lambat. Atur jeda antarlayer (detik) dan urutannya:",
        ),
        DIAGRAM(svg_stagger(["In order", "Reverse", "From centre", "Random"]), svg_stagger(["Berurutan", "Terbalik", "Dari tengah", "Acak"])),
        P(
            "The letters of the logo sample use stagger: <i>Draw On</i> on the group <code>Wordmark</code> with 0.125 s between letters. Random order is seeded, so it is the same on every render.",
            "Huruf-huruf pada contoh logo memakai stagger: <i>Draw On</i> pada grup <code>Wordmark</code> dengan jeda 0,125 s antarhuruf. Urutan acak memakai seed, jadi hasilnya sama di setiap render.",
        ),
        H3("combining-presets", "Combining presets", "Menggabungkan preset"),
        DIAGRAM(
            svg_blend(["Same property: the later one takes over", "the second Slide In wins where they overlap", "Loop and Emphasis add on top", "Float keeps moving during the Enter"]),
            svg_blend(["Properti sama: yang belakangan mengambil alih", "Slide In kedua menang di bagian yang tumpang tindih", "Loop dan Emphasis ditambahkan di atasnya", "Float tetap bergerak selama Enter"]),
        ),
        UL(
            ("<b>Enter and Exit</b> presets <i>override</i>: where two of them change the same property at the same time, the one that starts later wins.", "Preset <b>Enter dan Exit</b> bersifat <i>menimpa</i>: bila dua preset mengubah properti yang sama pada waktu yang sama, yang mulai belakangan yang menang."),
            ("<b>Loop and Emphasis</b> presets are <i>added</i> on top of everything else, so a layer can float while it slides in.", "Preset <b>Loop dan Emphasis</b> <i>ditambahkan</i> di atas yang lain, jadi layer bisa melayang sambil masuk."),
            ("<b>Keyframes</b> are the base: presets work relative to the keyframed value.", "<b>Keyframe</b> adalah dasarnya: preset bekerja relatif terhadap nilai keyframe."),
            ("Presets that rotate or scale (Swing, Spin, Pop…) turn around the <b>anchor point</b>; move it first if the pivot matters.", "Preset yang memutar atau menskala (Swing, Spin, Pop, dan lainnya) berporos pada <b>anchor point</b>; pindahkan dulu bila porosnya penting."),
        ),
        H3("bake", "Bake to Keyframes", "Bake ke Keyframe"),
        P(
            "<b>Animation ▸ Bake to Keyframes</b> turns the presets of the selected layer into ordinary keyframes, so you can fine-tune them in the Graph Editor. The badge next to each preset (<i>Bake</i>) means it is exported to Lottie in this baked form.",
            "<b>Animation ▸ Bake ke Keyframe</b> mengubah preset pada layer terpilih menjadi keyframe biasa, supaya bisa disetel halus di Graph Editor. Label di samping setiap preset (<i>Bake</i>) berarti preset itu diekspor ke Lottie dalam bentuk bake ini.",
        ),
        H3("preset-list", "All presets", "Daftar semua preset"),
    ]
    tag = {"enter": "Enter", "exit": "Exit", "loop": "Loop", "emphasis": "Emphasis"}
    s.append(
        TABLE(
            [B("Category", "Kategori"), B("Preset", "Preset"), B("Description", "Deskripsi")],
            [[f'<span class="tag {p["cat"]}">{tag[p["cat"]]}</span>', f"<b>{p['name']}</b>", B(p["en"], p["idn"])] for p in presets],
        )
    )
    s.append(
        TIP(
            "Presets marked <i>needs a stroke</i> (Draw On, Draw From Centre, Draw Off, Trace) animate Trim Paths and only show on paths with a stroke.",
            "Preset bertanda <i>butuh stroke</i> (Draw On, Draw From Centre, Draw Off, Trace) menganimasikan Trim Paths dan hanya terlihat pada path yang punya stroke.",
        )
    )

    content3.preset_reference(doc, G_ANIM, {n: content3.pretty(n) for n, _ in content3.easing_names()})

    # ============================================================ keyframes
    s = doc.section("keyframes", G_ANIM, B("Keyframes and easing", "Keyframe dan easing"), B("Full control: set values at moments in time and Motionator fills in the frames between.", "Kontrol penuh: tentukan nilai pada titik waktu tertentu dan Motionator mengisi frame di antaranya."))
    s += [
        IMG("timeline-keys", "The Advanced timeline: Plane twirled open, Position and Rotation have keyframes (diamonds).", "Timeline Advanced: Plane dibuka, Position dan Rotation punya keyframe (berlian)."),
        H3("making-keyframes", "Making keyframes", "Membuat keyframe"),
        STEPS(
            ("Switch to the <b>Advanced</b> workspace [[Shift+F11]] and twirl a layer open with its arrow.", "Pindah ke workspace <b>Advanced</b> [[Shift+F11]] dan buka layer dengan panahnya."),
            ("Click the <b>stopwatch</b> next to a property (here or in the Properties panel). A keyframe is made at the playhead with the current value.", "Klik <b>stopwatch</b> di samping properti (di sini atau di panel Properties). Keyframe dibuat di playhead dengan nilai saat ini."),
            ("Move the playhead and change the value, by dragging the number, typing, or moving the layer on the canvas. A new keyframe is added automatically.", "Pindahkan playhead lalu ubah nilainya, dengan menyeret angka, mengetik, atau memindah layer di canvas. Keyframe baru otomatis ditambahkan."),
            ("Use the ◇ button to add or remove a keyframe at the playhead, and ‹ › to jump between keyframes ([[J]] / [[K]]).", "Pakai tombol ◇ untuk menambah atau menghapus keyframe di playhead, dan ‹ › untuk melompat antarkeyframe ([[J]] / [[K]])."),
        ),
        UL(
            ("<b>Select</b> keyframes by clicking; [[Shift]]-click to select several.", "<b>Pilih</b> keyframe dengan klik; [[Shift]]+klik untuk memilih beberapa."),
            ("<b>Move</b> them by dragging; [[Delete]] removes them.", "<b>Pindahkan</b> dengan menyeret; [[Delete]] menghapusnya."),
            ("Clicking the stopwatch again removes all keyframes of that property.", "Klik stopwatch sekali lagi untuk menghapus semua keyframe properti itu."),
            ("[[U]] shows only the properties that are animated.", "[[U]] hanya menampilkan properti yang beranimasi."),
        ),
        H3("easing", "Easing", "Easing"),
        P(
            "Easing controls how a value speeds up and slows down between keyframes. Select keyframes and press:",
            "Easing mengatur bagaimana nilai mempercepat dan melambat di antara keyframe. Pilih keyframe lalu tekan:",
        ),
        DIAGRAM(svg_easing("progress ↑ / time →"), svg_easing("progres ↑ / waktu →")),
        TABLE(
            [B("Easing", "Easing"), B("Key", "Tombol"), B("Feels like", "Kesannya")],
            [
                ["Linear", "", B("Constant speed, mechanical.", "Kecepatan tetap, mekanis.")],
                ["Easy Ease", "[[F9]]", B("Slows into and out of the keyframe: natural motion.", "Melambat saat masuk dan keluar dari keyframe: gerakan alami.")],
                ["Easy Ease In", "[[Shift+F9]]", B("Arrives gently (slows down into the keyframe).", "Tiba dengan lembut (melambat menuju keyframe).")],
                ["Easy Ease Out", "[[Ctrl+Shift+F9]]", B("Leaves gently (speeds up out of the keyframe).", "Berangkat dengan lembut (mempercepat keluar dari keyframe).")],
            ],
        ),
        P(
            "For finer control, shape the curve in the Graph Editor.",
            "Untuk kontrol lebih halus, bentuk kurvanya di Graph Editor.",
        ),
    ]

    content3.easing_reference(doc, G_ANIM)

    # ============================================================ graph editor
    s = doc.section("graph-editor", G_ANIM, B("Graph Editor", "Graph Editor"), B("See and shape the timing of keyframes as curves.", "Lihat dan bentuk timing keyframe sebagai kurva."))
    s += [
        P(
            "Open it with [[Shift+F3]] or the graph button at the top of the timeline (Advanced workspace). Choose the property in the drop-down; only properties with keyframes are listed.",
            "Buka dengan [[Shift+F3]] atau tombol grafik di atas timeline (workspace Advanced). Pilih properti di drop-down; hanya properti berkeyframe yang ditampilkan.",
        ),
        IMG("graph-value", "Value graph: the value of Position X over time, with keys and easing handles.", "Grafik nilai: nilai Position X terhadap waktu, dengan key dan handle easing."),
        H3("value-graph", "Value graph", "Grafik nilai"),
        UL(
            ("Drag a <b>key</b> (square) up or down to change its value, left or right to change its time.", "Seret <b>key</b> (kotak) ke atas/bawah untuk mengubah nilainya, ke kiri/kanan untuk mengubah waktunya."),
            ("Drag the round <b>handles</b> to shape the easing: long, flat handles give a soft ease; short ones a sharp change.", "Seret <b>handle</b> bulat untuk membentuk easing: handle panjang dan datar memberi ease lembut; handle pendek memberi perubahan tajam."),
            ("<b>Easy Ease</b> and <b>Linear</b> buttons set the selected segments.", "Tombol <b>Easy Ease</b> dan <b>Linear</b> mengatur segmen terpilih."),
        ),
        H3("speed-graph", "Speed graph", "Grafik kecepatan"),
        IMG("graph-speed", "Speed graph of the plane: it speeds up and slows down between keys. For Position, it is the speed along the motion path.", "Grafik kecepatan pesawat: mempercepat dan melambat di antara key. Untuk Position, ini kecepatan di sepanjang motion path."),
        P(
            "The speed graph shows how fast the value changes (units per second). It is for reading: a smooth hill means a natural ease, a sharp corner means a jolt. Edit easing in the value graph and watch the result here.",
            "Grafik kecepatan menunjukkan seberapa cepat nilai berubah (satuan per detik). Grafik ini untuk dibaca: bukit yang halus berarti ease alami, sudut tajam berarti hentakan. Ubah easing di grafik nilai dan lihat hasilnya di sini.",
        ),
    ]

    # ============================================================ motion paths
    s = doc.section("motion-paths", G_ANIM, B("Motion paths", "Motion path"), B("Position keyframes form a path you can see and curve on the canvas.", "Keyframe posisi membentuk lintasan yang bisa dilihat dan dilengkungkan di canvas."))
    s += [
        IMG("motion-path", "The plane's motion path: squares are keyframes, circles are the curve handles.", "Motion path pesawat: kotak adalah keyframe, lingkaran adalah handle kurva."),
        UL(
            ("When Position has two or more keyframes, the selected layer shows its path on the canvas.", "Bila Position punya dua keyframe atau lebih, layer terpilih menampilkan lintasannya di canvas."),
            ("Drag a <b>keyframe square</b> to move that position.", "Seret <b>kotak keyframe</b> untuk memindah posisi itu."),
            ("Drag a <b>handle</b> to bend the path into a curve. Handles on both sides stay in line for a smooth curve.", "Seret <b>handle</b> untuk melengkungkan lintasan. Handle di kedua sisi tetap segaris agar kurvanya halus."),
            ("With the <b>Pen</b> tool [[G]], click a keyframe to switch between a smooth curve and a sharp corner.", "Dengan tool <b>Pen</b> [[G]], klik keyframe untuk beralih antara kurva halus dan sudut tajam."),
            ("Hold [[Alt]] while dragging a handle to break the pair and make a sharp turn.", "Tahan [[Alt]] saat menyeret handle untuk memisahkan pasangannya dan membuat belokan tajam."),
        ),
        TIP(
            "Motion paths are exported to Lottie as real curves, so the web version moves exactly like the video.",
            "Motion path diekspor ke Lottie sebagai kurva asli, jadi versi web bergerak persis seperti videonya.",
        ),
    ]

    # ============================================================ trim paths
    s = doc.section("trim-paths", G_ANIM, B("Trim Paths: drawing lines on", "Trim Paths: menggambar garis"), B("Show only part of each stroke to draw logos and line art on.", "Tampilkan hanya sebagian setiap stroke untuk menggambar logo dan line art."))
    s += [
        DIAGRAM(svg_trim(["Start", "End", "Offset shifts the visible part along the path"]), svg_trim(["Start", "End", "Offset menggeser bagian yang terlihat di sepanjang path"])),
        TABLE(
            [B("Property", "Properti"), B("Meaning", "Arti")],
            [
                ["Start", B("Where the visible part begins, 0–100 % of the path length.", "Awal bagian yang terlihat, 0–100 % panjang path.")],
                ["End", B("Where it ends. Animate End from 0 % to 100 % to draw the line on.", "Akhirnya. Animasikan End dari 0 % ke 100 % untuk menggambar garis.")],
                ["Offset", B("Shifts both along the path in degrees (360° = once around). Animate it to make a segment travel.", "Menggeser keduanya di sepanjang path dalam derajat (360° = satu putaran). Animasikan untuk membuat segmen berjalan.")],
            ],
        ),
        P(
            "Trim Paths applies to every stroked path inside the layer, each path trimmed on its own. The easiest way is the <i>Draw On</i>, <i>Draw From Centre</i>, <i>Draw Off</i> and <i>Trace</i> presets; for full control, keyframe Start, End and Offset.",
            "Trim Paths berlaku untuk setiap path ber-stroke di dalam layer, masing-masing dipangkas sendiri. Cara termudah adalah preset <i>Draw On</i>, <i>Draw From Centre</i>, <i>Draw Off</i>, dan <i>Trace</i>; untuk kontrol penuh, beri keyframe pada Start, End, dan Offset.",
        ),
        STRIP("logo", ["0.3 s", "0.9 s", "1.5 s", "2.6 s"], "The ring and the wave of the logo sample are drawn on with Draw On.", "Cincin dan gelombang pada contoh logo tergambar dengan Draw On."),
        WARN("Trim Paths only affects strokes. Filled shapes are not affected; reveal those with Wipe In or Iris In instead.", "Trim Paths hanya memengaruhi stroke. Bentuk berisi tidak terpengaruh; munculkan dengan Wipe In atau Iris In."),
    ]

    # ============================================================ effects
    s = doc.section("effects", G_ANIM, B("Effects and what each export supports", "Efek dan dukungan setiap ekspor"))
    s += [
        P(
            "Every layer has Skew, Blur, Tint and Reveal in the Properties panel, each with its own stopwatch. Not every web format can show every effect, so plan with this table if you export to Lottie or SVG:",
            "Setiap layer punya Skew, Blur, Tint, dan Reveal di panel Properties, masing-masing dengan stopwatch sendiri. Tidak semua format web bisa menampilkan setiap efek, jadi rencanakan dengan tabel ini bila mengekspor ke Lottie atau SVG:",
        ),
        TABLE(
            [B("Feature", "Fitur"), B("Video", "Video"), "Lottie", B("Animated SVG", "SVG animasi")],
            [
                [B("Transform, opacity, skew", "Transform, opacity, skew"), YES, YES, YES],
                [B("Curved motion paths", "Motion path melengkung"), YES, YES, YES],
                ["Trim Paths", YES, YES, YES],
                ["Blur", YES, NO, part("CSS blur (may differ slightly per browser)", "blur CSS (bisa sedikit beda antarbrowser)")],
                ["Tint", YES, YES, NO],
                ["Reveal / wipe", YES, part("as a mask (not on the root SVG layer)", "sebagai mask (tidak pada layer SVG utama)"), NO],
                [B("Clip paths from the SVG", "Clip-path dari SVG"), YES, part("outer clip only when nested", "hanya clip terluar bila bertingkat"), YES],
                [B("SVG filters, patterns, blend modes", "Filter, pattern, blend mode SVG"), YES, NO, YES],
                ["Audio", YES, NO, NO],
            ],
        ),
        NOTE(
            "Each export shows a compatibility report listing exactly what was simplified or left out, so nothing is lost silently.",
            "Setiap ekspor menampilkan laporan kompatibilitas yang mencantumkan apa saja yang disederhanakan atau diabaikan, jadi tidak ada yang hilang diam-diam.",
        ),
    ]

    # ============================================================ my presets
    s = doc.section("my-presets", G_ANIM, B("Saving your own presets", "Menyimpan preset sendiri"))
    s += [
        IMG("dialog-savepreset", "Save as Preset: keyframes are stored relative to the rest pose.", "Simpan sebagai Preset: keyframe disimpan relatif terhadap pose diam.", "medium"),
        STEPS(
            ("Animate a layer with keyframes until you like the motion.", "Animasikan layer dengan keyframe sampai gerakannya pas."),
            ("Choose <b>Animation ▸ Save as Preset…</b>, give it a name and a category (Enter, Exit, Loop or Emphasis).", "Pilih <b>Animation ▸ Simpan sebagai Preset…</b>, beri nama dan kategori (Enter, Exit, Loop, atau Emphasis)."),
            ("It appears under <b>My Presets</b> in the Presets panel, in every project. Apply it like any other preset.", "Preset muncul di <b>My Presets</b> pada panel Presets, di semua proyek. Terapkan seperti preset lain."),
        ),
        P(
            "Keyframes are saved as changes from the layer's rest pose (e.g. “move 200 px left and fade in”), so the preset works on other layers wherever they are. A project that uses your preset keeps its own copy, so it still opens on another computer. Delete a preset with the trash icon in My Presets.",
            "Keyframe disimpan sebagai perubahan dari pose diam layer (misalnya “geser 200 px ke kiri dan muncul perlahan”), jadi preset bekerja di layer lain di mana pun letaknya. Proyek yang memakai preset Anda menyimpan salinannya sendiri, jadi tetap bisa dibuka di komputer lain. Hapus preset dengan ikon tempat sampah di My Presets.",
        ),
    ]

    # ============================================================ audio
    s = doc.section("audio", G_ANIM, B("Audio", "Audio"), B("One soundtrack per project, with a waveform for timing.", "Satu trek audio per proyek, dengan waveform untuk mengatur timing."))
    s += [
        IMG("timeline-audio", "The audio track at the bottom of the timeline, with its waveform and fades.", "Trek audio di bawah timeline, dengan waveform dan fade-nya."),
        STEPS(
            ("Choose <b>File ▸ Import Audio…</b> [[Ctrl+Alt+I]] or drag an audio file onto the window (WAV, MP3, AAC/M4A, FLAC, OGG).", "Pilih <b>File ▸ Impor Audio…</b> [[Ctrl+Alt+I]] atau seret file audio ke jendela (WAV, MP3, AAC/M4A, FLAC, OGG)."),
            ("The track appears at the bottom of the timeline. Drag it to move it in time; drag its edges to trim it.", "Trek muncul di bawah timeline. Seret untuk menggeser waktunya; seret tepinya untuk memangkas."),
            ("Click the track to edit it in the Properties panel.", "Klik trek untuk mengeditnya di panel Properties."),
        ),
        IMG("panel-properties-audio", "Audio properties.", "Properti audio.", "small"),
        TABLE(
            [B("Setting", "Pengaturan"), B("Meaning", "Arti")],
            [
                [B("Starts at", "Mulai di"), B("Where the sound starts in the composition.", "Titik mulai suara di komposisi.")],
                [B("Trim start", "Potong awal"), B("Skips the beginning of the file.", "Melewati bagian awal file.")],
                [B("Duration", "Durasi"), B("How long it plays.", "Lama diputar.")],
                [B("Fade in / Fade out", "Fade in / Fade out"), B("Smooth volume ramps at both ends (seconds).", "Naik/turun volume yang halus di kedua ujung (detik).")],
                [B("Volume", "Volume"), B("Gain in dB (0 dB = original).", "Gain dalam dB (0 dB = asli).")],
                [B("Mute", "Bisukan"), B("Silences the track, in preview and export.", "Membisukan trek, saat preview dan ekspor.")],
            ],
        ),
        P(
            "Audio plays along with the preview and is mixed into MP4 (AAC 320 kbps), MOV (24-bit PCM) and WebM (Opus). Lottie and animated SVG have no sound. <b>Replace</b> swaps the file and keeps the timing; the trash icon removes the track.",
            "Audio ikut diputar saat preview dan dimasukkan ke MP4 (AAC 320 kbps), MOV (PCM 24-bit), dan WebM (Opus). Lottie dan SVG animasi tidak bersuara. <b>Ganti</b> menukar file dengan timing yang sama; ikon tempat sampah menghapus trek.",
        ),
        TIP(
            "The audio file is not stored inside the project. Keep it next to the <code>.motionator</code> file; if it is moved, the track shows <i>File missing</i> and <b>Replace</b> lets you find it again.",
            "File audio tidak disimpan di dalam proyek. Simpan di samping file <code>.motionator</code>; bila dipindah, trek menampilkan <i>File hilang</i> dan <b>Ganti</b> untuk mencarinya lagi.",
        ),
    ]

    content3.principles(doc, G_ANIM)

    # ============================================================ render queue
    s = doc.section("video-export", G_OUT, B("Video export: Render Queue", "Ekspor video: Render Queue"), B("Render one composition to several formats and sizes in one go.", "Render satu komposisi ke beberapa format dan ukuran sekaligus."))
    s += [
        IMG("render-queue", "The Render Queue with two outputs of the background sample, after a loop check.", "Render Queue dengan dua output dari contoh background, setelah cek loop."),
        STEPS(
            ("Click <b>Export</b> or press [[Ctrl+M]]: the composition is added to the queue. Add it again for more outputs.", "Klik <b>Export</b> atau tekan [[Ctrl+M]]: komposisi ditambahkan ke antrean. Tambahkan lagi untuk output lain."),
            ("Choose the <b>format</b> and <b>size</b> of each item, and tick <b>Blur</b> for motion blur.", "Pilih <b>format</b> dan <b>ukuran</b> setiap item, dan centang <b>Blur</b> untuk motion blur."),
            ("Click <b>Choose output…</b> to set the file name.", "Klik <b>Pilih tujuan…</b> untuk menentukan nama file."),
            ("Press <b>Render</b>. Items render one after another with progress and time left; each can be cancelled.", "Tekan <b>Render</b>. Item dirender satu per satu dengan progres dan sisa waktu; masing-masing bisa dibatalkan."),
        ),
        H3("formats", "Formats", "Format"),
        TABLE(
            [B("Format", "Format"), B("Transparency", "Transparansi"), B("Use it for", "Dipakai untuk")],
            [
                ["H.264 (MP4)", NO, B("Stock footage, social media, presentations: plays everywhere.", "Footage stok, media sosial, presentasi: bisa diputar di mana saja.")],
                ["ProRes 422 HQ (MOV)", NO, B("Masters for editing and for stock sites that accept ProRes; large files.", "Master untuk editing dan situs stok yang menerima ProRes; file besar.")],
                ["ProRes 4444 (MOV)", YES, B("Overlays with transparency for video editors (Premiere, Resolve, Final Cut).", "Overlay transparan untuk editor video (Premiere, Resolve, Final Cut).")],
                ["VP9 (WebM)", YES, B("Transparent video for websites.", "Video transparan untuk website.")],
            ],
        ),
        P(
            "<b>Size</b> scales the composition to 720p, 1080p, 1440p or 2160p (4K UHD) keeping its aspect ratio, or keeps the composition size. Because Motionator draws vectors, a 4K render is as sharp as the composition at any size. H.264 and VP9 need even widths and heights; an odd size is shown in red.",
            "<b>Ukuran</b> menskala komposisi ke 720p, 1080p, 1440p, atau 2160p (4K UHD) dengan rasio tetap, atau memakai ukuran komposisi. Karena Motionator menggambar vektor, render 4K tetap tajam di ukuran berapa pun. H.264 dan VP9 butuh lebar dan tinggi genap; ukuran ganjil ditandai merah.",
        ),
        P(
            "<b>Motion blur</b> blends 8 sub-frames per frame (180° shutter) for natural blur on fast motion. It takes about 8× longer to render.",
            "<b>Motion blur</b> memadukan 8 sub-frame per frame (shutter 180°) untuk blur alami pada gerakan cepat. Render menjadi sekitar 8× lebih lama.",
        ),
        H3("stock-presets", "Stock presets and checks", "Preset stok dan pemeriksaan"),
        P(
            "<b>Stock preset…</b> adds an item already set up for microstock sites:",
            "<b>Preset stok…</b> menambahkan item yang sudah diatur untuk situs microstock:",
        ),
        TABLE(
            [B("Preset", "Preset"), B("Output", "Output")],
            [
                ["Microstock 4K · H.264", B("3840×2160, high-quality H.264 (CRF 12)", "3840×2160, H.264 kualitas tinggi (CRF 12)")],
                ["Microstock 4K · ProRes 422 HQ", B("3840×2160 master", "Master 3840×2160")],
                ["Microstock HD · H.264", B("1920×1080, H.264 (CRF 14)", "1920×1080, H.264 (CRF 14)")],
            ],
        ),
        P(
            "A yellow warning appears on an item when something is commonly rejected by stock sites: a clip shorter than 5 s or longer than 60 s, a height below 1080 px, a non-standard frame rate, or a format with alpha. Always check the current rules of the site you upload to.",
            "Peringatan kuning muncul pada item bila ada yang umumnya ditolak situs stok: klip lebih pendek dari 5 s atau lebih panjang dari 60 s, tinggi di bawah 1080 px, frame rate tidak standar, atau format dengan alpha. Selalu cek aturan terbaru situs tujuan.",
        ),
        H3("loop-check", "Checking a seamless loop", "Memeriksa loop mulus"),
        DIAGRAM(svg_loop(["10 s", "the last frame must match the first"]), svg_loop(["10 s", "frame terakhir harus sama dengan frame pertama"])),
        P(
            "Looping backgrounds sell better when they repeat without a visible jump. <b>Check loop</b> compares every layer at the end of the composition with the start. If something differs, it lists the layers and properties. <b>Match the end to the start</b> adds keyframes at the end with the start values. Loop presets are always seamless; Enter, Exit and Emphasis presets cannot be fixed automatically, so use Loop presets or remove them.",
            "Background yang bisa di-loop lebih laku bila berulang tanpa lompatan yang terlihat. <b>Cek loop</b> membandingkan setiap layer di akhir komposisi dengan awalnya. Bila ada yang berbeda, layer dan propertinya dicantumkan. <b>Samakan akhir dengan awal</b> menambahkan keyframe di akhir dengan nilai awal. Preset Loop selalu mulus; preset Enter, Exit, dan Emphasis tidak bisa diperbaiki otomatis, jadi pakai preset Loop atau hapus.",
        ),
    ]

    # ============================================================ lottie
    s = doc.section("lottie", G_OUT, B("Lottie export", "Ekspor Lottie"), B("Small JSON animations for websites and apps.", "Animasi JSON kecil untuk website dan aplikasi."))
    s += [
        IMG("dialog-lottie", "Export Lottie with its compatibility report and the estimated size.", "Ekspor Lottie dengan laporan kompatibilitas dan perkiraan ukuran.", "medium"),
        STEPS(
            ("Choose <b>File ▸ Export Lottie…</b> [[Ctrl+Alt+L]].", "Pilih <b>File ▸ Ekspor Lottie…</b> [[Ctrl+Alt+L]]."),
            ("Decide whether to include the composition background (Lottie is usually transparent) and the number precision (fewer decimals = smaller file).", "Tentukan apakah background komposisi disertakan (Lottie umumnya transparan) dan presisi angka (lebih sedikit desimal = file lebih kecil)."),
            ("Read the compatibility report, then click <b>Export…</b> and save the <code>.json</code> file.", "Baca laporan kompatibilitas, lalu klik <b>Ekspor…</b> dan simpan file <code>.json</code>."),
        ),
        P(
            "Keyframes are exported as Lottie keyframes with their easing; presets are exported as sampled keyframes (simplified), which looks the same. Shapes, gradients, strokes, Trim Paths, clip paths and Tint are kept.",
            "Keyframe diekspor sebagai keyframe Lottie lengkap dengan easing-nya; preset diekspor sebagai keyframe sampel (disederhanakan) yang tampilannya sama. Bentuk, gradien, stroke, Trim Paths, clip-path, dan Tint dipertahankan.",
        ),
        H3("lottie-web", "Using it on a web page", "Memakainya di halaman web"),
        CODE("""<div id="logo" style="width:480px;height:270px"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.12.2/lottie.min.js"></script>
<script>
  lottie.loadAnimation({
    container: document.getElementById("logo"),
    renderer: "svg",
    loop: true,
    autoplay: true,
    path: "logo.json"
  });
</script>"""),
        P(
            "Or use the <code>&lt;lottie-player&gt;</code> / <code>&lt;dotlottie-player&gt;</code> web components, Lottie for Android/iOS, or upload the file to LottieFiles. Test the JSON in the player you will use: support for some features differs between players.",
            "Atau pakai web component <code>&lt;lottie-player&gt;</code> / <code>&lt;dotlottie-player&gt;</code>, Lottie untuk Android/iOS, atau unggah file ke LottieFiles. Uji JSON di player yang akan dipakai: dukungan beberapa fitur berbeda antarplayer.",
        ),
    ]

    # ============================================================ svg export
    s = doc.section("svg-export", G_OUT, B("Animated SVG export", "Ekspor SVG animasi"), B("One self-contained .svg that moves with CSS, with no library needed.", "Satu file .svg mandiri yang bergerak dengan CSS, tanpa library."))
    s += [
        IMG("dialog-svg", "Export Animated SVG: loop, background and the compatibility report.", "Ekspor SVG Animasi: loop, background, dan laporan kompatibilitas.", "medium"),
        P(
            "Choose <b>File ▸ Export Animated SVG…</b> [[Ctrl+Alt+G]]. Tick <b>Loop</b> to repeat forever or leave it off to stop on the last frame. The file contains your artwork and CSS keyframe animations; it plays in every modern browser.",
            "Pilih <b>File ▸ Ekspor SVG Animasi…</b> [[Ctrl+Alt+G]]. Centang <b>Loop</b> agar berulang terus, atau biarkan kosong agar berhenti di frame terakhir. File berisi artwork dan animasi CSS keyframe; bisa diputar di semua browser modern.",
        ),
        H3("svg-embed", "Putting it on a page", "Memasangnya di halaman"),
        CODE("""<!-- as an image: simplest, the animation plays on its own -->
<img src="icon.svg" width="256" height="256" alt="Paper plane">

<!-- inline in the HTML: lets your page's CSS reach inside -->
<div class="hero-icon">
  <!-- paste the contents of icon.svg here -->
</div>"""),
        UL(
            ("<b>&lt;img&gt;</b> and CSS <code>background-image</code> work and keep the animation; scripts on the page cannot control it.", "<b>&lt;img&gt;</b> dan CSS <code>background-image</code> bisa dipakai dan animasinya tetap jalan; script di halaman tidak bisa mengendalikannya."),
            ("Inline SVG can be paused with <code>animation-play-state: paused</code> on its elements.", "SVG inline bisa dijeda dengan <code>animation-play-state: paused</code> pada elemennya."),
        ),
        TABLE(
            [B("Choose", "Pilih"), B("When", "Bila")],
            [
                [B("Animated SVG", "SVG animasi"), B("Icons, logos and illustrations on websites, with no JavaScript. Usually the smallest file.", "Ikon, logo, dan ilustrasi di website, tanpa JavaScript. Biasanya file paling kecil.")],
                ["Lottie", B("Apps (Android, iOS, Flutter, React Native), or when you need to control playback from code.", "Aplikasi (Android, iOS, Flutter, React Native), atau bila pemutaran perlu dikendalikan lewat kode.")],
                [B("Video (VP9/MP4)", "Video (VP9/MP4)"), B("Complex scenes with heavy blur, many layers or filters.", "Adegan rumit dengan blur berat, banyak layer, atau filter.")],
            ],
        ),
    ]

    content3.web_integration(doc, G_OUT)
    content3.microstock(doc, G_OUT)

    # ============================================================ projects
    s = doc.section("projects", G_OUT, B("Projects, auto-save and recovery", "Proyek, auto-save, dan pemulihan"))
    s += [
        IMG("menu-file", "The File menu.", "Menu File.", "medium"),
        UL(
            ("<b>Save</b> [[Ctrl+S]] / <b>Save As…</b> [[Ctrl+Shift+S]] write a <code>.motionator</code> file. It contains the SVGs, keyframes, presets and your own presets used, so it is complete on its own (only audio stays a separate file).", "<b>Simpan</b> [[Ctrl+S]] / <b>Simpan Sebagai…</b> [[Ctrl+Shift+S]] menulis file <code>.motionator</code>. File ini berisi SVG, keyframe, preset, dan preset buatan sendiri yang dipakai, jadi lengkap dengan sendirinya (hanya audio yang tetap file terpisah)."),
            ("<b>New Project</b> [[Ctrl+Alt+N]] and <b>Open Project…</b> [[Ctrl+O]] ask first if there are unsaved changes. The title bar shows * when there are.", "<b>Proyek Baru</b> [[Ctrl+Alt+N]] dan <b>Buka Proyek…</b> [[Ctrl+O]] bertanya dulu bila ada perubahan yang belum disimpan. Title bar menampilkan * bila ada."),
            ("<b>Auto-save</b> keeps a recovery copy every minute (change it in Preferences). It never overwrites your file.", "<b>Auto-save</b> menyimpan salinan pemulihan setiap menit (ubah di Preferensi). Tidak pernah menimpa file Anda."),
            ("After a crash or power cut, Motionator offers <b>Recover project</b> on the next start. Choose Recover to continue, or Discard.", "Setelah crash atau listrik padam, Motionator menawarkan <b>Pulihkan proyek</b> saat dibuka lagi. Pilih Pulihkan untuk melanjutkan, atau Buang."),
        ),
    ]

    # ============================================================ tutorials
    s = doc.section("tutorial-logo", G_REF, B("Tutorial: logo reveal with sound", "Tutorial: logo reveal dengan suara"), B("Uses samples/logo.svg. Result: samples/logo.motionator.", "Memakai samples/logo.svg. Hasil: samples/logo.motionator."))
    s += [
        STRIP("logo", ["0.3 s", "0.9 s", "1.5 s", "2.6 s"]),
        STEPS(
            ("<b>New project.</b> Press [[Ctrl+K]]: 1920×1080, 30 fps, 4 s, white background.", "<b>Proyek baru.</b> Tekan [[Ctrl+K]]: 1920×1080, 30 fps, 4 s, background putih."),
            ("<b>Import</b> <code>logo.svg</code> [[Ctrl+I]]. The layers are <code>Mark</code> (Ring, Wave, Dot), <code>Wordmark</code> (the letters) and <code>Underline</code>.", "<b>Impor</b> <code>logo.svg</code> [[Ctrl+I]]. Layer-nya adalah <code>Mark</code> (Ring, Wave, Dot), <code>Wordmark</code> (huruf-huruf), dan <code>Underline</code>."),
            ("<b>Make it bigger.</b> Select the root layer <code>logo.svg</code> and set Scale to 210 %: vectors stay sharp.", "<b>Perbesar.</b> Pilih layer root <code>logo.svg</code> lalu atur Scale ke 210 %: vektor tetap tajam."),
            ("<b>Draw the mark.</b> At 0 s select <code>Ring</code> and apply <i>Draw On</i>, then do the same for <code>Wave</code>. In the Properties panel set each Duration to 1.5 s.", "<b>Gambar logonya.</b> Di 0 s pilih <code>Ring</code> lalu terapkan <i>Draw On</i>, lalu lakukan hal yang sama untuk <code>Wave</code>. Di panel Properties atur Durasi masing-masing ke 1,5 s."),
            ("<b>Write the letters one by one.</b> Tick <i>Stagger to child layers</i> with 0.125 s, In order. Move the playhead to 0.5 s, select <code>Wordmark</code> and apply <i>Draw On</i>: each letter draws a little after the previous one. Untick stagger afterwards.", "<b>Tulis huruf satu per satu.</b> Centang <i>Stagger ke anak layer</i> dengan 0,125 s, Berurutan. Pindahkan playhead ke 0,5 s, pilih <code>Wordmark</code> lalu terapkan <i>Draw On</i>: setiap huruf tergambar sedikit setelah huruf sebelumnya. Matikan stagger setelahnya."),
            ("<b>Pop the dot.</b> At 1.4 s select <code>Dot</code> and apply <i>Scale Pop</i>.", "<b>Munculkan titik.</b> Di 1,4 s pilih <code>Dot</code> lalu terapkan <i>Scale Pop</i>."),
            ("<b>Wipe the underline.</b> At 1.8 s select <code>Underline</code> and apply <i>Wipe In</i> (From the left).", "<b>Sapu garis bawah.</b> Di 1,8 s pilih <code>Underline</code> lalu terapkan <i>Wipe In</i> (Dari kiri)."),
            ("<b>Accent.</b> At 3.0 s select <code>Mark</code> and apply <i>Pop</i>; lower Amount to 8 % for a subtle beat.", "<b>Aksen.</b> Di 3,0 s pilih <code>Mark</code> lalu terapkan <i>Pop</i>; turunkan Amount ke 8 % agar ketukannya halus."),
            ("<b>Sound.</b> Import a short whoosh or chime with [[Ctrl+Alt+I]] and line it up with the Pop using the waveform.", "<b>Suara.</b> Impor efek whoosh atau chime pendek dengan [[Ctrl+Alt+I]] dan sejajarkan dengan Pop memakai waveform."),
            ("<b>Export.</b> MP4 for social media; for the website, <b>Export Animated SVG</b> without Loop so it stops on the finished logo.", "<b>Ekspor.</b> MP4 untuk media sosial; untuk website, <b>Ekspor SVG Animasi</b> tanpa Loop supaya berhenti di logo yang utuh."),
        ),
        TIP("Rotate or scale a logo part around its centre? Check where its anchor point is first: press [[Y]] and drag it, or use Layer ▸ Center Anchor Point.", "Ingin memutar atau menskala bagian logo pada pusatnya? Periksa dulu letak anchor point-nya: tekan [[Y]] lalu seret, atau pakai Layer ▸ Pusatkan Anchor Point."),
    ]

    s = doc.section("tutorial-stock", G_REF, B("Tutorial: seamless 4K stock background", "Tutorial: background stok 4K yang mulus"), B("Uses samples/background.svg and ambient.wav. Result: samples/background.motionator.", "Memakai samples/background.svg dan ambient.wav. Hasil: samples/background.motionator."))
    s += [
        STRIP("background", ["0 s", "2.5 s", "5 s", "7.5 s"]),
        IMG("bg-overview", "The background project: every layer uses Loop presets.", "Proyek background: semua layer memakai preset Loop."),
        STEPS(
            ("<b>Composition.</b> [[Ctrl+K]]: 3840×2160 (or 1920×1080, Motionator scales up sharply), 30 fps, <b>10 s</b>.", "<b>Komposisi.</b> [[Ctrl+K]]: 3840×2160 (atau 1920×1080, Motionator memperbesar dengan tajam), 30 fps, <b>10 s</b>."),
            ("<b>Import</b> <code>background.svg</code>: Backdrop, Sun_Glow, Sun, Bubbles (Bubble_1–5), Wave_Back, Wave_Front, Ribbon.", "<b>Impor</b> <code>background.svg</code>: Backdrop, Sun_Glow, Sun, Bubbles (Bubble_1–5), Wave_Back, Wave_Front, Ribbon."),
            ("<b>Use only Loop presets</b> so the end matches the start. The sample uses the settings in the table below.", "<b>Pakai preset Loop saja</b> supaya akhir sama dengan awal. Contoh ini memakai pengaturan di tabel bawah."),
            ("<b>Make periods divide the duration.</b> In a 10 s clip, use periods of 10, 5, 2.5 or 2 s so every cycle completes exactly at the end. The bubbles use 5, 3.33 and 2.5 s so they never move in step (10 ÷ 3.33 = 3 cycles).", "<b>Buat periode habis membagi durasi.</b> Pada klip 10 s, pakai periode 10, 5, 2,5, atau 2 s supaya setiap siklus selesai tepat di akhir. Gelembung memakai 5, 3,33, dan 2,5 s supaya tidak bergerak serempak (10 ÷ 3,33 = 3 siklus)."),
            ("<b>Audio (optional).</b> Import <code>ambient.wav</code>; set Fade in and Fade out to 1 s. Many stock sites prefer clips without sound, so you can also mute it for the upload.", "<b>Audio (opsional).</b> Impor <code>ambient.wav</code>; atur Fade in dan Fade out 1 s. Banyak situs stok lebih suka klip tanpa suara, jadi bisa juga dibisukan saat unggah."),
            ("<b>Check the loop.</b> [[Ctrl+M]], then <b>Check loop</b> in the Render Queue. It should say <i>Seamless</i>.", "<b>Cek loop.</b> [[Ctrl+M]], lalu <b>Cek loop</b> di Render Queue. Hasilnya harus <i>Loop mulus</i>."),
            ("<b>Render.</b> Choose <i>Microstock 4K · H.264</i> and, if the site accepts it, <i>Microstock 4K · ProRes 422 HQ</i>. Fix any yellow warning, then Render.", "<b>Render.</b> Pilih <i>Microstock 4K · H.264</i> dan, bila situs menerimanya, <i>Microstock 4K · ProRes 422 HQ</i>. Perbaiki peringatan kuning bila ada, lalu Render."),
        ),
        TABLE(
            [B("Layer", "Layer"), B("Preset", "Preset"), B("Settings", "Pengaturan")],
            [
                ["Sun", "Pulse", B("Amount 6 %, Period 5 s", "Amount 6 %, Periode 5 s")],
                ["Sun_Glow", "Glow", B("Min 45 %, Period 2.5 s", "Min 45 %, Periode 2,5 s")],
                ["Bubble_1 … Bubble_5", "Drift", B("Amplitude 40 px; Periods 5, 3.33, 2.5, 5, 3.33 s", "Amplitudo 40 px; Periode 5; 3,33; 2,5; 5; 3,33 s")],
                ["Wave_Back", "Sway", B("Angle 3°, Period 5 s", "Sudut 3°, Periode 5 s")],
                ["Wave_Front", "Float", B("Amplitude 14 px, Period 2.5 s", "Amplitudo 14 px, Periode 2,5 s")],
                ["Ribbon", "Trace", B("Length 35 %, Period 5 s", "Panjang 35 %, Periode 5 s")],
            ],
        ),
        NOTE(
            "Upload checklist: 5–60 s long, at least 1920×1080, standard frame rate, no logos or trademarks you do not own, a descriptive title and keywords. Mention “seamless loop” in the description.",
            "Daftar periksa unggah: durasi 5–60 s, minimal 1920×1080, frame rate standar, tanpa logo atau merek dagang milik orang lain, judul dan kata kunci yang deskriptif. Sebutkan “seamless loop” di deskripsi.",
        ),
    ]

    s = doc.section("tutorial-web", G_REF, B("Tutorial: animated icon for a website", "Tutorial: ikon animasi untuk website"), B("Uses samples/icon.svg. Result: samples/icon.motionator.", "Memakai samples/icon.svg. Hasil: samples/icon.motionator."))
    s += [
        STRIP("icon", ["0 s", "0.6 s", "1.2 s", "2.4 s"]),
        STEPS(
            ("<b>Composition</b> 1080×1080, 30 fps, 3 s, <b>Transparent</b> ticked. (Vectors scale, so a large composition costs nothing for Lottie or SVG.)", "<b>Komposisi</b> 1080×1080, 30 fps, 3 s, <b>Transparan</b> dicentang. (Vektor bisa diskala, jadi komposisi besar tidak ada ruginya untuk Lottie atau SVG.)"),
            ("<b>Import</b> <code>icon.svg</code>: Badge, Plane (Plane_Body, Plane_Fold) and Trail. Set the root layer's Scale to 190 %.", "<b>Impor</b> <code>icon.svg</code>: Badge, Plane (Plane_Body, Plane_Fold), dan Trail. Atur Scale layer root ke 190 %."),
            ("<b>Badge.</b> At 0 s apply <i>Scale Pop</i> to <code>Badge</code>, and <i>Hover</i> (Loop) with Amplitude 6 px and Period 1.5 s so it keeps floating.", "<b>Badge.</b> Di 0 s terapkan <i>Scale Pop</i> pada <code>Badge</code>, dan <i>Hover</i> (Loop) dengan Amplitudo 6 px dan Periode 1,5 s agar terus melayang."),
            ("<b>Fly the plane with keyframes.</b> Select <code>Plane</code>. At 0 s, drag it about 140 px left and 120 px down, rotate it to −25° and turn on the Position and Rotation stopwatches. At 1 s, drag it past its place (up and right) and rotate to 10°. At 2 s, put it back in place at 0°.", "<b>Terbangkan pesawat dengan keyframe.</b> Pilih <code>Plane</code>. Di 0 s, seret sekitar 140 px ke kiri dan 120 px ke bawah, putar ke −25°, lalu nyalakan stopwatch Position dan Rotation. Di 1 s, seret melewati tempatnya (ke kanan atas) dan putar ke 10°. Di 2 s, kembalikan ke tempatnya dengan 0°."),
            ("<b>Curve the path.</b> Drag the handles of the motion path on the canvas so the plane swoops.", "<b>Lengkungkan lintasan.</b> Seret handle motion path di canvas supaya pesawat meliuk."),
            ("<b>Ease it.</b> Select all keyframes and press [[F9]]. Check the speed graph [[Shift+F3]]: smooth hills, no sharp corners.", "<b>Beri easing.</b> Pilih semua keyframe lalu tekan [[F9]]. Cek grafik kecepatan [[Shift+F3]]: bukit halus, tanpa sudut tajam."),
            ("<b>Trail.</b> At 1 s apply <i>Draw On</i> to <code>Trail</code> and set its Duration to 1 s.", "<b>Jejak.</b> Di 1 s terapkan <i>Draw On</i> pada <code>Trail</code> lalu atur Durasinya ke 1 s."),
            ("<b>Export</b> both <b>Lottie</b> [[Ctrl+Alt+L]] for the app and <b>Animated SVG</b> [[Ctrl+Alt+G]] for the website, and compare the sizes in the dialogs.", "<b>Ekspor</b> <b>Lottie</b> [[Ctrl+Alt+L]] untuk aplikasi dan <b>SVG Animasi</b> [[Ctrl+Alt+G]] untuk website, lalu bandingkan ukurannya di dialog."),
        ),
    ]

    content3.tutorials_extra(doc, G_REF)

    # ============================================================ shortcuts
    s = doc.section("shortcuts", G_REF, B("Keyboard shortcuts", "Shortcut keyboard"), B("Shortcuts follow After Effects where possible.", "Shortcut mengikuti After Effects sebisa mungkin."))
    groups = [
        ("file", B("File", "File")),
        ("app", None),
        ("edit", B("Edit", "Edit")),
        ("comp", B("Composition and layer", "Komposisi dan layer")),
        ("layer", None),
        ("anim", B("Animation", "Animasi")),
        ("time", B("Time and playback", "Waktu dan pemutaran")),
        ("view", B("View", "Tampilan")),
        ("window", B("Workspaces", "Workspace")),
        ("tool", B("Tools", "Tool")),
    ]
    merged = {"app": "file", "layer": "comp"}
    rows = {g: [] for g, _ in groups}
    for cid, l_en, l_id, ks in shortcuts:
        g = cid.split(".")[0]
        rows[merged.get(g, g)].append([B(l_en, l_id), keys(ks)])
    for g, title in groups:
        if title is None or not rows[g]:
            continue
        s.append(H4(title["en"], title["id"]))
        s.append(TABLE([B("Command", "Perintah"), B("Shortcut", "Shortcut")], rows[g]))
    s.append(
        TABLE(
            [B("Mouse", "Mouse"), B("Action", "Fungsi")],
            [
                [B("Space + drag", "Space + seret"), B("Pan the canvas", "Geser canvas")],
                [B("Ctrl/Alt + wheel", "Ctrl/Alt + roda"), B("Zoom the canvas around the pointer", "Zoom canvas di sekitar kursor")],
                [B("Shift + drag", "Shift + seret"), B("Move only horizontally/vertically; rotate in 45° steps", "Gerak hanya horizontal/vertikal; putar per 45°")],
                [B("Ctrl + drag", "Ctrl + seret"), B("Invert snapping for this drag (free move when Snapping is on)", "Membalik snapping untuk seretan ini (gerak bebas saat Snapping aktif)")],
                [B("Double-click a preset", "Klik dua kali preset"), B("Apply it to the selected layer", "Terapkan ke layer terpilih")],
                [B("Esc while dragging a panel", "Esc saat menyeret panel"), B("Cancel the move", "Batalkan pemindahan")],
            ],
        )
    )

    # ============================================================ troubleshooting
    s = doc.section("troubleshooting", G_REF, B("Troubleshooting and FAQ", "Pemecahan masalah dan FAQ"))
    faq = [
        ("My SVG imports as one layer.", "SVG saya terimpor sebagai satu layer.", "The elements have no ids. Name the layers and groups in your design tool and export with ids (see Preparing SVG files).", "Elemennya tidak punya id. Beri nama layer dan grup di aplikasi desain lalu ekspor dengan id (lihat Menyiapkan file SVG)."),
        ("Text is missing.", "Teksnya hilang.", "Convert text to outlines before exporting the SVG.", "Ubah teks menjadi outline sebelum mengekspor SVG."),
        ("Draw On does nothing.", "Draw On tidak berefek.", "The paths have no stroke. Trim Paths only works on strokes; use Wipe In for filled shapes.", "Path-nya tidak punya stroke. Trim Paths hanya bekerja pada stroke; pakai Wipe In untuk bentuk berisi."),
        ("Rotation swings around the wrong point.", "Rotasi berputar di titik yang salah.", "Move the anchor point with the Anchor Point tool [[Y]] or centre it with [[Ctrl+Alt+Home]].", "Pindahkan anchor point dengan tool Anchor Point [[Y]] atau pusatkan dengan [[Ctrl+Alt+Home]]."),
        ("A preset seems to have no effect.", "Preset seperti tidak berpengaruh.", "Check the playhead: Enter presets start there, so the motion may be later in the timeline. Another Enter/Exit preset on the same property may also override it.", "Cek playhead: preset Enter mulai di sana, jadi gerakannya mungkin ada di bagian timeline yang lebih belakang. Preset Enter/Exit lain pada properti yang sama juga bisa menimpanya."),
        ("Playback stutters.", "Pemutaran tersendat.", "Let the cache fill (green bar), lower the preview resolution to Half, or switch off blur while working.", "Tunggu cache terisi (bar hijau), turunkan resolusi preview ke Half, atau matikan blur selama bekerja."),
        ("Export failed / FFmpeg not found.", "Ekspor gagal / FFmpeg tidak ditemukan.", "Reinstall Motionator. Also check that the output folder is writable and the disk has space (ProRes 4K needs several GB per minute).", "Pasang ulang Motionator. Periksa juga bahwa folder tujuan bisa ditulis dan disk masih cukup (ProRes 4K butuh beberapa GB per menit)."),
        ("“Width and height must be even”.", "“Lebar/tinggi harus genap”.", "Pick a size preset or set an even composition size; H.264 and VP9 need even sizes.", "Pilih preset ukuran atau atur ukuran komposisi genap; H.264 dan VP9 butuh ukuran genap."),
        ("The Lottie looks different in my app.", "Lottie tampil berbeda di aplikasi saya.", "Read the compatibility report; blur, filters and blend modes are not part of Lottie. Players also differ: test in the one you ship.", "Baca laporan kompatibilitas; blur, filter, dan blend mode bukan bagian dari Lottie. Player juga berbeda-beda: uji di player yang dipakai."),
        ("A panel disappeared.", "Panel hilang.", "Open it from the Window menu, or use Window ▸ Reset Layout.", "Buka lewat menu Window, atau pakai Window ▸ Reset Tata Letak."),
        ("The audio track says File missing.", "Trek audio bertuliskan File hilang.", "The audio was moved. Click the track and use Replace to locate it.", "Audio dipindah. Klik trek lalu pakai Ganti untuk mencarinya."),
    ]
    for q_en, q_id, a_en, a_id in faq + content3.FAQ_EXTRA:
        s.append(H4(q_en, q_id))
        s.append(P(a_en, a_id))

    content3.glossary(doc, G_REF)

    # ============================================================ licences
    s = doc.section("licenses", G_REF, B("About and licences", "Tentang dan lisensi"))
    s += [
        P(
            "Motionator is built with Tauri, React and Rust; vector rendering uses resvg/tiny-skia. <b>Help ▸ About</b> lists the version and the open-source components.",
            "Motionator dibuat dengan Tauri, React, dan Rust; rendering vektor memakai resvg/tiny-skia. <b>Help ▸ About</b> menampilkan versi dan komponen open-source.",
        ),
        P(
            "FFmpeg is included as a separate program under the GPL v3 and is used only to encode video and audio. Your exported videos, Lottie files and SVGs are yours to use commercially, including on stock sites.",
            "FFmpeg disertakan sebagai program terpisah dengan lisensi GPL v3 dan hanya dipakai untuk meng-encode video dan audio. Video, file Lottie, dan SVG hasil ekspor sepenuhnya milik Anda dan boleh dipakai secara komersial, termasuk di situs stok.",
        ),
        P(
            "The sample files in <code>samples/</code> were made for this guide and may be used freely for practice.",
            "File contoh di <code>samples/</code> dibuat untuk panduan ini dan boleh dipakai bebas untuk latihan.",
        ),
    ]
