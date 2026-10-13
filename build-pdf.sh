#!/bin/sh
# Rebuild the site and both PDFs (Windows, Edge headless).
set -e
cd "$(dirname "$0")"
PYTHONIOENCODING=utf-8 python build.py "${1:-../motionator}"
E="/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
D="$(pwd -W 2>/dev/null || pwd)"
mkdir -p pdf
"$E" --headless=new --disable-gpu --no-pdf-header-footer --virtual-time-budget=15000 --print-to-pdf="$D/pdf/Motionator-User-Guide-EN.pdf" "file:///$D/print-en.html"
"$E" --headless=new --disable-gpu --no-pdf-header-footer --virtual-time-budget=15000 --print-to-pdf="$D/pdf/Motionator-Panduan-ID.pdf" "file:///$D/print-id.html"
