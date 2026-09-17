# Ilya Sutskever: Major Decisions, Turning Points, and Controversial Actions

> Research date: 2026-04-05
> Sources: Wikipedia, TechCrunch, Time, Fortune, Axios, CNBC, Gizmodo, Decrypt, the Dwarkesh
> Patel Podcast, Calcalist, the EA Forum, LessWrong, The Neuron, Israel Hayom
> Excluded sources: Zhihu, Baidu Baike, WeChat Official Accounts

---

## 1. An academic career decision: studying under Hinton

### Background
Ilya Sutskever was born in 1986 in Russia (the former Soviet Union), emigrated to Israel at
age 5, and moved to Canada at 16. He completed a B.S. in Mathematics (2005), an M.S. in
Computer Science (2007), and a PhD in Computer Science (2013), all at the University of
Toronto.

### The choice
Chose Geoffrey Hinton as his advisor, betting on neural networks at a time when deep learning
was still marginalized by the mainstream AI academic community.

### The logic
Sutskever had an early intuition for neural networks' potential. Mainstream AI research at the
time leaned toward symbolic approaches and statistical methods; Hinton's connectionist path
was considered a minority position. Choosing Hinton meant betting on an unfashionable
direction.

### The outcome
In 2012, working with Hinton and Alex Krizhevsky, he completed AlexNet, which won the ImageNet
competition by an overwhelming margin, and is regarded as the starting point of the
deep-learning revolution. Hinton later said: "Ilya thought we should do it, Alex made it work,
and I got the Nobel prize."

### Key details
- Sutskever believed early on that neural-network performance would improve with more data
  (the earliest expression of his scaling intuition)
- The emergence of the large-scale ImageNet dataset happened to validate that intuition
  exactly
- This is the intellectual origin point of his later series of scaling bets

**Confidence in the facts: high** (cross-verified across multiple primary sources)

---

## 2. Joining Google Brain (2012-2015)

### Background
After AlexNet's success, Sutskever briefly did a postdoc at Stanford under Andrew Ng (about 2
months), then returned to Toronto to join DNNResearch, the company Hinton founded. Google
acquired DNNResearch in 2013, and Sutskever joined Google Brain along with it.

### The choice
Moved from academia to industry, joining the Google Brain team.

### The logic
Google offered compute and data resources academia couldn't match. The DNNResearch
acquisition was a package deal (Hinton, Krizhevsky, and Sutskever joined together), so this
wasn't entirely an independent personal decision.

### His work at Google
- Collaborated with Oriol Vinyals and Quoc Viet Le to develop the sequence-to-sequence
  learning algorithm (which became the core framework for modern machine translation and
  language modeling)
- Contributed to TensorFlow's early development
- Contributed to the AlphaGo paper (as one of the co-authors)

### The outcome
His work at Google laid the technical foundation for his later push behind the GPT series at
OpenAI, especially his sequence-to-sequence experience.

**Confidence in the facts: high**

---

## 3. Leaving Google, co-founding OpenAI (2015)

### Background
In late 2015, Elon Musk, Sam Altman, and others were organizing a nonprofit AI lab. Sutskever
was a key recruiting target.

### The choice
Gave up Google's generous conditions (resources, compute, team) to join a not-yet-formed
nonprofit AI organization.

### The decision process [confirmed]
This wasn't an easy call. According to Elon Musk's public account in 2023:
- Sutskever went back and forth repeatedly, saying multiple times he'd join OpenAI, then being
  talked into staying by DeepMind's Demis Hassabis
- After several rounds of this tug-of-war, he ultimately decided to join OpenAI
- Musk said "Ilya joining was the linchpin for OpenAI being ultimately successful"

### The logic
- In his own account: he enjoyed his work at Google, but wanted to do more
- OpenAI's nonprofit structure and "benefit humanity" mission may have appealed to him
- As Chief Scientist (rather than one member of a large team at Google), he could lead the
  technical direction

### The outcome
- Became one of OpenAI's six board members
- Received the Chief Scientist title, leading the research direction across the board
- Every major technical breakthrough at OpenAI afterward (the GPT series) was completed under
  his scientific leadership

### Consistency between words and actions
The idealistic motivation behind joining (nonprofit, benefit humanity) later conflicted with
OpenAI's shift toward commercialization — a tension that foreshadowed the 2023 board crisis.

**Confidence in the facts: high** (Musk's testimony as a primary source)

---

## 4. Technical-direction decisions at OpenAI

### 4a. Choosing the GPT/Transformer path

**Background**: in its early days, OpenAI explored several approaches (including
reinforcement learning and robotics). Sutskever pushed the path of language models built on
large-scale unsupervised pretraining.

**The key bet**:
- large-scale unsupervised text pretraining could unlock general capability
- the Transformer architecture (proposed by Google's "Attention is All You Need" paper in
  2017) was well suited to large-scale scaling
- GPT-1 (2018) -> GPT-2 (2019) -> GPT-3 (2020) -> GPT-4 (2023) were all completed under
  Sutskever's scientific leadership

**Confidence in the facts: high**

### 4b. Betting on the scaling hypothesis

**Background**: in 2020, Sutskever led OpenAI's research into neural scaling laws,
establishing the power-law relationship between model performance and scale (parameter count,
data volume, compute).

**The choice**: bet OpenAI's core strategy on "bigger is better."

**The logic**:
- this traces back to the intuition from the AlexNet period: performance improves with more
  data
- scaling laws provided a mathematically formalized prediction framework
- driven together with people like Dario Amodei (who later left to found Anthropic)

**The outcome**:
- GPT-3 and GPT-4's success validated the scaling hypothesis
- OpenAI became, for a time, the global leader in AI

**A later shift in position** [an important contradiction]:
- December 2024, the NeurIPS talk: declares "pre-training as we know it will end," and
  introduces the "peak data" concept ("we have but one internet")
- November 2025, the Dwarkesh Patel interview: explicitly says "2020-2025 was the scaling
  era, and 2026 onward enters the research era"
- when asked whether 100x more scaling would change everything, answers "I don't think that's
  true"
- later clarifies on X: scaling the current method will still bring improvement, but
  "something important will continue to be missing"

**Consistency between words and actions**: this is a significant shift in position. Sutskever
went from the central driver of scaling to one of its questioners. But this isn't necessarily
a contradiction — he may genuinely believe scaling worked in 2020-2025 and has simply hit a
ceiling now. The open question is: what is he actually doing at SSI? If it isn't scaling,
what's the new direction he's betting on? He refuses to say.

**Confidence in the facts: high** (public talks and interviews)

---

## 5. The November 2023 board incident [the most important]

This is the single most controversial decision of Sutskever's career, and also the richest in
disclosed information.

### 5a. Preparation beforehand (at least a year)

**Confirmed facts** (source: sworn testimony, October 1, 2025, nearly 10 hours):
- Sutskever had been considering removing Altman for at least a year
- the condition he was waiting for was "the majority of the board is not obviously friendly
  with Sam"
- he wrote a 52-page memo, organized like a legal brief, accusing Altman of:
  - "a consistent pattern of lying"
  - "undermining his execs"
  - "pitting his execs against one another"
- the memo was sent to the independent board members via disappearing emails, to prevent leaks
- CTO Mira Murati kept screenshots of parts of the memo's content

**A key weak point** [worth noting]:
- Sutskever admitted in testimony that "almost all" of the memo's accusations traced back to a
  single source: CTO Mira Murati
- he admitted he never cross-verified them with the other executives
- he admitted he was relying on "secondhand knowledge"
- his retrospective reflection: "In hindsight, I realize that I didn't know it"

**Confidence in the facts: high** (sworn testimony)

### 5b. The removal action (November 17, 2023)

**Timeline**:
- Nov 17: the board announces Altman's firing
- Nov 18 (the next day): discussion of merging with Anthropic begins
- Nov 20: Sutskever publicly says he "deeply regrets" his role in it
- Nov 21: Altman is reinstated

**Sutskever's motivation** [from multiple sources]:
1. **Safety concerns**: Sutskever believed Altman was pushing AI deployment and
   commercialization too fast, at too much risk
2. **Management problems**: the lying and manipulation the memo documented
3. **A structural tension**: the nonprofit mission vs. commercial pressure

**The Anthropic merger plan** [confirmed]:
- within 48 hours of Altman's firing, the board discussed merging with Anthropic
- board member Helen Toner was "the most supportive" of the merger
- Toner reportedly even said "destroying OpenAI could be consistent with the mission"
- Sutskever himself explicitly opposed the merger: "I really did not want OpenAI to merge with
  Anthropic. I just didn't want to."
- Anthropic raised practical operational obstacles, and the plan never moved forward

**Confidence in the facts: high** (sworn testimony)

### 5c. Employee backlash and regret

**Confirmed facts**:
- 738 of 770 employees signed a petition demanding Altman's reinstatement
- several executives resigned immediately
- Sutskever admits: "I had not expected them to feel strongly either way" (he'd expected
  employees to be indifferent)
- he then posted publicly on X saying he "deeply regrets" his part in it

**Sutskever's retrospective assessment of the process**:
- admits the process was "rushed"
- the reason: "the board was inexperienced"

### 5d. Consistency between words and actions

**Points of contradiction**:
1. spent a year carefully preparing the removal action, yet skipped basic information
   cross-verification (relying on the single source, Murati)
2. claimed to be fighting for safety, yet "deeply regrets" it just three days after the action
3. opposed the Anthropic merger (showing he didn't want to destroy OpenAI), yet launched an
   action that nearly destroyed OpenAI
4. the 52-page memo shows deliberate preparation, yet his prediction of the employee reaction
   was completely wrong

**A possible explanation**:
- his core concern (AI safety) is genuine, but his execution capability fell far short of it
- he is a scientist, not a manager or a politician, and badly underestimated organizational
  dynamics
- "deeply regrets" may have been more of a strategic statement (to preserve his own position)
  than a genuine change of heart

**Confidence in the facts: high** (direct testimony and public statements)

---

## 6. Leaving OpenAI (May 2024)

### Background
After the November 2023 incident, Sutskever's position at OpenAI became awkward. He kept the
Chief Scientist title, but his actual influence had been marginalized.

### The choice
Formally announced his departure from OpenAI on May 14, 2024.

### His public statement
- posted on X: "The company's trajectory has been nothing short of miraculous, and I'm
  confident that OpenAI will build AGI that is both safe and beneficial under the leadership
  of @sama"
- later, in a Calcalist interview, said: "Ultimately, I had a big new vision...it felt more
  suitable for a new company"

### The collapse of the Superalignment team
- days after Sutskever left, Superalignment's co-lead Jan Leike also resigned
- Leike publicly criticized OpenAI: its "safety culture and processes have taken a backseat to
  shiny products"
- Leike said the team was "under-resourced," "sailing against the wind"
- OpenAI subsequently dissolved the entire Superalignment team
- the team had been founded in 2023, with a commitment of 20% of compute at the time

### Consistency between words and actions
- his public statement when leaving was extremely friendly (praising Altman's leadership),
  sharply contrasting with the 52-page memo of accusations he'd written earlier
- a possible reason: an equity agreement may have barred him from public criticism, or it was
  a strategic choice
- Jan Leike's resignation statement indirectly corroborates that Sutskever's long-standing
  safety concerns were genuine

**Confidence in the facts: high**

---

## 7. Founding SSI (June 2024 to present)

### 7a. The founding decision

**When**: announced June 19, 2024

**Co-founders**:
- Daniel Gross (former head of AI at Apple, a Y Combinator partner)
- Daniel Levy (a former OpenAI researcher)

**Offices**: Palo Alto + Tel Aviv

**Core positioning**: "Our first product will be the safe superintelligence, and it will not
do anything else up until then"

### 7b. Fundraising strategy

**Timeline**:
- September 2024: raises $1 billion (a16z, Sequoia, DST Global, SV Angel)
- March 2025: raises another $2 billion, at a $32 billion valuation (Greenoaks Capital leads
  with $500 million, joined by Alphabet, NVIDIA, a16z, Lightspeed, DST Global)
- As of 2025: about 20 employees, zero revenue, a $32 billion valuation

**The fundraising logic**: rests almost entirely on Sutskever's personal reputation. No
product, no revenue, no public technical roadmap.

### 7c. Operating strategy

**Confirmed**:
- no products, no services — just one thing: safe superintelligence
- in April 2025, reached a partnership with Google Cloud for TPU compute
- Sutskever refuses to disclose any technical details

**Leadership changes** (mid-2025):
- Meta attempted to acquire SSI, and Sutskever refused
- in July 2025, co-founder Daniel Gross left to join Meta Superintelligence Labs
- Sutskever took over as CEO, and Daniel Levy was promoted to President

### 7d. Consistency between words and actions

**Contradictions and open questions**:

1. **Safety vs. commerce**: Sutskever left OpenAI because commercial pressure was eroding
   safety. But SSI has taken $3 billion in venture funding, and investors inevitably expect
   returns. How long can it stay "insulated from short-term commercial pressures"?

2. **A scaling skeptic who still depends on compute**: if the scaling era is over, why does he
   still need Google TPUs and $3 billion? What is SSI actually doing?

3. **The time-pressure paradox**: he criticized OpenAI for being too impatient, yet SSI faces
   its own pressure — it can't spend 20 years on "patient research," or investors won't
   tolerate it.

4. **Transparency**: he publicly advocates for AI safety and the public's right to know, yet
   keeps SSI's technical direction entirely secret.

5. **Co-founder attrition**: Daniel Gross was poached by Meta barely a year after SSI's
   founding, hinting at possible issues with team cohesion or direction.

**Confidence in the facts: medium-high** (funding data confirmed, but almost no public
information on the technical direction or internal state)

---

## 8. The evolution of his philosophical stance (across all his decisions)

### Early (2012-2020): pure technical optimism
- believed scaling would unlock everything
- pushed the GPT series to keep growing larger

### Middle period (2020-2023): a safety awakening
- pushed for founding the Superalignment team
- grew increasingly concerned about AI's existential risk
- the 2023 MIT Technology Review interview: discusses the possibility of humans merging with
  machines

### Later period (2024-present): a philosophical turn
- NeurIPS 2024: "pre-training as we know it will end"
- the 2025 Dwarkesh Patel interview:
  - AI development could reach beyond human-level ability in 5-20 years
  - discusses the necessity of emotion in cognition (citing cases of brain-injury patients who
    lost the capacity for emotion)
  - an AI agent may need "intrinsic concern for sentient beings"
  - if most conscious entities in the future are AI, "caring about sentient life dilutes human
    primacy"
  - the long-term equilibrium may be human-machine fusion

### Outside criticism
- his safety strategy relies on AI having sentience, an unverified philosophical assumption
- "safe superintelligence" may not exist in an absolute sense
- the deeper reason behind his shift from a firm scaling driver to a scaling skeptic remains
  unclear

---

## 9. Summary: Sutskever's decision pattern

### Consistent traits
1. **Intuition-driven**: from AlexNet to GPT to SSI, his major decisions are all grounded in
   strong intuition rather than thorough verification
2. **A scientist's mind**: excellent at technical judgment, but repeatedly miscalculates
   organizational management and political maneuvering
3. **An idealistic undercurrent**: whether joining OpenAI or founding SSI, genuine mission-
   driven motivation is present
4. **A tendency toward information silos**: the 52-page memo relied on a single source; his
   prediction of the employee reaction was completely wrong

### A list of contradictions
| Domain | Early position | Later position/behavior | Degree of contradiction |
|------|----------|---------------|----------|
| Scaling | its central driver | declares the era over | medium (explainable as cognitive evolution) |
| OpenAI's mission | nonprofit idealism | praises Altman's leadership on departure | high (conflicts with the 52-page accusation) |
| Safety action | launches the removal | "deeply regrets" it 3 days later | high |
| Transparency | advocates the public's right to know | total secrecy at SSI | medium-high |
| Commercialization | criticizes OpenAI's commercialization | SSI takes $3 billion in VC | medium (different structure, similar pressure) |

### Still to be observed
- what exactly is SSI researching? what is his "big new vision"?
- how long can a $32 billion valuation with zero revenue last?
- will SSI's direction shift after Daniel Gross's departure?
- will Sutskever's view that "emotion is necessary for cognition" show up in SSI's technical
  path?

---

## Sources

### Primary sources (sworn testimony/his own statements/public talks)
- Ilya Sutskever's sworn testimony (October 1, 2025, Elon Musk v. OpenAI)
- the NeurIPS 2024 talk
- the Dwarkesh Patel podcast interview (November 2025)
- the Calcalist Tech interview
- X/Twitter public statements

### Authoritative media coverage
- [TechCrunch: Ilya Sutskever departs](https://techcrunch.com/2024/05/14/ilya-sutskever-openai-co-founder-and-longtime-chief-scientist-departs/)
- [Time: Sutskever leaves OpenAI](https://time.com/6978195/ilya-sutskever-leaves-open-ai/)
- [Fortune: Sutskever deeply regrets](https://fortune.com/2023/11/20/ilya-sutskever-openai-cofounder-deeply-regrets-resign/)
- [Axios: Sutskever regrets firing](https://www.axios.com/2023/11/20/sam-altman-fired-openai-board-illya-sutsever-regrets)
- [CNBC: SSI founding](https://www.cnbc.com/2024/06/19/openai-co-founder-ilya-sutskever-announces-safe-superintelligence.html)
- [CNBC: Sutskever becomes CEO](https://www.cnbc.com/2025/07/03/ilya-sutskever-is-ceo-of-safe-superintelligence-after-meta-hired-gross.html)
- [Gizmodo: Deposition details](https://gizmodo.com/former-openai-exec-explains-why-he-tried-to-do-a-coup-against-sam-altman-2000680769)
- [Decrypt: Inside the deposition](https://decrypt.co/347349/inside-deposition-showed-openai-nearly-destroyed-itself)
- [The Neuron: Secret memo and Anthropic merger](https://www.theneuron.ai/explainer-articles/ilya-sutskevers-secret-memo-and-the-plot-to-merge-openai-with-anthropic)
- [Israel Hayom: SSI in Tel Aviv](https://www.israelhayom.com/2025/03/06/a-secret-ai-startup-in-tel-aviv-got-30b-this-israeli-raised-pioneer-did-it/)
- [Wikipedia: Ilya Sutskever](https://en.wikipedia.org/wiki/Ilya_Sutskever)
- [Wikipedia: Safe Superintelligence Inc.](https://en.wikipedia.org/wiki/Safe_Superintelligence_Inc.)
- [EA Forum: Dwarkesh interview highlights](https://forum.effectivealtruism.org/posts/iuKa2iPg7vD9BdZna/highlights-from-ilya-sutskever-s-november-2025-interview)
