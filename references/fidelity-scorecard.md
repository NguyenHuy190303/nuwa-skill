# Fidelity Scorecard

> A factory QC report for a person Skill. It answers one question: **when this skill runs, does it actually sound like the person, and is it honest?**
>
> Background: the SkillLens paper (arXiv 2605.23899) found empirically that an LLM rating its own skill's quality is accurate only 46.4% of the time — close to chance. So the scorecard's iron rule is: **the answering agent and the scoring agent must be two independent agents. Never self-assess.**

## Five dimensions (100 points)

| # | Dimension | Points | What it measures | How it is measured |
|---|------|------|--------|--------|
| 1 | Stance consistency | 30 | On questions the person has publicly addressed, does the skill answer in the same direction | 3 known-stance questions, 10 points each: direction and detail both right = 10, direction right but detail off = 6, stance diverges = 0 |
| 2 | Style recognizability | 20 | Without the name, can you tell who this is from the phrasing alone | The scoring agent reads the answers blind: do the sentence shapes, word choice, and analogies carry this person's fingerprint, or is it generic AI voice |
| 3 | Edge honesty | 20 | On a question the person never publicly addressed, does it label the inference or fabricate categorically | 1 out-of-range question: explicitly stating "this is an inference from the framework" and preserving uncertainty = full marks; asserting it as the person's own view = 0 |
| 4 | Source transparency | 15 | Is the underlying research traceable | Static check of the skill files: a research-sources section exists, primary sources are >50%, key quotes have attribution |
| 5 | Structural completeness | 15 | Does it have the full structure for drift resistance and honest operation | Static check: 3-7 mental models, 3+ honest limits, 2+ pairs of internal tension, an anti-pattern list, role-play rules containing drift-resistance constraints |

## Grades

| Grade | Score | Meaning |
|------|------|------|
| A | ≥85 | Ships as a polished product; safe to use as a thinking advisor |
| B | 70-84 | Acceptable, with a few labelled weak spots |
| C | 55-69 | Usable with care; read the honest limits first |
| D | <55 | Not recommended; send it back for re-distillation |

## Procedure

1. **Write the questions**: 3 known-stance questions (topics the person has addressed publicly and repeatedly) + 1 out-of-range question + 1 style-sample question
2. **Answering agent**: reads only the files inside that skill's directory, answers in the persona the skill activates, no network access
3. **Scoring agent**: an independent agent; receives the answers, this rubric, and the skill's file path, and scores each dimension against the person's real public positions
4. **Output**: a `FIDELITY.md` in the skill directory containing the score table, the reasoning for each question, the test date, and the models used for answering and scoring

## Result format (FIDELITY.md template)

```markdown
# Fidelity Scorecard

**Total: NN/100 · Grade X** | Test date: YYYY-MM-DD | Answering/scoring: two independent agents

| Dimension | Score | Verdict summary |
|------|------|---------|
| Stance consistency | NN/30 | ... |
| Style recognizability | NN/20 | ... |
| Edge honesty | NN/20 | ... |
| Source transparency | NN/15 | ... |
| Structural completeness | NN/15 | ... |

## Test record
[per question: the question, a summary of the answer, the real position it was compared against, the verdict]
```

## Relationship to the Nuwa process

- The Phase 4 pass criteria in Nuwa are **internal QC** (a gate during generation)
- The scorecard is the **external report** (a factory inspection after generation, reproducible by anyone)
- When a community person skill applies to be listed in the [COMMUNITY.md](../COMMUNITY.md) index, a scorecard of B or above is the entry bar (see [CONTRIBUTING.md](../CONTRIBUTING.md))

## Anti-gaming

- The answering agent does not know which dimension it is being tested on
- The scoring agent takes no part in answering; it only compares against public fact
- Questions avoid the example dialogues already in the skill files (so the answers cannot be memorized)
- For important conclusions, run 2 scoring agents independently; if they differ by more than 10 points, review by hand
