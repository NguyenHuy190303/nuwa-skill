# Andrej Karpathy — Major Decisions and Key Action Records

> Research date: 2026-04-05
> Sources: Wikipedia, TechCrunch, CNBC, the Lex Fridman Podcast, Karpathy's own Twitter/X,
> BDTechTalks, VentureBeat, Electrek, and others

---

## Decision 1: joining OpenAI's founding team (2015)

### Background
Karpathy was then a PhD student at Stanford (in Fei-Fei Li's lab), researching CNNs at the
intersection of computer vision and NLP. In 2015 he'd also interned at DeepMind on deep
reinforcement learning. OpenAI was announced that same year.

### Decision logic
He said publicly that what drew him in was OpenAI's unusual "academic-startup hybrid" model —
research freedom combined with the drive toward real-world application. That was a rare shape
for an AI institution at the time. He wanted to be an early participant in pushing AI into
practice, not just publishing papers.

### Later reflection
He's never publicly criticized this period. He characterizes it as the foundational period
where he built his core technical understanding. He's since returned to OpenAI twice, which
suggests his sense of connection to the institution has persisted.

---

## Decision 2: leaving OpenAI to join Tesla (2017)

### Background
Elon Musk personally recruited him. Tesla's Autopilot was at a critical expansion point at the
time, and needed someone who could actually turn academic deep-learning capability into real
engineering. For Karpathy, this was a chance to validate the "Software 2.0" idea (which he
laid out systematically in a blog post that November) at real-world scale.

### Decision logic
This is a classic "verifiability-driven" decision. Tesla had a data flywheel from a million
cars — precisely the largest possible testing ground for validating the paradigm of "neural
networks replacing hand-written rules." Moving from academic research to real-world
verification fits his epistemology: "if I can't build it, I don't really understand it."

He describes Musk's management style: "Elon likes small, elite, highly technical teams. He was
consistently a force against growing team size... if an engineer said there weren't enough
GPUs, hearing it twice was enough for him to call the head of the GPU cluster directly, then
call Jensen Huang."

---

## Decision 3: "fully vision-based, no LiDAR" — Tesla's technical direction

### Background and decision timeline
This wasn't a single-point decision, but a technical direction that evolved and hardened
continuously from 2017-2022. Key moments:
- His CVPR 2021 keynote, where Karpathy systematically argued for the vision-only approach
- Late 2021, Tesla removes radar, moving fully to vision-only
- 2022, ultrasonic sensors removed as well

### Decision logic (Karpathy's public argument)

**Core argument 1: the data flywheel matters more than the sensor stack**
"The real question isn't whether you have LiDAR — it's whether you have a fleet that can
collect data."

**Core argument 2: LiDAR's scaling problem**
"Collecting, building, and maintaining high-precision LiDAR maps doesn't scale."

**Core argument 3: the generality of the vision approach**
"Once you genuinely make it work, it's a general-purpose vision system that can, in principle,
deploy anywhere on Earth."

**Core argument 4: neural networks have already surpassed sensor fusion**
"Our deep-learning system is already a hundred times more precise than radar — radar started
becoming the limiting factor, starting to introduce noise."

### Consistency between words and actions
After leaving Tesla, Karpathy has never publicly disputed this technical direction. His
technical judgment has, to some extent, been validated by the market: Tesla FSD keeps
iterating, still vision-only. But the safety-data performance of multi-sensor approaches at
companies like Waymo has kept the debate alive.

---

## Decision 4: leaving Tesla (July 2022)

### Decision logic (his public statement)
His official statement: "It's been five years and I feel like I've grown a lot and accomplished
a lot together with the teams at Tesla... I don't have a specific plan for what's next but
want to dedicate more time towards returning back to my passions around technical work: hands-
on building, education and open source."

A more candid statement on the Lex Fridman podcast: "over five years, I let myself drift into
a management position. Most of my time was spent in meetings... that's not something I
fundamentally enjoy."

### Consistency between words and actions
**Consistent**: his departure fits his long-standing engineer identity completely. He
immediately began publishing YouTube technical videos at a rapid pace after leaving (nanoGPT,
the makemore series) — his way of proving his values through action.

---

## Decision 5: open-sourcing the nanoGPT educational project series (starting late 2022)

### Decision logic
His stated motivation for writing nanoGPT is direct: "a small repository for teaching people
the basics of GPT training."

Behind this is the core of his epistemology: "if I can't build it, I don't understand it" (he
attributes this to Feynman). nanoGPT is about 750 lines of code, capable of training a GPT-2-
scale model, designed so "anyone can read every line." Later came llm.c (implemented directly
in C/CUDA), going even lower-level.

### Impact
nanoGPT became one of the most-read pieces of code in AI education, a baseline and starting
point for a great many later projects.

---

## Decision 6: returning to OpenAI (February 2023)

After a "gap period" of publishing a huge volume of educational content, a few months before
GPT-4's release, he chose to return to OpenAI. He mainly worked on building a new team focused
on midtraining and synthetic-data generation, and also contributed to GPT-4's improvement.

---

## Decision 7: leaving OpenAI again (February 2024)

### His own words
"Hi everyone, yes I left OpenAI yesterday. First, nothing 'happened', this is not the result of
any particular event, issue, or drama (but please keep the conspiracy theories coming as they
are highly entertaining :)). Actually, my brief tenure at OpenAI over the last ~1 year was
really fun. The team is super strong, and I'm really bullish about the roadmap."

**Consistency**: this is the second time he's chosen "personal projects" over "a large
company." The pattern is remarkably stable — a period at a big company, making a contribution,
then returning to independent creative work.

---

## Decision 8: founding Eureka Labs (July 2024)

### Decision logic
He positions Eureka Labs as an "AI-native school." Mission: use an AI Teaching Assistant to
amplify course material written by human experts, scaling education. Its first product is
LLM101n.

This is highly consistent with a "sub-theme" that's run through his entire career: Stanford
CS231n (a deep-learning course, 150 -> 750 students) -> the YouTube "Zero to Hero" series ->
nanoGPT and llm.c -> Eureka Labs.

He never treated education as a side project — even at the height of his time at Tesla, he
kept maintaining open-source educational resources. Eureka Labs is turning "what he's always
been doing" into his main pursuit.

---

## Decision 9: proposing "vibe coding" and facing criticism (February 2025)

### The core of the original tweet
"There's a new kind of coding I call 'vibe coding', where you fully give in to the vibes,
embrace exponentials and forget that the code even exists... I just see stuff, say stuff, run
stuff, and copy paste stuff, and it mostly works."

### Reaction and criticism
The term went viral fast, was added to Merriam-Webster, and was named Collins English
Dictionary's 2025 word of the year. Criticism came from Andrew Ng, Simon Willison, and security
researchers (AI-collaborated code has a 2.74x higher vulnerability rate).

### Karpathy's response
He didn't fully concede — instead, he posted describing the distinction between the AI-
assisted coding rhythm of "real professional work" and vibe coding, responding by "adding
context" rather than "admitting fault."

In March 2026, he used vibe coding to build a labor-market AI-exposure chart, which was
misread and then deleted, with the explanation that it was "badly misread — it was a two-hour
Saturday-morning project."

---

## Cross-cutting analysis: his decision pattern

### Pattern 1: engineer identity comes before job title
Every time he feels "management is turning me into a different person," he leaves. He's never
attached to organizational power.

### Pattern 2: the educational mission runs through everything
Eureka Labs isn't "something he thought of after retiring" — it's the destination of
something he's been doing for 20 years.

### Pattern 3: "betting heavily" at key technical inflection points
He's entered before each wave crested (joining OpenAI in 2015, joining Tesla in 2017,
returning right before GPT-4 in 2023), showing early judgment about where things were headed.

### Pattern 4: using "building" to verify understanding
nanoGPT, llm.c, CS231n, LLM101n — every piece of educational output uses "can it be built
from scratch" as the ultimate test.

### Pattern 5: his posture toward criticism is "add context, don't admit fault"
Whether it's the vision-only controversy, the vibe-coding criticism, or the chart-deletion
incident, his response is consistently "you've misread this, let me add context."

### Consistency between words and actions
- Says "I like technical work, not management" -> in action, leaves a management role every
  time
- Says "education is a long-term passion" -> in action, builds Eureka Labs
- Says "building from scratch is the only way to understand" -> in action, writes nanoGPT,
  llm.c

### Open questions about consistency
- The tension between "vibe coding" and his core tenet of "understanding through building" —
  he's never fully explained in public how the two coexist
- How he actually handled Tesla engineers who raised concerns internally about removing radar
  has never been fully disclosed

---

## Key source index

- Karpathy's own statement leaving OpenAI: https://x.com/karpathy/status/1757600075281547344
- His own statement leaving Tesla: https://x.com/karpathy/status/1547332300186066944
- The original vibe-coding tweet: https://x.com/karpathy/status/1886192184808149383
- The Software 2.0 blog post (2017): https://karpathy.medium.com/software-2-0-a64152b37c35
- The Lex Fridman Podcast #333: https://lexfridman.com/andrej-karpathy/
- TechCrunch on leaving OpenAI: https://techcrunch.com/2024/02/13/andrej-karpathy-is-leaving-openai-again-but-he-says-there-was-no-drama/
- The CVPR 2021 vision-only argument: https://bdtechtalks.com/2021/06/28/tesla-computer-vision-autonomous-driving/
- The Eureka Labs introduction: https://techcrunch.com/2024/07/16/after-tesla-and-openai-andrej-karpathys-startup-aims-to-apply-ai-assistants-to-education/
