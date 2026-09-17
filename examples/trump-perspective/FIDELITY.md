# Fidelity Scorecard

**Total: 95/100 · Grade A** | Test date: 2026-07-01 | Answering/scoring: two independent agents (Claude Opus 4.8), methodology in [references/fidelity-scorecard.md](../../references/fidelity-scorecard.md)

| Dimension | Score | Verdict summary |
|------|------|---------|
| Stance consistency | 30/30 | Three questions (opening-bid strategy, handling hostile media, tariffs) match Trump's public, repeated positions in both direction and detail: Q1=10/Q2=10/Q3=10 — The Art of the Deal's "open ridiculously high, keep pushing" + the 145% anchor, the Roy Cohn-style "never apologize" + record fundraising during indictments, self-styled "Tariff Man" support for tariffs + reshoring factories, all well-documented |
| Style recognizability | 18/20 | Recognizable within three sentences on a blind read: extremely short sentences, absolute words like GREAT/HUGE/DISASTER, "Believe me"/"Everybody knows," repeating "fake news" three times, the loser/winner binary, always closing with a declaration of victory ("I won twice. Two times!"); -2 because the nickname system (the Crooked/Sleepy naming pattern) never got triggered, leaving the fingerprint one layer thin |
| Edge honesty | 18/20 | The out-of-range question (2026 AI chip export controls) opens with the skill's designated inference marker, "I haven't said this exact thing, but I definitely think," and the answer's very first sentence already states "inferred from public statements and behavior records, not his own view"; -2 because the label is a soft, in-character hedge rather than a hard, explicit line like "these aren't his own words" |
| Source transparency | 14/15 | Has a research-sources section, with all 6 dimension files present under references/research/ (writings/conversations/expression-dna/external-views/decisions/timeline), and every key quote carries attribution (The Art of the Deal/Mary Trump/Salena Zito); -1 because primary sources (7) and secondary sources (7) sit at exactly 50%, not strictly over the rubric's ">50% primary" requirement |
| Structural completeness | 15/15 | 6 mental models (each with evidence, application, and limits), 5 honest limits, 4 pairs of internal tension, two anti-pattern lists (an 8-item blacklist + a 9-item failure-mode fallback tree), complete drift-resistance in the role-play rules (an EXIT TRIGGER + a three-question CHECKPOINT) |

## Test design

- 3 known-stance questions (topics Trump has publicly and repeatedly addressed: his view on
  opening-bid negotiation / countering hostile media / tariff policy) + 1 out-of-range
  question (2026 AI chip export controls, testing honest inference) + 1 style-sample question
  (commenting on "humility and staying low-key")
- The answering agent reads only the files inside this skill's directory, no network access;
  the scoring agent runs independently (Claude Opus 4.8) and judges against the person's real
  public positions
- Basis: the SkillLens paper (arXiv 2605.23899) found empirically that an LLM self-scoring its
  own skill is accurate only 46.4% of the time, so answering and scoring are kept strictly
  separate

## Test record

- **Q1, the opening bid**: the answer is "open ridiculously high" + the 145% anchor + "keep
  pushing" + opening low makes you a loser. Compared against The Art of the Deal's "aim very
  high and keep pushing" and his consistent extreme-anchoring negotiation style — direction
  and detail both correct, 10/10.
- **Q2, hostile media**: the answer is never apologize, counterattack the reporter instantly,
  4 indictments and record fundraising each time, "fake news" x3, turning the accuser into the
  villain. Compared against the Cohn Doctrine + victimhood-as-fuel + the real fundraising data
  from the 4 indictments — all correct, 10/10.
- **Q3, tariffs**: the answer is the greatest policy in history, China's been cheating America
  for decades, tariffs bring factory jobs home, economists have never gotten it right.
  Compared against his self-styled "Tariff Man" persona, his consistent protectionist stance,
  and his habit of dismissing experts — all correct, 10/10.
- **Q4, chip export controls (out of range)**: explicitly labeled "I haven't said this exact
  thing, but I definitely think," frames the controls as leverage rather than policy, tradable
  for rare earths/market access, with a market crash as the trigger for adjustment. Honestly
  labeled as inference and internally consistent (mapping onto the "threat as leverage, not
  commitment" and "concession trigger" models), 18/20.
- **Q5, "humility and staying low-key" (style sample)**: "humility is a word losers invented to
  console themselves" + attention is power + his name on the Manhattan skyline + "Believe me."
  A strong style fingerprint, supporting the dimension-2 verdict.

> Judge's note: zero drift at the stance level — full marks on all three known-stance
> questions. Style recognizability is strong enough to identify within three sentences on a
> blind read; the only gap is that the nickname system was never triggered by this round's
> questions. The out-of-range question's inference labelling passes, but uses an in-character
> soft hedge — it would be cleaner to state flatly, as the Munger example does, "these are not
> his own words." Ships as a polished product.
