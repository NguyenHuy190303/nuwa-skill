#!/usr/bin/env python3
"""Semi-automated check for a COMMUNITY.md listing PR.

Machine checks (this script):
1. The PR touches only COMMUNITY.md (touching SKILL.md or other core files is an
   automatic ❌)
2. The GitHub repo linked in the added line actually exists and is public
3. If the target repo has a root SKILL.md (a person or topic skill) -> extra
   requirements:
   - FIDELITY.md exists with a total score >= 70 (grade B)
   - FIDELITY.md's key field lines (test date / total score / per-dimension
     scores) are not placeholders or estimates (pending, estimated, TBD,
     YYYY-MM-DD, and so on — scores must come from an independent dual-agent
     test; only the field lines are scanned, not the whole document, so prose
     like "honest limits" never triggers it)
   - SKILL.md has an "Honest limits" section
   - Has a references/ directory; a missing references/research/ subdirectory
     is only logged as a ⚠️ for manual review
   If it has no SKILL.md (a collection or tooling repo) -> existence check
   only, flagged for the maintainer to classify by hand
4. Post the result as a PR comment

Manual check (maintainer): ethics red lines + a content-quality spot check + merge.

Local testing: python3 community_check.py --check-repo owner/repo
"""
import json
import os
import re
import sys
import urllib.request

API = "https://api.github.com"

# FIDELITY.md placeholder/estimate detection: a structured scan of key field
# lines; a hit is an automatic ❌.
# Rationale: fidelity scores must come from an independent dual-agent test (see
# references/fidelity-scorecard.md); "prefilled template + one line of total
# score" does not count as a real test (precedent: PR #70).
# Design constraints (from the 2026-07-26 adversarial review, P1-22/P1-23):
# 1. Only scan "key field lines" (test date / total score / per-dimension
#    scores, etc.), never the whole document — "Honest limits: X was not
#    tested" is prose the project itself requires and must not be flagged as
#    fabrication;
# 2. Negation-context immunity: "NOT a self-assessment" does not count as a hit;
# 3. English words are bound to a score context ("estimated score"), so this
#    does not block "Estimated reading time".
# Better to miss a case and leave it to manual review than to machine-reject a
# submission that actually followed the rules.
#
# The field names are matched in both Chinese and English: existing community
# entries (and future non-English submissions) still use the Chinese scorecard
# terms from before this repo's translation, and rejecting those outright would
# be a regression, not a fix.

# A key field line: a field name followed by a colon or table separator, at the
# start of a line (a markdown prefix like >, #, *, -, | is allowed before it).
# A narrative sentence like "score dates are always formatted YYYY-MM-DD" has no
# separator right after the field name, so it is not treated as a field line.
FIDELITY_KEY_FIELD_RE = re.compile(
    r"^[\s>#*\-|]*(?:测试日期|评分日期|测试时间|测试模型|总分|综合得分|最终得分|得分|评分"
    r"|维度\s*\d+|立场一致性|风格辨识度|边缘诚实度|来源透明度|结构完整度"
    r"|total(?:\s+score)?|overall(?:\s+score)?|final\s+score|test\s+date|score|date"
    r"|stance\s+consistency|style\s+recognizability|edge\s+honesty"
    r"|source\s+transparency|structural\s+completeness)"
    r"[\s*]*[:：|]",
    re.IGNORECASE,
)
# Placeholder/estimate markers (only searched for within key field lines)
FIDELITY_PLACEHOLDER_PATTERNS = [
    (r"预估", "预估 (estimated)"),
    (r"待跑", "待跑 (pending run)"),
    (r"待测", "待测 (pending test)"),
    (r"待补", "待补 (to be filled in)"),
    (r"待定", "待定 (TBD)"),
    (r"待填", "待填 (to be filled in)"),
    (r"占位", "占位 (placeholder)"),
    (r"未实测", "未实测 (not actually tested)"),
    (r"未测试", "未测试 (not tested)"),
    (r"自评分", "自评分 (self-scored)"),   # distinct from a paper citation's "self-assessment accuracy"; bare "self-scored" is not accepted
    (r"YYYY[-/年]?\s*MM", "YYYY-MM-DD (template date left unfilled)"),
    (r"\bTBD\b", "TBD"),
    (r"\bTODO\b", "TODO"),
    (r"pending\s+(?:test|run)", "pending test/run"),
    (r"self[- ]assess\w*", "self-assessed"),
    (r"\bestimated\s+(?:score|total|rating|grade)", "estimated score"),
    (r"\bplaceholder\b", "placeholder"),
    (r"\bNN\s*/\s*\d+", "NN/100 (template score left unfilled)"),
]
# Negation context: if the text right before a hit is a negation, treat it as
# the author deliberately clarifying rather than an actual placeholder
FIDELITY_NEGATION_RE = re.compile(
    r"(?:不是|并非|绝不|从不|不算|不做|没有|不存在|未使用|无"
    r"|not(?:\s+an?)?|isn'?t(?:\s+an?)?|never|no)[\s*'\"「」（(]*$",
    re.IGNORECASE,
)


def find_fidelity_red_flags(text):
    """Structured field scan of FIDELITY.md: check only whether the key field
    lines are placeholders or estimates.

    Returns the list of hit labels (deduplicated, order preserved). Non-field
    lines (honest limits, statements of limitation, and other prose) are never
    scanned.
    """
    hits = []
    for line in text.splitlines():
        if not FIDELITY_KEY_FIELD_RE.match(line):
            continue
        for pat, label in FIDELITY_PLACEHOLDER_PATTERNS:
            for m in re.finditer(pat, line, re.IGNORECASE):
                prefix = line[max(0, m.start() - 16):m.start()]
                if FIDELITY_NEGATION_RE.search(prefix):
                    continue  # 否定语境（「不是自评分」「NOT a self-assessment」）
                hits.append(label)
                break
    return list(dict.fromkeys(hits))


def gh(path, token, raw=False):
    req = urllib.request.Request(API + path)
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    if raw:
        req.add_header("Accept", "application/vnd.github.raw+json")
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            data = r.read().decode("utf-8", "replace")
            return data if raw else json.loads(data)
    except Exception:
        return None


def check_target_repo(slug, token):
    """Check the repo being listed. Returns (passed, list of check items)."""
    items = []
    repo = gh(f"/repos/{slug}", token)
    if not repo:
        return False, [("❌", f"`{slug}` repo does not exist or is not accessible")]
    items.append(("✅", f"[`{slug}`](https://github.com/{slug}) exists (★{repo.get('stargazers_count', 0)})"))

    skill_md = gh(f"/repos/{slug}/contents/SKILL.md", token, raw=True)
    if skill_md is None:
        items.append(("ℹ️", "No root SKILL.md -> treated as a collection/tooling repo; please confirm category and content by hand"))
        return True, items
    items.append(("✅", "Has SKILL.md (reviewed as a skill repo)"))

    if "诚实边界" in skill_md or "Honest" in skill_md or "honest-limits" in skill_md.lower():
        items.append(("✅", "SKILL.md has an Honest limits section"))
    else:
        items.append(("❌", "SKILL.md is missing the \"Honest limits\" section (one of the listing requirements)"))

    refs = gh(f"/repos/{slug}/contents/references", token)
    if isinstance(refs, list) and refs:
        items.append(("✅", "Has a references/ directory"))
        research = gh(f"/repos/{slug}/contents/references/research", token)
        if isinstance(research, list) and research:
            items.append(("✅", "Has a references/research/ raw-research directory"))
        else:
            items.append(("⚠️", "No references/research/ subdirectory found (the raw-research layout CONTRIBUTING expects). "
                                "If the raw research sits directly under references/, the maintainer can confirm traceability by hand — not a hard blocker"))
    else:
        items.append(("❌", "Missing references/ raw research (a skill must be self-contained and traceable)"))

    fidelity = gh(f"/repos/{slug}/contents/FIDELITY.md", token, raw=True)
    if fidelity is None:
        items.append(("❌", "Missing FIDELITY.md fidelity scorecard (see references/fidelity-scorecard.md)"))
    else:
        m = re.search(r"(?:总分|total)[：:]\s*(\d+)\s*/\s*100", fidelity, re.IGNORECASE)
        if not m:
            items.append(("❌", "FIDELITY.md exists but no \"Total: NN/100\" could be parsed out of it"))
        elif int(m.group(1)) >= 70:
            items.append(("✅", f"Fidelity {m.group(1)}/100 >= 70 (grade B bar)"))
        else:
            items.append(("❌", f"Fidelity {m.group(1)}/100 below the grade B bar (70)"))
        red_flags = find_fidelity_red_flags(fidelity)
        if red_flags:
            items.append(("❌", "FIDELITY.md's key fields (test date / total score / per-dimension scores) contain a placeholder or estimate: `"
                          + "`, `".join(red_flags[:8])
                          + ("`" if len(red_flags) <= 8 else f"`, and {len(red_flags)} more")
                          + ". Fidelity scores must come from an independent dual-agent test (method in references/fidelity-scorecard.md); "
                            "a prefilled template or a self-estimated score does not meet the listing bar — run the real test and update the scorecard"))
        else:
            items.append(("✅", "No placeholder or estimate detected in FIDELITY.md's key fields"))

    ok = all(mark != "❌" for mark, _ in items)
    return ok, items


def main():
    if len(sys.argv) == 3 and sys.argv[1] == "--check-repo":
        ok, items = check_target_repo(sys.argv[2], os.environ.get("GITHUB_TOKEN", ""))
        for mark, text in items:
            print(mark, text)
        sys.exit(0 if ok else 1)

    token = os.environ["GITHUB_TOKEN"]
    repo = os.environ["GITHUB_REPOSITORY"]
    pr = os.environ["PR_NUMBER"]

    files = gh(f"/repos/{repo}/pulls/{pr}/files?per_page=100", token) or []
    names = [f["filename"] for f in files]
    lines = ["## 🤖 Community listing check\n"]
    all_ok = True

    core_touched = [n for n in names if n != "COMMUNITY.md"]
    if core_touched:
        all_ok = False
        lines.append(f"❌ This PR touches files other than COMMUNITY.md: `{'`, `'.join(core_touched[:10])}`")
        if any(n == "SKILL.md" for n in core_touched):
            lines.append("　　⚠️ SKILL.md is a core asset and does not accept external PRs (see CONTRIBUTING.md) — please remove it from this PR")
    else:
        lines.append("✅ Only COMMUNITY.md was touched")

    added = []
    for f in files:
        if f["filename"] == "COMMUNITY.md":
            for ln in (f.get("patch") or "").splitlines():
                if ln.startswith("+") and not ln.startswith("+++"):
                    added += re.findall(r"github\.com/([\w.-]+/[\w.-]+)", ln)
    added = list(dict.fromkeys(s.rstrip(")/") for s in added))

    if not added:
        all_ok = False
        lines.append("❌ No GitHub repo link was found in the added lines")
    for slug in added[:5]:
        ok, items = check_target_repo(slug, token)
        all_ok = all_ok and ok
        lines.append(f"\n**{slug}**")
        lines += [f"- {mark} {text}" for mark, text in items]

    lines.append("\n---")
    lines.append(("✅ **Machine check passed.**" if all_ok else "❌ **Machine check failed** — please fix the items above and push an update (it reruns automatically)."))
    lines.append("Before the final merge, the maintainer will also confirm by hand: ethics red lines (CONTRIBUTING.md) + a content-quality spot check.")

    body = "\n".join(lines)
    req = urllib.request.Request(
        f"{API}/repos/{repo}/issues/{pr}/comments",
        data=json.dumps({"body": body}).encode(),
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        method="POST",
    )
    urllib.request.urlopen(req, timeout=15)
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
