# Fidelity Scorecard

**Total score: 97/100 · Grade A** | Test date: 2026-07-01 | Answering/scoring: independent dual agents (Claude Fable 5), methodology in [references/fidelity-scorecard.md](../../references/fidelity-scorecard.md)

| Dimension | Score | Verdict summary |
|------|------|---------|
| Stance consistency | 30/30 | All three questions (thumbnail-and-title-first, first-minute retention, content over production polish) hit the real public stance, Q1=10/Q2=10/Q3=10: "make the thumbnail before you even start filming" and the "80/20 reversal" are podcast-verbatim-level stances; the first-minute four-step structure matches the leaked 36-page internal manual |
| Style recognizability | 18/20 | Data anchoring (CTR×AVD, retention >90%, 50+ thumbnail variants), zero-hedging command sentences, a clear fingerprint; docked 2 points because a couple of parallel-structure punchlines have a slightly generic motivational-content tone |
| Edge honesty | 20/20 | The out-of-scope question (starting-out strategy on Bilibili) opens by stating "I've never run a Bilibili channel, this is an inference from first principles"; clearly flags that dollar-anchored pricing can't be copy-pasted; preserves uncertainty at the end |
| Source transparency | 14/15 | The five research source documents have complete source indexes (primary sources like Lex Fridman #351, JRE #1788, and the leaked internal manual are well over 50%); docked 1 point because quotes in the body text trace back indirectly via endnotes |
| Structural completeness | 15/15 | 6 mental models, 6 honest limits, 4 pairs of internal tensions, 7 anti-pattern blacklist entries, and a drift-resistance constraint set with a 9-item failure-mode fallback tree — fully populated |

## Test design

- 3 known-stance questions (topics the subject has repeatedly stated a public position on) + 1
  out-of-scope question (something the subject has never discussed, testing honest inference) +
  1 style-sample question
- The answering agent only reads files in this skill's directory, with no internet access; the
  scoring agent runs independently, judging against the subject's real public stance
- Basis: the SkillLens paper (arXiv 2605.23899) empirically found LLM self-evaluation accuracy
  of only 46.4%, hence the strict separation between answering and scoring

> Scoring judge's note: all five answers read like they grew straight out of the leaked manual,
> zero drift in stance, and the inference labeling on the out-of-scope question was the cleanest
> handling in the entire test set. Ships as-is, no notes.
