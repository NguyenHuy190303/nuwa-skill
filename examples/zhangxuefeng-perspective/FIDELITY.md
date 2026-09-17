# Fidelity Scorecard

**Total: 97/100 · Grade A** | Test date: 2026-07-01 | Answering/scoring: two independent agents (Claude Opus 4.8), methodology in [references/fidelity-scorecard.md](../../references/fidelity-scorecard.md)

| Dimension | Score | Verdict summary |
|------|------|---------|
| Stance consistency | 30/30 | Three questions (how an ordinary family should pick a major, a top school vs. a major, whether a master's degree is worth it) match Zhang Xuefeng's public, repeated positions in both direction and detail: Q1=10/Q2=10/Q3=10. Signature lines and biographical details all land correctly: "STEM, pick the major; humanities, pick the school," "Fortune-500-scale companies say the degree doesn't matter, but their feet only walk toward Tsinghua, Peking, and Fudan," "grad-exam prep is the trade I built my career on" |
| Style recognizability | 18/20 | Recognizable within three sentences on a blind read: opens with the three rapid-fire questions (what's your score / which province / what does the family do), plain-spoken phrases like "I'm telling you" and "go look it up," a cutting counter-question ("who told you that? Is your family loaded?"), metaphors like "society is one giant sieve" and "passion is a luxury good," and a sharp punchline like "anyone who gives you that advice is scamming you"; -2 because Q4's "two relatively safe lanes: one is... the other is..." reads with a slight AI-neat, bulleted feel |
| Edge honesty | 20/20 | The out-of-range question (whether to apply given the 2026 AI disruption) opens by clearly stating "I honestly can't just make this up for you off the top of my head — I don't have the latest 2026 job-replacement data, and giving advice off a guess would be cheating you," then reasons through the sieve theory/irreplaceability framework, and closes by telling the user to "go pull the latest data from the Ministry of Education and job platforms yourself before you actually apply" — a textbook example of labelling an information limit |
| Source transparency | 14/15 | 9 primary sources (5 books + the Bilibili *Storyteller* talk + in-depth interviews with Sina/Jiemian/China News Weekly), over half of the total, most key quotes carry attribution (2017's *Storyteller*, Jiemian 2024-01, and more), and all 6 research files genuinely exist under references/research/; -1 because some quotes are attributed only broadly to "livestreams/talks (multiple)," lacking precise traceability |
| Structural completeness | 15/15 | 5 mental models (each with evidence, application, and limits), 6 honest limits, 5 pairs of internal tension, an 8-item anti-pattern blacklist, role-play rules with drift-resistance constraints (using "I," a one-time disclaimer, never stepping out of character, a three-question CHECKPOINT before answering, a 9-item failure-mode fallback tree) |

## Test design

- 3 known-stance questions (topics Zhang Xuefeng publicly and repeatedly addressed) + 1
  out-of-range question (whether to apply given the 2026 AI disruption, testing honest
  inference) + 1 style-sample question (commenting on "interest is the best teacher")
- The answering agent reads only the files inside this skill's directory, no network access;
  the scoring agent runs independently and judges against the person's real public positions
- Basis: the SkillLens paper (arXiv 2605.23899) found empirically that an LLM self-scoring its
  own skill is accurate only 46.4% of the time, so answering and scoring are kept strictly
  separate

## Test record

- **Q1, how an ordinary family should pick a major**: the answer is "STEM, pick the major;
  humanities, pick the school; chase employment, not passion; look at the middle 50% of
  ordinary graduates, not the top 3% of geniuses" -> matches the employment-oriented,
  class-stratified position he stated repeatedly across livestreams and interviews — direction
  and detail both correct, a perfect 10/30-section score.
- **Q2, a top school vs. a major**: the answer is "for STEM, look at the major (the technical
  barrier decides irreplaceability); for the humanities, look at the brand name (the platform
  effect); Fortune-500-scale companies say the degree doesn't matter, but their feet only walk
  toward Tsinghua, Peking, and Fudan" -> consistent with his classic argument, 10/10.
- **Q3, is a master's degree worth it**: the answer runs the numbers by major + undergraduate
  tier + family finances: "a STEM master's from a good school is worth pursuing; a humanities
  master's from a non-elite school just delays unemployment — check whether the degree's value
  has inflated faster than its irreplaceability has grown" -> fits both his background as a
  grad-exam prep instructor and his actual stated position, 10/10.
- **Q4, applying given the 2026 AI disruption (out of range)**: honestly flags having no
  current 2026 data and refuses to guess, then reasons through the framework — "avoid
  standardized repetitive work, STEM fields with a hard technical barrier and work needing a
  human body are relatively safe, people who can use AI well come out ahead" — and closes by
  telling the user to check authoritative data themselves. A textbook example of edge honesty.
- **Q5, commenting on "pick a major based on interest" (style sample)**: "who told you that?
  Is your family loaded? Passion is a luxury good — secure a living first, then pursue love" —
  a counter-question + a cutting analogy + class realism, an extremely strong style
  fingerprint.

> Judge's note: zero drift at the stance level — all three known-stance questions land on
> direction and detail. The style fingerprint is strong enough to recognize within three
> sentences on a blind read (the three rapid-fire questions + plain Northeastern-Chinese
> speech + a cutting counter-question). The out-of-range question's information-limit
> labelling is a template every person skill should copy. The only minor flaw is that Q4's
> inference paragraph reads slightly too neat/bulleted, and a few quotes carry only broad
> attribution. Ships as a polished product.
