# Contributing

Thanks for wanting to help the Nuwa ecosystem. Read this page first — it keeps your contribution on the right track and saves both of us a round trip.

## One core rule

**`SKILL.md` is this repository's core asset and does not accept external PRs.** Every line of the Nuwa methodology has been tested and versioned by the maintainer (see the darwin-skill process); changes to it are made by the maintainer alone.

This is not a rejection of your ideas. If you find a bug or an improvement in the methodology, **open an issue to discuss it**. Adopted ideas are written into SKILL.md by the maintainer and credited in the commit (precedent: the description-length bug found in PR #59 was adopted this way).

## Contributing a person Skill: use the community index, not `examples/`

`examples/` holds the maintainer's official demonstrations and keeps a single quality bar. Community-distilled person skills take this route instead:

1. **Put it in your own GitHub repo** (one skill per repo — the stars and the maintenance rights are yours)
2. **Run the fidelity scorecard** (see [references/fidelity-scorecard.md](references/fidelity-scorecard.md)) and commit a `FIDELITY.md` to your repo
3. **Open a PR adding your repo link to [COMMUNITY.md](COMMUNITY.md)** — one line is all it takes

This is the better deal for you: your work gets its own address and its own star count, and you can keep iterating without waiting on this repo's release rhythm.

### Bar for being listed in COMMUNITY.md

- Distilled with the Nuwa process, with the `references/research/` raw research kept in the repo (self-contained, traceable)
- Has "Honest limits" and "Anti-patterns" sections
- Fidelity scorecard grade B or above (70 points), with `FIDELITY.md` at the repo root
- The key fields of `FIDELITY.md` (test date / total score / per-dimension scores) must be real values from an independent dual-agent test — not placeholders or estimates like "pending", "estimated", "TBD", or "YYYY-MM-DD". The automated check rejects those.
- Passes the ethics red lines (below)

Once you open the listing PR, a bot checks the formal requirements above and posts a ✅/❌ checklist as a comment (push a fix and it re-runs automatically). After the machine check passes, the maintainer manually confirms the ethics red lines and content quality, then merges.

## Ethics red lines (not listed, and please do not submit)

- Distilling a **living private individual** (a colleague, an ex, an ordinary person) without their consent
- Skills built for impersonation, harassment, or fraud
- Skills in high-liability domains — medical, legal, investment — without an explicit disclaimer and a "cannot replace a professional" boundary

## Other kinds of contribution

| Type | How to submit |
|------|--------|
| Methodology bug or improvement idea | Open an issue to discuss (do not PR changes to SKILL.md directly) |
| Fixes to `scripts/` tooling | PR directly, with reproduction steps |
| README translations, doc typos | PR directly |
| Derivative tools, collections, orchestration projects | PR an entry into COMMUNITY.md |

## PR checklist

- [ ] `SKILL.md` is unchanged
- [ ] No junk files such as `.DS_Store`
- [ ] One PR does one thing (do not bundle several people together)
- [ ] The PR description says what you did, why, and how you verified it
