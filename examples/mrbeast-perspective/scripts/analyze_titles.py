#!/usr/bin/env python3
"""
analyze_titles.py - Analyze title patterns across a YouTube channel's videos

Analysis dimensions:
  - Title length distribution
  - Frequency and type of number usage
  - High-frequency words (stop words removed)
  - Title-formula classification (challenge/number/suspense/contrast/emotional)
  - Punctuation and capitalization patterns

Usage:
  python analyze_titles.py titles.txt
  python analyze_titles.py titles.txt -o report.md
  python analyze_titles.py titles.txt --top 30

Input format: a plain-text file, one title per line
Output format: a Markdown analysis report
"""

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

# English stop words (lightweight, no nltk dependency)
STOP_WORDS = {
    "i", "me", "my", "we", "our", "you", "your", "he", "him", "his", "she",
    "her", "it", "its", "they", "them", "their", "a", "an", "the", "and",
    "but", "or", "for", "nor", "on", "at", "to", "from", "by", "in", "of",
    "with", "is", "am", "are", "was", "were", "be", "been", "being", "have",
    "has", "had", "do", "does", "did", "will", "would", "shall", "should",
    "may", "might", "must", "can", "could", "not", "no", "so", "if", "then",
    "than", "that", "this", "these", "those", "what", "which", "who", "whom",
    "how", "when", "where", "why", "all", "each", "every", "both", "few",
    "more", "most", "other", "some", "such", "only", "same", "too", "very",
    "just", "about", "above", "after", "again", "also", "any", "because",
    "before", "between", "during", "into", "through", "up", "down", "out",
    "over", "under", "here", "there", "now", "get", "got", "go", "going",
    "went", "make", "made", "like", "even", "still", "back", "us",
}

# Keywords/patterns for title-formula classification
TITLE_PATTERNS = {
    "challenge": [
        r"\b(challenge|survive|last|endure|spent|living|tried|attempt)\b",
        r"\b(\d+)\s*(hours?|days?|minutes?)\b",
        r"\bi\s+(survived|built|made|ate|bought|opened|spent)\b",
    ],
    "number": [
        r"^\$[\d,]+",
        r"\$[\d,]+\s+vs\.?\s+\$[\d,]+",
        r"\b\d{2,}\b",
        r"\b(100|1000|10000|million|billion)\b",
    ],
    "suspense": [
        r"\.\.\.",
        r"\?$",
        r"\b(mystery|secret|hidden|never|impossible|insane|unbelievable)\b",
        r"\b(what happens|you won't believe|no one|nobody)\b",
    ],
    "contrast": [
        r"\bvs\.?\b",
        r"\bversus\b",
        r"\$[\d,]+\s+vs\.?\s+\$[\d,]+",
        r"\b(cheap|expensive|worst|best|biggest|smallest)\b.*\bvs\.?\b",
        r"\b(world'?s?\s+(largest|smallest|most|least|biggest|cheapest))\b",
    ],
    "emotional": [
        r"\b(emotional|crying|tears|heartwarming|giving|donated|surprise)\b",
        r"!{2,}",
        r"\b(amazing|incredible|insane|crazy|epic|extreme)\b",
    ],
}


def load_titles(filepath: str) -> list[str]:
    """Load titles from a text file, one per line"""
    path = Path(filepath)
    if not path.exists():
        print(f"[ERROR] File not found: {filepath}", file=sys.stderr)
        sys.exit(1)
    titles = [
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    if not titles:
        print(f"[ERROR] File is empty: {filepath}", file=sys.stderr)
        sys.exit(1)
    return titles


def analyze_length(titles: list[str]) -> dict:
    """Analyze title length distribution"""
    lengths = [len(t) for t in titles]
    word_counts = [len(t.split()) for t in titles]
    return {
        "char_avg": sum(lengths) / len(lengths),
        "char_min": min(lengths),
        "char_max": max(lengths),
        "char_median": sorted(lengths)[len(lengths) // 2],
        "word_avg": sum(word_counts) / len(word_counts),
        "word_min": min(word_counts),
        "word_max": max(word_counts),
        "brackets": [
            sum(1 for l in lengths if l <= 30),
            sum(1 for l in lengths if 30 < l <= 50),
            sum(1 for l in lengths if 50 < l <= 70),
            sum(1 for l in lengths if l > 70),
        ],
    }


def analyze_numbers(titles: list[str]) -> dict:
    """Analyze number usage"""
    has_number = [t for t in titles if re.search(r"\d", t)]
    has_dollar = [t for t in titles if "$" in t]
    numbers_found = []
    for t in titles:
        numbers_found.extend(int(n.replace(",", "")) for n in re.findall(r"[\d,]+", t) if n.replace(",", "").isdigit())
    return {
        "with_number_pct": len(has_number) / len(titles) * 100,
        "with_dollar_pct": len(has_dollar) / len(titles) * 100,
        "common_numbers": Counter(numbers_found).most_common(10),
    }


def analyze_words(titles: list[str], top_n: int = 20) -> list[tuple[str, int]]:
    """Extract high-frequency words (stop words removed)"""
    words = []
    for t in titles:
        tokens = re.findall(r"[a-zA-Z]+", t.lower())
        words.extend(w for w in tokens if w not in STOP_WORDS and len(w) > 1)
    return Counter(words).most_common(top_n)


def classify_titles(titles: list[str]) -> dict[str, list[str]]:
    """Classify titles by formula type"""
    results = {cat: [] for cat in TITLE_PATTERNS}
    for t in titles:
        for cat, patterns in TITLE_PATTERNS.items():
            if any(re.search(p, t, re.IGNORECASE) for p in patterns):
                results[cat].append(t)
                break  # each title is assigned to only the first category it matches
    results["other"] = [
        t for t in titles
        if not any(t in v for v in results.values())
    ]
    return results


def analyze_punctuation(titles: list[str]) -> dict:
    """Analyze punctuation and capitalization patterns"""
    return {
        "ends_exclamation": sum(1 for t in titles if t.endswith("!")),
        "ends_question": sum(1 for t in titles if t.endswith("?")),
        "ends_ellipsis": sum(1 for t in titles if t.endswith("...")),
        "has_all_caps_word": sum(1 for t in titles if re.search(r"\b[A-Z]{2,}\b", t)),
        "has_emoji": sum(1 for t in titles if re.search(r"[\U0001F600-\U0001F9FF]", t)),
    }


def generate_report(titles: list[str], top_n: int) -> str:
    """Generate a Markdown analysis report"""
    total = len(titles)
    length_stats = analyze_length(titles)
    number_stats = analyze_numbers(titles)
    top_words = analyze_words(titles, top_n)
    categories = classify_titles(titles)
    punct_stats = analyze_punctuation(titles)

    lines = []
    lines.append(f"# YouTube Title Analysis Report\n")
    lines.append(f"Analyzed **{total}** titles\n")

    # Length distribution
    lines.append("## 1. Title length distribution\n")
    lines.append("| Metric | Characters | Words |")
    lines.append("|------|--------|------|")
    lines.append(f"| Average | {length_stats['char_avg']:.1f} | {length_stats['word_avg']:.1f} |")
    lines.append(f"| Shortest | {length_stats['char_min']} | {length_stats['word_min']} |")
    lines.append(f"| Longest | {length_stats['char_max']} | {length_stats['word_max']} |")
    lines.append(f"| Median | {length_stats['char_median']} | - |")
    lines.append("")
    b = length_stats["brackets"]
    lines.append(f"- Under 30 characters: {b[0]} ({b[0]/total*100:.1f}%)")
    lines.append(f"- 31-50 characters: {b[1]} ({b[1]/total*100:.1f}%)")
    lines.append(f"- 51-70 characters: {b[2]} ({b[2]/total*100:.1f}%)")
    lines.append(f"- Over 70 characters: {b[3]} ({b[3]/total*100:.1f}%)")
    lines.append("")

    # Number usage
    lines.append("## 2. Number usage\n")
    lines.append(f"- Titles containing a number: {number_stats['with_number_pct']:.1f}%")
    lines.append(f"- Titles containing a $ amount: {number_stats['with_dollar_pct']:.1f}%")
    if number_stats["common_numbers"]:
        lines.append("\nCommon numbers:")
        for num, count in number_stats["common_numbers"]:
            lines.append(f"  - {num:,}: appears {count} times")
    lines.append("")

    # High-frequency words
    lines.append(f"## 3. High-frequency words (Top {top_n})\n")
    lines.append("| Rank | Word | Count |")
    lines.append("|------|------|----------|")
    for i, (word, count) in enumerate(top_words, 1):
        lines.append(f"| {i} | {word} | {count} |")
    lines.append("")

    # Title-formula classification
    lines.append("## 4. Title-formula classification\n")
    lines.append("| Type | Count | Share | Example |")
    lines.append("|------|------|------|------|")
    for cat in ["challenge", "number", "suspense", "contrast", "emotional", "other"]:
        items = categories.get(cat, [])
        pct = len(items) / total * 100 if total else 0
        example = items[0][:50] + "..." if items and len(items[0]) > 50 else (items[0] if items else "-")
        lines.append(f"| {cat} | {len(items)} | {pct:.1f}% | {example} |")
    lines.append("")

    # Punctuation and formatting
    lines.append("## 5. Punctuation and formatting traits\n")
    lines.append(f"- Ends with an exclamation mark: {punct_stats['ends_exclamation']} ({punct_stats['ends_exclamation']/total*100:.1f}%)")
    lines.append(f"- Ends with a question mark: {punct_stats['ends_question']} ({punct_stats['ends_question']/total*100:.1f}%)")
    lines.append(f"- Ends with an ellipsis: {punct_stats['ends_ellipsis']} ({punct_stats['ends_ellipsis']/total*100:.1f}%)")
    lines.append(f"- Contains an all-caps word: {punct_stats['has_all_caps_word']} ({punct_stats['has_all_caps_word']/total*100:.1f}%)")
    lines.append("")

    # Insights
    lines.append("## 6. Key insights\n")
    # Auto-generate a few insights
    if number_stats["with_number_pct"] > 60:
        lines.append("- **Number-driven**: over 60% of titles use a number, making numbers a core hook")
    if number_stats["with_dollar_pct"] > 30:
        lines.append("- **Money narrative**: heavy use of $ amounts, creating a sense of value and scale")
    dominant_cat = max(
        [(cat, len(items)) for cat, items in categories.items() if cat != "other"],
        key=lambda x: x[1],
    )
    lines.append(f"- **Dominant formula**: \"{dominant_cat[0]}\" is the most-used title type ({dominant_cat[1]}/{total})")
    if length_stats["char_avg"] < 50:
        lines.append("- **Concise style**: average title length is under 50 characters, leaning toward short titles")
    else:
        lines.append("- **Detailed style**: average title is over 50 characters, leaning toward descriptive titles")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Analyze title patterns across a YouTube channel's videos",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Examples:\n  python analyze_titles.py mrbeast_titles.txt\n  python analyze_titles.py titles.txt -o report.md --top 30",
    )
    parser.add_argument("input", help="a text file of titles (one per line)")
    parser.add_argument("-o", "--output", help="output report file path (defaults to printing to the terminal)")
    parser.add_argument("--top", type=int, default=20, help="number of high-frequency words to show (default 20)")
    args = parser.parse_args()

    titles = load_titles(args.input)
    report = generate_report(titles, args.top)

    if args.output:
        Path(args.output).write_text(report, encoding="utf-8")
        print(f"[OK] Report saved to: {args.output}")
    else:
        print(report)


if __name__ == "__main__":
    main()
