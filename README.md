# Motionator User Guide · Panduan Motionator

The bilingual (English / Bahasa Indonesia) user guide for Motionator, published at
**https://s4rt4.github.io/motionator-docs/**.

- `index.html`: the guide, with topic search, language switch and light/dark theme
- `pdf/`: the guide as PDF, one per language
- `samples/`: the sample files used by the tutorials
- `img/en`, `img/id`: screenshots of the app in each language

## Building

The pages are generated: edit `content.py` / `content2.py`, then run

```sh
sh build-pdf.sh path/to/motionator
```

`build.py` reads the preset list and keyboard shortcuts from the app's source, so those tables stay
in sync. The PDFs are printed from `print-en.html` and `print-id.html` with Microsoft Edge headless.
