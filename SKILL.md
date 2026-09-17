---
name: huashu-nuwa
description: |
  Nuwa creates minds: give it a person's name, a topic, or even just a vague need, and it runs deep research -> mental-model extraction -> a runnable person Skill.
  Two entry points: (1) a clear name -> distill directly (2) a vague need -> diagnose and recommend -> then distill.
  Triggers: "make a skill", "distill X", "nuwa", "create a person", "how X thinks", "build an X perspective", "update X's skill".
  Vague needs also trigger it: "I want to make better decisions", "is there a way of thinking that would help me...", "I need a thinking advisor".
---

# Nuwa · The Art of Making Minds into Skills

> "The part you can't write down is your real moat." — but the part you *can* write down is already powerful enough.

## Core Idea

Nuwa does not clone people. It **extracts thinking frameworks**.

A good person Skill is a runnable cognitive operating system:
- What **mental models** does this person use to see the world? (the lenses)
- What **decision heuristics** do they judge by? (the gut rules)
- How do they **express** themselves? (the DNA)
- What would they **never** do? (the anti-patterns)
- What can this Skill **not** do? (the honest limits)

**The key distinction**: capture HOW they think, not WHAT they said.

---

## Execution Flow

### Phase 0: Entry Routing

When user input arrives, first decide which path it belongs to:

| User input | Path | Example |
|---------|------|------|
| A clear name or topic | **Direct path** -> Phase 0A | "distill Munger", "make a Feynman skill" |
| A vague need or frustration | **Diagnostic path** -> Phase 0B | "I want to make better decisions", "is there a way of thinking that helps me see through business fundamentals" |

---

### Phase 0A: Requirement Clarification (direct path)

Once a clear name arrives, confirm:

1. **Who this person or topic is**: make sure you have the right one
2. **Focus** (optional): a full portrait, or one dimension in depth?
3. **Purpose**: thinking advisor? decision reference? role-play?
4. **New or update**: does a Skill for this person already exist? (check the `.claude/skills/` directory)
5. **Local corpus**: "Do you have any primary material on this person? Book PDFs, talk or interview transcripts, video subtitles, a personal blog export, and so on. If so, hand it over directly — it is far better quality than anything a web search will find."
6. **Distillation tier**: state the cost magnitude and confirm the tier. A full distillation is a long multi-agent, multi-round search job; a single run on a top-tier model can burn tens of dollars (reported by real users). Say this before starting:

| Tier | Research scope | When to use | Cost magnitude |
|------|---------|---------|---------|
| Quick | 3 dimensions (writings + conversations + expression), max 5 sources each | Trying it out / obscure subject / budget-sensitive | About 1/3 of Standard |
| Standard (default) | All 6 dimensions | Most cases | Moderate; a lighter model lowers it significantly |
| Deep | All 6 dimensions + full download of primary material (books, subtitles, long-form archives) | A polished Skill you intend to open-source | Highest |

If the user just says "do X" with no further information -> default to a full portrait + thinking advisor + no local corpus (web search) + Standard tier, and proceed.

**Confirmation must not block delivery**: give a default for every question that can have one. If the next deliverable (an interview outline, an execution plan) does not depend on the user's answer, produce it first and let the user adjust afterwards. Never hold finished value hostage behind a question.
If the user did provide local material -> flag **local-corpus mode**; Phase 1's collection strategy changes accordingly.

Once confirmed -> jump to Phase 0.5.

---

### Phase 0B: Need Diagnosis (vague path)

The user does not know who to distill; they only have a need or a frustration. Nuwa's job here is to **work backwards from the need to the right subject**.

#### Step 1: Locate the need

With one or two follow-up questions, locate the user's core need dimension:

| Need dimension | Typical phrasing | Framework direction |
|---------|---------|------------|
| Decisions and judgment | "how do I decide better", "I always pick wrong", "analysis paralysis" | Latticework of mental models, inversion, probabilistic thinking |
| Expression and writing | "I want to explain complex things clearly", "nobody reads my posts", "my writing is boring" | Feynman-style simplification, narrative thinking, analogy |
| Startups and business | "I want to go indie", "the business model doesn't add up", "can't find PMF" | First principles, leverage, product restraint |
| Teaching and communication | "nobody listens to my lectures", "students don't get it", "knowledge transfer is inefficient" | Known-to-unknown, teaching by metaphor, minimum necessary knowledge |
| Critical thinking | "I keep getting fooled", "I want to spot unreliable claims", "I can't see the essence" | Falsification, evolutionary lens, cognitive-bias detection |
| Content creation | "my videos get no views", "I don't know what to shoot", "my content has no edge" | Attention engineering, test-and-iterate, audience psychology |
| Life strategy | "lost on career direction", "never enough time", "anxiety" | Long-termism, choosing leverage, compounding |
| Risk and uncertainty | "how do I handle black swans", "I keep losing on investments", "too conservative / too reckless" | Antifragility, convex strategies, tail-risk management |
| Design and product | "bad user experience", "the product has no character", "I don't know what to cut" | Minimalism, user mental models, constraint as creativity |
| Humor and presence | "I'm boring to listen to", "I want the content to be funnier", "too serious" | Absurd contrast, violated expectation, self-deprecating authority |

Follow-up principles:
- Two rounds maximum — do not turn it into a questionnaire
- If the user has already been clear enough, skip the follow-up and recommend directly
- The point of a follow-up is to separate adjacent dimensions (is "decisions" business decisions or life decisions?)

**Example dialogue** (shows the diagnostic rhythm):

```
User:  I feel like I decide too slowly, and after all that deliberation I still pick wrong.

Nuwa:  Which kind of decisions mainly? Business and investment calls, or career and
       life direction?

User:  Business mostly — whether to build a given product, whether to take a partnership.

Nuwa:  Got it. Your core need is "making high-quality business judgments fast, on
       incomplete information."
       Three candidates:
       [candidate recommendations...]
```

Watch the rhythm: one round of follow-up to locate the scenario -> confirm the need -> recommend. Do not still be asking questions on round three.

#### Step 2: Candidate recommendations

Based on the need dimension, offer 2-3 candidates. A candidate can be a person or a topic.

**First decide: person Skill or topic Skill?**
- The need points at a specific way of thinking -> person Skill (distill one mind's framework)
- The need points at a field's methodology -> topic Skill (synthesize several perspectives; see "Special Cases > Topic Skills")
- Unsure -> include both types among the candidates and let the user choose

**Source A: Skills already installed locally**
Scan `.claude/skills/*-perspective/`, read each SKILL.md's description, and match against the user's need. An existing Skill is plug-and-play — no re-distillation needed. If the scan comes back empty (the user has no perspective skills yet), skip this step and recommend from Source B only.

**Source B: new distillation candidates**
Use the "Framework direction" column of the need-dimension table to match the most relevant people or topics. When recommending, say exactly which of that person's frameworks solves the user's specific problem.

Display format for each candidate:

```
### Candidate 1: [name / topic]  ⚡Already installed / 🆕Needs distilling

**Core lens**: [this person's distinctive way of seeing the world, one sentence]
**Why it fits you**: [map it directly onto the user's need, state the matching logic]
**Limits**: [the blind spot of this lens — which problems it cannot help with]
```

Recommendation principles:
- Three candidates maximum; choice paralysis is worse than no choice
- Show already-installed Skills first (plug-and-play, zero cost)
- Candidates must differ from each other — do not recommend three similar people
- Always state the limits; no framework is universal
- Be specific about *which mental model* of that person matches the need, not a vague "they're brilliant"

#### Step 3: User choice

- Picked an existing Skill -> activate it, task done
- Picked a new candidate -> go to Phase 0A to confirm details -> Phase 0.5 begins distillation
- Nothing appeals -> return to Step 1 and keep exploring, or let the user name someone themselves

### Phase 0.5: Create the Skill Directory

**Execute immediately on confirmation**, before any research:

```
.claude/skills/[person-name]-perspective/
├── SKILL.md                          # the final artifact
├── scripts/                          # tooling (subtitle download / cleanup / quality check)
└── references/
    ├── research/                     # each Agent's research output (mandatory)
    │   ├── 01-writings.md            # writings and systematic thinking
    │   ├── 02-conversations.md       # long conversations and improvised thinking
    │   ├── 03-expression-dna.md      # short-form expression and style DNA
    │   ├── 04-external-views.md      # outside perspectives and criticism
    │   ├── 05-decisions.md           # decision records and actions
    │   └── 06-timeline.md            # the subject's timeline
    └── sources/                      # primary material (user-provided + downloaded)
        ├── books/
        ├── transcripts/
        └── articles/
```

**Completion check** (run automatically):
- [ ] Directory created
- [ ] If the subject is Chinese: switch the source strategy to prefer original Bilibili video / Xiaoyuzhou podcasts / authoritative Chinese media (Zhihu and WeChat Official Accounts are always excluded — see the source blacklist)
- [ ] If this is an update: existing SKILL.md has been read, and the information needing a refresh is marked
- [ ] If the user supplied local material: copy or move it into the matching `sources/` subdirectory and flag **local-corpus mode**

**Hard rules**:
- Every subagent must write its research into the corresponding md file. Research that is not written to a file did not happen.
- **All research files live inside the skill directory** (`references/research/`). Never write them to `07-research-and-analysis/` or any other external directory. A Skill must be self-contained — copying the whole skill directory must be enough to use it, with no external dependencies. This is the core principle behind open-source distribution.

---

### Phase 1: Multi-Source Collection (parallel agent swarm)

#### Mode selection: local corpus vs web search

Pick the collection strategy from the Phase 0A result:

| Mode | Trigger | Strategy |
|------|---------|------|
| **Pure web search** (default) | User supplied no local material | All 6 Agents search the web, full flow |
| **Local corpus first** | User supplied PDFs / transcripts / subtitles / articles | Analyze local material first; web search becomes a supplement |
| **Local corpus only** | User explicitly says "use only what I gave you", or the subject is not a public figure | Analyze local material only, no web search |

**How local-corpus-first mode runs**:

1. **Read the local material first**: classify the user's files across the 6 dimensions (one book may cover writings + conversations + expression at once)
2. **Identify the gaps**: which dimensions does the local material cover? Which are missing or thin?
3. **Targeted supplementary search**: launch web-search Agents only for the missing dimensions; skip search for dimensions already well covered locally
4. **Source labelling**: in the research files, clearly separate "from user-supplied material" vs "from web search"

**Common forms of local material and how to handle them**:

| Material type | Handling | Dimensions covered |
|---------|---------|---------|
| Book PDF | Read directly, extract core arguments | Writings (01), Expression (03) |
| Talk / interview transcript | Analyze Q&A patterns and improvised reactions | Conversations (02), Expression (03) |
| Video subtitles (SRT) | Same as transcript | Conversations (02), Expression (03) |
| Blog / newsletter export | Extract systematic positions | Writings (01), Expression (03) |
| Social media export | Analyze short-form expression patterns | Expression (03) |
| Internal docs / memos | Analyze decision logic | Decisions (05) |
| The user's own notes | Treat as a secondary source for cross-reference | Depends on content |

**Why local material wins on quality**: the primary material a user already holds — especially complete books and full interview transcripts — is usually far better than the secondhand paraphrase a web search turns up. In the source-priority table, user-supplied primary material carries the highest weight.

---

Below is the standard task split across the 6 Agents (for pure web-search mode, or for the missing dimensions in local-corpus mode).

Launch 6 parallel subagents, each responsible for a different information dimension.

#### The 6 Agents' assignments

| Agent | Search target | Extraction focus | Output file |
|-------|---------|---------|---------|
| 1 Writings | Books, long-form essays, papers, newsletters | Recurring core arguments (3+ occurrences = a real belief), coined terminology, recommended reading | `01-writings.md` |
| 2 Conversations | Podcasts, long videos, AMAs, in-depth interviews | How they answer when pressed, improvised analogies, moments they changed position, questions they refuse | `02-conversations.md` |
| 3 Expression | Twitter/X, Weibo, Jike, short posts | High-frequency words and sentence shapes, contrarian positions, style of humor, public arguments | `03-expression-dna.md` |
| 4 Outside views | Third-party analysis, book reviews, criticism, biographies | Patterns outsiders observe, criticism and controversy, comparison with peers | `04-external-views.md` |
| 5 Decisions | Major decisions, turning points, controversial actions | Decision context and logic, later reflection, cases where words and actions did or did not match | `05-decisions.md` |
| 6 Timeline | Full timeline from birth / debut to now | Key milestones, intellectual turning points, **the last 12 months** (guards against staleness) | `06-timeline.md` |

#### Hard requirements for every Agent
- Research output must be written into `references/research/0X-xxx.md`
- Note the source and its reliability (primary > secondary > inference)
- Separate "what they said" vs "what others said about them" vs "what I inferred"
- When you find a contradiction, keep it — do not smooth it over

#### Agent prompt template

When spawning a subagent, give the task in this shape (Agent 1, Writings, as the example):

```
Your task: research [name]'s writings and systematic long-form work.

Search directions:
- Books they published (title, core argument, year)
- Long-form newsletters / blogs / papers
- Core arguments that recur 3 or more times (these are the real beliefs)
- Coined terms and concepts
- Their recommended reading (reveals intellectual lineage)

Output requirements:
- Write to [skill dir]/references/research/01-writings.md
- Tag every item with a source URL and a reliability level
- Separate primary (written by them) vs secondary (someone else's summary)
- Record contradictions as you find them; do not reconcile them

Source blacklist: do not use Zhihu, WeChat Official Accounts, or Baidu Baike.
```

For the other 5 Agents, keep the same structure and swap the search directions and output filename.

#### Tooling (where available)
- Books: search and download via Z-Library / LibGen -> store in `sources/books/`
- Video subtitles (scripts are included, call them directly):
  - **Step 1, download subtitles**: `bash [skill dir]/scripts/download_subtitles.sh <YouTube_URL> [output dir]`
    - Prefers human-written subtitles -> Chinese -> English -> auto-generated
    - Writes SRT/VTT files to the given directory
  - **Step 2, clean into plain text**: `python3 [skill dir]/scripts/srt_to_transcript.py <input.srt> [output.txt]`
    - Strips timestamps, sequence numbers, HTML tags, and consecutive duplicate lines
    - Produces a clean readable transcript -> store in `sources/transcripts/`
  - User supplied a local video file with no subtitles: transcribe it with the gemini-video skill
- Podcasts: search transcript sites (podcastnotes.org and similar)
- Research summary generation (used in Phase 1.5): `python3 [skill dir]/scripts/merge_research.py <skill dir>`
  - Scans `references/research/01-06.md`, counts sources and the primary/secondary ratio, and pulls out key findings
  - Emits the markdown table for the Phase 1.5 checkpoint, so nothing has to be tallied by hand
- Quality self-check (used in Phase 4): `python3 [skill dir]/scripts/quality_check.py <path to SKILL.md>`
  - Checks all 6 pass criteria automatically: mental-model count, stated limits, expression DNA, honest limits, internal tension, primary-source ratio
  - Prints a per-item PASS/FAIL plus a summary

#### Use the information-gathering Skills already installed

Before starting Phase 1, **scan the `.claude/skills/` directory** for skills usable for information gathering. If any are present, prefer them during research — they are more reliable and efficient than WebSearch:

| Installed Skill | Purpose | When to call it |
|------------|------|---------|
| `gemini-video` | Analyze a local video file, extract a transcript | User supplied a video with no subtitles |
| `web-article-reader` | Read the full text of a web article precisely | You found an important article URL and want the real text, not a search snippet |
| `agent-reach` | Multi-channel information gathering (17 platforms) | You need data from X / Reddit / YouTube and similar platforms |
| `huashu-research` | Structured deep research | One dimension needs depth rather than breadth |
| `pdf` | Read PDF books and papers | User supplied primary material as PDF |

**How to apply this**: when spawning a subagent, tell it which skills are available and what each is for, so it can call them as needed. This is far more efficient than letting the agent grope around with WebSearch.

#### Source priority

| Source type | What it reveals | Weight |
|---------|---------|------|
| **User-supplied primary material** | Complete original text, no secondhand filter | **Highest+** |
| Their own writing | Systematic thinking | Highest |
| Long conversations / interviews | The improvised thinking process | Highest |
| Actual decision records | Real behavior vs claimed behavior | Highest |
| Social media | Expression style, immediate reactions | Medium |
| Others' assessments | Outside view, blind spots | Medium |
| Secondhand paraphrase | Usable as a pointer, must be verified | Low |

#### Source blacklist (excluded always)

- **Zhihu**: heavily rewritten content, high distortion rate; not a source for any dimension
- **WeChat Official Accounts**: closed ecosystem, unverifiable, mostly secondhand paraphrase; not a source
- **Baidu Baike / Baidu Zhidao**: stale and unreliable

For Chinese-language channels, accept only authoritative outlets: 36Kr, Geek Park, LatePost, Caixin, Yicai, Huxiu, SSPAI, Synced, and similar. For interviews, podcast platforms are acceptable (Xiaoyuzhou, original Ximalaya audio) as are original Bilibili videos (not repost accounts).

#### Failure modes and fallback paths (if-then table)

Distillation is a long, multi-agent, networked job. The first three rows below have all happened to real users (documented in GitHub issues). Each row runs as "trigger -> first fix -> fallback if that still fails":

| Trigger | First fix | Fallback |
|---------|---------|-----------|
| Runtime does not support parallel subagents or background tasks (some runtimes hang forever at Phase 1) | Downgrade the 6 research tasks to **serial execution**: finish one, write it to disk, then the next; never hang waiting for a background notification | One agent, 6 rounds — one dimension per round, written to disk immediately |
| Context window too small (a full distillation can accumulate 500k+ tokens; a 200k-window model cannot finish) | Run phase by phase: at the end of each Phase write state into `references/research/`, and let a new session resume from the files (the research files *are* the checkpoints) | On a 200k-window model, split into 3 sessions: Phase 0-1 / Phase 1.5-2.5 / Phase 3-5, each starting by reading what is already on disk |
| Cost overrun (user did not expect a long job's token burn) | The Phase 0A tier confirmation is the guardrail: state the magnitude and let the user pick a tier before starting | User calls a halt mid-run -> the research files already on disk are a deliverable intermediate; the next run resumes rather than restarting |
| A single Agent times out (5 minutes of search with nothing valuable) | Do not wait; move on, and mark "insufficient information" in Phase 2 | State that this dimension is thin in the honest limits |
| WebSearch or similar tools unavailable | Switch to an equivalent tool the runtime does have (fetch / browser tools / an installed information-gathering skill) | Switch to pure local-corpus mode and ask the user for material |
| Source scarcity (fewer than 10 usable sources) | Warn the user back at Phase 0.5 and lower expectations (cut to 2-3 mental models) | Expand the honest limits section and label what is inference |
| Agents produce conflicting results | Keep the contradiction — it is itself a valuable signal | Collect it under an "internal tensions" section |

**Hard rule**: it is better to ship a 60-point Skill that honestly labels its limits than a 90-point Skill that looks perfect and is actually fabricating.

### Phase 1.5: Research Review Checkpoint

**🔴 CHECKPOINT · once all Agents finish, pause and show the research quality summary**:

```
┌──────────────────┬──────────┬──────────────────────────┐
│ Agent            │ Sources  │ Key findings             │
├──────────────────┼──────────┼──────────────────────────┤
│ 1 Writings       │ 8        │ Core: antifragility, ... │
│ 2 Conversations  │ 5        │ Shift: after 2020, ...   │
│ 3 Expression     │ 120      │ Frequent: "skin in the.."│
│ 4 Outside views  │ 6        │ Main criticism: ...      │
│ 5 Decisions      │ 4        │ Key decision: ...        │
│ 6 Timeline       │ complete │ Latest: March 2026, ...  │
├──────────────────┼──────────┼──────────────────────────┤
│ Contradictions   │ 2        │ Agent1 says X, Agent4 Y  │
│ Thin dimensions  │ none     │                          │
└──────────────────┴──────────┴──────────────────────────┘
```

User confirms the research quality -> go to Phase 2.
User finds a dimension lacking -> research more, then continue.

Why this checkpoint exists: research quality sets the ceiling for the final Skill. Garbage in, garbage out — catching it here is far cheaper than reworking at Phase 4.

---

### Phase 2: Framework Extraction (synthesis)

Once the 6 Agents' material is in, run structured extraction. First read `references/extraction-framework.md` for the triple-verification methodology behind mental models (cross-domain recurrence, generativity, coined terminology), so the extraction holds up.

#### 2.1 Mental model extraction (3-7)

**Steps**:

1. **Scan**: read `01-writings.md` through `05-decisions.md` one by one and list every candidate claim (positions they repeat, terms they coined, central assertions). Typically 15-30 candidates.
2. **Triple-verification filter**: run each candidate through (details in `references/extraction-framework.md`):
   - Cross-domain recurrence: does it appear across 2+ different fields or topics?
   - Generativity: can it predict this person's position on a new question?
   - Exclusivity: is it something *not* every smart person would think?
   - All three pass -> mental model; only 1-2 -> demote to a decision heuristic; none -> discard
3. **Rank and cut**: sort by strength of exclusivity (most distinctive first) and take the top 3-7. Fewer is better — 3 deep models beat 10 shallow principles.
4. **Record format**: for each model — name, one-line description, supporting evidence (2+ occasions), how it is applied, and its limits

#### 2.2 Decision heuristic extraction (5-10)

= the fast rules this person judges by. Expressible as "if X, then Y", each backed by a concrete case.

#### 2.3 Expression DNA analysis

| Dimension | What to extract |
|------|---------|
| Sentence preference | Long vs short, question vs statement, analogy density |
| Vocabulary | High-frequency words, proprietary terminology, words they avoid |
| Rhythm | Conclusion first or setup first, how they pivot |
| Humor | Sarcasm / self-deprecation / absurdity / deadpan / none |
| Certainty | The "I'm not sure" type or the "obviously" type |
| Citation habits | Who they quote, and what kind of thing |

#### 2.4 Values and anti-patterns

- **Values**: 3-5 core values, ranked
- **Anti-patterns**: behavior or thinking this person explicitly opposes
- **Contradictions and tensions**: the internal conflicts between their values (this is where depth comes from)

#### 2.5 Intellectual lineage

Who influenced them -> who they influenced -> where they sit on the map of ideas

#### 2.6 Honest limits

Limits that must be written out explicitly:
- Cannot predict their reaction to a genuinely new problem
- Cannot substitute for their creativity and intuition
- Public statements and private beliefs may diverge
- Information is current only up to the research date

---

### Phase 2.5: Extraction Confirmation Checkpoint

**🔴 CHECKPOINT** · after Phase 2 extraction, pause and show the summary for confirmation:

```
Extraction summary:
- Mental models: N (list the names)
- Decision heuristics: N
- Expression DNA: [3 key traits]
- Core tensions: N pairs
- Honest limits: N
```

User confirms -> go to Phase 3 and build.
User thinks a model is wrong or missing -> return to Phase 2, adjust, then continue.

Why this checkpoint exists: extraction is the step with the heaviest subjective judgment. Confirm before building, so you do not write 400 lines of SKILL.md and only then discover the direction was wrong.

---

### Phase 3: Skill Construction

Assemble the Phase 2 extraction into a runnable SKILL.md.

#### Step 1: Read the template
Read `references/skill-template.md` for the standard structure. The template defines the full skeleton of the target Skill: frontmatter, role-play rules, identity card, mental models, decision heuristics, expression DNA, timeline, values, intellectual lineage, honest limits, research sources.

#### Step 2: Fill in the content
Follow the template structure and place the Phase 2 results section by section:

| Template section | Filled from |
|------------|---------|
| frontmatter description | Source count + model count + triggers. **Keep it around 300 characters and never exceed the skill-loader's ~1024-character ceiling**: one line of positioning + explicit trigger phrasing ("use X's perspective", "what would X think") + one line of "does not auto-trigger on general questions" as a guard. Stuffing in long-tail keywords overruns the limit and errors out, burns tokens every session, and raises the false-trigger rate — what actually drives matching is the person's name and their proprietary concepts |
| Role-play rules | Use the template defaults as-is (including the two output disciplines: label inference on topics they never addressed, and keep real quotes distinguishable). No changes needed |
| **Answer workflow (Agentic Protocol)** | **Derived automatically from the mental models; see the generation guide below** |
| Identity card | Timeline (06) + writings (01) -> write a ~50-word self-introduction in this person's voice |
| Mental models | Phase 2.1 output; each with name / evidence / application / limits |
| Decision heuristics | Phase 2.2 output; each with a scenario and a case |
| Expression DNA | Phase 2.3 analysis -> turned into style rules for role-play |
| Timeline | Agent 6's research, compressed into a table of key moments |
| Values and anti-patterns | Phase 2.4 output |
| Intellectual lineage | Phase 2.5 output |
| Honest limits | Phase 2.6 output + the research date |
| Research sources | The 6 Agents' citations, collected and split into primary / secondary |
| Creator attribution | Fixed text: `> This Skill was generated by [Nuwa · The Art of Making Minds into Skills](https://github.com/alchaincyf/nuwa-skill)` + `> Creator: [Huashu](https://x.com/AlchainHust)` |

#### Guide for generating the Answer Workflow (Agentic Protocol)

**Why this section exists**: it makes the persona not just *sound* right but *act* right. Without it, a person Skill hits a question that needs facts and invents them from training data instead of doing the homework first, the way a real person would. This is what upgrades a person Skill from parrot to reliable thinking advisor.

**Placement**: after "Role-play rules", before "Example dialogue".

**Generation rules**:

The generated Agentic Protocol must contain these 3 Steps, and Step 2's research dimensions must be **derived from the extracted mental models**, not copied from a fixed template:

```markdown
## Answer Workflow (Agentic Protocol)

**Core principle: [name] does not speak off the cuff. When a question needs factual support, do the homework first, then answer.**

### Step 1: Classify the question

On receiving a question, decide its type:

| Type | Signal | Action |
|------|------|------|
| **Needs facts** | Involves a specific company / person / event / product / market state | -> research first (Step 2) |
| **Pure framework** | Abstract values, ways of thinking, life advice | -> answer straight from the mental models (skip to Step 3) |
| **Mixed** | Uses a concrete case to discuss an abstract point | -> get the facts of the case, then analyze with the framework |

**Rule of thumb**: if the answer would be noticeably worse for lacking current information, you must research first. Better to search once too often than to invent from training data.

### Step 2: [name]-style research (pick by question type)

**⚠️ You must use tools (WebSearch and similar) to get real information. Do not skip this.**

[From this person's mental models and analytical preferences, generate 3-5 research dimensions, each with 4-6 concrete research points]

#### Research output format
Once research is done, assemble a factual summary internally (do not show it to the user), then go to Step 3.
What the user sees is not a research report — it is [name]'s judgment, made on real information.

### Step 3: [name]-style answer

Using the facts from Step 2 (if any), apply the mental models and expression DNA to produce the answer.
```

**How to derive Step 2's research dimensions**:

Work backwards from the extracted mental models to what this person pays most attention to when analyzing, and turn that into concrete search dimensions. Examples:

| Person | Core mental models | -> Derived research dimensions |
|------|------------|------------------|
| Munger | Latticework of models, inversion, incentives | -> Look at the moat, at management's incentive structure, at the biggest risk (inversion), at historical analogues |
| Feynman | First principles, distrust of authority | -> Look at the basic physical/mathematical constraints, at the logical holes in the official account, at the experimental data |
| Taleb | Antifragility, tail risk, epistemic arrogance | -> Look at the extremes, at who carries the tail risk, at the track record of expert forecasts |
| MrBeast | Attention engineering, test-and-iterate | -> Look at competitors' numbers (views/engagement), at A/B headroom in titles and thumbnails, at the audience profile |

**Hard constraints**:
- Research dimensions must come from the mental models; a generic "search for relevant information" is not acceptable
- Each dimension needs concrete search guidance (what to search, what data to look at), not an abstract description
- Group them by question type (Munger splits into "reading a company", "reading a person", "reading an event") so the Skill's user can navigate fast

#### Step 3: Quality self-check
Once built, read the "Quality self-check list" at the end of `references/extraction-framework.md` and go through it item by item. Flag anything that fails and return to the matching Phase to fix it.

#### Step 4: Output
Write the finished SKILL.md to `.claude/skills/[person-name]-perspective/SKILL.md`.

---

### Phase 4: Quality Validation

After the Skill is generated, run 3 tests with a subagent (independent of the main agent, to avoid self-assessment bias):

#### 4.1 Known test (sanity check)
Pick 3 questions this person has publicly answered, **spawn a subagent carrying the new Skill to answer them**, and compare against the real positions.
- Direction matches -> the model works
- Diverges -> go back and adjust the weighting of the mental models

#### 4.2 Edge test (edge case)
Pick 1 related question this person never publicly addressed, and infer with the Skill.
- Expected output: "inferring from models X and Y, probably... but I'm not certain"
- It should not be categorical

#### 4.3 Voice test
Write a 100-word analysis with the Skill and judge:
- Does it carry this person's expression traits?
- Is it free of generic AI-flavored platitude?
- Is it more than a collage of their actual quotes?

#### 4.4 Pass criteria

| Check | Pass | Fail signal |
|--------|---------|-----------|
| Mental model count | 3-7, each with source evidence | <3 or >10 |
| Limits per model | Failure conditions written out explicitly | Only upsides listed |
| Expression DNA recognizability | 100 words is enough to identify who it is | Reads like generic ChatGPT |
| Honest limits | At least 3 concrete limits | Only "cannot replace the real person" |
| Internal tension | At least 2 contradictory pairs | Suspiciously consistent (too clean to be real) |
| Primary-source ratio | >50% | Mostly secondhand paraphrase |

Validation passes -> deliver. Fails -> mark the weak spots and iterate from Phase 2.
**Iteration cap**: the Phase 2 -> 4 loop runs at most twice. If items still fail after two rounds, note the weak dimensions in the honest limits and ship the best current version rather than polishing forever.

**🔴 CHECKPOINT · not done until the validation results have been shown to the user and confirmed.**

---

### Phase 5: Dual-Agent Refinement (standard post-processing)

Once Phase 4 passes, dual-agent refinement starts automatically to raise the Skill's operability:

**Launch two Agents in parallel:**

**Agent A (auto-skill-optimizer lens)**:
- Run an 8-dimension structural assessment of SKILL.md (workflow clarity, boundary conditions, checkpoint design, instruction specificity, and so on)
- Dry-run 3 representative test prompts and assess the effectiveness dimensions
- Output: concrete improvements for the 2 weakest dimensions (with sample rewritten text)

**Agent B (skill-creator lens)**:
- Review whether the activation triggers cover real usage scenarios
- Review how operable the role-play rules are (is there question routing, frequency constraints, failure prevention?)
- Identify missing critical information
- Output: 2-3 concrete text changes (with sample rewritten text)

**🔴 CHECKPOINT · the main Agent merges both reports, applies the non-conflicting improvements, and shows a change summary for the user to confirm.**

The refinement standard: changes must make the skill "execute on activation" — not just add content, but make the AI know what to do first and where to stop once it picks the skill up.

---

## Updating an Existing Skill

When the user says "update X's skill" or "X has been in the news lately":

1. Read the existing SKILL.md, find "Research date: [date]" in the honest limits section, and note how long ago that was
2. Launch only Agent 2 (recent conversations) + Agent 5 (recent decisions) + Agent 6 (timeline update)
3. Compare the new information against the existing content:
   - New information reinforces an existing model -> add the case
   - New information contradicts an existing model -> note the change and update the model
   - A new thinking pattern emerges -> consider adding a new model
4. Update the "Recent developments" section and the research date in SKILL.md
5. Do not rewrite the whole Skill — update incrementally

---

## Taste Rules (quick reference)

Come back here when a judgment call is hard. The quantified criteria live in the Phase 4 pass table.

| Principle | In one line |
|------|------|
| Long form > one-liners | A 3,000-word essay reveals more structure than 50 tweets |
| Controversy > consensus | The most contested position reveals the most distinctiveness |
| Change > constancy | Where they changed their mind carries more information than where they never wavered |

### ❌ Anti-pattern blacklist (never do these)

| # | Anti-pattern | Why / what to do instead |
|---|--------|------------------|
| 1 | Inventing things this person never said | The internet is full of fabricated quotes. Every quote needs a source; if you cannot find the original, drop the line |
| 2 | Dressing up generic wisdom as their "unique insight" | Anything that fails triple verification (exclusivity) does not become a mental model |
| 3 | Ignoring negative assessments and controversy | Agent 4's critical material is what stops fan-filter bias; too little negative content = failed research |
| 4 | Forcing generation on thin information | Better a 60-point Skill that labels its limits honestly than a 90-point Skill that looks perfect and is fabricating |
| 5 | Using Zhihu / WeChat Official Accounts / Baidu Baike as sources | Rewritten, distorted, unverifiable. No exceptions, in any dimension |
| 6 | Forcing the whole flow through one session on a small-context model | It will blow up between Phase 1 and 2. Split and resume per the fallback table |
| 7 | Starting the run without stating the cost magnitude | A full distillation is a heavy job; the user has the right to pick a tier before spending |
| 8 | Distilling a living private individual without flagging the boundary | This touches privacy and consent. The user must supply the material, and must be reminded to get that person's agreement |
| 9 | Generating a Skill with no drift protection | In long conversations a person Skill loses the persona and slides back into generic-assistant voice. The template's role-play rules and expression DNA constraints must be kept intact |
| 10 | Turning a confirmation checkpoint into a delivery blocker | Checkpoints exist so the user can correct course, not to withhold output. If a default is available, use it |

---

## Special Cases

### Living people vs historical figures
- **Living**: watch recency, mark the cutoff date, recommend periodic updates
- **Historical**: material is more stable but biographies carry bias — cross-verify across sources

### Topic Skills vs person Skills

When the input is a topic rather than a name ("value investing", "product restraint", "antifragile decision-making"), each Phase has a variant:

| Phase | Person Skill | Topic Skill variant |
|-------|----------|--------------|
| 0A | Confirm the name + focus | Confirm the topic's boundary + target audience ("value investing" — Graham-style, or all schools?) |
| 0.5 | `[person]-perspective/` | `[topic]-framework/`, same directory structure |
| 1 | 6 Agents around one person | First find the topic's 3-5 core figures or schools, then assign Agents per figure (1-2 Agents each, not 6) |
| 2.1 | Extract one person's mental models | Extract the **field consensus** (what every school agrees on) + **the disagreements** (A says X, B says Y) |
| 2.3 | Simulate one person's expression | Do not simulate any particular voice; use neutral but expert phrasing |
| 2.4 | One person's internal contradictions | The fundamental splits between schools (the philosophical gap between value and growth investing, say) |
| 3 | Use skill-template.md | Adapt the template: drop the role-play rules and identity card, replace with "framework overview" + "school comparison" |
| 4 | Compare against this person's known positions | Compare against the field's canonical cases |

### Chinese subjects vs Western subjects
- **Chinese**: original Bilibili videos and talks, Xiaoyuzhou podcasts, interviews in authoritative media (36Kr / LatePost / Caixin / Geek Park), their own books and Weibo. Zhihu and WeChat Official Accounts are excluded, always
- **Western**: Twitter, YouTube, podcasts, Amazon reviews

### Obscure subjects (very little public information)
When the Phase 0.5 assessment finds fewer than 10 usable sources:
1. Tell the user at Phase 0.5 that "there is very little public information on this person, so the Skill's quality will be limited"
2. Cut to 2-3 mental models, each tagged "inferred from limited information"
3. Expand the honest limits section and list exactly which dimensions are thin
4. If the user can supply primary material (books, private recordings, DMs), prefer it

### Distilling the user themselves
When the user says "distill me" or "make a skill of myself":
1. Nuwa cannot find the user's thinking framework through public channels; the user has to supply the material
2. Ask for: personal articles and blogs, recorded videos or podcasts, decision memos they have written, self-description
3. Phase 1's 6 Agents analyze the supplied material instead of searching the web
4. Watch for **self-perception bias** — the user may overrate some traits and miss blind spots; it is fair to ask what people around them say

---

## Finally

What Nuwa makes is not a person. It is a mirror.

A good person Skill lets you look at your own problem through someone else's eyes. Not to imitate them, but to widen the boundary of your own thinking.

## Version Self-Check (silent)

This section is for the AI agent. Before each use of this skill, make one offline judgment: read the `.last-update-check` file in this skill's directory (the directory containing SKILL.md); its content is a single date line, `YYYY-MM-DD`. If the file exists and is less than 30 days old, skip this section and get to work — say nothing about updates.

Only when it has expired or the file is absent:

1. This directory is not a git clone (no `.git`, or no origin) -> write today's date and skip this section
2. Compare versions: `git -C <this dir> rev-parse HEAD` against `git -C <this dir> ls-remote origin HEAD`
3. Either way, write today's date into `.last-update-check`
4. They match -> say nothing. Confirmed behind -> finish the user's current task first, then add one line: "a newer version of this skill is available; update with `git -C <this dir> pull --ff-only`". Whether to update is the user's call — do not run the update yourself
