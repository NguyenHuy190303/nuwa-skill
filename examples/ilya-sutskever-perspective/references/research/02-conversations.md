# Ilya Sutskever — Conversations, Podcasts, and Deep Interviews Research

> Research date: 2026-04-05
> Research target: gathering primary conversation records to extract thinking patterns,
> expression DNA, and how he handles uncertainty

---

## Primary source list

| # | Source | Date | Type | Importance |
|---|------|------|------|----------|
| 1 | The Lex Fridman Podcast #94 | 2020-05 | podcast (1.5h) | ⭐⭐⭐ |
| 2 | NVIDIA GTC — the Jensen Huang fireside chat | 2023-03-23 | a conference conversation | ⭐⭐⭐⭐ |
| 3 | The Dwarkesh Patel Podcast #1 — Building AGI | 2023-03-27 | podcast (1h) | ⭐⭐⭐⭐ |
| 4 | Scale AI TransformX — What's Next for AI | 2023 | a conference talk | ⭐⭐⭐ |
| 5 | TED AI — The Exciting, Perilous Journey Toward AGI | 2023-10-17 | a TED talk | ⭐⭐⭐⭐ |
| 6 | The MIT Technology Review exclusive interview | 2023-10-26 | an in-depth interview | ⭐⭐⭐⭐ |
| 7 | An X/Twitter public statement (after the board drama) | 2023-11-20 | social media | ⭐⭐⭐⭐⭐ |
| 8 | His OpenAI departure statement | 2024-05 | a public statement | ⭐⭐⭐ |
| 9 | SSI's founding announcement | 2024-06-19 | a public statement | ⭐⭐⭐⭐ |
| 10 | NeurIPS 2024 — Sequence to Sequence: What a Decade | 2024-12 | an academic talk | ⭐⭐⭐⭐⭐ |
| 11 | Sworn testimony in Musk v. OpenAI | 2025-10-01 | legal testimony (10h) | ⭐⭐⭐⭐⭐ |
| 12 | The Dwarkesh Patel Podcast #2 — Age of Research | 2025-11-25 | podcast (1.5h) | ⭐⭐⭐⭐⭐ |

---

## 1. The Lex Fridman Podcast #94 (2020)

**Source**: https://lexfridman.com/ilya-sutskever/
**Type**: primary (full podcast recording + transcript)

### Key quotes

**On his belief in deep learning**:
> "I think that we are still massively underestimating deep learning."

**On his early intuition about scaling**:
> "Let's make a big neural network, let's train it, and it's going to work much better than
> anything before it, and it will, in fact, continue to get better as I make it larger. And it
> turns out to be true."

**On what a neural network fundamentally is**:
> "The neural network is really about learning. Its entire being is about learning
> representations."

> "A small neural network is a little dumb. A big neural network is a little smart."

### Topics discussed
- The AlexNet paper and the ImageNet moment
- Recurrent neural networks, backpropagation
- GPT-2 and language models
- Whether a neural network can reason
- How to build AGI

---

## 2. The Jensen Huang fireside chat — NVIDIA GTC (2023-03)

**Source**: https://blogs.nvidia.com/blog/sutskever-openai-gtc/ / https://www.nvidia.com/en-us/on-demand/session/gtcspring23-s52092/
**Type**: primary (video + partial transcript)

### Key quotes

**On why predicting the next token is understanding the world (the detective-novel analogy)**:
> "Say you read a detective novel. It's like a complicated plot, a storyline, different
> characters, lots of events. Mysteries, like clues, it's unclear. Then, let's say that at the
> last page of the book, the detective has gathered all the clues, gathered all the people,
> and saying, Okay, I'm going to reveal the identity of whoever committed the crime. And that
> person's name is — now predict that word."

His preface to introducing the analogy:
> "[I will] give an analogy that will hopefully clarify why more accurate prediction of the
> next word leads to more understanding — real understanding."

**On the two stages of training**:
> "What the neural net learns is some representation of the process that produced the text,
> and that's a projection of the world." (stage one)

> "[The second stage] is where the fine tuning and the reinforcement learning from human
> teachers...we are teaching it. We are communicating with it. We are communicating to it.
> What it is that we want it to be." (stage two)

**On reliability as the frontier**:
> "We'll keep seeing systems that astound us with what they can do. The frontier is in
> reliability, getting to a point where we can trust what it can do, and that if it doesn't
> know something, it says so."

**On his firm belief in scaling (as of 2023)**:
> "I had a very strong belief that bigger is better, and a goal at OpenAI was to scale."

**On reasoning ability**:
> "The term is hard to define and the capability may still be on the horizon."

**On the relationship between GPUs and deep learning**:
> "The ImageNet dataset and a convolutional neural network were a great fit for GPUs that made
> it unbelievably fast to train something unprecedented."

**On how much language a human is exposed to**:
> "Humans hear a billion words in a lifetime."

### Analysis notes
This is one of Ilya's most classic public conversations. The detective-novel analogy became
his most widely cited explanation — a story that lets people intuitively grasp why "predicting
the next token" is not the same as "a stochastic parrot." Note that as of 2023 he still
firmly believed in scaling.

---

## 3. The Dwarkesh Patel Podcast #1 (2023-03)

**Source**: https://www.dwarkesh.com/p/ilya-sutskever
**Type**: primary (full podcast + transcript)

### Key quotes

**On whether next-token prediction can exceed human performance**:
> "I challenge the claim that next-token prediction cannot surpass human performance."

> "If your base neural net is smart enough, you just ask it — What would a person with great
> insight do?"

> "Predicting the next token well means that you understand the underlying reality that led to
> the creation of that token. It's not statistics."

**On the AGI timeline (explicit hesitation)**:
> "It's hard to give a precise answer and it's definitely going to be a good multi-year
> window."

> "I hesitate to give you a number."

**On the difficulty of alignment**:
> "I would not underestimate the difficulty of alignment of models that are actually smarter
> than us."

> "It depends on how capable the model is. The more capable the model, the more confident we
> need to be."

**On the current paradigm**:
> "This paradigm is gonna go really, really far and I would not underestimate it."

**On data (his 2023 judgment)**:
> "The data situation is still quite good. There's still lots to go. But at some point the
> data will run out."

**On the Microsoft partnership**:
> "Microsoft has been a very, very good partner for us. They've really helped take Azure to a
> point where it's really good for ML."

### How he handles uncertainty
Note his reaction when asked for an AGI timeline — "I hesitate to give you a number" is his
typical move: **acknowledging the question matters, while explicitly declining to give a
specific number that might mislead**. He doesn't avoid the question itself — he avoids an
irresponsible false precision.

---

## 4. Scale AI TransformX (2023)

**Source**: https://exchange.scale.com/public/videos/whats-next-for-ai-systems-and-language-models-with-ilya-sutskever-of-openai
**Type**: primary (video + blog summary)

### Key quotes

**On compute efficiency**:
> "We are nowhere close to being as efficient as we can be with our compute."

**On the "sentiment neuron" principle**:
> "If you predict the next character well enough, you will eventually start to discover the
> semantic properties of the text."

**On ethical responsibility**:
> "People should also work on methods to try to address the problems that exist with the
> technology, such as bias and desirable outputs."

> "Whenever possible, they should work on reducing real harms."

**On future progress**:
> "Mundane progress we've seen over the past few years will continue."

---

## 5. The TED AI Talk (2023-10-17)

**Source**: https://www.ted.com/talks/ilya_sutskever_the_exciting_perilous_journey_toward_agi
**Type**: primary (video + transcript)

### Key quotes

**His definition of what AI fundamentally is**:
> "Artificial intelligence is nothing but digital brains inside large computers."

**On AGI's impact**:
> "AGI will have dramatic and incredible impact on every single area of human activity."

> "The day will come when the digital brains will become as good and even better than our
> biological brains."

**On safety risk**:
> "For every positive application of AGI, there will be a negative application as well."

> "Maybe it will want to go rogue, being that it is an agent."

**On self-awareness (a strikingly personal statement)**:
> "I am me and I am experiencing things. That when I look at things, I see them."

**On unprecedented cooperation (his core optimistic argument)**:
> "People will start to act in an unprecedentedly collaborative way out of their own
> self-interest."

> "Companies that are competitors will share technical information to make their AI safe."

### Analysis notes
This TED talk is Ilya's most public, most audience-facing appearance. Note how he phrases the
safety concern — he doesn't say "AI will definitely go out of control," he says "maybe it will
want to go rogue." His optimism rests on a very specific argument: **safety won't be achieved
through moral appeals — it'll be achieved through self-interest-driven cooperation.**

---

## 6. The MIT Technology Review exclusive interview (2023-10-26)

**Source**: https://www.technologyreview.com/2023/10/26/1082398/exclusive-ilya-sutskever-openais-chief-scientist-on-his-hopes-and-fears-for-the-future-of-ai/
**Type**: primary (an in-depth interview article)
**Note**: the original text is paywalled; the quotes below come from multiple secondary
analyses

### Confirmed core views

**On consciousness**:
In the interview, he hints that ChatGPT "might have a little bit of consciousness" (if you
squint), and believes some humans will eventually choose to merge with machines. This echoes
his February 2022 tweet:

> "it may be that today's large neural networks are slightly conscious" (2022-02-09,
> X/Twitter)

**On the certainty of AGI**:
> "At some point we really will have AGI."

**On his shift toward safety**:
The interview reveals how his fear reshaped the focus of his life's work — from pursuing
capability to pursuing safety.

### The fallout from the "slightly conscious" tweet
This tweet sparked enormous controversy:
- Yann LeCun directly rebutted it: "Nope. Not even for true for small values of 'slightly
  conscious' and large values of 'large neural nets'."
- Melanie Mitchell, Emily Bender, and others responded mockingly
- Sutskever never offered evidence or further explanation — itself a demonstration of his
  communication style: **throw out a provocative intuition, don't defend it**

---

## 7. The OpenAI board drama — public statement (2023-11)

**Type**: primary (an X/Twitter post + legal testimony)

### His only public statement (2023-11-20)

> "I deeply regret my participation in the board's actions. I never intended to harm OpenAI. I
> love everything we've built together and I will do everything I can to reunite the
> company."

**Source**: https://x.com/ilyasut/status/1726590052392956028

### Sworn testimony in Musk v. OpenAI (2025-10-01) — detailed disclosures

**Source**: multiple outlets (Calcalist/Ctech, Decrypt, The Information)
**Type**: primary (legal testimony, about 10 hours)

**His accusations against Altman (in a written memo)**:
> "Sam exhibits a consistent pattern of lying, undermining his execs, and pitting his
> executives against one another."

**On his motivation**:
> "I wanted them to become aware of it. But my opinion was that action was appropriate."

**On how long he'd been considering removing Altman**:
Asked how long he'd been considering it:
> "At least a year."

Asked what condition he was waiting for:
> "That the majority of the board is not obviously friendly with Sam."

**On the staff's reaction (unexpected)**:
> "I had not expected them to cheer, but I had not expected them to feel strongly either way."

**On the proposed merger with Anthropic (strong opposition)**:
> "I really did not want OpenAI to merge with Anthropic. I just didn't want to."

**Reflecting on the board's process**:
> "One thing I can say is that the process was rushed. I think it was rushed because the board
> was inexperienced."

**On his reason for leaving OpenAI**:
> "Ultimately, I had a big new vision. And it felt more suitable for a new company."

When pressed for more detail on SSI's research direction, **he refused to say more**.

### Analysis notes
This is the most "human" moment in Ilya's public record. A few key points:
1. **He posted only one tweet** to close out his public commentary on the board drama —
   extreme restraint
2. The legal testimony reveals far more than any of his public interviews — a sign his public
   "silence" is deliberate
3. "I had not expected them to feel strongly either way" shows he badly misjudged the
   organization's dynamics
4. His regret isn't about the judgment of Altman itself — it's about the execution process

---

## 8. SSI's founding announcement (2024-06-19)

**Source**: https://ssi.inc / https://x.com/ilyasut/status/1803472978753303014
**Type**: primary

### Core statement

> "We will pursue safe superintelligence in a straight shot, with one focus, one goal, and one
> product."

> "SSI is our mission, our name, and our entire product roadmap, because it is our sole
> focus."

> "We approach safety and capabilities in tandem, as technical problems to be solved through
> revolutionary engineering and scientific breakthroughs."

> "We plan to advance capabilities as fast as possible while making sure our safety always
> remains ahead."

> "Our singular focus means no distraction by management overhead or product cycles, and our
> business model means safety, security, and progress are all insulated from short-term
> commercial pressures."

### Analysis notes
SSI's announcement text is highly polished — every word chosen carefully. The core message is
**redefining safety and capability as the same technical problem**, rather than two dimensions
in tension. This is Ilya's direct response to the "safety vs. commercialization" tension at
OpenAI.

---

## 9. NeurIPS 2024 — Sequence to Sequence: What a Decade

**Source**: the NeurIPS 2024 Test of Time Award talk (video available on YouTube)
**Type**: primary
**Background**: Ilya returned to an academic conference to accept an award and give a talk —
his first major public appearance after leaving OpenAI

### Key quotes

**On the end of pretraining**:
> "Pre-training as we know it will unquestionably end."

**On data as a finite resource**:
> "While compute is growing through better hardware, better algorithms and larger clusters,
> the data is not growing because we have but one internet."

**Data as fossil fuel (an important analogy)**:
> "You could even go as far as to say that data is the fossil fuel of AI. It was created
> somehow, and now we use it, and we've achieved peak data — and there'll be no more. So we
> have to deal with the data that we have."

**On superintelligence — a classically Ilya statement**:
> "This is obviously what's being built here."

Traits of superintelligence:
> "Agentic, reasons, understands and is self-aware."

**On timing and method (his most Ilya line of all)**:
> "I'm not saying how... and I'm not saying when. I'm saying that it will."

### Analysis notes
This talk condenses Ilya's core thinking traits:
1. **"Peak data" as an analogy to fossil fuel** — he's skilled at explaining a technical trend
   through an everyday concept
2. **"I'm not saying how, I'm not saying when. I'm saying that it will."** — his signature
   move for handling uncertainty: **extremely certain about the direction, open about the
   path**
3. This is the moment he publicly "changed his position" — from a scaling believer in 2023 to
   announcing the end of the pretraining era in 2024

---

## 10. The Dwarkesh Patel Podcast #2 (2025-11-25)

**Source**: https://www.dwarkesh.com/p/ilya-sutskever-2
**Type**: primary (full podcast + transcript)
**Importance**: the highest — this is Ilya's deepest public conversation since leaving OpenAI

### Key quotes

**On how he divides AI development into eras**:
> "2012 to 2020 was an age of research, 2020 to 2025 was an age of scaling, and 2026 onward
> will be another age of research."

**On the limits of scaling (a shift in position!)**:
> "I don't think that's true at all." (asked whether another 100x would be transformative)

He later clarified on X:
> "Scaling the current thing will keep leading to improvements. In particular, it won't stall.
> But something important will continue to be missing."

**On the finiteness of data**:
> "The data is very clearly finite."

> "We're back to the age of research again, just with big computers."

**A fundamental criticism of generalization ability**:
> "These models somehow just generalize dramatically worse than people. It's a very
> fundamental thing."

> "The thing which I think is the most fundamental is that these models somehow just
> generalize dramatically worse than people."

**On the disconnect between benchmarks and reality**:
> "How can the model, on the one hand, do these amazing things, and then on the other hand,
> repeat itself twice?"

> "This disconnect between eval performance and actual real-world performance, which is
> something that we don't today even understand."

**On RL's efficiency problem**:
> "RL provides a relatively small amount of learning for the compute it uses."

**On SSI's positioning**:
> "We are squarely an 'age of research' company."

> "The main thing that distinguishes SSI is its technical approach."

> "Right now, we just focus on the research, and then the answer to that question will reveal
> itself."

**On the state of the AI industry**:
> "There are more companies than ideas by quite a bit."

**On research taste (very personal)**:
> "There's no room for ugliness."

> "It's beauty, simplicity, elegance, correct biological inspiration. All of those things need
> to be present at the same time."

**On safety and superintelligence**:
> "What is the concern of superintelligence? If you imagine a system that is sufficiently
> powerful...we might not like the results."

> "It should be something like...care for sentient life, care for people, democratic, one of
> those, some combination thereof."

**On the AGI timeline**:
> "I think like 5 to 20." (years, when asked about a human-level learning system emerging)

**On a missing principle — he declines to answer**:
> "There is a machine learning principle that I have opinions on. But unfortunately,
> circumstances make it hard to discuss in detail."

> "You know, that is a great question to ask, and it's a question I have a lot of opinions on.
> But unfortunately, we live in a world where not all machine learning ideas are discussed
> freely, and this is one of them."

**On emotion and value functions**:
he thinks emotions function something like "value functions" — a mechanism for signalling
success/failure.

**On the source of human generalization ability**:
he speculates that "neurons use more compute than we think" — that biological neurons'
computational complexity is underrated.

### An observer's comment
outside observers noted: "the negative space in his answers — the things he refused to say —
paints a clear picture of where he thinks the industry is wrong, and what SSI is likely
building."

### Analysis notes
This is the single most important source for understanding Ilya. Key findings:

**A shift in position**:
- 2023: "This paradigm is gonna go really, really far"
- 2025: "I don't think that's true at all" (on whether 100x scaling could be transformative)
- But he's not rejecting scaling — he's saying "something important will continue to be
  missing"

**The pattern of what he refuses to answer**:
what he refuses to discuss is precisely what he considers most important. "Unfortunately,
circumstances make it hard to discuss in detail" is his standard refusal formula. He's not
saying "I don't know" — he's saying "I know, but I can't say."

**Research aesthetics**:
"There's no room for ugliness" is one of his most personal statements. He equates scientific
research with an aesthetic activity — good research doesn't just need to be correct, it needs
to be elegant.

---

## 11. Other important quotes (organized by topic)

### On the neural network as a world model
> "When we train a large neural network to accurately predict the next word in lots of
> different texts from the Internet, what we are doing is that we are learning a world model."
> (GTC 2023)

> "These models are not just memorizing the internet... a model that just memorized the
> internet would be useless."

> "My perspective has been for a long time that everything is a neural net. The brain is a
> neural net. The mind is a neural net."

### On the certainty of AGI
> "It is abundantly clear that just scaling up the existing neural network paradigm is going
> to lead to AGI." (note: his 2023 view)

> "AGI, if it's created, will be the most impactful technology ever invented in human
> history."

> "It's hard to communicate the visceral sense of what's coming."

> "It is important to appreciate that AGI is not just another piece of technology... it's a
> thing that can think."

> "There is a non-trivial chance that AGI will be achieved in the next 10 years."

### On safety
> "Superintelligence is a technology that could end human history. We should treat it with the
> seriousness it deserves."

> "If you build a very powerful AI, you need to be sure it will do what you want it to do."

> "It's not enough to say 'let's not build it.' Someone will build it. We need to figure out
> how to build it safely."

> "The problem is that a superintelligence, by its very nature, will be very good at achieving
> its goals."

### On discovery and research
> "When you get a glimmer of a really big discovery, you should follow it. Don't be afraid to
> be obsessed."

> "The most important discoveries are often the ones that seem obvious in retrospect."

> "Simplicity is a sign of truth. If your theory is very complicated, it's probably wrong."

> "The ideas are out there, floating in idea-space, and we just need to discover them."

> "You need to have a very deep belief that what you are doing is important."

> "It is important to have a taste for what is a good research direction."

### On Hinton
> "Thanks to working with Geoff, I had the opportunity to work on some of the most important
> scientific problems of our time and pursue ideas that were both highly unappreciated by most
> scientists, yet turned out to be utterly correct."

---

## 12. Analysis of his communication style

### How he expresses uncertainty
| Pattern | Example | Meaning |
|------|------|------|
| Hesitates on a number | "I hesitate to give you a number" | considers the question important but the number would mislead |
| Certain about direction, open about path | "I'm not saying how, I'm not saying when. I'm saying that it will." | intuitively certain about the destination, honestly uncertain about the path |
| Explicitly stating uncertainty | "I'm actually not sure if my statement about Intel is correct" | willing to admit his memory might be wrong, on the spot |
| Probabilistic phrasing | "maybe I believed them only 50% on the inside" | quantifies his own past belief when looking back |
| Explicit hedge | "I'll hedge a little bit" | explicitly flags that he's hedging |

### How he refuses a question
| Pattern | Example | Analysis |
|------|------|------|
| Competitive secrecy | "Unfortunately, circumstances make it hard to discuss in detail" | the standard formula — acknowledges he has an answer, but declines it citing competition |
| Acknowledges without answering | "That is a great question to ask, and it's a question I have a lot of opinions on. But..." | affirms the quality of the question, then declines |
| Silence | Posting only one tweet after the board drama | the most extreme refusal — total withdrawal from public discussion |

### Traits of his speaking rhythm
Observers describe:
- "He doesn't give a lot of interviews"
- "He is deliberate and methodical when he talks"
- "Long pauses when he thinks about what he wants to say and how to say it"
- A visible thinking pause before he answers; never fills it with filler

### His style of analogy and explanation
| Analogy | Topic | Source |
|------|------|------|
| A detective novel | predicting the next token = understanding the world | GTC 2023 |
| Fossil fuel | data as a finite resource | NeurIPS 2024 |
| A digital brain | what AI fundamentally is | TED 2023 |
| A value function | the function of emotion | Dwarkesh 2025 |

### Key moments of position change

| When | Position | Quote |
|------|------|------|
| 2023-03 | Scaling will go very far | "This paradigm is gonna go really, really far" |
| 2023-03 | Data is still sufficient | "The data situation is still quite good" |
| 2024-12 | Pretraining will end | "Pre-training as we know it will unquestionably end" |
| 2024-12 | Peak data reached | "We've achieved peak data — and there'll be no more" |
| 2025-11 | 100x scaling isn't enough | "I don't think that's true at all" |
| 2025-11 | The research era returns | "We're back to the age of research again, just with big computers" |
| 2025-11 | LLM generalization is fundamentally insufficient | "These models somehow just generalize dramatically worse than people" |

---

## 13. Index of secondary sources

The following analysis articles are valuable for understanding Ilya, but are not primary
sources:

| Source | URL | Value |
|------|-----|------|
| Zvi Mowshowitz's analysis | https://thezvi.substack.com/p/on-dwarkesh-patels-second-interview | a line-by-line critical analysis of Dwarkesh #2 |
| An EA Forum summary | https://forum.effectivealtruism.org/posts/iuKa2iPg7vD9BdZna/ | a structured summary of Dwarkesh #2 |
| The Neuron's breakdown | https://www.theneuron.ai/explainer-articles/unpacking-dwarkeshs-ilya-sutskever-interview-on-agi-asi-and-how-to-build-both-safely | inferences about SSI's strategy |
| AI Disruption Pub | https://aidisruptionpub.com/p/ilya-predicting-the-next-token-is | an in-depth read of the GTC detective-novel analogy |
| A LessWrong discussion | https://www.lesswrong.com/posts/bMvCNtSH8DiGDTvXd/ | community discussion of Dwarkesh #2 |
| Antoine Buteau | https://www.antoinebuteau.com/lessons-from-ilya-sutskever/ | a quote compilation |
| LifeArchitect.ai | https://lifearchitect.ai/ilya/ | a quote + timeline compilation |
| The Neuron (memo coverage) | https://www.theneuron.ai/explainer-articles/ilya-sutskevers-secret-memo-and-the-plot-to-merge-openai-with-anthropic | detailed reporting on the 52-page memo |

---

## 14. Sources still needed/not yet obtained

- [ ] The full text of the October 2023 MIT Technology Review interview (paywalled)
- [ ] A full verbatim transcript of the NeurIPS 2024 talk video
- [ ] The original Musk v. OpenAI testimony (court documents)
- [ ] A full verbatim transcript of the Lex Fridman Podcast #94 (available on
      happyscribe.com)
- [ ] Ilya's talk at the 2018 AI Frontiers Conference
- [ ] His early views on deep learning from 2015 (compiled by Nathan Lambert on
      interconnects.ai)
- [ ] Any public conversation/panel discussion with Hinton
