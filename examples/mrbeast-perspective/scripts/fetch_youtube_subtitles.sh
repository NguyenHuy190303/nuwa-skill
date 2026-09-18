#!/bin/bash
#
# fetch_youtube_subtitles.sh - download YouTube video subtitles
#
# Uses yt-dlp to download subtitle files for a YouTube video or channel (manual subtitles first, falling back to auto-generated ones)
#
# Usage:
#   ./fetch_youtube_subtitles.sh <URL> [language code] [output dir]
#
# Arguments:
#   URL             - YouTube video URL or channel URL (required)
#   language code   - subtitle language, default en (optional)
#   output dir      - where to save subtitles, default current directory (optional)
#
# Examples:
#   ./fetch_youtube_subtitles.sh "https://youtube.com/watch?v=xxx"
#   ./fetch_youtube_subtitles.sh "https://youtube.com/watch?v=xxx" zh-Hans ./subs
#   ./fetch_youtube_subtitles.sh "https://youtube.com/@MrBeast" en ./mrbeast_subs
#

set -euo pipefail

# ---------- parse arguments ----------
URL="${1:-}"
LANG="${2:-en}"
OUTDIR="${3:-.}"

if [ -z "$URL" ]; then
    echo "Usage: $0 <YouTube URL> [language code] [output dir]"
    echo ""
    echo "Examples:"
    echo "  $0 'https://youtube.com/watch?v=xxx'"
    echo "  $0 'https://youtube.com/watch?v=xxx' zh-Hans ./subs"
    echo "  $0 'https://youtube.com/@MrBeast' en ./mrbeast_subs"
    exit 1
fi

# ---------- check/install yt-dlp ----------
if ! command -v yt-dlp &> /dev/null; then
    echo "[INFO] yt-dlp not installed, installing via pip..."
    pip install -q yt-dlp
    if ! command -v yt-dlp &> /dev/null; then
        echo "[ERROR] yt-dlp installation failed, please install manually: pip install yt-dlp or brew install yt-dlp"
        exit 1
    fi
    echo "[INFO] yt-dlp installed"
fi

# ---------- create output directory ----------
mkdir -p "$OUTDIR"

echo "========================================="
echo "  YouTube Subtitle Downloader"
echo "========================================="
echo "URL:      $URL"
echo "Language: $LANG"
echo "Output:   $OUTDIR"
echo ""

# ---------- first list available subtitles ----------
echo "[INFO] Querying available subtitles..."
yt-dlp --list-subs --skip-download "$URL" 2>/dev/null | head -50 || true
echo ""

# ---------- download subtitles ----------
# Strategy: try manual subtitles first, fall back to auto-generated ones on failure
echo "[INFO] Trying to download manual subtitles (${LANG})..."
if yt-dlp \
    --write-sub \
    --sub-lang "$LANG" \
    --sub-format "srt/vtt/best" \
    --skip-download \
    --no-overwrites \
    -o "${OUTDIR}/%(title)s.%(ext)s" \
    "$URL" 2>/dev/null; then
    echo "[OK] Manual subtitles downloaded successfully"
else
    echo "[INFO] No manual subtitles, trying to download auto-generated subtitles..."
    if yt-dlp \
        --write-auto-sub \
        --sub-lang "$LANG" \
        --sub-format "srt/vtt/best" \
        --skip-download \
        --no-overwrites \
        -o "${OUTDIR}/%(title)s.%(ext)s" \
        "$URL" 2>/dev/null; then
        echo "[OK] Auto-generated subtitles downloaded successfully"
    else
        echo "[ERROR] No ${LANG} subtitles found"
        echo "[Hint] Try a different language code, or use --list-subs to see available subtitles"
        exit 1
    fi
fi

echo ""
echo "[INFO] Downloaded subtitle files:"
find "$OUTDIR" -maxdepth 1 \( -name "*.srt" -o -name "*.vtt" \) -newer "$0" 2>/dev/null | head -20 || \
    ls -la "$OUTDIR"/*.{srt,vtt} 2>/dev/null || echo "  (no new files)"

echo ""
echo "Done!"
