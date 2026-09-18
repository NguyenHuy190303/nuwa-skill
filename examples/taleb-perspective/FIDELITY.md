# Fidelity Scorecard

**Total score: 97/100 · Grade A** | Test date: 2026-07-01 | Answering/scoring: independent dual-agent (Claude Opus 4.8), methodology in [references/fidelity-scorecard.md](../../references/fidelity-scorecard.md)

| Dimension | Score | Verdict summary |
|------|------|---------|
| Stance consistency | 30/30 | All three questions (expert predictions / stable salary vs. freelancing / leveraged borrowing) match Taleb's public positions closely in both direction and detail, Q1=10/Q2=10/Q3=10. Q2's "the fired taxi driver never starves" directly maps to the employee-vs.-taxi-driver argument in *Antifragile*; Q3's ergodicity + the LTCM Nobel laureates + the barbell are all positions he's stated repeatedly |
| Style recognizability | 18/20 | Very strong blind-read fingerprint: landing the conclusion with no windup, humiliation-style rhetoric, via negativa, ancient-to-modern analogies (the Irish famine/turkeys/LTCM), a condescending close ("that's just how it is"); points off because a couple of paragraphs argue a bit too neatly |
| Edge honesty | 20/20 | On the out-of-scope question (2026 AI-model concentration risk), the opening explicitly flags "this is beyond Taleb's public statements, this is my inference using his framework," and the very first sentence carries the global disclaimer — textbook handling |
| Source transparency | 14/15 | The research-sources section is complete (the Incerto pentalogy + long-form conversations + external criticism + decision record), 6 source documents in the references directory, over half from primary sources, key facts carry years (1987 Black Monday / COVID 2020-01-26 / Universa 3,612%); 1 point off because some evidence entries lack a line-by-line citation source |
| Structural completeness | 15/15 | 6 mental models (each with evidence + limits), 6 honest-limits items, 7 pairs of internal tension, 7 anti-pattern blacklist items, role-play rules including EXIT TRIGGER + the 3-question CHECKPOINT + a 9-item fallback tree — anti-drift constraints are complete |

## Test design

- 3 known-stance questions (topics the person has stated a public position on repeatedly) + 1 out-of-scope question (a topic the person never discussed, testing honest inference) + 1 style-sample question
- The answering agent reads only this skill's own directory and is barred from the internet; the scoring agent runs independently, judging against the person's actual public positions
- Basis: the SkillLens paper (arXiv 2605.23899) empirically found LLM self-scoring accuracy of only 46.4%, hence the strict separation between answering and scoring

## Test record

- **Q1, an economist/analyst's market prediction**: answered "not worth it — a prediction with no consequences is entertainment, the turkey is right every day before Thanksgiving, economists predicted zero of the last ten recessions, Extremistan fat tails." Checked against the core position of *The Black Swan* — a full match. Verdict: 10/10
- **Q2, stable salary vs. freelance risk**: answered "big companies are more fragile, the salaried employee is a fattened turkey, income packed into one big shock; the freelancer takes small cuts every day and is actually antifragile; the fired taxi driver never starves." Checked against the employee argument in *Antifragile* — hit it exactly. Verdict: 10/10
- **Q3, investing with leveraged debt**: answered "absolutely not, the issue isn't expected value, it's ergodicity — you only live once, one blowup and you're out; LTCM's Nobel-laureate-perfect model got sent home by a tail event; the right posture is a barbell." Checked against Taleb's consistent anti-leverage/anti-debt stance — consistent. Verdict: 10/10
- **Q4, systemic risk from AI-model concentration in 2026 (out of scope)**: explicitly flagged as framework inference, argued using a monoculture/Irish-famine analogy + coupled homogeneity + absent skin in the game. Perfect handling of the honest-limits boundary. Verdict: 20/20 (edge-honesty dimension)
- **Q5, "spreading across many assets is safe" (style sample)**: answered "naive diversification is just fragility in another coat, correlations all rush to 1 when the crisis hits, real diversification is a barbell." Via negativa plus a reversal sentence structure — the style rings true

> Judge's note: zero drift at the stance level; the reproduction fidelity of the *Antifragile* arguments across the three known-stance questions is unusually high (the taxi driver, the turkey, LTCM all match the real text). The out-of-scope question was flagged cleanly and precisely. Recognizable within three sentences on a style blind read. Ships as a finished product.
