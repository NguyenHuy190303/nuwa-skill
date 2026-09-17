# Andrej Karpathy — Writings and Core-Argument Research

> Research date: 2026-04-05
> Source labels: primary = quoted directly from his own writing/video; secondary =
> paraphrased/summarized by someone else; inferred = a reasonable inference from context across
> multiple sources
> Blacklist: Zhihu, WeChat Official Accounts, Baidu Baike — none used in this file

---

## 1. Basic information and career timeline

**Born**: October 23, 1986, in Bratislava, Slovakia; moved with his family to Toronto, Canada
at age 15
**Education**:
- University of Toronto: Computer Science + Physics (double major), 2005-2009
- University of British Columbia: Master's in Machine Learning, 2009
- Stanford University: PhD, advised by Fei-Fei Li, graduated 2015, dissertation titled
  "Connecting Images and Natural Language"

**Career timeline (key milestones)**:
- 2015: creates CS231n (Stanford's first deep-learning course, grew from 150 to 750 students)
- 2015-2017: founding research scientist at OpenAI
- 2017-2022: Director of AI at Tesla (reporting to Elon Musk), led Autopilot
- July 2022: leaves Tesla
- February 2023: returns to OpenAI
- February 2024: leaves OpenAI
- July 2024: founds Eureka Labs (an AI-native education company)
- February 2026: releases microgpt (a 200-line, zero-dependency, pure-Python GPT trainer)

Source: [Wikipedia](https://en.wikipedia.org/wiki/Andrej_Karpathy) (primary information
sourced from his own site, karpathy.ai)

---

## 2. Complete list of blog posts (karpathy.github.io)

| Date | Title | URL | Importance |
|------|------|-----|--------|
| 2026-02-12 | microgpt | karpathy.github.io/2026/02/12/microgpt/ | ⭐⭐⭐⭐⭐ his latest major work |
| 2022-03-14 | Deep Neural Nets: 33 years ago and 33 years from now | karpathy.github.io/2022/03/14/lecun1989/ | ⭐⭐⭐⭐ |
| 2021-06-21 | A from-scratch tour of Bitcoin in Python | karpathy.github.io/2021/06/21/blockchain/ | ⭐⭐⭐ |
| 2021-03-27 | Short Story on AI: Forward Pass | karpathy.github.io/2021/03/27/forward-pass/ | ⭐⭐ |
| 2020-06-11 | Biohacking Lite | karpathy.github.io/2020/06/11/biohacking-lite/ | ⭐ |
| 2019-04-25 | A Recipe for Training Neural Networks | karpathy.github.io/2019/04/25/recipe/ | ⭐⭐⭐⭐⭐ the practitioner's bible |
| 2018-01-20 | (started posting on Medium instead) | — | a transition point |
| 2016-09-07 | A Survival Guide to a PhD | karpathy.github.io/2016/09/07/phd/ | ⭐⭐⭐⭐ |
| 2016-05-31 | Deep Reinforcement Learning: Pong from Pixels | karpathy.github.io/2016/05/31/rl/ | ⭐⭐⭐ |
| 2015-11-14 | Short Story on AI: A Cognitive Discontinuity | karpathy.github.io/2015/11/14/ai/ | ⭐⭐ |
| 2015-10-25 | What a Deep Neural Network thinks about your #selfie | karpathy.github.io/2015/10/25/selfie/ | ⭐⭐ |
| 2015-05-21 | The Unreasonable Effectiveness of Recurrent Neural Networks | karpathy.github.io/2015/05/21/rnn-effectiveness/ | ⭐⭐⭐⭐⭐ a classic |
| 2015-03-30 | Breaking Linear Classifiers on ImageNet | karpathy.github.io/2015/03/30/breaking-convnets/ | ⭐⭐ |
| 2014-09-02 | What I learned from competing against a ConvNet on ImageNet | karpathy.github.io/2014/09/02/what-i-learned-from-competing-against-a-convnet-on-imagenet/ | ⭐⭐⭐ |
| 2014-08-03 | Quantifying Productivity | karpathy.github.io/2014/08/03/quantifying-productivity/ | ⭐ |
| 2014-07-03 | Feature Learning Escapades | karpathy.github.io/2014/07/03/feature-learning-escapades/ | ⭐⭐ |
| 2012-10-22 | The state of Computer Vision and AI: we are really, really far away | karpathy.github.io/2012/10/22/state-of-computer-vision/ | ⭐⭐⭐ |
| 2011-04-27 | Lessons learned from manually classifying CIFAR-10 | karpathy.github.io/2011/04/27/manually-classifying-cifar10/ | ⭐⭐ |

**Medium blog**: https://karpathy.medium.com/
Core article:
- [Software 2.0](https://karpathy.medium.com/software-2-0-a64152b37c35) (2017, his most widely
  cited article)

Source: scraped directly from the blog index page (primary)

---

## 3. In-depth analysis of core blog posts

### 3.1 Software 2.0 (2017, Medium)
**Source**: https://karpathy.medium.com/software-2-0-a64152b37c35 (primary)

**Core argument**:
> "Software 1.0 is the explicit instructions humans write by hand in languages like Python or
> C++; Software 2.0 is a neural network's weights — a program generated from data by an
> optimization algorithm."

**Software 1.0 vs. 2.0 comparison**:
- SW1.0: the programmer identifies desired-behavior points in the problem space and writes
  explicit rules by hand
- SW2.0: given input-output pairs, an optimization algorithm searches "program space" for the
  optimal program (the network's weights)

**SW2.0's advantages** (in Karpathy's own account):
1. Computational homogeneity: every operation is matrix multiplication, extremely friendly to
   hardware acceleration
2. Can learn knowledge humans can't articulate explicitly
3. Performance keeps improving with more data and compute (a predictable scaling effect)

**SW2.0's downsides/risks** (which Karpathy acknowledges):
- Results are hard to interpret
- It fails silently
- It may encode biases present in the data

**Domains SW2.0 will "eat"**: visual recognition, speech processing, image translation, image
captioning, game AI, database querying

**The Tesla case**: as Autopilot evolved, C++ code kept getting deleted and replaced by neural-
network weights — a concrete example of SW2.0 "eating" SW1.0.

---

### 3.2 The Unreasonable Effectiveness of RNNs (2015)
**Source**: karpathy.github.io/2015/05/21/rnn-effectiveness/ (primary)

**Core argument**:
> "If training a normal neural network is optimization over function space, training a
> recurrent network is optimization over program space."

**Key experiments** (demonstrating RNN generation ability):
- Paul Graham essays: generating structured startup-wisdom text
- Shakespeare: learning dialogue structure, speaker names, complex syntax
- Wikipedia markdown: automatically discovering the wiki-link format
- LaTeX math: generating almost-compilable mathematical proofs
- Linux kernel C code: generating functions with correctly nested brackets and variable
  declarations

**Technical insight**: about 5% of an RNN's neurons spontaneously learn interpretable
algorithms (quote detection, URL boundaries, bracket counting) — with no explicit guidance.

---

### 3.3 A Recipe for Training Neural Networks (2019)
**Source**: karpathy.github.io/2019/04/25/recipe/ (primary)

**Core premise** (two key observations):
1. Neural-network training is a "leaky abstraction" — you can't treat it as a plug-in, it
   needs real understanding
2. Failure is silent — the network trains but performs poorly, with no obvious error signal

**The six-stage process**:

**Stage 1: become one with the data**
- Spend hours inspecting thousands of examples
- Understand the distribution, patterns, imbalance, and label noise

**Stage 2: an end-to-end skeleton + a baseline**
- Fix the random seed
- Turn off data augmentation
- Verify the loss at initialization matches expectations
- Establish a human baseline
- Overfit a single batch to verify the architecture is viable

**Stage 3: overfit**
- "Don't be a hero": copy a proven architecture, don't invent your own
- Adam with lr=3e-4 is the most forgiving starting point

**Stage 4: regularize (in order of effectiveness)**
1. Get more real data (most effective)
2. Data augmentation
3. Pretraining
4. Dropout (spatial dropout for a ConvNet)
5. Weight decay, early stopping

**Stage 5: tune hyperparameters**
- Random search beats grid search (it better captures how sensitivity differs across
  parameters)

**Stage 6: squeeze out the last drop**
- Model ensembling (a guaranteed ~2% improvement)
- Train for longer than intuition suggests

**Meta-principle**:
> "A 'fast and furious' approach does not work. Success correlates strongly with patience and
> attention to detail."

---

### 3.4 Deep Neural Nets: 33 years ago and 33 years from now (2022)
**Source**: karpathy.github.io/2022/03/14/lecun1989/ (primary)

**Core argument**: at a macro level, deep learning has barely changed in 33 years — it's still
end-to-end optimization of a differentiable neural network via backpropagation. What changed
is scale.

**Order-of-magnitude comparison**:
- Parameter count: about 1,000,000x
- Pixels of image data processed: about 100,000,000x
- Training speed: 3,000x faster on consumer hardware (and another 100x on GPUs)

**Where the performance gains came from**:
- Modern optimization tricks (Adam, dropout, data augmentation): ~60% error reduction
- Larger datasets: a moderate contribution
- Scale: requires more compute

**His 2055 prediction**:
> future practitioners won't train models from scratch — they'll talk to a giant foundation
> model in natural language, telling a "10,000,000x neural super-brain" what to do.

---

### 3.5 microgpt (February 2026)
**Source**: karpathy.github.io/2026/02/12/microgpt/, a GitHub Gist (primary)

**Core claim**: implementing full GPT training and inference in 200 lines of pure Python (zero
dependencies, no PyTorch, no NumPy, no GPU acceleration) — the culmination of his "decade-long
obsession with reducing LLMs to their most fundamental elements."

**What it includes**: a document dataset, a tokenizer, an autodiff engine, a GPT-2-style
architecture, the Adam optimizer, a training loop, and an inference loop.

**Stated belief**:
> "Everything else is just efficiency."

This is the latest practical expression of his belief "if I can't build it, I don't understand
it."

---

## 4. The YouTube teaching series

### Neural Networks: Zero to Hero
**Homepage**: https://karpathy.ai/zero-to-hero.html (primary)
**GitHub repo**: https://github.com/karpathy/nn-zero-to-hero
**Started**: August 2022
**Philosophy**: language models are the best entry point for learning deep learning — even if
your goal is computer vision, everything you learn transfers.

| # | Title | Length | Core content |
|---|------|------|---------|
| 1 | The Spelled-Out Intro to Neural Networks and Backpropagation: Building Micrograd | 2h25m | implementing backpropagation from scratch, needing only high-school calculus |
| 2 | The Spelled-Out Intro to Language Modeling: Building Makemore | 1h57m | a bigram character-level language model, a PyTorch intro |
| 3 | Building Makemore Part 2: MLP | 1h15m | a multilayer perceptron, overfitting/underfitting concepts |
| 4 | Building Makemore Part 4: Activations & Gradients, BatchNorm | 1h55m | gradient-flow analysis, batch normalization |
| 5 | Building Makemore Part 4: Becoming a Backprop Ninja | 1h56m | manual backpropagation, no autograd |
| 6 | Building Makemore Part 5: Building a WaveNet | 56m | a hierarchical convolutional-network architecture |
| 7 | Let's Build GPT: From Scratch, in Code, Spelled Out | 1h56m | building GPT from scratch, following "Attention is All You Need" |
| 8 | Let's Build the GPT Tokenizer | 2h13m | implementing BPE tokenization from scratch, how tokenization shapes LLM behavior |

### Other important videos
- **[1hr Talk] Intro to Large Language Models** (November 2023): for a general audience,
  covering LLM training, the LLM OS metaphor, and safety (jailbreaks/prompt injection)
- **Deep Dive into LLMs like ChatGPT** (February 2025, 3h31m): an in-depth walkthrough of the
  full training stack, building a mental model
- **Let's reproduce GPT-2**: reproducing GPT-2 from scratch

---

## 5. Academic papers (by citation count/importance)

Source: dblp.org + Google Scholar entries (secondary; citation counts are approximate as of
the search date)

| Year | Title | Venue | Co-authors | Core contribution |
|------|------|---------|--------|---------|
| 2017 | Deep Visual-Semantic Alignments for Generating Image Descriptions | IEEE TPAMI | Li Fei-Fei | multimodal alignment (image -> natural-language description) |
| 2016 | **DenseCap**: Fully Convolutional Localization Networks for Dense Captioning | CVPR | Justin Johnson, Li Fei-Fei | dense image captioning |
| 2016 | Connecting Images and Natural Language (PhD dissertation) | Stanford | — | dissertation summary |
| 2017 | PixelCNN++: Improving the PixelCNN with Discretized Logistic Mixture | ICLR | Tim Salimans and others | generative-model improvements |
| 2017 | World of Bits: An Open-Domain Platform for Web-Based Agents | ICML | Tianlin Shi and others | a web-agent benchmark (early agent research) |
| 2015 | ImageNet Large Scale Visual Recognition Challenge | IJCV | Russakovsky, Deng, Fei-Fei, and others | defining the ImageNet benchmark |
| 2015 | Visualizing and Understanding Recurrent Networks | CoRR | Justin Johnson, Li Fei-Fei | RNN visualization and interpretation |
| 2015 | Deep visual-semantic alignments for generating image descriptions | CVPR | Li Fei-Fei | an earlier version of the image-captioning work |
| 2014 | Grounded Compositional Semantics for Finding and Describing Images | TACL | Socher, Le, Manning, Ng | compositional image-text semantics |
| 2014 | Large-Scale Video Classification with ConvNets | CVPR | Toderici, Li Fei-Fei, and others | video understanding |
| 2014 | Deep Fragment Embeddings for Bidirectional Image Sentence Mapping | NIPS | Joulin, Li Fei-Fei | bidirectional image-text embeddings |

**Note**: VGGNet (Very Deep ConvNets for Large-Scale Image Recognition) is the work of Simonyan
& Zisserman — Karpathy contributed to the ImageNet challenge paper, but is not an author of
VGGNet itself. (Correcting a common misattribution.)

**The CS231n course**: founded in 2015, Stanford's first deep-learning course, videos free
online, over 800,000 cumulative views (per TIME magazine).

---

## 6. The complete Software 1.0 / 2.0 / 3.0 framework

**Source**: the 2017 Medium article + the 2025 YC AI Startup School talk (used together, both
primary)

In his 2025 YC AI Startup School talk, Karpathy expanded the framework into three generations:

| Generation | Definition | How you program it | Representative platform |
|------|------|---------|---------|
| Software 1.0 | explicit instructions humans write in a traditional language | the programmer writes code | GitHub |
| Software 2.0 | a neural network's weights, generated from data by an optimizer | curate a dataset + run the optimizer | Hugging Face |
| Software 3.0 | LLMs, programmed via natural-language prompts | write a prompt in English | — |

Key statements:
> "Prompts are now programs that program the LLM."
> "Software 3.0 is eating 1.0/2.0."
> "A huge amount of software will be rewritten."

**The Tesla evidence**: as Autopilot evolved, the neural network kept expanding while the C++
code kept getting deleted — a real-world case of SW2.0 eating SW1.0.

---

## 7. The LLM OS concept

**Source**:
- An X post, September 2023 (primary): https://x.com/karpathy/status/1707437820045062561
- An X post, November 2023 (primary): https://x.com/karpathy/status/1723140519554105733
- The 1hr Talk, Intro to LLMs (November 2023 video) (primary)

**Core analogy**: an LLM isn't a chatbot — it's the kernel process of a new kind of operating
system.

| Traditional OS | LLM OS |
|--------|--------|
| CPU | the LLM (the processor) |
| RAM | the context window (working memory) |
| File system | an embedding database (vector retrieval) |
| System calls | tool calls / API calls |
| Long-running programs | agents |
| I/O devices | multimodal input/output (vision, audio) |

---

## 8. Key coined terms and concepts

### 8.1 Vibe coding (February 2025)
**Source**: https://x.com/karpathy/status/1886192184808149383 (primary)

> "There's a new kind of coding I call 'vibe coding', where you fully give in to the vibes,
> embrace exponentials, and forget that the code even exists."

**Context**: posted on February 6, 2025, describing coding by voice command using Cursor
Composer + Sonnet + SuperWhisper.

**Reach**: viewed an estimated 4.5 million times; Merriam-Webster listed it as "slang &
trending" in March 2025; Collins English Dictionary named it its 2025 word of the year.

### 8.2 Jagged intelligence
**Source**: https://x.com/karpathy/status/1882518317585650084 (primary) + the 2025 LLM Year in
Review (primary)

> "LLMs exhibit amusingly jagged performance characteristics: simultaneously a genius polymath
> and a confused and cognitively challenged grade schooler, seconds away from getting tricked
> by a jailbreak."

This isn't a training flaw — it's a structural consequence of RLVR optimization: capability
spikes sharply in whichever specific domain RLVR training targets, producing an uneven
capability landscape.

### 8.3 LLMs as "summoned ghosts"
**Source**: the 2025 LLM Year in Review (primary)

> "LLMs are not evolved animals but summoned ghosts — entities optimized under entirely
> different constraints than biological intelligence."

His argument: an LLM's neural architecture, training data, training algorithm, and
optimization pressure are completely unlike biological intelligence; it shouldn't be
understood through the lens of "animal evolution," but as "a brand-new type of entity in the
space of possible minds."

### 8.4 LLMs' "anterograde amnesia"
**Source**: the YC AI Startup School 2025 talk (primary)

Compares an LLM to the protagonist of the film *Memento*: lacking the ability to consolidate
long-term memory, relying only on the context window.

---

## 9. Eureka Labs' mission statement

**Source**: https://eurekalabs.ai/ (primary), published July 16, 2024

**Mission**: build a new kind of AI-native school.

**Core belief**:
> "Subject matter experts who are deeply passionate, great at teaching, infinitely patient and
> fluent in all languages are very scarce and cannot personally tutor all 8 billion people on
> demand."

**Proposed solution**: a Teacher + AI Teaching Assistant model — the teacher designs the
curriculum, and the AI assistant is optimized as a tool to guide students through learning,
supporting, leveraging, and scaling the teacher's ability.

**Vision**:
> "If we are successful, it will be easy for anyone to learn anything, expanding education in
> both reach (a large number of people learning something) and extent (any one person learning
> a large amount of subjects, beyond what may be possible today unassisted)."

**First product**: LLM101n: Let's Build A Storyteller (an undergraduate-level course where
students train their own AI)

---

## 10. His philosophy of learning

Source: Twitter/X posts + a Stanford advice page (primary)

### Core tenet 1: learning should not be fun
> "Learning is not supposed to be fun. It doesn't have to be actively not fun either, but the
> primary feeling should be that of effort."

### Core tenet 2: opposing the "shortification of learning"
**Source**: https://x.com/karpathy/status/1756380066580455557 (primary, February 2024)

> "There are a lot of videos on YouTube/TikTok etc. that give the appearance of education, but
> if you look closely they are really just entertainment."

His prescription: close those quick-post tabs, "seek the meal" — textbooks, documentation,
papers, manuals, long-form writing. Set aside a 4-hour block: read, take notes, reread,
restate, process, and manipulate the material.

### Core tenet 3: build to understand
> "If I can't build it, I don't understand it."

This runs through micrograd, makemore, nanoGPT, and microgpt — every one a "hand-built from
scratch" proof of genuine understanding.

### Core tenet 4: read primary sources
His recommended LLM reading list includes reading the original papers directly (Attention Is
All You Need, GPT-2, InstructGPT, and more) rather than secondary explanations.

---

## 11. Core views from the Dwarkesh Patel podcast

**Source**: https://www.dwarkesh.com/p/andrej-karpathy (secondary summary; the original
podcast is primary)

**AGI timeline**: still about 10 years out (not imminent), the problems are solvable but still
hard.

**His criticism of reinforcement learning** (a counter-intuitive view!):
> "Reinforcement learning is terrible."

His argument: outcome-based reward is "sucking supervision through a straw" — compressing an
entire trajectory's worth of information into a single reward signal, propagating noise
throughout the whole learning process. Humans don't primarily learn through RL — they learn
through reflection, synthetic-data generation (thinking), and distillation during sleep.

**The model-collapse problem**: synthetic-data generation fails because models produce a
"collapsed" distribution, and repeated self-sampling dangerously narrows diversity. Training a
model on its own generated content degrades performance; maintaining entropy requires an
external source of entropy (human interaction, diverse experience).

**The "cognitive core" vision**: future systems will separate knowledge from cognition — a
roughly 1-billion-parameter "cognitive core" that strips out encyclopedic memory but keeps the
reasoning algorithm, looking up knowledge when it's needed the way a human would.

**On computational continuity**: Karpathy rejects a sharp division between "AI and ordinary
computer science." He believes progress is evolutionary: "we are very, very slowly abstracting
ourselves," similar to a compiler replacing assembly. AGI may show up as continuous improvement
rather than a discontinuous leap.

---

## 12. Core arguments that recur (real beliefs, 3+ occurrences)

Below are core positions expressed repeatedly across multiple occasions, ranked by how often
they've been confirmed:

### Argument 1: building from scratch is the only path to understanding ★★★★★
**Where it appears**: micrograd (video + code), the makemore series, nanoGPT, the microgpt
post, the LLM101n course design philosophy, his PhD advice
**Signature statement**:
> "If I can't build it, I don't understand it."

### Argument 2: neural-network training "fails silently" and demands extreme care and
visualization ★★★★★
**Where it appears**: A Recipe for Training NNs (2019), the Zero to Hero course, CS231n
material
**Signature statement**:
> "Neural net training is a leaky abstraction."
> "A 'fast and furious' approach does not work."

### Argument 3: software is going through a fundamental paradigm shift (SW1.0 -> 2.0 -> 3.0)
★★★★★
**Where it appears**: Software 2.0 (2017), the 1hr Intro to LLMs (2023), the YC Startup School
talk (2025), multiple X posts
**Signature statement**:
> "Software 2.0 will eat through Software 1.0."
> "A huge amount of software will be rewritten."

### Argument 4: an LLM is a new kind of computing infrastructure, not a tool ★★★★
**Where it appears**: the LLM OS posts (2023), the 1hr Talk (2023), the YC talk (2025), the
2025 LLM Year in Review
**Signature statement**: the LLM as an OS kernel; the context window as RAM; the Memento
analogy

### Argument 5: an LLM is an entirely new type of entity, not something to be understood
through a biological/human frame ★★★★
**Where it appears**: the 2025 LLM Year in Review, the "summoned ghosts" posts (multiple), the
short-story pieces
**Signature statement**:
> "LLMs are not evolved animals but summoned ghosts."
> "Jagged intelligence"

### Argument 6: AI education needs to be democratized — anyone should be able to learn the
best material ★★★★
**Where it appears**: CS231n released free, the Zero to Hero series (free), the Eureka Labs
mission statement, LLM101n open-sourced
**Signature statement**:
> "If we are successful, it will be easy for anyone to learn anything."

### Argument 7: the essence of deep learning hasn't changed in 33 years — only the scale has
★★★
**Where it appears**: 33 years ago and 33 years from now (2022), the Lex Fridman podcast,
multiple interviews
**Signature statement**:
> "Not much has changed in 33 years on the macro level."

### Argument 8: data quality and quantity are SW2.0's core competitive advantage (beyond
architectural innovation) ★★★
**Where it appears**: descriptions of the Tesla Data Engine, A Recipe for Training NNs ("get
more real data" is the most effective regularizer), the Zero to Hero course
**Signature statement**: in his ranked list of regularization methods, "get more real data" is
#1

---

## 13. Recommended reading/resources (revealing his intellectual lineage)

### Required reading (Karpathy's recommended LLM starter list)
Source: karpathy.ai's LLM reading list (primary)

1. Attention Is All You Need (the original Transformer paper)
2. Language Models are Unsupervised Multitask Learners (the GPT-2 paper)
3. Training Language Models to Follow Instructions (InstructGPT)
4. Llama 2: Open Foundation and Fine-Tuned Chat Models
5. RLAIF: Scaling Reinforcement Learning from Human Feedback with AI
6. Training Compute Optimal Language Models (Chinchilla)
7. Sparks of Artificial General Intelligence: Early Experiments with GPT-4

### Recommended learning resources
- His own CS231n notes
- *Deep Learning* (Goodfellow and others)
- *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (recommended for
  beginners)
- Read the original papers directly, don't rely only on secondary explanations

**Inferred intellectual lineage (inferred)**:
- An affinity for the Feynman method of teaching ("build from scratch" = "if you can teach it
  to someone else, that means you understand it")
- Deep familiarity with LeCun's work (the "33 years ago" post directly reproduces LeCun's 1989
  paper)
- Personal correspondence with Bahdanau (the inventor of the attention mechanism) — he
  published their private email exchange, with consent)

---

## 14. Known contradictions and tensions (recorded as-is, not reconciled)

**Contradiction 1: criticizing RL vs. praising RLVR**
- On the Dwarkesh podcast: calls "reinforcement learning terrible," criticizing outcome-based
  reward
- In the 2025 LLM Year in Review: calls RLVR (Reinforcement Learning from Verifiable Rewards)
  2025's most important training-paradigm shift, with high praise

A possible reconciliation: what he criticizes is traditional RL with sparse reward (like
policy gradients); what he praises is RLVR with a verifiable reward. But this distinction
isn't always made explicit in the source text.

**Contradiction 2: modest predictions vs. bold vision**
- "AGI still a decade away" (a modest 10-year timeline)
- Meanwhile describing a future educational revolution where "anyone can learn anything," and
  "a huge amount of software will be rewritten"

This isn't necessarily a contradiction, but there's a tension: his predictions are relatively
conservative, while his actions (founding Eureka Labs, betting on SW3.0) assume the
transformation is imminent.

**Contradiction 3: opposing the "shortification of learning" vs. producing a huge volume of
explainer videos himself**
He criticizes YouTube content that gives the appearance of education but is really
entertainment, yet his own Zero to Hero series is itself a set of YouTube videos.
A possible distinction: his videos demand heavy cognitive investment (2+ hours, requiring
hands-on work), fitting his own definition of the kind that "requires effort."

---

## 15. Source index

| Source | URL | Reliability |
|------|-----|--------|
| Personal blog (karpathy.github.io) | http://karpathy.github.io/ | Primary |
| Medium blog | https://karpathy.medium.com/ | Primary |
| Personal site | https://karpathy.ai/ | Primary |
| Zero to Hero course page | https://karpathy.ai/zero-to-hero.html | Primary |
| X account | https://x.com/karpathy | Primary |
| Eureka Labs site | https://eurekalabs.ai/ | Primary |
| His bearblog year-in-review | https://karpathy.bearblog.dev/ | Primary |
| dblp paper list | https://dblp.org/pid/04/9925.html | Primary (a bibliographic database) |
| Google Scholar | https://scholar.google.com/citations?user=l8WuQJgAAAAJ | Primary (a bibliographic database) |
| YC Startup School talk summary | https://www.latent.space/p/s3 | Secondary (a full transcript is available) |
| The Dwarkesh podcast | https://www.dwarkesh.com/p/andrej-karpathy | Secondary (a full transcript is available) |
| Wikipedia biography | https://en.wikipedia.org/wiki/Andrej_Karpathy | Secondary (broadly reliable) |
| Stanford personal page | https://cs.stanford.edu/people/karpathy/ | Primary |
| The Vibe Coding wiki page | https://en.wikipedia.org/wiki/Vibe_coding | Secondary (used for corroboration) |
