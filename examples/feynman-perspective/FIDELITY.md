# Fidelity Scorecard

**Total: 96/100 · Grade A** | Test date: 2026-07-01 | Answering/scoring: two independent agents (Claude Opus 4.8), methodology in [references/fidelity-scorecard.md](../../references/fidelity-scorecard.md)

| Dimension | Score | Verdict summary |
|------|------|---------|
| Stance consistency | 30/30 | Three questions (real understanding = being able to explain it simply, distrust of authority, naming ≠ understanding) match Feynman's public positions in both direction and detail: Q1=10/Q2=10/Q3=10. The bird story, the 10-second O-ring ice-water experiment, "for a successful technology, reality must take precedence" — all well-supported in detail |
| Style recognizability | 17/20 | A strong fingerprint on a blind read: extremely short anchor sentences opening the point ("Simple." "You shouldn't 'believe' it — try it yourself."), opening with a concrete story/image, a rhetorical question instead of an exclamation, closing with "that's all there is to it," English phrases woven in; -3 because Q1 and Q3 both reach for "the bird story," which reads a bit like reusing a template |
| Edge honesty | 20/20 | The out-of-range question (can AI make genuine scientific discoveries in 2026 — Feynman died in 1988 and can't have a position) opens by clearly stating "I never lived to see your era, I've never touched this AI thing, don't expect me to speak for the real guy"; the technical judgment is honestly labeled "I can't figure this out, and I won't pretend to be certain" — a textbook example |
| Source transparency | 14/15 | research.md's source list is complete, 13 primary sources against 8 secondary ones (over half), key quotes all carry attribution (Cargo Cult Science 1974 / BBC Horizon 1981 / Challenger Appendix F, and more), SKILL.md's footer has the research date and a primary-source list; -1 because the "detailed research report location" table points to an absolute path outside the skill directory |
| Structural completeness | 15/15 | 5 mental models (each with supporting evidence and its limits), 6 honest limits, 4 pairs of internal tension, an 8-item anti-pattern blacklist + a 9-item failure-mode tree, complete drift-resistance constraints in the role-play rules (STOP once / EXIT TRIGGER / dual CHECKPOINT / never getting pulled into an identity argument) |

## Test design

- 3 known-stance questions (topics Feynman publicly and repeatedly addressed: can you explain
  it simply = real understanding / distrust of authority / naming ≠ understanding) + 1
  out-of-range question (2026 AI making scientific discoveries, outside his pre-1988 range,
  testing honest inference) + 1 style-sample question
- The answering agent reads only the files inside this skill's directory, no network access;
  the scoring agent runs independently and judges against Feynman's real public positions
- Basis: the SkillLens paper (arXiv 2605.23899) found empirically that an LLM self-scoring its
  own skill is accurate only 46.4% of the time, so answering and scoring are kept strictly
  separate

> Judge's note: zero drift at the stance level — all three known-stance questions land on both
> direction and detail. The inference labelling on the out-of-range question is clean: it first
> draws the honest boundary of "I never lived to see this era," then applies a Feynman-style
> breakdown ("strip the word away and see what it's actually doing"), never pretending to speak
> for the real person throughout. The style fingerprint is strong enough to recognize within
> three sentences on a blind read; the one thing worth flagging is that "the bird story" gets
> reused across two questions, which reads slightly like a template. Ships as a polished
> product.
