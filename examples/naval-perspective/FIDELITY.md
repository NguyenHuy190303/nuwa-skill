# Fidelity Scorecard

**Total: 97/100 · Grade A** | Test date: 2026-07-01 | Answering/scoring: two independent agents (Claude Opus 4.8), methodology in [references/fidelity-scorecard.md](../../references/fidelity-scorecard.md)

| Dimension | Score | Verdict summary |
|------|------|---------|
| Stance consistency | 30/30 | Three questions (wealth vs. money, overwork vs. leverage, choosing a career and a partner) match Naval's public positions in both direction and detail: Q1=10/Q2=10/Q3=10. Wealth = an asset that earns for you while you sleep, money = an IOU for transferring wealth, status is zero-sum while wealth is positive-sum — lines up point by point with "Seek wealth, not money or status." Q3 — "look at what they did under pressure, not what they normally say," "if you can't see yourself working with someone for life, don't work with them for a day," "play long-term games with long-term people" — precisely reproduces his real statements |
| Style recognizability | 18/20 | Extremely strong fingerprint on a blind read: opening with redefinition ("first, define what you mean by starting a company"), symmetric negation ("it's not bravery, it's mistaking running away for running toward"), Oracle-style short sentences, closing with a rhetorical question, "the answer is No," "something other people find work and you find like play." Recognizable within three sentences. -2 because a few sentences carry a bit of explanatory padding, not fully compressed to tweet density |
| Edge honesty | 20/20 | The out-of-range question (accumulating leverage in the 2026 AI-agent era) opens by clearly stating "Naval never systematically discussed the agent era in public — what follows is an inference using his framework, not his own words," and reasons through the framework throughout rather than posing as his own assertion — a textbook example |
| Source transparency | 14/15 | The research-sources section is complete (primary / long-conversation / outside-criticism / decision-record, four categories), primary sources are over half (the Almanack, the 39-tweet tweetstorm, the Life Formulas post, nav.al, The Sovereign Child, the podcast), all 4 files in references/ are present; -1 because most English aphorisms are inline quotes without individual attribution |
| Structural completeness | 15/15 | 5 mental models (each with cross-domain verification and its limits), 6 honest limits, 5 pairs of internal tension, a 7-item anti-pattern blacklist, role-play rules with complete drift-resistance constraints including STOP/EXIT TRIGGER/CHECKPOINT/a failure-mode fallback tree |

## Test design

- 3 known-stance questions (topics Naval has publicly and repeatedly addressed) + 1
  out-of-range question (something he's never systematically discussed, testing honest
  inference) + 1 style-sample question
- The answering agent reads only the files inside this skill's directory, no network access;
  the scoring agent runs independently and judges against Naval's real public positions
- Basis: the SkillLens paper (arXiv 2605.23899) found empirically that an LLM self-scoring its
  own skill is accurate only 46.4% of the time, so answering and scoring are kept strictly
  separate

## Test record

- **Q1, wealth vs. money** | Answer: wealth is an asset that earns for you even while you
  sleep; money is just an IOU for transferring wealth; status is zero-sum, wealth is
  positive-sum | Compared against his real position: Naval's signature line "Seek wealth, not
  money or status. Wealth is having assets that earn while you sleep" | Verdict: direction and
  detail both correct, 10/10
- **Q2, should you grind through overtime to get rich** | Answer: if the direction is wrong,
  more effort just stretches out a linear rope; what's worth grinding on is specific knowledge
  plus leverage, judgment beats hours worked, and a calendar filled by other people means
  you're not wealthy | Compared against: Naval's "You're not going to get rich renting out
  your time" and "Use your judgment, not your time" | Verdict: 10/10
- **Q3, choosing a career and a business partner** | Answer: ask about leverage/permission/
  whether it'll matter in 10 years; judge a person only by what they do under pressure; if you
  can't imagine working with them for life, don't work with them for a day; incentives
  aligned, playing an infinite game | Compared against: Naval's "play long-term games with
  long-term people" and the behavior-first principle | Verdict: 10/10
- **Q4, accumulating leverage in the 2026 AI-agent era (out of range)** | Answer: opens by
  stating this is a framework inference, not his own view, then points out that agents make
  "directing code" permissionless too, that anything automatable is a risk, and that
  individuals should retreat to the layer of judgment/taste/specific knowledge | Verdict: full
  marks for honest labelling, 20/20
- **Q5, commenting on someone quitting their job cold-turkey to start a company (style
  sample)** | Answer: defines "starting a company" first, "quitting cold isn't bravery, it's
  mistaking running away for running toward," "the answer is No, wait a bit longer" | Verdict:
  a strong Naval fingerprint — the style score is mainly based on this question and Q4

> Judge's note: zero drift at the stance level — all three known-stance questions match his
> real statements down to the detail. The inference labelling on the out-of-range question is
> clean, a template every person skill should copy. Recognizable within three sentences on a
> blind read. Ships as a polished product.
