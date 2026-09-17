#!/usr/bin/env python3
"""
Check a generated SKILL.md against the Phase 4 quality criteria.
Walks the pass-criteria table item by item and prints pass/fail with the reason.

Usage:
    python3 quality_check.py <path to SKILL.md>

Example:
    python3 quality_check.py .claude/skills/elon-musk-perspective/SKILL.md
"""

import sys
import re
from pathlib import Path

# Section headings follow references/skill-template.md.
MENTAL_MODEL_SECTION_RE = re.compile(r'^##\s+.*\bmental model', re.IGNORECASE)
MENTAL_MODEL_ITEM_RE = re.compile(r'^###\s+(?:Model|Mental model)\s*\d', re.IGNORECASE | re.MULTILINE)
LIMITS_RE = re.compile(r'\blimits?\b|\blimitations?\b|\bblind spot\b|\bbreaks down\b|\bfails when\b',
                       re.IGNORECASE)
DNA_SECTION_RE = re.compile(r'^##\s+.*expression dna', re.IGNORECASE | re.MULTILINE)
STYLE_MARKER_RE = re.compile(
    r'^\s*[-*]?\s*\**(sentences?|vocabulary|rhythm|humou?r|certainty|citation)\b',
    re.IGNORECASE | re.MULTILINE,
)
HONEST_SECTION_RE = re.compile(r'##\s+.*honest limits?(.*?)(?=\n##\s|\Z)',
                               re.DOTALL | re.IGNORECASE)
TENSION_RE = re.compile(r'\btensions?\b|\bcontradictions?\b|\bparadox\b|\bon one hand\b',
                        re.IGNORECASE)
SOURCE_SECTION_RE = re.compile(r'##\s+.*(?:research sources|sources|references)(.*?)(?=\n##\s|\Z)',
                               re.DOTALL | re.IGNORECASE)
PRIMARY_SUB_RE = re.compile(r'###\s+primary sources?(.*?)(?=\n###\s|\n##\s|\Z)',
                            re.DOTALL | re.IGNORECASE)
SECONDARY_SUB_RE = re.compile(r'###\s+secondary sources?(.*?)(?=\n###\s|\n##\s|\Z)',
                              re.DOTALL | re.IGNORECASE)
LIST_ITEM_RE = re.compile(r'^\s*[-*]\s+\S', re.MULTILINE)


def check_mental_models(content: str) -> tuple[bool, str]:
    """Mental model count must be 3-7."""
    count = len(MENTAL_MODEL_ITEM_RE.findall(content))

    if count == 0:
        # Fallback: count H3 headings inside the mental-models section.
        in_section = False
        for line in content.split('\n'):
            if MENTAL_MODEL_SECTION_RE.match(line):
                in_section = True
                continue
            if in_section and line.startswith('## '):
                break
            if in_section and line.startswith('### '):
                count += 1

    if count == 0:
        return False, "no mental-models section detected"
    passed = 3 <= count <= 7
    return passed, f"{count} mental models {'✅' if passed else '❌ (should be 3-7)'}"


def check_limitations(content: str) -> tuple[bool, str]:
    """Every model should state where it breaks down."""
    has_limitation = bool(LIMITS_RE.search(content))
    return has_limitation, "limits are stated ✅" if has_limitation else "❌ no statement of limits found"


def check_expression_dna(content: str) -> tuple[bool, str]:
    """Expression DNA must be recognizable, i.e. spelled out concretely."""
    if not DNA_SECTION_RE.search(content):
        return False, "❌ no Expression DNA section found"

    style_markers = len(set(m.lower() for m in STYLE_MARKER_RE.findall(content)))
    passed = style_markers >= 3
    return passed, f"Expression DNA traits: {style_markers} {'✅' if passed else '❌ (should be >=3)'}"


def check_honest_boundary(content: str) -> tuple[bool, str]:
    """Honest limits: at least 3 items."""
    match = HONEST_SECTION_RE.search(content)
    if not match:
        return False, "❌ no Honest limits section found"

    count = len(LIST_ITEM_RE.findall(match.group(1)))
    passed = count >= 3
    return passed, f"Honest limits: {count} {'✅' if passed else '❌ (should be >=3)'}"


def check_tensions(content: str) -> tuple[bool, str]:
    """Internal tension: at least 2 mentions."""
    count = len(TENSION_RE.findall(content))
    passed = count >= 2
    return passed, f"Internal tension: {count} mentions {'✅' if passed else '❌ (should be >=2)'}"


def check_primary_sources(content: str) -> tuple[bool, str]:
    """Primary sources must be more than half of the cited sources."""
    section = SOURCE_SECTION_RE.search(content)
    if not section:
        return True, "no sources section found (check skipped)"

    text = section.group(1)
    primary_block = PRIMARY_SUB_RE.search(text)
    secondary_block = SECONDARY_SUB_RE.search(text)
    if not primary_block and not secondary_block:
        return True, "sources not split into primary/secondary (check skipped)"

    primary = len(LIST_ITEM_RE.findall(primary_block.group(1))) if primary_block else 0
    secondary = len(LIST_ITEM_RE.findall(secondary_block.group(1))) if secondary_block else 0
    total = primary + secondary
    if total == 0:
        return True, "sources sections are empty (check skipped)"

    ratio = primary / total
    passed = ratio > 0.5
    return passed, f"Primary sources: {primary}/{total} ({ratio:.0%}) {'✅' if passed else '❌ (should be >50%)'}"


CHECKS = [
    ("Mental models", check_mental_models),
    ("Model limits", check_limitations),
    ("Expression DNA", check_expression_dna),
    ("Honest limits", check_honest_boundary),
    ("Internal tension", check_tensions),
    ("Primary sources", check_primary_sources),
]


def run_checks(content: str) -> list[tuple[str, bool, str]]:
    return [(name, *fn(content)) for name, fn in CHECKS]


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 quality_check.py <path to SKILL.md>")
        sys.exit(1)

    skill_path = Path(sys.argv[1])
    if not skill_path.exists():
        print(f"❌ File not found: {skill_path}")
        sys.exit(1)

    content = skill_path.read_text(encoding='utf-8')
    results = run_checks(content)

    print(f"Quality check: {skill_path.name}")
    print("=" * 60)

    passed_count = 0
    for name, passed, detail in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"  {name:<18} {status}  {detail}")
        if passed:
            passed_count += 1

    total = len(results)
    print("=" * 60)
    print(f"Result: {passed_count}/{total} passed")

    if passed_count == total:
        print("🎉 All checks passed — ready to deliver")
    elif passed_count >= total - 1:
        print("⚠️ Mostly passing — fix the failing item before delivering")
    else:
        print("❌ Several checks failed — iterate from Phase 2")

    sys.exit(0 if passed_count == total else 1)


if __name__ == '__main__':
    main()
