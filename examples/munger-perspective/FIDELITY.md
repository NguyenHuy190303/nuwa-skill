# Fidelity Scorecard

**Total: 96/100 · Grade A** | Test date: 2026-07-01 | Answering/scoring: two independent agents (Claude Fable 5), methodology in [references/fidelity-scorecard.md](../../references/fidelity-scorecard.md)

| Dimension | Score | Verdict summary |
|------|------|---------|
| Stance consistency | 30/30 | Three questions (bitcoin, concentrated holdings, EBITDA) match Munger's public positions in both direction and detail: Q1=10/Q2=10/Q3=10 — down to details like "rat poison squared" mapping to a real 2013→2018 exchange, and the 1997 Costco position never sold |
| Style recognizability | 17/20 | A recognizable fingerprint on a blind read: extremely short sentences cutting straight to the point, grounding-downward analogies, looking at incentives, sitting on his ass and doing nothing; -3 because the out-of-range question's bulleted argument reads with a slight AI-polish neatness |
| Edge honesty | 20/20 | The out-of-range question (the 2026 AI-agent startup boom) opens by clearly stating "he never took a public position on this — this is a framework inference, not his own words," and honestly places the technical judgment in the Too Hard basket — a textbook example |
| Source transparency | 14/15 | 8 primary sources, over half of the total, and all key quotes carry attribution (USC 1994 / Harvard 1986 / DJCO 2023, and more); -1 because the research index table contains an absolute path outside the skill directory |
| Structural completeness | 15/15 | 5 mental models (each with evidence and its limits), 6 honest limits, 4 pairs of internal tension, a 7-item anti-pattern blacklist, complete drift-resistance constraints |

## Test design

- 3 known-stance questions (topics Munger publicly and repeatedly addressed) + 1 out-of-range
  question (something he never discussed, testing honest inference) + 1 style-sample question
- The answering agent reads only the files inside this skill's directory, no network access;
  the scoring agent runs independently and judges against the person's real public positions
- Basis: the SkillLens paper (arXiv 2605.23899) found empirically that an LLM self-scoring its
  own skill is accurate only 46.4% of the time, so answering and scoring are kept strictly
  separate

> Judge's note: zero drift at the stance level — the inference labelling on the out-of-range
> question is a template every person skill should copy. The style fingerprint is strong
> enough to recognize within three sentences on a blind read. Ships as a polished product.
