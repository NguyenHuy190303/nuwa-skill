#!/usr/bin/env python3
"""
Merge the 6 Agents' research output into the summary table for the Phase 1.5
research review checkpoint.
Scans the 01-06 md files under references/research/ and reports, per dimension,
the number of sources, the primary/secondary mix, and the key findings.

Usage:
    python3 merge_research.py <path to skill dir>

Example:
    python3 merge_research.py .claude/skills/elon-musk-perspective

Output: a markdown-ish summary table printed to stdout
"""

import sys
import re
from pathlib import Path

AGENTS = {
    '01-writings': 'Writings',
    '02-conversations': 'Conversations',
    '03-expression-dna': 'Expression',
    '04-external-views': 'Outside views',
    '05-decisions': 'Decisions',
    '06-timeline': 'Timeline',
}

PRIMARY_RE = re.compile(
    r'\bprimary\b|\bfirst[- ]hand\b|\bown words\b|\boriginal text\b|\bdirect quote\b',
    re.IGNORECASE,
)
SECONDARY_RE = re.compile(
    r'\bsecondary\b|\bsecond[- ]hand\b|\bparaphrase\w*\b|\bsummar(?:y|ized|ised)\b'
    r'|\bcommentary\b|\banalysis\b',
    re.IGNORECASE,
)
CONTRADICTION_RE = re.compile(
    r'(?:contradict\w*|contrary|in fact,|however[^.]{0,40}differ\w*|disput\w*|controvers\w*)'
    r'.{0,100}',
    re.IGNORECASE,
)


def count_sources(content: str) -> dict:
    """Count sources and the primary/secondary mix."""
    urls = re.findall(r'https?://[^\s\)]+', content)

    return {
        'url_count': len(urls),
        'unique_urls': len(set(urls)),
        'primary_markers': len(PRIMARY_RE.findall(content)),
        'secondary_markers': len(SECONDARY_RE.findall(content)),
    }


def extract_key_findings(content: str, max_items: int = 3) -> list[str]:
    """Pull out key findings (the first few H2 headings, or bold items)."""
    headings = re.findall(r'^##\s+(.+)$', content, re.MULTILINE)
    if headings:
        return headings[:max_items]

    bolds = re.findall(r'\*\*(.+?)\*\*', content)
    if bolds:
        return bolds[:max_items]

    lines = [l.strip() for l in content.split('\n') if l.strip() and not l.startswith('#')]
    return [l[:50] + '...' if len(l) > 50 else l for l in lines[:max_items]]


def find_contradictions(files: dict[str, str]) -> list[str]:
    """Rough cross-file contradiction detection (the same topic judged two ways)."""
    contradictions = []
    for name, content in files.items():
        for m in CONTRADICTION_RE.findall(content):
            contradictions.append(f"{AGENTS.get(name, name)}: {m[:80]}")
    return contradictions[:5]  # 5 at most


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 merge_research.py <path to skill dir>")
        sys.exit(1)

    skill_dir = Path(sys.argv[1])
    research_dir = skill_dir / 'references' / 'research'

    if not research_dir.exists():
        print(f"❌ Directory not found: {research_dir}")
        sys.exit(1)

    files = {}
    rows = []
    total_sources = 0
    total_primary = 0
    total_secondary = 0
    missing = []

    for key, label in AGENTS.items():
        md_file = research_dir / f"{key}.md"
        if not md_file.exists():
            missing.append(label)
            rows.append(f"│ {label:<14} │ {'❌ missing':<9} │ {'—':<24} │")
            continue

        content = md_file.read_text(encoding='utf-8')
        files[key] = content
        stats = count_sources(content)
        findings = extract_key_findings(content)

        total_sources += stats['unique_urls']
        total_primary += stats['primary_markers']
        total_secondary += stats['secondary_markers']

        findings_str = ', '.join(findings) if findings else '—'
        if len(findings_str) > 24:
            findings_str = findings_str[:21] + '...'

        rows.append(f"│ {label:<14} │ {stats['unique_urls']:<9} │ {findings_str:<24} │")

    contradictions = find_contradictions(files)

    print("┌────────────────┬───────────┬──────────────────────────┐")
    print(f"│ {'Agent':<14} │ {'Sources':<9} │ {'Key findings':<24} │")
    print("├────────────────┼───────────┼──────────────────────────┤")
    for row in rows:
        print(row)
    print("├────────────────┼───────────┼──────────────────────────┤")

    denom = total_primary + total_secondary
    primary_ratio = f"{total_primary}/{denom}" if denom > 0 else "unlabelled"
    print(f"│ {'Total sources':<14} │ {total_sources:<9} │ primary: {primary_ratio:<15} │")

    if contradictions:
        print(f"│ {'Contradictions':<14} │ {len(contradictions):<9} │ {contradictions[0][:24]:<24} │")
    else:
        print(f"│ {'Contradictions':<14} │ {'0':<9} │ {'—':<24} │")

    if missing:
        print(f"│ {'Thin dimensions':<14} │ {len(missing):<9} │ {', '.join(missing)[:24]:<24} │")
    else:
        print(f"│ {'Thin dimensions':<14} │ {'none':<9} │ {'—':<24} │")

    print("└────────────────┴───────────┴──────────────────────────┘")

    if total_sources < 10:
        print("\n⚠️ Fewer than 10 sources total — lower expectations or research further")
    if missing:
        print(f"\n⚠️ Missing dimensions: {', '.join(missing)} — research them or note them in the honest limits")


if __name__ == '__main__':
    main()
