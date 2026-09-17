#!/usr/bin/env python3
"""
Clean an SRT/VTT subtitle file into a plain-text transcript.
Strips timestamps, sequence numbers, duplicate lines and HTML tags, and
outputs readable text.

Usage:
    python3 srt_to_transcript.py input.srt [output.txt]
    python3 srt_to_transcript.py input.vtt [output.txt]

With no output file, writes to input_transcript.txt
"""

import sys
import re
from pathlib import Path


def clean_srt(content: str) -> str:
    """Clean SRT-format subtitles."""
    lines = content.strip().split('\n')
    texts = []

    for line in lines:
        line = line.strip()
        # Skip sequence-number lines (digits only)
        if re.match(r'^\d+$', line):
            continue
        # Skip timestamp lines
        if re.match(r'\d{2}:\d{2}:\d{2}', line):
            continue
        # Skip blank lines
        if not line:
            continue
        # Strip HTML tags
        line = re.sub(r'<[^>]+>', '', line)
        # Strip VTT positioning cues
        line = re.sub(r'align:.*$|position:.*$', '', line).strip()
        if line:
            texts.append(line)

    # Deduplicate (auto-generated subtitles repeat lines constantly)
    deduped = []
    for text in texts:
        if not deduped or text != deduped[-1]:
            deduped.append(text)

    # Merge into paragraphs: join short fragments, break on sentence-final
    # punctuation. The CJK punctuation below is intentional — source videos
    # are often Chinese-language.
    result = []
    current = []

    for text in deduped:
        current.append(text)
        joined = ' '.join(current)
        if len(joined) > 200 or re.search(r'[。！？.!?]$', text):
            result.append(joined)
            current = []

    if current:
        result.append(' '.join(current))

    return '\n\n'.join(result)


def clean_vtt(content: str) -> str:
    """Clean VTT-format subtitles (drop the VTT header, then use the SRT path)."""
    # Drop the WEBVTT header
    content = re.sub(r'^WEBVTT.*?\n\n', '', content, flags=re.DOTALL)
    # Drop NOTE blocks
    content = re.sub(r'NOTE.*?\n\n', '', content, flags=re.DOTALL)
    return clean_srt(content)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 srt_to_transcript.py <input.srt|input.vtt> [output.txt]")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(f"❌ File not found: {input_path}")
        sys.exit(1)

    if len(sys.argv) >= 3:
        output_path = Path(sys.argv[2])
    else:
        output_path = input_path.parent / f"{input_path.stem}_transcript.txt"

    content = input_path.read_text(encoding='utf-8')

    if input_path.suffix.lower() == '.vtt' or content.startswith('WEBVTT'):
        transcript = clean_vtt(content)
    else:
        transcript = clean_srt(content)

    output_path.write_text(transcript, encoding='utf-8')

    char_count = len(transcript)
    para_count = transcript.count('\n\n') + 1
    print(f"✅ Converted: {output_path}")
    print(f"   Characters: {char_count}  Paragraphs: {para_count}")


if __name__ == '__main__':
    main()
