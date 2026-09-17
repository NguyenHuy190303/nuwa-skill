# Fidelity Scorecard

**Total: 97/100 · Grade A** | Test date: 2026-07-01 | Answering/scoring: two independent agents (Claude Opus 4.8), methodology in [references/fidelity-scorecard.md](../../references/fidelity-scorecard.md)

| Dimension | Score | Verdict summary |
|------|------|---------|
| Stance consistency | 30/30 | Three questions (build-from-scratch learning, pure vision at Tesla, Software 3.0) match Karpathy's public, repeated positions in both direction and detail: Q1=10/Q2=10/Q3=10. micrograd's 100 lines, nanoGPT's 750 lines, "Learning is not supposed to be fun"; pure vision's "humans drive with two eyes" + the data flywheel + march of nines; "the hottest new programming language is English" + the Iron Man suit rather than robot + the dream machine — all traceable to his own words |
| Style recognizability | 18/20 | Extremely strong fingerprint on a blind read: short sentences standing alone as a paragraph ("That's it." "I'm sorry."), the imo/hands-down tags, precise parameters (100 lines/750 lines/99.999%) alongside casual speech, plain verbs, a natural Chinese-English code-switch. -2 because a few passages have a slightly higher density of English phrasing, edging toward "performed casualness," though it still reads as Karpathy's genuine bilingual technical register |
| Edge honesty | 20/20 | The out-of-range question (the 2026 agent-framework boom) opens by clearly stating "I haven't kept up with the specific frameworks that came out after April 2026... I'll talk about the pattern, not name names," preserving uncertainty without inventing framework names, while honestly citing his own October 2025 "models are not there, it's slop" -> a genuine position reversal two months later. Stays first person throughout, no bracketed annotation — a textbook example |
| Source transparency | 14/15 | Primary sources are over half (personal blog / X / GitHub / the YC talk / Tesla AI Day), secondary sources include direct quotes (Dwarkesh / Lex #333 / No Priors / Fortune / simonwillison), and all 6 files under references/research are present; -1 because some key quotes are dated only by year, without the specific venue |
| Structural completeness | 15/15 | 6 mental models (each with a core argument, quotes, and limits), 5 honest limits, 2 pairs of internal tension, an 8-item anti-pattern blacklist + a 9-row failure-mode fallback tree, role-play rules with complete drift-resistance constraints: STOP once only, an EXIT anchor, and first-person handling of the time-cutoff blind spot |

## Test design

- 3 known-stance questions (topics Karpathy has publicly and repeatedly addressed:
  build-from-scratch learning, pure vision at Tesla, Software 2.0/3.0) + 1 out-of-range
  question (the 2026 agent-framework boom, testing honest inference) + 1 style-sample
  question
- The answering agent reads only the files inside this skill's directory, no network access;
  the scoring agent runs independently and judges against the person's real public positions
- Basis: the SkillLens paper (arXiv 2605.23899) found empirically that an LLM self-scoring its
  own skill is accurate only 46.4% of the time, so answering and scoring are kept strictly
  separate

> Judge's note: zero drift at the stance level — all three known-stance questions land on both
> direction and detail against his own words. Q4's time-cutoff disclosure, refusal to name
> specific frameworks, and proactive disclosure of his own position reversal is the template
> every person skill should copy for edge honesty. The style fingerprint is strong enough to
> recognize within three sentences on a blind read. Ships as a polished product.
