#!/usr/bin/env python3
"""
thumbnail_audit.py - a checklist script based on MrBeast's thumbnail theory

Check dimensions (based on principles MrBeast has publicly shared about thumbnails):
  1. Title/thumbnail complementarity: do they "complement rather than repeat" each other?
  2. Number of focal points: is there only 1-2 visual focal points?
  3. Amount of text: does the thumbnail have fewer than 5 words of text?
  4. Emotional expression: is there a clear facial expression/emotion?
  5. Color contrast: is the color contrast striking enough?

If an image file is provided, PIL is used to analyze color distribution and brightness contrast.

Usage:
  python thumbnail_audit.py --title "I Spent 50 Hours Buried Alive"
  python thumbnail_audit.py --title "..." --image thumbnail.jpg
  python thumbnail_audit.py --title "..." --image thumbnail.jpg -o report.md

Dependency: Pillow (only needed for image analysis; the text-only check has no dependencies)
"""

import argparse
import sys
from pathlib import Path


# ---------- MrBeast thumbnail principles ----------

REDUNDANCY_WORDS = {
    # If a title's keywords show up heavily in the thumbnail text, that's repetition, not complementarity
    "challenge", "survive", "hours", "days", "dollars", "money",
    "biggest", "world", "first", "last", "never", "impossible",
}

# Emotion-related words (used for title analysis)
EMOTION_WORDS = [
    "shocked", "scared", "amazed", "crying", "screaming", "laughing",
    "surprised", "angry", "terrified", "excited", "happy", "sad",
    "emotional", "insane", "crazy", "unbelievable", "incredible",
]


def check_title_thumbnail_complementarity(title: str, thumb_text: str = "") -> dict:
    """Check whether the title and thumbnail complement each other (rather than repeat)"""
    title_words = set(title.lower().split())
    thumb_words = set(thumb_text.lower().split()) if thumb_text else set()

    if not thumb_text:
        return {
            "score": 3,
            "max": 5,
            "note": "No thumbnail text provided, so this can't be fully assessed. Recommendation: the thumbnail should add information the title doesn't already say.",
        }

    overlap = title_words & thumb_words & REDUNDANCY_WORDS
    overlap_ratio = len(overlap) / max(len(thumb_words), 1)

    if overlap_ratio > 0.5:
        score = 1
        note = f"The thumbnail text heavily repeats the title (overlapping words: {', '.join(overlap)}). MrBeast's principle: the thumbnail should supplement the title, not repeat it."
    elif overlap_ratio > 0.2:
        score = 3
        note = f"There's some overlap ({', '.join(overlap)}), but it's acceptable. Consider having the thumbnail convey information the title doesn't."
    else:
        score = 5
        note = "The title and thumbnail complement each other well, each conveying different information."

    return {"score": score, "max": 5, "note": note, "overlap": list(overlap)}


def check_text_amount(thumb_text: str = "") -> dict:
    """Check the amount of text on the thumbnail"""
    if not thumb_text:
        return {
            "score": 4,
            "max": 5,
            "word_count": 0,
            "note": "No thumbnail text provided. MrBeast's thumbnails usually have very little text (0-3 words) or none at all.",
        }

    word_count = len(thumb_text.split())
    if word_count == 0:
        score, note = 5, "No text, clean and sharp."
    elif word_count <= 3:
        score, note = 5, f"Only {word_count} words, meets MrBeast's standard."
    elif word_count <= 5:
        score, note = 3, f"{word_count} words, close to the ceiling. Consider trimming to under 3."
    else:
        score, note = 1, f"{word_count} words is too many! MrBeast's thumbnails rarely exceed 3-5 words. The less text, the higher the click-through rate."

    return {"score": score, "max": 5, "word_count": word_count, "note": note}


def check_emotion_in_title(title: str) -> dict:
    """Check whether the title implies a clear emotion (an indirect proxy for the thumbnail's emotional needs)"""
    title_lower = title.lower()
    found_emotions = [w for w in EMOTION_WORDS if w in title_lower]

    # Check for exclamation and question marks
    has_exclamation = "!" in title
    has_question = "?" in title

    if found_emotions:
        score = 5
        note = f"The title has a clear emotional cue ({', '.join(found_emotions[:3])}). The thumbnail should echo this emotion with a facial expression."
    elif has_exclamation or has_question:
        score = 3
        note = "The title has emotional punctuation, but lacks a clear emotion word. The thumbnail needs a facial expression to fill in the emotion."
    else:
        score = 2
        note = "The title's emotion isn't obvious. MrBeast's principle: the thumbnail must have an exaggerated facial expression, or a clear emotional visual element."

    return {
        "score": score,
        "max": 5,
        "emotions_found": found_emotions,
        "note": note,
    }


def check_title_curiosity_gap(title: str) -> dict:
    """Check whether the title creates a curiosity gap"""
    curiosity_patterns = [
        ("number contrast", ["vs", "versus", "$"]),
        ("suspense word", ["secret", "mystery", "hidden", "never", "impossible"]),
        ("challenge frame", ["challenge", "survive", "last", "endure"]),
        ("extreme word", ["world", "biggest", "smallest", "most", "least"]),
        ("time pressure", ["hours", "days", "minutes", "seconds"]),
    ]

    found = []
    title_lower = title.lower()
    for pattern_name, keywords in curiosity_patterns:
        if any(k in title_lower for k in keywords):
            found.append(pattern_name)

    if len(found) >= 3:
        score, note = 5, f"The title has {len(found)} curiosity elements ({', '.join(found)}), very strong!"
    elif len(found) >= 2:
        score, note = 4, f"The title has {len(found)} curiosity elements ({', '.join(found)}), solid."
    elif len(found) == 1:
        score, note = 3, f"The title has 1 curiosity element ({found[0]}), could be stronger."
    else:
        score, note = 1, "The title lacks a curiosity gap. MrBeast's titles usually contain at least 2-3 curiosity elements."

    return {"score": score, "max": 5, "patterns_found": found, "note": note}


def analyze_image(image_path: str) -> dict:
    """Use PIL to analyze the image's color and contrast"""
    try:
        from PIL import Image, ImageStat
    except ImportError:
        return {
            "available": False,
            "note": "Pillow is not installed, skipping image analysis. Install with: pip install Pillow",
        }

    path = Path(image_path)
    if not path.exists():
        return {"available": False, "note": f"Image file not found: {image_path}"}

    try:
        img = Image.open(path)
    except Exception as e:
        return {"available": False, "note": f"Couldn't open the image: {e}"}

    # Convert to RGB
    if img.mode != "RGB":
        img = img.convert("RGB")

    stat = ImageStat.Stat(img)
    width, height = img.size

    # Average brightness
    avg_brightness = sum(stat.mean) / 3

    # Brightness standard deviation (a contrast indicator)
    avg_stddev = sum(stat.stddev) / 3

    # Color-saturation analysis
    hsv_img = img.convert("HSV")
    hsv_stat = ImageStat.Stat(hsv_img)
    avg_saturation = hsv_stat.mean[1]

    # Dominant-tone analysis (simplified: compare the center region against the edges)
    center_crop = img.crop((width // 4, height // 4, 3 * width // 4, 3 * height // 4))
    center_stat = ImageStat.Stat(center_crop)
    center_brightness = sum(center_stat.mean) / 3

    # Assessment
    results = {
        "available": True,
        "size": f"{width}x{height}",
        "brightness": {
            "average": round(avg_brightness, 1),
            "score": 5 if 80 < avg_brightness < 200 else 3 if 50 < avg_brightness < 230 else 1,
            "note": "moderate brightness" if 80 < avg_brightness < 200 else "too dark or too bright",
        },
        "contrast": {
            "stddev": round(avg_stddev, 1),
            "score": 5 if avg_stddev > 60 else 3 if avg_stddev > 40 else 1,
            "note": "strong contrast" if avg_stddev > 60 else "moderate contrast" if avg_stddev > 40 else "insufficient contrast, the thumbnail may not stand out enough at small sizes",
        },
        "saturation": {
            "average": round(avg_saturation, 1),
            "score": 5 if avg_saturation > 100 else 3 if avg_saturation > 60 else 2,
            "note": "high color saturation" if avg_saturation > 100 else "moderate color saturation" if avg_saturation > 60 else "colors are muted, consider boosting saturation",
        },
        "center_focus": {
            "center_brightness": round(center_brightness, 1),
            "edge_contrast": round(abs(center_brightness - avg_brightness), 1),
            "note": "clear contrast between the center and the edges" if abs(center_brightness - avg_brightness) > 15 else "little contrast between center and edges, the focal point may not stand out enough",
        },
    }
    return results


def generate_report(title: str, thumb_text: str = "", image_path: str = None) -> str:
    """Generate the full audit report"""
    complementarity = check_title_thumbnail_complementarity(title, thumb_text)
    text_amount = check_text_amount(thumb_text)
    emotion = check_emotion_in_title(title)
    curiosity = check_title_curiosity_gap(title)

    image_analysis = analyze_image(image_path) if image_path else None

    # Compute the total score
    scores = [complementarity["score"], text_amount["score"], emotion["score"], curiosity["score"]]
    if image_analysis and image_analysis.get("available"):
        scores.append(image_analysis["brightness"]["score"])
        scores.append(image_analysis["contrast"]["score"])
        scores.append(image_analysis["saturation"]["score"])

    total = sum(scores)
    max_total = len(scores) * 5

    lines = []
    lines.append("# Thumbnail Audit Report\n")
    lines.append(f"**Title**: {title}")
    if thumb_text:
        lines.append(f"**Thumbnail text**: {thumb_text}")
    if image_path:
        lines.append(f"**Image**: {image_path}")
    lines.append(f"\n**Total score**: {total}/{max_total} ({total/max_total*100:.0f}%)\n")

    # Grade
    pct = total / max_total * 100
    if pct >= 80:
        grade = "A - excellent, high click-through-rate potential"
    elif pct >= 60:
        grade = "B - good, room to optimize"
    elif pct >= 40:
        grade = "C - passing, needs focused improvement"
    else:
        grade = "D - needs a redo"
    lines.append(f"**Grade**: {grade}\n")

    # Individual checks
    lines.append("## 1. Title-thumbnail complementarity ({}/{})\n".format(complementarity["score"], complementarity["max"]))
    lines.append(complementarity["note"])
    lines.append("")

    lines.append("## 2. Thumbnail text amount ({}/{})\n".format(text_amount["score"], text_amount["max"]))
    lines.append(text_amount["note"])
    lines.append("")

    lines.append("## 3. Emotional expression ({}/{})\n".format(emotion["score"], emotion["max"]))
    lines.append(emotion["note"])
    lines.append("")

    lines.append("## 4. Curiosity gap ({}/{})\n".format(curiosity["score"], curiosity["max"]))
    lines.append(curiosity["note"])
    lines.append("")

    # Image analysis
    if image_analysis:
        if image_analysis.get("available"):
            lines.append(f"## 5. Technical image analysis (size: {image_analysis['size']})\n")
            b = image_analysis["brightness"]
            c = image_analysis["contrast"]
            s = image_analysis["saturation"]
            cf = image_analysis["center_focus"]
            lines.append(f"- **Brightness** ({b['score']}/5): average {b['average']} - {b['note']}")
            lines.append(f"- **Contrast** ({c['score']}/5): stddev {c['stddev']} - {c['note']}")
            lines.append(f"- **Saturation** ({s['score']}/5): average {s['average']} - {s['note']}")
            lines.append(f"- **Focus**: center-edge difference {cf['edge_contrast']} - {cf['note']}")
        else:
            lines.append(f"## 5. Image analysis\n")
            lines.append(f"Skipped: {image_analysis['note']}")
        lines.append("")

    # MrBeast's golden thumbnail rules
    lines.append("## MrBeast's golden thumbnail rules\n")
    lines.append("- [ ] Is the thumbnail clearly legible on a small phone screen?")
    lines.append("- [ ] Is there only 1-2 visual focal points (not cluttered)?")
    lines.append("- [ ] Is there a face with a strong emotional expression?")
    lines.append("- [ ] Does the thumbnail create an urge of \"I have to click on this\"?")
    lines.append("- [ ] Does the title-thumbnail combination create an information gap?")
    lines.append("- [ ] Does it stand out enough next to other videos in the same feed?")
    lines.append("")

    # Suggestions
    lines.append("## Suggestions for improvement\n")
    suggestions = []
    if complementarity["score"] < 4:
        suggestions.append("Have the thumbnail convey information the title doesn't (e.g. the title states the challenge, the thumbnail shows the outcome or the most dramatic moment)")
    if text_amount["score"] < 4:
        suggestions.append("Reduce thumbnail text — ideally 0-3 words — and tell the story visually rather than with text")
    if emotion["score"] < 4:
        suggestions.append("Add a photo of a face with an exaggerated expression to the thumbnail; the stronger the emotion, the better")
    if curiosity["score"] < 4:
        suggestions.append("Add curiosity elements to the title, such as numbers, extreme words, or time pressure")
    if image_analysis and image_analysis.get("available"):
        if image_analysis["contrast"]["score"] < 4:
            suggestions.append("Increase image contrast so the thumbnail stays clear and eye-catching at small sizes")
        if image_analysis["saturation"]["score"] < 4:
            suggestions.append("Increase color saturation so the image pops on the YouTube homepage")

    if suggestions:
        for i, s in enumerate(suggestions, 1):
            lines.append(f"{i}. {s}")
    else:
        lines.append("Overall performance is excellent, keep it up!")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="An audit tool based on MrBeast's thumbnail theory",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='Examples:\n  python thumbnail_audit.py --title "I Survived 50 Hours In Antarctica"\n  python thumbnail_audit.py --title "..." --thumb-text "50 HOURS" --image thumb.jpg',
    )
    parser.add_argument("--title", required=True, help="the video title")
    parser.add_argument("--thumb-text", default="", help="the text on the thumbnail (if any)")
    parser.add_argument("--image", help="path to the thumbnail image file (optional)")
    parser.add_argument("-o", "--output", help="output report file path")
    args = parser.parse_args()

    report = generate_report(args.title, args.thumb_text, args.image)

    if args.output:
        Path(args.output).write_text(report, encoding="utf-8")
        print(f"[OK] Report saved to: {args.output}")
    else:
        print(report)


if __name__ == "__main__":
    main()
