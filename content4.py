"""Guide content, part 4 (roadmap 2): text layers, generators, 2.5D presets and brush reveals,
glow, microstock tools (checks, metadata CSVs, batch variations) and AI agents (Ask AI, MCP)."""
from build import B, CARDS, CODE, H3, NOTE, P, STEPS, STRIP, TABLE, TIP, UL, WARN


def text_layers(doc, G):
    s = doc.section("text-layers", G, B("Text layers and per-letter animation", "Layer teks dan animasi per huruf"), B("Type text in Motionator and animate it letter by letter.", "Ketik teks di Motionator lalu animasikan huruf demi huruf."))
    s += [
        STRIP("drop", ["0.25 s", "0.5 s", "0.75 s", "1.6 s"], "Drop Bounce on each letter with a 0.08 s stagger: the letters fall, squash on landing and settle.", "Drop Bounce pada setiap huruf dengan stagger 0,08 s: huruf jatuh, tergencet saat mendarat, lalu diam."),
        P(
            "Text inside an imported SVG is not drawn (it must be outlined first). For titles, captions and animated words, make the text in Motionator instead: it is laid out with any font installed on your computer, with proper kerning, and every letter becomes its own layer.",
            "Teks di dalam SVG impor tidak digambar (harus di-outline dulu). Untuk judul, keterangan, dan kata yang bergerak, buat teksnya di Motionator: teks disusun dengan font apa pun yang terpasang di komputer Anda, dengan kerning yang benar, dan setiap huruf menjadi layer sendiri.",
        ),
        H3("text-add", "Adding text", "Menambah teks"),
        STEPS(
            ("Choose <b>Layer ▸ New Text</b> or press [[Ctrl+T]]. A text layer reading <i>Motionator</i> appears in the middle, in a colour that shows on your background, and is selected.", "Pilih <b>Layer ▸ Teks Baru</b> atau tekan [[Ctrl+T]]. Layer teks bertuliskan <i>Motionator</i> muncul di tengah, dengan warna yang terlihat di atas latar Anda, dan langsung terpilih."),
            ("In the <b>Text</b> group of the <b>Properties</b> panel, type your text. Press [[Ctrl+Enter]] or click elsewhere to apply it; press Enter for a new line.", "Di grup <b>Teks</b> pada panel <b>Properties</b>, ketik teks Anda. Tekan [[Ctrl+Enter]] atau klik di tempat lain untuk menerapkannya; Enter untuk baris baru."),
            ("Pick the font, size, weight, italic, colour, alignment, letter spacing and line height. Every change rebuilds the letters at once.", "Pilih font, ukuran, ketebalan, miring, warna, rata, jarak huruf, dan jarak baris. Setiap perubahan langsung membangun ulang hurufnya."),
            ("Choose <b>Layer per</b>: <i>Letter</i> (default), <i>Word</i> or <i>Line</i>. This decides what each child layer is.", "Pilih <b>Layer per</b>: <i>Huruf</i> (default), <i>Kata</i>, atau <i>Baris</i>. Ini menentukan isi setiap layer anak."),
        ),
        P(
            "In the Layers panel the text is a root layer with one child per letter, named after it: <code>L1 H</code>, <code>L2 e</code>… Words are named <code>W1 hello</code> and lines <code>Line1 …</code>.",
            "Di panel Layers, teks menjadi layer utama dengan satu anak per huruf yang dinamai sesuai hurufnya: <code>L1 H</code>, <code>L2 e</code>, dan seterusnya. Kata dinamai <code>W1 hello</code> dan baris <code>Line1 …</code>.",
        ),
        H3("text-per-letter", "Animating letter by letter", "Menganimasikan huruf demi huruf"),
        STEPS(
            ("Select the <b>text layer</b> (the root, not a letter).", "Pilih <b>layer teks</b> (layer utamanya, bukan satu huruf)."),
            ("In the <b>Presets</b> panel, tick <b>Stagger to child layers</b>, set the step (0.05–0.1 s reads well) and the order.", "Di panel <b>Presets</b>, centang <b>Stagger ke anak layer</b>, atur jeda (0,05–0,1 s enak dilihat) dan urutannya."),
            ("Double-click a preset. It is applied to every letter, each starting a step after the one before.", "Klik dua kali sebuah preset. Preset diterapkan ke setiap huruf, masing-masing mulai satu jeda setelah huruf sebelumnya."),
        ),
        TABLE(
            [B("Preset", "Preset"), B("Effect on text", "Efek pada teks"), B("Tip", "Tips")],
            [
                ["Typewriter", B("Each letter appears at once: typed out", "Setiap huruf muncul seketika: seperti diketik"), B("Step 0.1 s; a monospace font such as Consolas", "Jeda 0,1 s; font monospace seperti Consolas")],
                ["Backspace", B("Each letter vanishes at once", "Setiap huruf hilang seketika"), B("Order <b>Reverse</b>, so the last letter goes first", "Urutan <b>Terbalik</b>, agar huruf terakhir hilang lebih dulu")],
                ["Drop Bounce", B("Falls, bounces twice with squash and stretch", "Jatuh, memantul dua kali dengan squash & stretch"), B("Playful titles; set the drop height", "Judul ceria; atur tinggi jatuh")],
                ["Neon Flicker", B("Stutters on like a neon tube, then stays lit with glow", "Menyala tersendat seperti lampu neon, lalu menyala tetap dengan glow"), B("Dark background; Layer per <i>Line</i> for signs", "Latar gelap; Layer per <i>Baris</i> untuk papan nama")],
                ["Scale Pop, Elastic Pop", B("Pops in with an overshoot", "Muncul membesar dengan sedikit pantulan"), B("Step 0.05 s", "Jeda 0,05 s")],
                ["Blur In, Slide In ↑", B("Calm, corporate reveals", "Kemunculan tenang ala korporat"), B("Layer per <i>Word</i>", "Layer per <i>Kata</i>")],
            ],
        ),
        STRIP("neon", ["0.1 s", "0.6 s", "1.2 s", "2.5 s"], "Neon Flicker on two lines (Segoe Script, Layer per Line, 0.5 s stagger).", "Neon Flicker pada dua baris (Segoe Script, Layer per Baris, stagger 0,5 s)."),
        STRIP("typewriter", ["0.15 s", "0.4 s", "0.65 s", "1.2 s"], "Typewriter with a 0.12 s step.", "Typewriter dengan jeda 0,12 s."),
        H3("text-wave", "Looping waves across letters", "Gelombang berulang di sepanjang huruf"),
        STRIP("wave", ["0 s", "0.25 s", "0.5 s", "0.75 s"], "Float (period 1 s) on each letter with a 0.15 s stagger: a wave that still loops seamlessly.", "Float (periode 1 s) pada setiap huruf dengan stagger 0,15 s: gelombang yang tetap loop mulus."),
        P(
            "With a <b>Loop</b> preset (Float, Swing, Pulse, Glow Pulse…), stagger shifts each letter's <i>phase</i> rather than its start: every letter moves from the first frame, each a step behind the one before, and the clip still ends exactly as it began. This is how to make waving or rippling titles for stock loops.",
            "Pada preset <b>Loop</b> (Float, Swing, Pulse, Glow Pulse, dan lainnya), stagger menggeser <i>fase</i> setiap huruf, bukan awalnya: setiap huruf bergerak sejak frame pertama, masing-masing tertinggal satu jeda dari huruf sebelumnya, dan klip tetap berakhir persis seperti awalnya. Begitulah cara membuat judul yang melambai atau beriak untuk loop stok.",
        ),
        H3("text-edit", "Editing text later", "Mengedit teks belakangan"),
        P(
            "Change the text or its settings any time. Letters that keep their place keep their presets and keyframes, so changing <i>Hey</i> to <i>Hello</i> keeps the animation on H and e and adds new layers for the rest. The text layer itself stays where you put it.",
            "Ubah teks atau pengaturannya kapan saja. Huruf yang posisinya tetap mempertahankan preset dan keyframe-nya, jadi mengganti <i>Hey</i> menjadi <i>Hello</i> mempertahankan animasi pada H dan e, lalu menambah layer baru untuk sisanya. Layer teksnya sendiri tetap di tempat yang Anda atur.",
        ),
        NOTE(
            "The letters are stored as outlines, so a project opens and renders the same on a computer without the font. If the font has no shape for a character, the status bar names it; pick another font.",
            "Huruf disimpan sebagai outline, jadi proyek terbuka dan dirender sama di komputer yang tidak punya font tersebut. Bila font tidak punya bentuk untuk suatu karakter, status bar menyebutkannya; pilih font lain.",
        ),
    ]


def generators(doc, G):
    s = doc.section("generators", G, B("Generator layers: confetti, counters, landscapes and more", "Layer generator: confetti, counter, pemandangan, dan lainnya"), B("Twenty-three kinds of content made from settings instead of artwork, ready to loop.", "Dua puluh tiga jenis konten yang dibuat dari pengaturan, bukan dari artwork, siap untuk loop."))
    s += [
        STRIP("gen1", ["Confetti", "Snow", "Bokeh", "Bubbles"]),
        STRIP("gen2", ["Plexus", "Fireworks", "Twinkle", B("Stacked + text", "Ditumpuk + teks")["en"]]),
        STRIP("gen3", ["Equalizer", "Equalizer · circle", "Gradient", "Waves"]),
        STRIP("gen4", ["Rings", "Rings · stripes", "Equalizer · mirror"]),
        STRIP("gen5", ["Drone Show", "Constellation", "Particle Text", "Word Cloud"]),
        STRIP("gen6", ["Counter · flip", "Counter · odometer", "Circuit", "Halftone"]),
        STRIP("gen7", ["Landscape", "Paper Cut · tunnel", "Paper Cut · hills", "Grid Floor"]),
        STRIP("gen8", ["Ensō", "Chart · bars", "Chart · line", "Chart · donut"]),
        P(
            "A generator draws hundreds of moving pieces from a few settings. Every piece moves on a path worked out for each moment, never simulated step by step, and every motion repeats a whole number of times over the composition. So a generator loops seamlessly (the ones that build up can too, see below), any frame renders on its own, and the same settings always give the same result.",
            "Generator menggambar ratusan elemen bergerak dari beberapa pengaturan. Setiap elemen bergerak di jalur yang dihitung untuk setiap momen, bukan disimulasikan langkah demi langkah, dan setiap gerakan berulang dalam jumlah bulat sepanjang komposisi. Jadi generator loop mulus (yang dibangun bertahap juga bisa, lihat di bawah), setiap frame bisa dirender sendiri, dan pengaturan yang sama selalu memberi hasil yang sama.",
        ),
        H3("generator-add", "Adding a generator", "Menambah generator"),
        STEPS(
            ("Open the <b>Generator</b> category at the top of the <b>Presets</b> panel.", "Buka kategori <b>Generator</b> di bagian atas panel <b>Presets</b>."),
            ("Double-click a generator. It is added as a new layer on top, covering the composition, and selected.", "Klik dua kali sebuah generator. Generator ditambahkan sebagai layer baru paling atas, menutupi komposisi, dan langsung terpilih."),
            ("Adjust it in the <b>Generator</b> group of the <b>Properties</b> panel. <b>Variation</b> is the seed: another number gives another arrangement with the same look. <b>Shuffle</b> picks one at random.", "Atur di grup <b>Generator</b> pada panel <b>Properties</b>. <b>Variasi</b> adalah seed: angka lain memberi susunan lain dengan tampilan yang sama. <b>Acak</b> memilihnya secara acak."),
        ),
        TABLE(
            [B("Generator", "Generator"), B("What it draws", "Yang digambar"), B("Main settings", "Pengaturan utama")],
            [
                ["Confetti", B("Paper pieces falling, tumbling and swaying", "Kertas berjatuhan, berputar, dan berayun"), B("Count, size, fall speed, sway, shapes, 4 colours", "Jumlah, ukuran, kecepatan jatuh, ayunan, bentuk, 4 warna")],
                ["Snow", B("Soft flakes in depth: near ones bigger and faster", "Salju lembut berkedalaman: yang dekat lebih besar dan cepat"), B("Count, size, speed, drift, colour, opacity", "Jumlah, ukuran, kecepatan, hanyut, warna, opasitas")],
                ["Bokeh", B("Soft circles of light drifting and pulsing", "Lingkaran cahaya lembut yang melayang dan berdenyut"), B("Count, size, drift, softness, opacity, 3 colours", "Jumlah, ukuran, gerak, kelembutan, opasitas, 3 warna")],
                ["Bubbles", B("Rising bubbles with a rim and a highlight", "Gelembung naik dengan tepi dan kilau"), B("Count, size, rise speed, wobble, colour", "Jumlah, ukuran, kecepatan naik, goyang, warna")],
                ["Plexus", B("Moving dots linked by lines when close (tech, data)", "Titik bergerak yang tersambung garis saat berdekatan (teknologi, data)"), B("Count, link distance, drift, dot and line size and colour", "Jumlah, jarak sambung, gerak, ukuran dan warna titik serta garis")],
                ["Fireworks", B("Bursts with trails, gravity and twinkle", "Ledakan dengan ekor, gravitasi, dan kerlip"), B("Bursts per loop, sparks, size, gravity, 4 colours", "Ledakan per loop, percikan, ukuran, gravitasi, 4 warna")],
                ["Twinkle", B("Stars and sparkles twinkling in place", "Bintang dan kilau yang berkelip di tempat"), B("Count, size, twinkle rate, colour", "Jumlah, ukuran, kecepatan kelip, warna")],
                ["Equalizer", B("Audio bars to a beat: from the bottom, mirrored or in a circle", "Bar audio mengikuti ketukan: dari bawah, dicerminkan, atau melingkar"), B("Bars, style, height, beat (bpm), gap, base and tip colour", "Jumlah bar, gaya, tinggi, ketukan (bpm), celah, warna pangkal dan ujung")],
                ["Gradient", B("A soft gradient flowing slowly (mesh-gradient look)", "Gradien lembut yang mengalir pelan (tampilan mesh gradient)"), B("Speed, spread, 4 colours (the first is the base)", "Kecepatan, sebaran, 4 warna (yang pertama jadi dasar)")],
                ["Waves", B("Layered waves rolling by", "Gelombang berlapis yang mengalun"), B("Layers, wave height, waves across, speed, 4 colours (back to front)", "Lapisan, tinggi gelombang, jumlah gelombang, kecepatan, 4 warna (belakang ke depan)")],
                ["Rings", B("Colour bands in rings or diagonal stripes, always moving outward", "Pita warna melingkar atau garis diagonal yang terus bergerak keluar"), B("Shape, band width, speed, 4 colours", "Bentuk, lebar pita, kecepatan, 4 warna")],
                ["Drone Show", B("Hundreds of lights flying into a text, then a heart, star or circle, then scattering", "Ratusan titik cahaya terbang membentuk teks, lalu hati, bintang, atau lingkaran, lalu bubar"), B("Text, font, second shape, count, size, 3 colours", "Teks, font, bentuk kedua, jumlah, ukuran, 3 warna")],
                ["Constellation", B("Stars appearing along the letters' outlines, joined by lines", "Bintang muncul di sepanjang tepi huruf, tersambung garis"), B("Text, font, star spacing and size, line width, background stars, 2 colours", "Teks, font, jarak dan ukuran bintang, tebal garis, bintang latar, 2 warna")],
                ["Particle Text", B("Particles flying in to form a text, then scattering", "Partikel melesat membentuk teks, lalu tersebar"), B("Text, font, count, size, spread, 3 colours", "Teks, font, jumlah, ukuran, sebaran, 3 warna")],
                ["Word Cloud", B("Words popping in and packing together, the first one biggest", "Kata-kata muncul dan tersusun rapat, kata pertama paling besar"), B("Words (one per line), font, biggest size, some vertical, 4 colours", "Kata (satu per baris), font, ukuran terbesar, sebagian tegak, 4 warna")],
                ["Counter", B("A number counting up or down: flip clock, odometer, slot machine or plain", "Angka yang menghitung naik atau turun: flip clock, odometer, slot, atau angka biasa"), B("Style, from, to, minimum digits, start, end, clip ending, size, font, digit and card colour", "Gaya, dari, ke, digit minimum, mulai, selesai, akhir klip, ukuran, font, warna angka dan kartu")],
                ["Circuit", B("A circuit board with chips, 45° traces and pulses of light", "Papan sirkuit dengan chip, jalur 45°, dan pulsa cahaya"), B("Extra traces, chips, grid step, share of pulses, pulse speed, 4 colours (board, traces, pulses, chips)", "Jalur tambahan, chip, jarak kisi, porsi pulsa, kecepatan pulsa, 4 warna (papan, jalur, pulsa, chip)")],
                ["Halftone", B("Pop-art dots growing and shrinking in waves", "Titik pop art yang membesar dan mengecil seperti gelombang"), B("Pattern (waves, ripples, diagonal), dot spacing, grid angle, waves, speed, 2 colours", "Pola (gelombang, riak, diagonal), jarak titik, sudut kisi, jumlah gelombang, kecepatan, 2 warna")],
                ["Landscape", B("Hills, mountains and pines scrolling sideways with parallax", "Bukit, gunung, dan pohon cemara yang bergeser ke samping dengan parallax"), B("Hill layers, speed, trees, sun, 4 colours (sky top, horizon, far, near)", "Lapisan bukit, kecepatan, pohon, matahari, 4 warna (langit atas, cakrawala, jauh, dekat)")],
                ["Paper Cut", B("Cut paper with soft shadows: an endless tunnel or layered hills", "Kertas berpotongan dengan bayangan lembut: terowongan tanpa akhir atau bukit berlapis"), B("Style, hole shape, layers, speed, shadow, 4 colours (the first is the deepest)", "Gaya, bentuk lubang, lapisan, kecepatan, bayangan, 4 warna (yang pertama paling dalam)")],
                ["Grid Floor", B("A synthwave grid rushing towards you under a striped sun", "Kisi synthwave yang melaju ke arah Anda di bawah matahari bergaris"), B("Speed, line width, horizon height, sun, 4 colours (sky, horizon, grid, sun)", "Kecepatan, tebal garis, tinggi cakrawala, matahari, 4 warna (langit, cakrawala, kisi, matahari)")],
                ["Ensō", B("A Zen circle of dry brush painted in one stroke", "Lingkaran Zen dari sapuan kuas kering dalam satu tarikan"), B("Size, brush width, start, end, clip ending, ink colour", "Ukuran, lebar kuas, mulai, selesai, akhir klip, warna tinta")],
                ["Chart", B("Bars, a line or a donut growing in, with counting numbers", "Batang, garis, atau donat yang tumbuh, dengan angka yang ikut menghitung"), B("Type, values (comma separated), numbers, font, start, end, clip ending, 4 colours", "Jenis, nilai (dipisah koma), angka, font, mulai, selesai, akhir klip, 4 warna")],
            ],
        ),
        H3("generator-words", "Text, counters and charts", "Teks, counter, dan grafik"),
        P(
            "Drone Show, Constellation, Particle Text, Word Cloud, Counter and Chart draw letters or digits with an installed font, picked in their <b>Font</b> setting. Type the text in the <b>Text</b> box and press [[Enter]]; Word Cloud takes one word per line, applied with [[Ctrl+Enter]].",
            "Drone Show, Constellation, Particle Text, Word Cloud, Counter, dan Chart menggambar huruf atau angka dengan font yang terpasang, dipilih di pengaturan <b>Font</b>. Ketik teksnya di kotak <b>Teks</b> lalu tekan [[Enter]]; Word Cloud menerima satu kata per baris, diterapkan dengan [[Ctrl+Enter]].",
        ),
        P(
            "Counter, Ensō and Chart <b>build up</b>: they run between <b>Start</b> and <b>End</b> (percent of the composition) and then hold. For a seamless stock loop, set <b>Clip ending</b> to <i>Go back to the start</i>: the last part of the clip returns them to how they began. The Counter's flip clock turns each card when its digit changes, the odometer rolls a higher drum while the ones below it pass 9 to 0, and the slot machine spins each reel and lands it on the final digit, left to right.",
            "Counter, Ensō, dan Chart <b>dibangun bertahap</b>: berjalan antara <b>Mulai</b> dan <b>Selesai</b> (persen komposisi), lalu berhenti. Untuk loop stok yang mulus, atur <b>Akhir klip</b> ke <i>Kembali ke awal</i>: bagian akhir klip mengembalikannya ke keadaan semula. Flip clock pada Counter membalik setiap kartu saat digitnya berubah, odometer memutar drum yang lebih tinggi saat digit di bawahnya bergulir dari 9 ke 0, dan slot memutar setiap gulungan lalu menghentikannya di digit akhir, dari kiri ke kanan.",
        ),
        H3("generator-tips", "Working with generators", "Bekerja dengan generator"),
        UL(
            ("<b>A generator is a normal layer.</b> Move and scale it, fade it in with a preset, add glow, put artwork or text above it, or stack several (bokeh behind, confetti in front).", "<b>Generator adalah layer biasa.</b> Geser dan skalakan, munculkan dengan preset, beri glow, taruh artwork atau teks di atasnya, atau tumpuk beberapa (bokeh di belakang, confetti di depan)."),
            ("<b>Sizes in pixels mean pixels at 1080p</b> and scale with the composition, so the same settings look the same in 4K.", "<b>Ukuran dalam piksel berarti piksel pada 1080p</b> dan ikut berskala dengan komposisi, jadi pengaturan yang sama tampak sama di 4K."),
            ("<b>Loops follow the composition.</b> Change the duration and the motion still ends where it began.", "<b>Loop mengikuti komposisi.</b> Ubah durasinya, gerakan tetap berakhir di titik awalnya."),
            ("<b>Video only.</b> Lottie and animated SVG exports leave generator layers empty and say so in their report.", "<b>Hanya untuk video.</b> Ekspor Lottie dan SVG animasi membiarkan layer generator kosong dan menyebutkannya di laporan."),
        ),
        TIP(
            "Fireworks, Plexus, Twinkle, Drone Show, Constellation and Circuit look their best with a little <b>Glow</b> on a dark background.",
            "Fireworks, Plexus, Twinkle, Drone Show, Constellation, dan Circuit paling bagus dengan sedikit <b>Glow</b> di latar gelap.",
        ),
    ]


def depth_presets(doc, G):
    s = doc.section("presets-2-5d", G, B("2.5D presets, brush reveals and render effects", "Preset 2.5D, reveal sapuan kuas, dan efek render"), B("Coins, cards and paper that turn and peel, long shadows, waving flags and sparklers, on any artwork.", "Koin, kartu, dan kertas yang berputar dan terkelupas, bayangan panjang, bendera berkibar, dan kembang api lidi, pada artwork apa pun."))
    s += [
        P(
            "These presets do more than move a layer: the renderer gives it thickness, a back side, a shine or a paper fold. They work on any shape, not only circles and rectangles, and render in video only.",
            "Preset ini melakukan lebih dari sekadar menggerakkan layer: renderer memberinya ketebalan, sisi belakang, kilau, atau lipatan kertas. Semuanya bekerja pada bentuk apa pun, tidak hanya lingkaran dan persegi, dan hanya dirender di video.",
        ),
        STRIP("coin", ["0 s", "0.25 s", "0.4 s", "0.6 s"], "Coin Spin: thickness in the edge colour and a shine that sweeps the face; a whole number of turns, so it loops.", "Coin Spin: ketebalan berwarna sisi dan kilau yang menyapu permukaan; jumlah putarannya bulat, jadi loop mulus."),
        STRIP("cardflip", ["0.3 s", "0.5 s", "0.65 s", "0.9 s"], "Card Flip: turns over, showing a coloured back.", "Card Flip: berbalik dan memperlihatkan sisi belakang berwarna."),
        STRIP("peel", ["0.9 s", "1.3 s", "1.7 s", "2.2 s"], "Peel Off on green screen: the paper's back shows, the shadow falls only on the paper, and the screen ends fully green.", "Peel Off di green screen: sisi belakang kertas terlihat, bayangan hanya jatuh di atas kertas, dan layar berakhir hijau penuh."),
        TABLE(
            [B("Preset", "Preset"), B("Category", "Kategori"), B("Settings", "Pengaturan")],
            [
                ["Coin Spin", "Loop", B("Period, direction, axis (vertical coin or horizontal board), thickness, edge colour, back side (same, mirrored, plain colour), shine", "Periode, arah, sumbu (koin tegak atau papan datar), ketebalan, warna sisi, sisi belakang (sama, dicerminkan, warna polos), kilau")],
                ["Card Flip In", "Enter", B("Turns from its back to its front; same settings as Coin Spin", "Berbalik dari belakang ke depan; pengaturan sama dengan Coin Spin")],
                ["Card Flip", "Emphasis", B("One full turn, showing the back on the way", "Satu putaran penuh, memperlihatkan sisi belakang di tengah jalan")],
                ["Peel On / Peel Off", "Enter / Exit", B("Starts at a corner or an edge, paper back colour, shadow; the flap leaves the screen", "Mulai dari sudut atau tepi, warna belakang kertas, bayangan; lipatan keluar layar")],
                ["Peel Corner", "Emphasis", B("A corner lifts by an amount and settles back", "Sudut terangkat sejauh nilai tertentu lalu kembali rata")],
                ["Brush In / Brush Out", "Enter / Exit", B("Painted in (or wiped away) by a brush going back and forth", "Dilukis masuk (atau dihapus) oleh kuas yang menyapu bolak-balik")],
                ["Long Shadow / Long Shadow Grow", "Loop / Enter", B("A flat shadow swept away from the light: direction, length, colour, opacity, fade at the end", "Bayangan datar yang memanjang menjauhi cahaya: arah, panjang, warna, opasitas, memudar di ujung")],
                ["Flag Wave", "Loop", B("Waves like cloth with light and shade in the folds: wave height, waves across, period, left edge held, light and shade", "Berkibar seperti kain dengan terang-gelap di lipatan: tinggi gelombang, jumlah gelombang, periode, tepi kiri dipegang, terang-gelap")],
                ["Sparkler Draw", "Enter", B("Strokes draw on while sparks fly from the tip: sparks per second, size, launch speed, colour, ease", "Garis tergambar sementara percikan berhamburan dari ujungnya: percikan per detik, ukuran, kecepatan lontar, warna, ease")],
            ],
        ),
        STRIP("longshadow", ["0.1 s", "0.3 s", "0.6 s", "1.2 s"], "Long Shadow Grow on a badge: the shadow keeps the badge's outline, at 45°.", "Long Shadow Grow pada badge: bayangannya mengikuti bentuk badge, pada sudut 45°."),
        STRIP("flag", ["0 s", "0.4 s", "0.8 s", "1.2 s"], "Flag Wave: held at the pole, with light and shade in the folds; a seamless loop.", "Flag Wave: dipegang di tiang, dengan terang-gelap di lipatan; loop mulus."),
        STRIP("sparkler", ["0.3 s", "0.9 s", "1.6 s", "2.4 s"], "Sparkler Draw on a stroked path: sparks fly and fall from the drawing tip and burn out after it.", "Sparkler Draw pada path ber-stroke: percikan terlontar dan jatuh dari ujung yang sedang menggambar, lalu padam setelahnya."),
        STRIP("brush", ["0.3 s", "0.7 s", "1.1 s", "1.7 s"], "Brush In: four back-and-forth strokes paint the layer in. The same reveal is in Properties ▸ Reveal from ▸ Brush strokes.", "Brush In: empat sapuan bolak-balik melukis layer. Reveal yang sama ada di Properties ▸ Reveal dari ▸ Sapuan kuas."),
        TIP(
            "For a page-curl transition, put all the artwork in one group covering the frame and apply <b>Peel Off</b> to it over a <code>#00B140</code> background, then run <b>Stock check</b> in the Render Queue.",
            "Untuk transisi page curl, taruh semua artwork dalam satu grup yang menutupi frame, terapkan <b>Peel Off</b> di atas latar <code>#00B140</code>, lalu jalankan <b>Cek stok</b> di Render Queue.",
        ),
        NOTE(
            "A layer that spins does not also peel (the spin wins), and a layer that spins or peels does not wave or cast a long shadow. Bake to keyframes keeps these presets as presets, since they have no keyframe form, and Lottie and animated SVG leave them out.",
            "Layer yang berputar tidak sekaligus terkelupas (putaran yang dipakai), dan layer yang berputar atau terkelupas tidak berkibar atau berbayangan panjang. Bake ke keyframe mempertahankan preset ini sebagai preset, karena tidak punya bentuk keyframe, dan Lottie serta SVG animasi tidak menyertakannya.",
        ),
        TIP(
            "Put a long shadow on the outermost group of an icon, not on its parts as well: shadows of shadows take much longer to render.",
            "Pasang long shadow di grup terluar ikon, jangan juga di bagian-bagiannya: bayangan dari bayangan jauh lebih lama dirender.",
        ),
    ]


def glow(doc, G):
    s = doc.section("glow", G, B("Glow", "Glow"), B("Light around a layer, in its own colours.", "Cahaya di sekitar layer, dalam warnanya sendiri."))
    s += [
        STRIP("glow", ["0 %", "100 %", B("100 %, radius 60", "100 %, radius 60")["en"], "250 %"]),
        P(
            "<b>Glow</b> in the Effects group of the Properties panel adds the layer's own light around it. It has a stopwatch like Blur, so it can be keyframed; <b>Glow radius</b> sets how far the light spreads, in composition pixels. The presets <b>Glow Pulse</b> (a seamless loop) and <b>Glow Flash</b> (once) animate it for you, and <b>Neon Flicker</b> uses it for text.",
            "<b>Glow</b> di grup Efek pada panel Properties menambahkan cahaya layer itu sendiri di sekitarnya. Glow punya stopwatch seperti Blur, jadi bisa di-keyframe; <b>Radius glow</b> mengatur seberapa jauh cahayanya menyebar, dalam piksel komposisi. Preset <b>Glow Pulse</b> (loop mulus) dan <b>Glow Flash</b> (sekali) menganimasikannya untuk Anda, dan <b>Neon Flicker</b> memakainya untuk teks.",
        ),
        UL(
            ("<b>Thin lines still light up</b>, and strong light turns softly towards white, like a real glow.", "<b>Garis tipis tetap menyala</b>, dan cahaya kuat berangsur memutih dengan lembut, seperti glow sungguhan."),
            ("<b>It sits in the layer's place.</b> Layers above it cover its light, as they cover the layer.", "<b>Glow berada di posisi layernya.</b> Layer di atasnya menutupi cahayanya, sama seperti menutupi layernya."),
            ("<b>Glow only brightens</b>, so it shows on dark backgrounds and not on white.", "<b>Glow hanya menerangkan</b>, jadi terlihat di latar gelap dan tidak di latar putih."),
            ("<b>Video only.</b> Lottie and animated SVG exports leave it out and say so.", "<b>Hanya untuk video.</b> Ekspor Lottie dan SVG animasi mengabaikannya dan menyebutkannya."),
        ),
        NOTE(
            "Glow is rendered at a quarter of the output size and blurred there, so even 4K stays quick. Glow on a whole SVG, a generator or a text layer is the fastest; glow on a part inside an SVG takes a little longer.",
            "Glow dirender pada seperempat ukuran output lalu di-blur di sana, jadi 4K pun tetap cepat. Glow pada seluruh SVG, generator, atau layer teks paling cepat; glow pada bagian di dalam SVG sedikit lebih lama.",
        ),
    ]


def stock_tools(doc, G):
    s = doc.section("stock-tools", G, B("Microstock tools: checks, metadata and batches", "Alat microstock: cek, metadata, dan batch"), B("Catch rejections before uploading and write each site's CSV.", "Temukan penyebab penolakan sebelum mengunggah dan tulis CSV setiap situs."))
    s += [
        H3("stock-templates", "Stock templates", "Template stok"),
        P(
            "In the composition's Properties (click empty canvas), <b>Stock template</b> sets size, frame rate, duration and background for a kind of clip:",
            "Di Properties komposisi (klik area kosong canvas), <b>Template stok</b> mengatur ukuran, frame rate, durasi, dan latar untuk satu jenis klip:",
        ),
        TABLE(
            [B("Template", "Template"), B("Setup", "Pengaturan"), B("Rule", "Aturan")],
            [
                [B("Green-screen transition", "Transisi green screen"), B("3840×2160, 30 fps, 5 s, #00B140", "3840×2160, 30 fps, 5 s, #00B140"), B("Green at both ends, fully covered around 2.3–2.7 s (the cut point)", "Hijau di kedua ujung, tertutup penuh sekitar 2,3–2,7 s (titik potong)")],
                ["Luma matte", B("3840×2160, 30 fps, 5 s, black", "3840×2160, 30 fps, 5 s, hitam"), B("First frame pure black, last pure white", "Frame pertama hitam murni, terakhir putih murni")],
                [B("Stock loop", "Loop stok"), B("3840×2160, 30 fps, 10 s", "3840×2160, 30 fps, 10 s"), B("Ends exactly as it starts (Check loop)", "Berakhir persis seperti awalnya (Cek loop)")],
            ],
        ),
        H3("stock-check", "Stock check", "Cek stok"),
        P(
            "<b>Stock check</b> in the Render Queue renders a few frames and tests what reviewers reject. It knows the clip kind from the background (chroma green means a transition) and lists each problem in one line:",
            "<b>Cek stok</b> di Render Queue merender beberapa frame dan menguji hal yang ditolak reviewer. Jenis klip dikenali dari latarnya (hijau kroma berarti transisi), dan setiap masalah ditampilkan dalam satu baris:",
        ),
        UL(
            ("<b>Every clip:</b> standard frame rate and 5–60 s (errors), 3840×2160 (a warning below 4K).", "<b>Setiap klip:</b> frame rate standar dan 5–60 s (error), 3840×2160 (peringatan bila di bawah 4K)."),
            ("<b>Green-screen transition:</b> first frame 100 % chroma, last frame at least 99.9 %, no chroma at all at the cut point, no green or teal artwork (it would be keyed out), and no half-transparent edges over the green such as glow, blur or shadows (they leave a green fringe).", "<b>Transisi green screen:</b> frame pertama 100% kroma, frame terakhir minimal 99,9%, sama sekali tanpa kroma di titik potong, tanpa artwork hijau atau toska (akan ikut terhapus saat keying), dan tanpa tepi setengah transparan di atas hijau seperti glow, blur, atau bayangan (meninggalkan pinggiran hijau)."),
            ("<b>Luma matte:</b> first frame pure black, last frame pure white.", "<b>Luma matte:</b> frame pertama hitam murni, frame terakhir putih murni."),
        ),
        H3("stock-metadata", "Stock metadata and CSVs", "Metadata stok dan CSV"),
        P(
            "Fill in <b>Stock metadata</b> in the composition's Properties once per project: title, description (at least 5 words), keywords (most important first), one or two Shutterstock categories and the Adobe Stock category. After rendering, <b>Metadata CSV</b> in the Render Queue writes four files into a <code>metadata</code> folder next to the finished videos, one row per video:",
            "Isi <b>Metadata stok</b> di Properties komposisi sekali per proyek: judul, deskripsi (minimal 5 kata), keyword (yang terpenting dulu), satu atau dua kategori Shutterstock, dan kategori Adobe Stock. Setelah render, <b>Metadata CSV</b> di Render Queue menulis empat file ke folder <code>metadata</code> di sebelah video yang sudah jadi, satu baris per video:",
        ),
        TABLE(
            [B("File", "File"), B("Adapted to the site", "Disesuaikan dengan situs")],
            [
                ["shutterstock_metadata.csv", B("Video category names (art, health care), at most 50 keywords", "Nama kategori video (art, health care), maksimal 50 keyword")],
                ["adobestock_metadata.csv", B("Title up to 200 characters, at most 49 keywords, category number", "Judul maksimal 200 karakter, maksimal 49 keyword, nomor kategori")],
                ["vecteezy_metadata.csv", B("No underscores in file names, letters and digits only, words such as <i>vector</i>, <i>video</i>, <i>AI</i> removed, licence Pro", "Tanpa garis bawah di nama file, hanya huruf dan angka, kata seperti <i>vector</i>, <i>video</i>, <i>AI</i> dibuang, lisensi Pro")],
                ["pond5_metadata.csv", B("Title up to 80 characters, clean description, price 39 (4K) and 25 (HD)", "Judul maksimal 80 karakter, deskripsi bersih, harga 39 (4K) dan 25 (HD)")],
            ],
        ),
        P(
            "Loops get the keywords <i>seamless loop</i> and <i>looping animation</i> automatically. Anything a site would refuse is shown in the status bar.",
            "Klip loop otomatis mendapat keyword <i>seamless loop</i> dan <i>looping animation</i>. Apa pun yang akan ditolak suatu situs ditampilkan di status bar.",
        ),
        H3("batch", "Batch variations", "Batch variasi"),
        STRIP("batch", ["sale_navy_4k", "sale_gold_4k", "promo_green_4k"], "One project, three variations: another seed, swapped colours, a new background and new text.", "Satu proyek, tiga variasi: seed lain, warna ditukar, latar baru, dan teks baru."),
        STEPS(
            ("Build one clip as a template. Generators, text layers and colours are what variations can change.", "Buat satu klip sebagai template. Generator, layer teks, dan warna adalah hal yang bisa diubah oleh variasi."),
            ("In the Render Queue, click <b>Batch variations…</b>. Each row is one video: file name, seed, replacements for the project's six main colours, background, new text for the first text layer and its own stock title.", "Di Render Queue, klik <b>Batch variasi…</b>. Setiap baris adalah satu video: nama file, seed, pengganti untuk enam warna utama proyek, latar, teks baru untuk layer teks pertama, dan judul stoknya sendiri."),
            ("Add rows, choose the output folder and click <b>Add to the queue</b>. Every row becomes a 4K H.264 item that renders its own variation.", "Tambah baris, pilih folder output, lalu klik <b>Tambah ke antrean</b>. Setiap baris menjadi item 4K H.264 yang merender variasinya sendiri."),
            ("Press <b>Render</b>, then <b>Metadata CSV</b>: each row keeps its own title.", "Tekan <b>Render</b>, lalu <b>Metadata CSV</b>: setiap baris mempertahankan judulnya sendiri."),
        ),
        WARN(
            "Variations change the look, not the motion. Stock sites reject batches of near-identical clips (\"similar content\"), so mix variations with clips that move differently or have their own style.",
            "Variasi mengubah tampilan, bukan gerakan. Situs stok menolak kumpulan klip yang nyaris sama (\"similar content\"), jadi campur variasi dengan klip yang gerakannya berbeda atau punya gaya sendiri.",
        ),
    ]


def ai(doc, G):
    s = doc.section("ai", G, B("AI agents: Ask AI and the MCP server", "Agent AI: Ask AI dan server MCP"), B("Let Claude build and change animations, with your own subscription.", "Biarkan Claude membuat dan mengubah animasi, dengan langganan Anda sendiri."))
    s += [
        P(
            "Motionator includes <code>motionator-mcp</code>, a server that gives AI agents its tools: create projects, import or write SVG, add text and generators, apply presets and keyframes, look at frames, check loops and stock rules, render, and write metadata. The intelligence comes from the agent you already use, such as Claude Code or opencode, logged in with your own account. Motionator stores no API keys.",
            "Motionator menyertakan <code>motionator-mcp</code>, server yang memberi alat-alatnya kepada agent AI: membuat proyek, mengimpor atau menulis SVG, menambah teks dan generator, menerapkan preset dan keyframe, melihat frame, mengecek loop dan aturan stok, merender, dan menulis metadata. Kecerdasannya datang dari agent yang sudah Anda pakai, seperti Claude Code atau opencode, yang login dengan akun Anda sendiri. Motionator tidak menyimpan API key.",
        ),
        H3("ask-ai", "Ask AI inside the app", "Ask AI di dalam aplikasi"),
        STEPS(
            ("Install <b>Claude Code</b> from claude.com/claude-code and run <code>claude</code> once in a terminal to log in.", "Pasang <b>Claude Code</b> dari claude.com/claude-code dan jalankan <code>claude</code> sekali di terminal untuk login."),
            ("Open <b>Window ▸ Ask AI</b>.", "Buka <b>Window ▸ Ask AI</b>."),
            ("Describe what you want, e.g. <i>Add confetti behind and a SALE text that drops and bounces</i>, and press <b>Send</b> ([[Ctrl+Enter]]).", "Tulis yang Anda inginkan, misalnya <i>Tambahkan confetti di belakang dan teks SALE yang jatuh memantul</i>, lalu tekan <b>Kirim</b> ([[Ctrl+Enter]])."),
            ("Watch it work: each change appears in the open project at once, and the panel lists the tools it uses. Every change is one step in <b>Edit ▸ Undo</b>.", "Lihat agent bekerja: setiap perubahan langsung muncul di proyek yang terbuka, dan panel menampilkan alat yang dipakainya. Setiap perubahan adalah satu langkah di <b>Edit ▸ Undo</b>."),
        ),
        NOTE(
            "You can keep editing while it works; it picks up your changes before each step. <b>Cancel</b> stops it. It does not save, render or export unless you ask.",
            "Anda tetap bisa mengedit selama agent bekerja; agent mengambil perubahan Anda sebelum setiap langkah. <b>Batalkan</b> menghentikannya. Agent tidak menyimpan, merender, atau mengekspor kecuali Anda minta.",
        ),
        H3("mcp-setup", "Using Motionator from Claude Code or opencode", "Memakai Motionator dari Claude Code atau opencode"),
        STEPS(
            ("Open <b>Help ▸ Connect AI (Claude Code, opencode)…</b>. Each agent shows whether it is installed and connected.", "Buka <b>Help ▸ Hubungkan AI (Claude Code, opencode)…</b>. Setiap agent menunjukkan apakah sudah terpasang dan terhubung."),
            ("Click <b>Connect</b> next to the agent. Motionator registers its server for you: with Claude Code's own <code>claude mcp add</code>, and in opencode's global settings (a copy of the original file is kept as <code>opencode.jsonc.motionator-backup</code>).", "Klik <b>Hubungkan</b> di sebelah agent. Motionator mendaftarkan servernya untuk Anda: lewat <code>claude mcp add</code> milik Claude Code, dan di pengaturan global opencode (salinan file aslinya disimpan sebagai <code>opencode.jsonc.motionator-backup</code>)."),
            ("Click <b>Open terminal</b> to start the agent in a new window, in your Documents folder, and ask away. <b>Disconnect</b> removes the registration again.", "Klik <b>Buka terminal</b> untuk menjalankan agent di jendela baru, di folder Documents, lalu langsung minta. <b>Lepas</b> menghapus pendaftarannya lagi."),
        ),
        P(
            "To register by hand instead: the installer puts the server next to Motionator, normally in <code>%LOCALAPPDATA%\\Motionator</code>.",
            "Untuk mendaftarkan secara manual: installer menaruh servernya di sebelah Motionator, biasanya di <code>%LOCALAPPDATA%\\Motionator</code>.",
        ),
        CODE('claude mcp add motionator -- "%LOCALAPPDATA%\\Motionator\\motionator-mcp.exe"'),
        P("For opencode, add it to <code>opencode.json</code>:", "Untuk opencode, tambahkan ke <code>opencode.json</code>:"),
        CODE('{\n  "mcp": {\n    "motionator": { "type": "local", "command": ["C:\\\\Users\\\\you\\\\AppData\\\\Local\\\\Motionator\\\\motionator-mcp.exe"], "enabled": true }\n  }\n}'),
        P(
            "Then ask in plain words, e.g. <i>Make 5 seamless 4K stock loops about Ramadan with Motionator, save them in D:\\stock and write the CSVs</i>. The agent reads Motionator's guide and preset list, looks at preview frames to check its work, and queues renders in the background. To work on the project open in the app, ask it to <i>work on my open Motionator project</i>: it connects in live mode, like Ask AI.",
            "Lalu minta dengan kalimat biasa, misalnya <i>Buat 5 loop stok 4K bertema Ramadan dengan Motionator, simpan di D:\\stock, dan tulis CSV-nya</i>. Agent membaca panduan dan daftar preset Motionator, melihat frame preview untuk mengecek hasilnya, dan mengantrekan render di latar belakang. Untuk mengerjakan proyek yang terbuka di aplikasi, minta agent <i>mengerjakan proyek Motionator saya yang sedang terbuka</i>: agent tersambung dalam mode live, seperti Ask AI.",
        ),
        TABLE(
            [B("Tools", "Alat"), B("What the agent can do", "Yang bisa dilakukan agent")],
            [
                [B("Project", "Proyek"), B("New (with stock templates), open, save, info, canvas, undo, redo, live connect", "Baru (dengan template stok), buka, simpan, info, canvas, undo, redo, live connect")],
                [B("Content", "Konten"), B("Import or write SVG, text layers and fonts, generators, layer properties and geometry", "Impor atau tulis SVG, layer teks dan font, generator, properti dan geometri layer")],
                [B("Animation", "Animasi"), B("Preset catalogue, apply/update/remove presets with stagger, keyframes", "Katalog preset, terapkan/ubah/hapus preset dengan stagger, keyframe")],
                [B("Checking", "Pengecekan"), B("Preview frames and contact sheets (it sees the result), loop check, stock check", "Frame preview dan contact sheet (agent melihat hasilnya), cek loop, cek stok")],
                [B("Output", "Output"), B("Render queue, batch variations, Lottie, animated SVG, stock metadata and CSVs", "Antrean render, batch variasi, Lottie, SVG animasi, metadata stok dan CSV")],
            ],
        ),
        NOTE(
            "The server never runs commands and only writes Motionator's kinds of file (projects, videos, Lottie, SVG, CSV). Set <code>MOTIONATOR_MCP_ROOTS</code> to a list of folders separated by <code>;</code> to keep it inside them.",
            "Server tidak pernah menjalankan perintah dan hanya menulis jenis file Motionator (proyek, video, Lottie, SVG, CSV). Isi <code>MOTIONATOR_MCP_ROOTS</code> dengan daftar folder yang dipisah <code>;</code> untuk membatasinya di folder-folder itu.",
        ),
    ]
