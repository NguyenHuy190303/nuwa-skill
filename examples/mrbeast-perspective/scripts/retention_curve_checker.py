#!/usr/bin/env python3
"""
retention_curve_checker.py - a video-script retention checker based on MrBeast's methodology

Check dimensions (based on retention theory MrBeast has shared publicly):
  1. The first-30-seconds hook: is there a clear hook that grabs the viewer?
  2. Re-engagement moments: is there an escalation/twist every 3-5 minutes?
  3. Ending CTA/cliffhanger: does the ending have a call to action or a cliffhanger?
  4. Boring parts: are there long stretches with no action ("dead zones")?
  5. Escalating structure: does the content keep escalating (MrBeast's core principle)

Usage:
  python retention_curve_checker.py script.txt
  python retention_curve_checker.py script.txt -o report.md
  python retention_curve_checker.py script.txt --duration 15

Input format: a plain-text script file. Supports both Chinese- and English-language scripts —
the hook/re-engagement/CTA/action-word pattern lists below intentionally include Chinese-character
patterns alongside the English ones so scripts in either language can be scored.
"""

import argparse
import re
import sys
from pathlib import Path


# ---------- Constants ----------

# Average speaking rate (Chinese: ~250 characters/minute, English: ~150 words/minute)
WORDS_PER_MINUTE_EN = 150
CHARS_PER_MINUTE_ZH = 250

# Keywords/patterns for the hook check
HOOK_PATTERNS = [
    r"\b(today|right now|in this video|let me show|watch what happens)\b",
    r"\b(challenge|bet|dare|surprise|secret|reveal|biggest|craziest)\b",
    r"\$[\d,]+",
    r"\b\d+\s*(hours?|days?|people|dollars)\b",
    r"[!?]{1,}",
    # Chinese-language hooks
    r"(今天|现在|接下来|你绝对|不敢相信|挑战|赌|秘密|最大的|最疯狂的)",
]

# Re-engagement signal words
REENGAGEMENT_PATTERNS = [
    r"\b(but wait|it gets (better|worse|crazier)|plot twist|here'?s where)\b",
    r"\b(next|now|then|suddenly|finally|the (biggest|craziest|best) part)\b",
    r"\b(level \d|round \d|phase \d|stage \d|part \d)\b",
    r"\b(upgrade|double|triple|10x|100x|even more|even bigger)\b",
    # Chinese
    r"(但是等等|更疯狂的是|转折来了|接下来|突然|最关键的|升级|加倍|翻倍)",
    r"(第[一二三四五六七八九十\d]+[轮关回])",
]

# CTA and cliffhanger patterns
CTA_PATTERNS = [
    r"\b(subscribe|like|comment|share|click|next video|see you)\b",
    r"\b(what do you think|let me know|tell me)\b",
    r"\b(next time|coming soon|stay tuned|part \d|to be continued)\b",
    # Chinese
    r"(关注|点赞|评论|分享|下期|下次|下一个视频|你觉得呢|告诉我|敬请期待)",
]

# Boring-part detection: long stretches with no action words
ACTION_WORDS = [
    r"\b(explode|run|jump|scream|crash|build|destroy|open|reveal|surprise)\b",
    r"\b(win|lose|fail|succeed|break|smash|launch|drop|fly|race)\b",
    r"[!?]",
    r"\$[\d,]+",
    # Chinese
    r"(爆炸|跑|跳|尖叫|建造|打开|揭晓|惊喜|赢|输|失败|打破|发射)",
]


def detect_language(text: str) -> str:
    """Roughly detect the text's primary language"""
    zh_chars = len(re.findall(r"[一-鿿]", text))
    en_words = len(re.findall(r"[a-zA-Z]+", text))
    return "zh" if zh_chars > en_words else "en"


def estimate_duration(text: str, lang: str) -> float:
    """Estimate script duration (minutes)"""
    if lang == "zh":
        char_count = len(re.findall(r"[一-鿿]", text))
        return char_count / CHARS_PER_MINUTE_ZH
    else:
        word_count = len(text.split())
        return word_count / WORDS_PER_MINUTE_EN


def split_into_segments(text: str, segment_minutes: float, lang: str) -> list[str]:
    """Split the script into segments by duration"""
    lines = text.splitlines()
    if lang == "zh":
        chars_per_seg = int(CHARS_PER_MINUTE_ZH * segment_minutes)
        segments = []
        current = []
        current_len = 0
        for line in lines:
            line_len = len(re.findall(r"[一-鿿]", line))
            if current_len + line_len > chars_per_seg and current:
                segments.append("\n".join(current))
                current = [line]
                current_len = line_len
            else:
                current.append(line)
                current_len += line_len
        if current:
            segments.append("\n".join(current))
        return segments
    else:
        words_per_seg = int(WORDS_PER_MINUTE_EN * segment_minutes)
        segments = []
        current = []
        current_len = 0
        for line in lines:
            line_len = len(line.split())
            if current_len + line_len > words_per_seg and current:
                segments.append("\n".join(current))
                current = [line]
                current_len = line_len
            else:
                current.append(line)
                current_len += line_len
        if current:
            segments.append("\n".join(current))
        return segments


def check_hook(text: str, first_n_chars: int = 500) -> dict:
    """Check whether the first 30 seconds have a hook"""
    opening = text[:first_n_chars]
    matches = []
    for pattern in HOOK_PATTERNS:
        found = re.findall(pattern, opening, re.IGNORECASE)
        if found:
            matches.extend(found)
    score = min(len(matches), 5)  # 0-5 points
    return {
        "score": score,
        "max": 5,
        "matches": matches[:5],
        "opening_preview": opening[:200].replace("\n", " "),
    }


def check_reengagement(segments: list[str]) -> dict:
    """Check whether each segment has a re-engagement moment"""
    results = []
    for i, seg in enumerate(segments):
        matches = []
        for pattern in REENGAGEMENT_PATTERNS:
            found = re.findall(pattern, seg, re.IGNORECASE)
            if found:
                matches.extend(found)
        results.append({
            "segment": i + 1,
            "has_reengagement": len(matches) > 0,
            "matches": matches[:3],
        })
    segments_with = sum(1 for r in results if r["has_reengagement"])
    total = len(results)
    score = round(segments_with / total * 5) if total > 0 else 0
    return {
        "score": score,
        "max": 5,
        "segments_with": segments_with,
        "total_segments": total,
        "details": results,
    }


def check_ending(text: str, last_n_chars: int = 500) -> dict:
    """Check whether the ending has a CTA or a cliffhanger"""
    ending = text[-last_n_chars:]
    matches = []
    for pattern in CTA_PATTERNS:
        found = re.findall(pattern, ending, re.IGNORECASE)
        if found:
            matches.extend(found)
    score = min(len(matches), 5)
    return {
        "score": score,
        "max": 5,
        "matches": matches[:5],
        "ending_preview": ending[-200:].replace("\n", " "),
    }


def check_boring_parts(segments: list[str]) -> dict:
    """Check for action-free "dead zone" segments"""
    boring_segments = []
    for i, seg in enumerate(segments):
        action_count = 0
        for pattern in ACTION_WORDS:
            action_count += len(re.findall(pattern, seg, re.IGNORECASE))
        # flag a segment if its action-word density is too low
        word_count = max(len(seg.split()), 1)
        density = action_count / word_count * 100
        if density < 0.5:  # below 0.5% action-word density
            boring_segments.append({
                "segment": i + 1,
                "preview": seg[:100].replace("\n", " ") + "...",
                "action_density": round(density, 2),
            })
    # 5 points if there are no boring segments, minus 1 point per boring segment
    score = max(0, 5 - len(boring_segments))
    return {
        "score": score,
        "max": 5,
        "boring_count": len(boring_segments),
        "details": boring_segments,
    }


def check_escalation(segments: list[str]) -> dict:
    """Check whether the content keeps escalating (MrBeast's core principle: every minute has to top the last one)"""
    escalation_words = [
        r"\b(more|bigger|better|crazier|harder|faster|extreme|ultimate|final)\b",
        r"\b(upgrade|level up|raise|increase|double|triple|max|peak)\b",
        r"(更大|更好|更疯狂|更难|升级|加码|翻倍|终极|最终)",
    ]
    scores_per_seg = []
    for seg in segments:
        count = 0
        for pattern in escalation_words:
            count += len(re.findall(pattern, seg, re.IGNORECASE))
        scores_per_seg.append(count)

    # Ideally, the second half should have more escalation words than the first half
    if len(scores_per_seg) >= 2:
        mid = len(scores_per_seg) // 2
        first_half = sum(scores_per_seg[:mid])
        second_half = sum(scores_per_seg[mid:])
        is_escalating = second_half >= first_half
    else:
        is_escalating = True

    total_escalation = sum(scores_per_seg)
    score = min(total_escalation, 3) + (2 if is_escalating else 0)
    return {
        "score": min(score, 5),
        "max": 5,
        "is_escalating": is_escalating,
        "escalation_per_segment": scores_per_seg,
    }


def generate_report(filepath: str, text: str, duration_override: float = None) -> str:
    """Generate the full check report"""
    lang = detect_language(text)
    duration = duration_override or estimate_duration(text, lang)
    segments = split_into_segments(text, 3.0, lang)  # one segment per 3 minutes

    hook = check_hook(text)
    reengagement = check_reengagement(segments)
    ending = check_ending(text)
    boring = check_boring_parts(segments)
    escalation = check_escalation(segments)

    total_score = hook["score"] + reengagement["score"] + ending["score"] + boring["score"] + escalation["score"]
    max_score = 25

    lines = []
    lines.append("# Retention Check Report\n")
    lines.append(f"**File**: {filepath}")
    lines.append(f"**Language**: {'Chinese' if lang == 'zh' else 'English'}")
    lines.append(f"**Estimated duration**: {duration:.1f} minutes")
    lines.append(f"**Segments**: {len(segments)} (every 3 minutes)")
    lines.append(f"**Total score**: {total_score}/{max_score}\n")

    # Grade
    if total_score >= 20:
        grade = "A - Excellent, retention structure is solid"
    elif total_score >= 15:
        grade = "B - Good, room for improvement"
    elif total_score >= 10:
        grade = "C - Passing, needs focused optimization"
    else:
        grade = "D - Needs a major rewrite"
    lines.append(f"**Grade**: {grade}\n")

    # 1. Hook check
    lines.append("## 1. First-30-seconds hook ({}/{})\n".format(hook["score"], hook["max"]))
    if hook["score"] >= 3:
        lines.append("The opening has a clear hook element.")
    elif hook["score"] >= 1:
        lines.append("The opening has a partial hook, but it isn't strong enough.")
    else:
        lines.append("**Warning**: the opening lacks a hook — viewers may drop off in the first 10 seconds.")
    if hook["matches"]:
        lines.append(f"\nDetected hook elements: {', '.join(str(m) for m in hook['matches'][:5])}")
    lines.append(f"\n> Opening preview: {hook['opening_preview']}")
    lines.append("")
    lines.append("**MrBeast principle**: the first 30 seconds must tell the viewer \"this video is worth watching to the end.\" Either preview the final payoff, or throw out an irresistible cliffhanger right away.\n")

    # 2. Re-engagement
    lines.append("## 2. Re-engagement moments ({}/{})\n".format(reengagement["score"], reengagement["max"]))
    lines.append(f"Of {reengagement['total_segments']} segments, {reengagement['segments_with']} contain a re-engagement signal.\n")
    for detail in reengagement["details"]:
        status = "present" if detail["has_reengagement"] else "**missing**"
        lines.append(f"- Segment {detail['segment']}: {status}")
        if detail["matches"]:
            lines.append(f"  Signal words: {', '.join(str(m) for m in detail['matches'])}")
    lines.append("")
    lines.append("**MrBeast principle**: there has to be a moment that \"re-grabs the viewer\" every 3-5 minutes — a new challenge escalation, an unexpected twist, or raised stakes.\n")

    # 3. Ending
    lines.append("## 3. Ending CTA/cliffhanger ({}/{})\n".format(ending["score"], ending["max"]))
    if ending["score"] >= 3:
        lines.append("The ending has a clear CTA or cliffhanger.")
    elif ending["score"] >= 1:
        lines.append("The ending has a partial CTA element, but could be stronger.")
    else:
        lines.append("**Warning**: the ending falls flat, with no call to action or teaser for the next video.")
    lines.append(f"\n> Ending preview: ...{ending['ending_preview']}")
    lines.append("")

    # 4. Boring parts
    lines.append("## 4. Boring-parts detection ({}/{})\n".format(boring["score"], boring["max"]))
    if boring["boring_count"] == 0:
        lines.append("No obvious \"dead zone\" segments detected.")
    else:
        lines.append(f"Detected **{boring['boring_count']}** low-action-density segments:\n")
        for b in boring["details"]:
            lines.append(f"- Segment {b['segment']} (action density: {b['action_density']}%): {b['preview']}")
    lines.append("")
    lines.append("**MrBeast principle**: \"If it's boring, cut it.\" A segment with no action and no tension is exactly the moment a viewer clicks away.\n")

    # 5. Escalating structure
    lines.append("## 5. Escalating structure ({}/{})\n".format(escalation["score"], escalation["max"]))
    if escalation["is_escalating"]:
        lines.append("The content trends upward — the second half has more escalation words than the first half.")
    else:
        lines.append("**Warning**: the second half feels less escalated than the first half, which risks losing viewers midway through.")
    lines.append(f"\nEscalation-word count per segment: {escalation['escalation_per_segment']}")
    lines.append("")
    lines.append("**MrBeast principle**: every minute of the video should top the last one. Viewer expectations keep rising, and the content has to keep pace.\n")

    # Improvement suggestions
    lines.append("## Improvement suggestions\n")
    if hook["score"] < 3:
        lines.append("1. **Strengthen the opening**: consider a \"payoff-first\" strategy — show the video's most striking moment in the first 5 seconds, then rewind to tell the story from the start.")
    if reengagement["segments_with"] < reengagement["total_segments"] * 0.6:
        missing = [d["segment"] for d in reengagement["details"] if not d["has_reengagement"]]
        lines.append(f"2. **Add more turning points**: segments {missing} are missing re-engagement — consider adding a new challenge, an unexpected event, or raised stakes.")
    if ending["score"] < 3:
        lines.append("3. **Strengthen the ending**: add a clear CTA (subscribe/like) or a teaser for the next video, giving viewers a reason to come back.")
    if boring["boring_count"] > 0:
        lines.append(f"4. **Trim the dead zones**: {boring['boring_count']} segment(s) have too low an action density — consider tightening them or adding visual/action elements.")
    if not escalation["is_escalating"]:
        lines.append("5. **Restructure**: move the most exciting content into the second half, to make sure viewers feel a continuous escalation.")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="A video-script retention checker based on MrBeast's methodology",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Examples:\n  python retention_curve_checker.py script.txt\n  python retention_curve_checker.py script.txt --duration 15 -o report.md",
    )
    parser.add_argument("input", help="a video-script text file")
    parser.add_argument("-o", "--output", help="output report file path")
    parser.add_argument("--duration", type=float, help="manually specify video duration (minutes), overriding the automatic estimate")
    args = parser.parse_args()

    path = Path(args.input)
    if not path.exists():
        print(f"[ERROR] File not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    text = path.read_text(encoding="utf-8")
    if not text.strip():
        print(f"[ERROR] File is empty: {args.input}", file=sys.stderr)
        sys.exit(1)

    report = generate_report(args.input, text, args.duration)

    if args.output:
        Path(args.output).write_text(report, encoding="utf-8")
        print(f"[OK] Report saved to: {args.output}")
    else:
        print(report)


if __name__ == "__main__":
    main()
