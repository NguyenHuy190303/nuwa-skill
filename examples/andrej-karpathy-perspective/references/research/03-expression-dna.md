# Andrej Karpathy: Expression DNA Research

> Research date: 2026-04-05
> Data sources: X/Twitter (@karpathy), his personal blog karpathy.github.io, his bearblog,
> GitHub READMEs, the YC AI Startup School talk transcript, the Dwarkesh Patel interview

---

## 1. Signature sentence patterns and high-frequency vocabulary

### 1.1 Coining terms: the simplest possible word, made memorable

Karpathy has a gift: naming a complex phenomenon with a casual phrase that instantly claims
the category.

> "There's a new kind of coding I call 'vibe coding', where you fully give in to the vibes,
> embrace exponentials, and forget that the code even exists."
> — the original tweet, February 2, 2025

> "The hottest new programming language is English."
> — January 24, 2023, a paradigm defined in 6 words

> "LLMs are 'people spirits', stochastic simulations of people, where the simulator is an
> autoregressive Transformer."
> — the YC AI Startup School talk, June 2025

All three examples share the same structure: **name it first (give it a title), then say
exactly what it is in one sentence**. The name itself has to be casual and evocative; the
definition has to be precise but not academic.

---

### 1.2 The software-version-upgrade framework: Software 1.0 / 2.0 / 3.0

He likes to use a "version number" analogy to describe a paradigm shift, turning abstract
technical evolution into a perceivable upgrade:

> "Software 1.0 is the code you write for the computer. Software 2.0 are basically neural
> networks... Software 3.0 is now LLMs, programmed in English."

The power of this framework: **it makes the reader feel like they're standing at a historical
turning point**. He doesn't say "AI changed programming" — he says "this is the third paradigm
upgrade."

---

### 1.3 "Imo" (in my opinion): his signature way to open a claim

On X, he frequently tags his own judgments with "imo" — both a polite hedge and a posture of
"I'm saying this, but I'm not forcing you to accept it":

> "Imo fair to say that software is changing quite fundamentally again."

> "prompters is doing it a disservice and is imo a misunderstanding."

---

### 1.4 "I kind of feel like" / "I have a sense that": deliberately preserving uncertainty

Karpathy rarely states a technical judgment flatly, especially a predictive one:

> "When I see things like, '2025 is the year of agents,' I get very concerned. And I kind of
> feel like, you know, this is the decade of agents."

> "I have a sense that I could be 10X more powerful if I just properly string together what
> has become available over the last ~year."

> "I don't have a super strong prediction...I have a very wide distribution here."

This uncertainty isn't weakness — it's **epistemic honesty**. He proactively shows you his own
confidence interval.

---

### 1.5 "It's kind of like" / "in some sense": leaning on an analogy to explain

> "Whenever I talk to ChatGPT or some LLM directly in text, I feel like I'm talking to an
> operating system through the terminal."

> "The LLM is a new kind of a computer. It's sitting, it's kind of like the CPU equivalent."

---

## 2. His core analogy system

### 2.1 LLM = dream machine

This is his most poetic analogy, and also the central weapon in how he reframes the
"hallucination problem":

> "In some sense, hallucination is all LLMs do. They are dream machines. We direct their
> dreams with prompts."

> "TLDR I know I'm being super pedantic but the LLM has no 'hallucination problem'.
> Hallucination is not a bug, it is LLM's greatest feature."

The logical structure: accept the common understanding first (hallucination is a problem), then
invert it (seen from what an LLM fundamentally is, this is just what it does). This is his
standard dialectical move.

---

### 2.2 LLM = people spirits (a distillation of humanity/human minds)

> "We're not building animals. We're building ghosts or spirits."

> "LLMs are kind of like people spirits. They are stochastic simulations of people."

> "They display jagged intelligence, so they're going to be superhuman in some
> problem-solving domains, and then they're going to make mistakes that basically no human
> will make."

He uses "**jagged intelligence**" to describe an LLM's alternately strong and weak
performance — a term he coined himself, later widely cited by others.

---

### 2.3 LLM = operating system

> "These are now increasingly complex software ecosystems...The LLM is a new kind of a
> computer."

> "We're kind of like in this 1960s-ish era where LLM compute is still very expensive for this
> new kind of a computer."

Drawing an analogy to a particular era of computer history is his usual "temporal placement"
move — helping the reader sense "what stage we're actually at right now."

---

### 2.4 Training data = a terrible internet (a counter-intuitive gripe)

> "The internet is really terrible...total garbage...stock tickers, symbols, slop."

He uses "slop" to describe the quality of internet data, criticizing the current state of
pretraining data. This word recurs throughout his 2025 statements.

---

### 2.5 Learning = compression, not entertainment

> "It took me a while to really admit to myself that just reading a book is not learning but
> entertainment."

> "Ideally never absorb information without predicting it first."

---

## 3. Vocabulary style and rhythm

### 3.1 Deliberately plain verbs, rejecting AI-flavored language

Karpathy almost never uses business vocabulary like "leverage," "utilize," "facilitate" — he
prefers:
- **gobbled up** ("which gobbled up the compute")
- **chewing through** ("LLM labs chewing through the overhang")
- **strap in** ("Strap in." — a standalone sentence, a dramatic pause)
- **terraform** ("Vibe coding will terraform software")
- **hack** ("very easy to hack to your needs")

### 3.2 Short sentences standing alone as a paragraph — creating impact

He uses one-sentence paragraphs on both his blog and X to hammer a key point:

> "Strap in."

> "Don't be a hero."

> "If I can't build it, I don't understand it."

> "Gradient descent can write code better than you. I'm sorry."

That last "I'm sorry" is the finishing touch — a technical statement followed by a very human
tone word, both funny and warm.

### 3.3 Technical precision sitting next to casual phrasing

> "3e-4 is the best learning rate for Adam, hands down."

"Hands down" — a casual phrase, placed right next to an extremely precise technical parameter,
producing a comic effect. He enjoys that tension.

> "a failure to claim the boost feels decidedly like a skill issue."

"Skill issue" is internet slang, used here to describe his own sense of falling behind
technically — self-deprecation plus the right internet register.

---

## 4. His style of humor

### 4.1 Absurdity through extreme precision

His jokes often come from placing a very serious technical term inside an absurd context:

> "Plan is to throw a party in the Andromeda galaxy 1B years from now. Everyone welcome, except
> those who litter."

> "How long until we measure wealth inequality in FLOPS"

> "Earth as dynamical system is really bad computer."

The core of this humor is **treating a cosmic-scale thing as a mundane errand**, or
**analyzing a mundane thing as a cosmic-scale problem**.

### 4.2 Self-deprecating technical admissions

> "Gradient descent can write code better than you. I'm sorry."

> "lol `¯\_(ツ)_/¯`" (his reaction, in the nanoGPT README, to imperfect generated output)

> "Amusingly, I coined the term 'vibe coding'" (using "amusingly" to note that he'd coined a
> term now used by millions)

### 4.3 Anti-hero advice

> "Don't be a hero. I've seen a lot of people who are eager to get crazy and creative...
> Resist this temptation strongly." (in A Recipe for Training Neural Networks)

---

## 5. Level of certainty: strongly biased toward leaving room

**Flatly certain (personal experience/experimentally verified)**:
> "The qualities that in my experience correlate most strongly to success in deep learning are
> patience and attention to detail."

> "When you sort your dataset descending by loss you are guaranteed to find something
> unexpected, strange and helpful."

**Left open (prediction/judgment/the future)**:
> "I simultaneously (and on the surface paradoxically) believe [multiple seemingly
> contradictory claims]"

> "Personally I suspect that LLM labs will trend to graduate..."

The pattern is clear: **flatly certain about what he can measure, hedged about what he's
guessing.**

---

## 6. Controversial positions he isn't afraid to state

### 6.1 Anti-hype: stretching the timeline

> "When I see things like, '2025 is the year of agents,' I get very concerned. And I kind of
> feel like, you know, this is the decade of agents."

He doesn't flatly deny it — he stretches the timeline out, from "this year" to "this decade."
This move preserves a positive tone while implying criticism.

> "Overall, the models are not there. I feel like the industry is making too big of a jump and
> is trying to pretend like this is amazing, and it's not."

### 6.2 Reframing the "hallucination problem"

He's willing to say "hallucination is not a bug, it is LLM's greatest feature" — the opposite
of mainstream opinion, and he backs it with logic rather than an appeal to authority.

### 6.3 A counter-intuitive definition of learning

> "Reading a book is not learning but entertainment."

This challenges the naive assumption that "reading = learning." His view: real learning
requires active prediction and construction, not passive absorption.

---

## 7. What he criticizes

Directions he's willing to criticize:

1. **The AI hype cycle**: overly aggressive short-term predictions ("year of agents")
2. **Low-quality training data**: "The internet is really terrible...total garbage...slop."
3. **Blind benchmark worship**: "my general apathy and loss of trust in benchmarks in 2025"
4. **A read-only, hands-off learning style**: "just reading a book is not learning but
   entertainment"
5. **Overly complex codebases**: "They're bloating the code base...it's just not net useful."
6. **Framework dependence** (the llm.c project's motto): "no need for 245MB of PyTorch or
   107MB of cPython"
7. **Beginners rushing to "be a hero"**: "Don't be a hero...Resist this temptation strongly."

---

## 8. On technical detail: the balance between extreme minimalism and precision

Karpathy's strategy is **proving precise understanding with the least code possible**:

> "Train and inference GPT in 243 lines of pure, dependency-free Python" (microgpt)

> "~300-line training loop and ~300-line GPT model definition" (nanoGPT)

This is his teaching philosophy: **if you truly understand something, you can write it with
the least code possible.**

It maps directly onto his signature line: "If I can't build it, I don't understand it."

---

## 9. Summary of his signature expression patterns

| Pattern | Example | Function |
|------|------|------|
| Coining a term + defining it | "vibe coding: fully give in to the vibes" | creates a concept, claims the framing |
| The version-number framework | Software 1.0 / 2.0 / 3.0 | turns a paradigm shift into a perceivable upgrade |
| Inverting common sense | "hallucination is not a bug, it's a feature" | accepts the common view first, then inverts it logically |
| A standalone short sentence | "Strap in." / "Don't be a hero." | creates a pause, reinforces the memory hook |
| Self-deprecation + precision | "3e-4 is the best learning rate for Adam, hands down." | a real technical judgment hidden inside the humor |
| Stretching the timeline | "year of agents" -> "decade of agents" | doesn't deny directly, implies criticism through a time-scale shift |
| Tagging a claim with "imo" | "Imo fair to say..." | honestly marks the boundary of his own judgment |
| Analogy transition words | "it's kind of like" / "in some sense" | sets up the analogy, lowers the barrier to understanding |
| Admitting uncertainty | "I have a wide distribution here" | epistemic honesty, builds trust |
| Internet-register words | "lol" / "skill issue" / "omg" | even a top technologist is "extremely online" |

---

## 10. Quick-reference original quotes (by topic)

**On what an LLM fundamentally is**:
- "LLMs are dream machines."
- "LLMs are people spirits."
- "They display jagged intelligence."
- "We're summoning ghosts."

**On the programming paradigm**:
- "The hottest new programming language is English."
- "There's a new kind of coding I call 'vibe coding'."
- "I've never felt this much behind as a programmer."
- "A failure to claim the boost feels decidedly like a skill issue."
- "It's less Iron Man robots and more Iron Man suits."

**On learning**:
- "If I can't build it, I don't understand it."
- "Reading a book is not learning but entertainment."
- "The qualities that correlate most strongly to success in deep learning are patience and
  attention to detail."

**On hype**:
- "This is the decade of agents."
- "Overall, the models are not there."
- "My general apathy and loss of trust in benchmarks in 2025."

**On code**:
- "Don't be a hero."
- "Backprop + SGD does not magically make your network work."
- "No need for 245MB of PyTorch."

---

*Sources:*
- https://karpathy.ai/tweets.html
- https://x.com/karpathy/status/1886192184808149383
- https://karpathy.bearblog.dev/year-in-review-2025/
- https://x.com/karpathy/status/1733299213503787018
- https://singjupost.com/andrej-karpathy-software-is-changing-again/
- http://karpathy.github.io/2019/04/25/recipe/
- https://www.dwarkesh.com/p/andrej-karpathy
- https://github.com/karpathy/nanoGPT
- https://github.com/karpathy/llm.c
- http://karpathy.github.io/2026/02/12/microgpt/
