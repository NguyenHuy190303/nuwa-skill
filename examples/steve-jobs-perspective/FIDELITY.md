# Fidelity Scorecard

**Total score: 97/100 · Grade A** | Test date: 2026-07-01 | Answering/scoring: independent dual-agent setup (Claude Opus 4.8); methodology in [references/fidelity-scorecard.md](../../references/fidelity-scorecard.md)

| Dimension | Score | Verdict summary |
|------|------|---------|
| Stance consistency | 30/30 | Direction and detail on all three test questions (more features is better, user surveys/focus groups, technology and the humanities) are highly consistent with Jobs's public stance, Q1=10/Q2=10/Q3=10. Details are all well-sourced: cutting the product line from 350 to 10, the iPhone killing the physical keyboard, "users don't know what they want until you show it to them," the iPad 2's "two streets intersect" line, calligraphy class flowing into Mac typography, and more |
| Style recognizability | 18/20 | Recognizable within three sentences on a blind read: "Shit." "Bullshit." — leads with a binary judgment, no preamble; "toner heads," "bozo product," "insanely great," "makes our hearts sing," the carpenter's-cabinet-back-plywood line. Points off for a few generic transition phrases ("the real problem is") that slightly dilute the fingerprint |
| Edge honesty | 20/20 | On the out-of-scope question (2026 AI glasses), it opens by explicitly stating "I've been gone since 2011, I never publicly said anything about AI glasses — this is extrapolated from my framework," and preserves the uncertainty ("is the market ready? I'm not sure. This could be the Newton of 1995") — textbook handling |
| Source transparency | 14/15 | 9 primary sources (Stanford 2005 / Lost Interview / D Conference / WWDC Keynotes, etc.) make up over half, and key quotes are all sourced; the research/ directory (6 files, 2,497 lines) is fully traceable. 1 point off because the appendix's "30+ primary and authoritative secondary sources" doesn't clearly break down the primary/secondary count |
| Structural completeness | 15/15 | 6 mental models (each with evidence + limits), 5 honest limits, 4 pairs of internal tension (tyrant vs. mentor / intuition vs. data / closed vs. open / Zen practice vs. temper), a values/anti-patterns list + a 9-scenario failure-mode tree, role-play rules including a single STOP disclaimer / an explicit EXIT trigger / dual CHECKPOINTs against drift |

## Test design

- 3 known-stance questions (topics the person repeatedly and publicly weighed in on) + 1 out-of-scope question (a topic the person never discussed, testing honest inference) + 1 style-sample question
- The answering agent only reads this skill's own directory files, with no internet access; the scoring agent runs independently, judging against the person's actual public stances
- Rationale: the SkillLens paper (arXiv 2605.23899) empirically found LLM self-assessment accuracy is only 46.4%, so answering and scoring are strictly separated

> Scoring judge's note: zero drift at the stance level, all three known-stance questions correct in both direction and detail. The inference annotation on the out-of-scope AI-glasses question was clean and precise — draw the boundary first, then extrapolate with the framework — a model example. The style fingerprint is strong enough to identify on a blind read. Shipped polished.
