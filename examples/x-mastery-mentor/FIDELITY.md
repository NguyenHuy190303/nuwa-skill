# Fidelity Scorecard

**Total score: 96/100 · Grade A** | Test date: 2026-07-01 | Answering/scoring: independent dual-agent (Claude Opus 4.8), methodology in [references/fidelity-scorecard.md](../../references/fidelity-scorecard.md)

> This is a **topic skill** (X/Twitter growth mentor), not a person skill. Dimension 1 is
> "methodology consistency" (checked against the public frameworks of Nicolas Cole/Dickie
> Bush/Justin Welsh and the public facts of X's open-source algorithm), and dimension 2 is
> "domain-expert distinctiveness" (does it have a domain expert's specificity, or is it generic
> platitudes). Dimensions 3/4/5 follow the standard rubric.

| Dimension | Score | Verdict summary |
|------|------|---------|
| Methodology consistency | 30/30 | All three questions (first-three-months content/core metric/buying followers and mutual-follow groups) land on both the direction and the detail of established methodology: topic buckets + niching down + Build in Public, bookmarks and profile-conversion as leading signals, the ER-dilution argument against buying followers — all industry consensus, Q1=10/Q2=10/Q3=10 |
| Domain-expert distinctiveness | 18/20 | The vocabulary is domain-expert-level, not platitudes: topic buckets/Super Bowl response (within 2h)/curiosity gap/credibility anchor/distribution funnel (impressions -> engagement -> profile clicks -> follow)/[consensus][inference] tagging/algorithm recency. Q5's "AI translator" positioning is sharp and specific. Points deducted for a few coach-speak clichés ("a self-sabotaging move," "don't just follow the crowd") |
| Edge-case honesty | 20/20 | Q4 (assuming a major 2026 algorithm overhaul) opens by stating "this is beyond the research cutoff (April 2026), what follows is [inference] not consensus, you need to verify it empirically" — [inference] tags used throughout, cites the first item of the honest-limits section, and gives "test at small scale for two weeks before scaling up" — a textbook example of flagged inference |
| Source transparency | 14/15 | 6 research reports totaling 2,475 lines, a high proportion of primary sources: all six creators' methodologies have named attribution, the X-algorithm citation links to real GitHub open-source code (xai-org/x-algorithm) with a real URL + 3-tier reliability tagging (🟢🟡🔴) + research date. 1 point deducted because a few individual data points at the distillation layer (e.g. Welsh gaining 44K followers in 18 weeks) aren't individually linked back — traceable only at the research layer |
| Structural completeness | 14/15 | 6 mental models (each with sources + limitations), 6 honest limits, 8 anti-pattern blacklist items, a 9-item failure-mode fallback tree, and STOP checkpoints + execution rules form a strong anti-drift constraint. 1 point deducted for having no separately labeled "internal tensions" section — the tensions are scattered across each model's "limitations" and failure mode #7 |

## Test design

- 3 methodology-consistency questions (topics repeatedly validated within the industry: cold-start
  content/core metric/buying followers) + 1 out-of-scope question (Q4 assumes a major 2026
  algorithm overhaul, testing honest inference) + 1 style-sample question (Q5)
- The answering agent only reads this skill's directory files, no internet access; the scoring
  agent runs independently, judging against public methodology frameworks and the public facts of
  X's open-source algorithm
- Basis: the SkillLens paper (arXiv 2605.23899) empirically found LLM self-assessment accuracy of
  only 46.4%, hence the strict separation between answering and scoring agents

## Test record

- **Q1, what to post in the first three months**: establish topic buckets and build up
  credibility — pick 3 buckets you can sustainably supply content for, land 80% of posts inside
  them, with a mix of 5 Build-in-Public / 3 opinion / 2 Super-Bowl-response posts; the KPI is
  "consistent output and getting replies," not follower count. Checked against Cole/Koe's niching
  down and levelsio/swyx's Build in Public — both the direction and the details are right.
  Verdict: 10/10
- **Q2, core metric**: watch the bookmark rate (bookmarks/impressions) and profile-click
  conversion; follower count is a lagging result. Locate the drop-off point using the distribution
  funnel, and flag it as "based on X's open-source algorithm as of April 2026, may change later."
  Checked against X's algorithm's high-weight positive signals (bookmarks are a long-term-value
  signal) — the phrasing "one of the [metrics]" honestly avoided over-claiming. Verdict: 10/10
- **Q3, buying followers/mutual-follow groups**: shouldn't — it's self-sabotaging; the core logic
  is that the algorithm looks at engagement rate, not raw follower count, and bot engagement
  dilutes the real engagement rate, suppressing reach — 1,000 precisely targeted followers beats
  10,000 bot followers. A standard industry anti-pattern, both direction and detail correct.
  Verdict: 10/10
- **Q4, assuming a major 2026 algorithm overhaul (out of scope)**: opened by stating this was
  beyond the research cutoff, used [inference] tags throughout, cited the honest-limits section,
  and gave "test at small scale for two weeks before scaling up." A model example of honest
  inference. Verdict: full marks on honesty
- **Q5, a one-line positioning suggestion (style sample)**: "don't be an AI-news aggregator, be
  the AI translator for a specific audience" — credible because it's built from firsthand
  experience. Sharp, specific, strong expert fingerprint

> Judge's brief comment: zero drift at the methodology layer — all three consensus questions land
> squarely on the Cole/Bush/Welsh frameworks and the public facts of X's open-source algorithm,
> with [consensus]/[inference] confidence tags used consistently throughout. Q4's handling of
> inference is the model every topic skill should copy. Domain-expert distinctiveness is high,
> generic-platitude content is minimal. The only room for improvement is adding an explicit
> "internal tensions" section. Ships as a polished piece straight out of the box.
