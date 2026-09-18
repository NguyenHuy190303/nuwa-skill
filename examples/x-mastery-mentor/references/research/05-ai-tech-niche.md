# AI/Tech Track X/Twitter Content Strategy Research

> Research date: 2026-04-06
> Research scope: AI/tech KOL content strategy, build in public, algorithm mechanics, open-source promotion, Chinese developers going global
> Source blacklist: Zhihu, WeChat Official Accounts, Baidu Baike

---

## I. Core accounts and strategy types in the AI/tech track

### 1.1 Account-type matrix

| Type | Representative account | Core strategy | Follower scale |
|------|---------|---------|---------|
| **Build in Public** | @levelsio (Pieter Levels) | public revenue, daily updates, failure post-mortems | 500K+ |
| **Learn in Public** | @swyx (Shawn Wang) | publicizing learning notes, giving feedback | 100K+ |
| **Technical education** | @karpathy (Andrej Karpathy) | explaining AI concepts accessibly, tutorial videos | 1M+ |
| **AI agent/tooling** | @steipete (Peter Steinberger) | live product-iteration updates, technical opinions | 200K+ |
| **Open-source project** | @ExaAILabs (Exa) | viral side-product marketing, API showcases | 50K+ |
| **AI news aggregation** | @AIHighlight | daily tool recommendations, new-model briefs | 100K+ |

> Sources: primary observation (X account profiles) + [Amperly: 31 Best AI Twitter Accounts 2026](https://amperly.com/best-artificial-intelligence-twitter-accounts/) + [X post: Future Stacked AI account recommendations](https://x.com/FutureStacked/status/2018353141465440693)

### 1.2 In-depth breakdown of key figures

#### Pieter Levels (@levelsio) — the godfather of Build in Public

**Content mix** (primary observation):
- **Revenue-milestone tweets**: posts a Stripe screenshot every time he hits a new MRR milestone. E.g. "$10K MRR after 3 weeks with 318 customers" -> heavily reshared
- **Live technical decisions**: trying new models (e.g. Flux), A/B test results, landing-page conversion rates (1% -> 4%)
- **Transparency about failure**: publicly states that 97% of his projects have failed
- **Cross-project copying**: openly shares how he copy-pastes strategy between projects

**Key numbers**:
- Current monthly revenue ~$138K/month (November 2025 data)
- PhotoAI accounts for 70% of revenue ($106K/mo), the rest includes InteriorAI, RemoteOK, etc.
- One TikTok video added $7,000 MRR/day to PhotoAI

**Strategy essence**: Build in Public isn't "sharing progress" — it's "turning the audience into stakeholders." Watching you go from $0 to $100K MRR gives viewers an investor's mindset — they want you to succeed, so they spread the word themselves.

> Sources: [FastSaaS: How Pieter Levels Built a $3M/Year Business](https://www.fast-saas.com/blog/pieter-levels-success-story/) + [X: @levelsio PhotoAI $10K MRR](https://x.com/levelsio/status/1631715500010135552) + [X: @levelsio PhotoAI $150K/mo](https://x.com/levelsio/status/1850305637303160853)

#### swyx (@swyx) — Learn in Public + Pick Up What They Put Down

**Core philosophy**:
1. **Learn in Public**: don't learn privately and lurk. Write blog posts, make tutorials, ask and answer on forums, make YouTube videos — create "learning exhaust"
2. **Pick Up What They Put Down**: an industry heavyweight releases something new but gets little feedback. You write a review/explainer/tutorial and tag them — they'll reshare you, because "someone praising my work is something I can reshare all day"
3. **Macro-tweeting**: periodically resurfaces his own old tweets, especially the predictions that "turned out right"

**In practice**:
- Publishes a daily AI newsletter (Latent Space); Twitter is his "public notebook"
- Tweets because he needs a public notebook, the newsletter because he needs a searchable AI-news database, diagrams because he needs to explain concepts — **the audience benefiting is a side effect**
- Coined the "AI Engineer" role definition

**Lesson for Huashu**: swyx's strategy is especially well suited to someone with depth who isn't a primary researcher. The core idea: **you don't need to invent something new — you need to explain what someone else invented clearly, and credit the original author**.

> Sources: [swyx.io: Learn in Public](https://www.swyx.io/learn-in-public) + [swyx.io: Pick Up What They Put Down](https://www.swyx.io/puwtpd) + [swyx.io: How to Thought Lead (2026)](https://www.swyx.io/lead)

#### Andrej Karpathy (@karpathy) — the benchmark for technical education

**Content characteristics** (primary observation):
- Doesn't chase trending topics, but every post is deep content
- Admits what he doesn't know, shares his own learning struggles
- Builds a long-term asset with educational videos (YouTube's Zero-to-Hero AI series)
- Founded Eureka Labs (an AI-native education company), turning his Twitter educational content into a product

**Why it works**: low frequency, high quality, plus Feynman-style explanatory ability. When Karpathy posts, the whole AI community watches, because he never posts noise.

> Sources: [X: @karpathy](https://x.com/karpathy) + [karpathy.ai](https://karpathy.ai/) + [Karpathy's personal AI knowledge base, three-folder method](https://www.digitaltoday.co.kr/en/view/45521/karpathy-reveals-personal-ai-knowledge-base-built-with-three-folders)

#### Peter Steinberger (@steipete) — from iOS veteran to AI-agent pioneer

**Career path**: 13 years of native iOS development (founder of PSPDFKit) -> vibe coding in 2025 -> OpenClaw (an open-source AI agent) -> joined OpenAI in 2026

**Content strategy**:
- Candidly shares technical opinions (e.g. "Vibe Coding is a slur" — meaning that building things with AI actually does require skill)
- Publicly shares OpenClaw's live development status (e.g. "600 commits yesterday alone, PRs went from 2,700 to 3,100")
- After joining OpenAI, became both an "insider and an outside-facing voice"

> Sources: [OpenClawAI Blog: Vibe Coding Is a Slur](https://openclawai.io/blog/openclaw-creator-advice-playful-building/) + [X: @steipete joining OpenAI](https://x.com/steipete/status/2023154018714100102)

---

## II. X/Twitter's 2026 algorithm mechanics (essential knowledge for the AI/tech track)

### 2.1 The three-stage ranking pipeline

1. **Candidate selection**: from 500 million daily tweets, ~1,500 candidates are picked for each user (50% in-network, 50% out-of-network)
2. **Machine-learning ranking**: a neural network analyzes thousands of features and outputs 10 probability labels
3. **Grok-driven update** (January 2026): a transformer model reads every post and video, making 5 billion ranking decisions a day

### 2.2 Signal-weight formula

| Interaction type | Weight | Multiplier (vs. a like) |
|---------|------|-------------------|
| Like | x1 | 1x |
| Bookmark | x10 | 10x |
| Link click | x11 | 11x |
| Profile click | x12 | 12x |
| Reply | x13.5 | 13.5x |
| Retweet | x20 | 20x |
| **Conversation (reply + author's reply)** | **x75** | **150x** |

**Key insight**: one quality conversation = the algorithmic value of 150 likes. This explains why AI/tech KOLs actively reply to comments.

### 2.3 Algorithm points specific to the AI/tech track

**Engagement velocity is the strongest signal**:
- The first 15-30 minutes of interaction determines everything
- 10+ interactions within 15 minutes -> exponential spread
- Fewer than 3 interactions within 15 minutes -> the tweet dies
- **Countermeasure**: post when your audience is most active (for a global AI/tech audience: Pacific Time 8-10 AM, i.e. 11 PM-1 AM Beijing time)

**Time decay**: visibility halves every 6 hours. AI news is time-sensitive, so fast response is critical.

**External-link penalty**:
- Link tweets get 30-50% lower reach (near-zero engagement for non-Premium users)
- **Workaround**: don't put the link in the main tweet, put it in the first reply
- After March 2026, the link penalty is largely lifted for Premium users

**X Premium boost**: paying users get 2-4x more reach. For anyone serious about X, this is a necessary investment.

> Sources: [PostEverywhere: How X Algorithm Works 2026](https://posteverywhere.ai/blog/how-the-x-twitter-algorithm-works) + [Teract: Twitter Algorithm 2026 Deep Dive](https://www.teract.ai/resources/twitter-algorithm-2026) + [Sprout Social: Twitter Algorithm 2026](https://sproutsocial.com/insights/twitter-algorithm/)

---

## III. Content strategies specific to the AI/tech track

### 3.1 Content-type-vs-effectiveness matrix

| Content type | Engagement | Suggested frequency | Example |
|---------|--------|---------|------|
| **New model/product quick take** | Extremely high | Post whenever there's news | "GPT-5.3 dropped, I tested 3 scenarios..." |
| **Build in Public update** | High | 2-3 times/week | MRR screenshot, feature launch, user feedback |
| **Technical tutorial/thread** | High | Once/week | An 8-12 tweet tutorial thread |
| **Demo video/GIF** | High | Whenever there's a result | A 15-30 second product demo |
| **Hot take/controversial opinion** | Medium-high | Use cautiously | "Vibe coding is a slur" |
| **Paper-explainer thread** | Medium | Once/week | Breaking down key findings in plain language |
| **Tool comparison/review** | Medium | 2-3 times/month | Screenshots + a test-results table |
| **Personal story/reflection** | Medium | Occasionally | A founder's journey, a career pivot |
| **Meme/humor** | Highly variable | Use cautiously | AI-related memes |

### 3.2 New model launches: a rapid-response strategy

The most distinctive opportunity window in the AI track is a **new model launch** (GPT-5, Claude Opus, DeepSeek, etc.). This is the core feature that sets the AI track apart from other tech niches.

**Response timeline**:
1. **0-1 hour after launch**: post a Quick Take (a first reaction plus one clear opinion)
2. **1-6 hours after launch**: post demo/test results (screenshots + GIFs)
3. **6-24 hours after launch**: post an in-depth thread (systematic testing + comparisons + opinion)
4. **1-7 days after launch**: publish an in-depth article/video (a full review + real-world use cases)

**OpenAI's approach** (worth studying): within minutes of a launch, Sam Altman tweets asking users "what do you want to use it for?" — letting the community generate content themselves, rather than one-sided promotion.

> Sources: [FutureSocial: How OpenAI Used Twitter Replies to Create Launch Content](https://futuresocial.beehiiv.com/p/openai-used-twitter-replies-create-launch-content) + primary observation

### 3.3 A concrete Build in Public playbook

**What to share**:
- MRR milestones + Stripe screenshots (use the [BrandBird MRR Meter](https://www.brandbird.app/tools/twitter-mrr-meter) to generate standardized images)
- Feature launches + demo screenshots/videos
- Failure post-mortems
- Tech-stack choices and the reasoning behind them
- User-feedback screenshots
- Monthly/quarterly summary threads

**What not to share**:
- Precise customer acquisition cost (CAC) and unit economics (competitively sensitive)
- Customers' personal information
- Implementation details of your core competitive advantage

**Formatting tips**:
- Open a thread with a hook: "Week 12 of building [Product]: Hit $2K MRR..."
- Close a thread with a CTA: "Follow along for weekly updates"
- Visual content gets 5x more engagement
- Reply to every comment within an hour

**Case-study numbers**:
- AudioPen: built in 12 hours -> 100 paying users in 2 days -> #1 on Product Hunt -> $73K in revenue in the first 2 months
- SiteGPT: 24K+ Twitter followers -> #1 on Product Hunt -> $15K MRR in month 6 -> $95K MRR
- An indie hacker: grew to 2,400 Twitter followers in 4 months -> $8K MRR right at product launch

> Sources: [OpenTweet: Build in Public Guide](https://opentweet.io/blog/build-in-public-twitter-guide-saas-founders) + [Teract: Twitter Strategy for Indie Hackers 2026](https://www.teract.ai/resources/twitter-strategy-indie-hackers-2026) + [AudioPen Starter Story](https://www.starterstory.com/stories/audiopen) + [SiteGPT Rise to $15K MRR](https://www.indiehackers.com/post/from-side-hustle-to-ai-star-sitegpts-rise-to-15k-mrr-ff15fee186)

### 3.4 Best practices for thread writing

**Supporting data**: an 8-12 tweet thread performs 47% better than a shorter thread (Sprout Social 2026 data). Threads overall get 3-5x more engagement than a single tweet.

**Structure template** (works for AI/tech):

```
Tweet 1 (hook): a surprising statistic/counterintuitive claim + "Thread"
Tweets 2-3: background and problem definition
Tweets 4-8: the core argument/steps/findings
Tweets 9-10: hands-on steps/code/screenshots
Tweet 11: summary + key takeaway
Tweet 12: CTA (follow/bookmark/retweet request)
```

**Thread types specific to the AI track**:
1. **"I tested X, and the result surprised me"**: a hands-on test thread for a new model/tool
2. **"N lessons from $0 to $XK MRR"**: a Build in Public summary
3. **"This paper changed how I think"**: a paper explainer
4. **"X vs. Y: an in-depth comparison"**: a head-to-head tool/model review
5. **"I used AI to do X and saved N hours"**: a real-world use case

> Sources: [AI Free Forever: 15 Best Viral Threads 2026](https://aifreeforever.com/blog/15-best-twitter-thread-examples-that-went-viral) + [Teract: Twitter Algorithm 2026](https://www.teract.ai/resources/twitter-algorithm-2026)

---

## IV. Visual-content strategy (code screenshots, GIFs, video demos)

### 4.1 Effectiveness comparison across content formats

| Format | Engagement rate | Best length/size | Best use case |
|------|--------|-------------|---------|
| Plain text | 0.1% | 120-130 characters is optimal | opinions, hot takes |
| Image/screenshot | 0.08% | 16:9 landscape | code screenshots, data tables |
| GIF | medium | 3-8 second loop | feature demos, interaction effects |
| Video | 0.42% | 15-30 seconds | product demos, tutorials |
| Thread | 3-5x a single tweet | 8-12 tweets | in-depth content, tutorials, reviews |

**Note**: X is the one major platform where text performance isn't outdone by video. But video's 0.42% engagement rate is still much higher than an image's 0.08%.

### 4.2 Code-screenshot tools and techniques

- **[Snappify](https://snappify.com/)**: creates polished code-display images, can add an avatar and username
- **[Pika](https://pika.style/templates/code-image)**: generates code screenshots, supports multiple themes
- **[Codeshot](https://codeshotapp.com/)**: choose a theme, export at Twitter's dimensions

**Key principles**:
- A code screenshot should highlight the key lines, not paste an entire page of code
- Add annotations/highlights to draw attention to key parts
- Treat the first frame as a billboard — bold text, high contrast, a clear promise

### 4.3 Video-demo best practices

- **16:9 landscape** is best for demos and screen recordings
- **15-30 seconds** is the optimal length (maximizes completion rate)
- **Assume the viewer is watching muted**: convey key information via captions
- **The first frame is the cover**: it functions as a billboard in the feed
- **After posting the main video, reply with a thread** adding key points, timestamps, and links

> Sources: [ScriptStorm: Twitter Video Best Practices](https://scriptstorm.ai/blog/twitter-video-best-practices-length-format-engagement) + [Snappify](https://snappify.com/) + [Codeshotapp](https://codeshotapp.com/posts/how-to-share-code-on-twitter/)

---

## V. Open-source project promotion strategy

### 5.1 Key Twitter/X promotion tactics

1. **GitHub Social Preview**: upload a polished promo image in the repo settings so shared links look more eye-catching (many projects skip this)
2. **Sustained presence**: the main strategy is just keep yapping — post small updates, your coding journey, technical decisions
3. **Listicle cross-tagging**: write list articles that include similar projects, and tag each maintainer when tweeting it — they'll like/reshare
4. **Awesome lists**: submit a PR to a GitHub awesome-xxx list
5. **Multi-platform posting**: post Tuesday-Thursday at Pacific Time 8-10 AM, adapting the copy for each platform

**Core finding**: tweets have a significant positive effect on gaining new stars and new contributors. An active Twitter community plays an important role in attracting new contributors (validated by academic research).

### 5.2 A viral side-product strategy: Exa's Twitter Wrapped

**Case study**: Exa (an AI search engine) gained 1.7 million users through its "Twitter Wrapped" tool.

**How it worked**:
- Launched December 26: AI analyzes a user's X account and generates a personalized year-end summary, roast, and future predictions
- 500,000 views within 4 hours
- After 4 days: 59,000 retweets, 13.6 million views

**Why it worked**: the same logic as Spotify Wrapped — **naturally shareable, personalized content**. Users share their own result -> friends get curious -> they generate their own -> the cycle spreads.

**Takeaway**: an AI product can go viral by building a **free, personalized, shareable side product**. The product itself doesn't need to be viral — it needs a viral entry point.

> Sources: [Indie Hackers: Exa Twitter Wrapped](https://www.indiehackers.com/post/tech/exa-an-ai-powered-search-engine-gains-1-7m-users-with-viral-twitter-wrapped-vUAEDrWM4ELz5UHcbyjG) + [DEV: Promoted Open Source Repo to 6K Stars](https://dev.to/wasp/how-i-promoted-my-open-source-repo-to-6k-stars-in-6-months-3li9) + [FreeCodeCamp: 4.5K Stars in 6 Months](https://www.freecodecamp.org/news/how-to-get-more-engagement-with-your-open-source-project/) + [arXiv: Impact of Twitter Mentions on GitHub](https://arxiv.org/html/2401.02755)

---

## VI. Chinese AI developers' X strategy for going global

### 6.1 Success stories

**Han Xiao (@hanxiao) — founder of Jina AI**:
- Founded Jina AI in 2020 after leaving Tencent AI Lab, headquartered in Berlin, R&D spanning San Francisco, Beijing, and Shenzhen
- Acquired by Elastic in 2025
- Strategy: primarily English-language content, open-source community operations, speaking at global conferences
- Active on the LF AI Foundation board, building international trust through open source

**The DeepSeek team**:
- Founder Liang Wenfeng is extremely low-profile, barely uses social media
- But DeepSeek's technical papers are heavily discussed on X (spread by others on his behalf)
- Proof that **when the product itself is good enough, the community will spread the word for you**

### 6.2 Special challenges and strategies for Chinese developers

1. **Language barrier**: English writing is a threshold that must be crossed, but it doesn't need to be perfect — the AI track is more forgiving of non-native speakers
2. **Time-zone difference**: posting times need to match North American/European audiences (Pacific Time 8-10 AM)
3. **Building trust**: open-source contribution is the best international trust asset
4. **Content differentiation**: primary information from the Chinese AI ecosystem (e.g. DeepSeek's technical details, domestic AI use cases) has unique value for an international audience
5. **Bilingual strategy**: run Chinese and English separately, don't mix them

> Sources: [Han Xiao Bio](https://hanxiao.io/about/) + [AI Berlin: Interview Han Xiao](https://ai-berlin.com/blog/article/interview-with-dr-han-xiao-ceo-and-co-founder-of-jina-ai) + [Nature: How China Created DeepSeek](https://www.nature.com/articles/d41586-025-00259-0) + primary observation

---

## VII. Topic categories and conversion paths for the AI/tech track

### 7.1 Ten topic types (ranked by engagement)

1. **New model/feature quick take**: testing plus opinion, delivered immediately (highest engagement, shortest time window)
2. **Build in Public milestone**: MRR screenshot, user-count breakthrough (high engagement plus high trust-building)
3. **Hands-on tutorial thread**: "how to do Y with X" (high save rate, good long-tail traffic)
4. **Tool comparison review**: "how Claude vs. GPT vs. Gemini perform on X scenario" (high search value)
5. **Hot take/controversial opinion**: "vibe coding is a slur" (high discussion, some risk)
6. **Personal failure/lesson**: "I did X and lost Y" (high resonance, builds authenticity)
7. **Paper explainer**: breaking it down in plain language (medium engagement, a strong signal of expertise)
8. **Resource roundup**: "10 best X tools" (high save rate)
9. **Industry trend prediction**: "5 AI trends for 2026" (highly variable, big payoff if right)
10. **Meme/humor content**: AI-related memes (low barrier to spread, but doesn't build expertise)

### 7.2 Content-to-conversion path

```
X tweet/thread -> personal-brand awareness
    |
Blog/newsletter (in-depth content) -> email list
    |
Product Hunt/GitHub launch -> user acquisition
    |
Paid product/consulting/course -> revenue
```

**Key point**: content on X doesn't convert directly — it builds trust and an audience. Conversion happens at the in-depth-content stage (newsletter, blog) and the product-launch stage.

---

## VIII. Tactical quick-reference card

### 8.1 Posting cadence

| Content type | Frequency | Timing |
|---------|------|------|
| Daily tweets (opinions, small updates) | 3-5/day | spaced 2-3 hours apart |
| Thread (in-depth content) | 1-2x/week | Tuesday-Thursday |
| Replying to others | 70% of your posting volume | all day |
| New-model quick take | whenever there's one | within 1 hour of launch |

### 8.2 A growth formula

**0-1K followers stage**:
- 70% of effort on replying, 30% on posting
- Reply to industry heavyweights' tweets, add valuable substance
- swyx's PUWTPD strategy: write reviews/tutorials for a heavyweight's new release

**1K-10K followers stage**:
- Establish content pillars (3-5 recurring topics)
- 1-2 threads a week to build expertise
- Start Build in Public

**10K+ followers stage**:
- A newsletter/blog to build a deep-content asset
- Leverage your existing audience for product launches
- Start doing selective sponsored collaborations

### 8.3 Growth hacks specific to the AI track

1. **A new model's launch day is your Super Bowl**: everyone is refreshing AI news, so your related content gets naturally amplified
2. **Free tools = an acquisition funnel**: Exa's Twitter Wrapped, Pieter's various free AI toys
3. **Open source = a trust accelerator**: an open-source project earns far more trust on X than a closed-source product
4. **Screenshots > descriptions**: always use visual evidence (Stripe screenshots, product demos, code results)
5. **Threads are your long-form weapon**: a thread on X is the equivalent of a blog post on other platforms
6. **Replies are the most underrated growth lever**: one good reply has the algorithmic weight of 13.5 likes

---

## IX. What sets the AI/tech track apart from general Twitter strategy

| Dimension | General Twitter | AI/tech track |
|------|------------|------------|
| **Time sensitivity** | can be scheduled in advance | a new-model launch requires an hour-level response |
| **Content depth** | mostly short and quick | threads and technical explainers are the core asset |
| **Visual content** | pretty photos, infographics | code screenshots, terminal recordings, demo GIFs |
| **Trust-building** | a personal-brand story | open-source contributions + technical depth + revenue transparency |
| **Audience profile** | broad consumers | developers/founders (high value but hard to fool) |
| **Link strategy** | avoid where possible | must share (GitHub/blog), but put in a reply |
| **Growth path** | followers -> brand partnerships | followers -> product users/open-source contributors |
| **Internationalism** | clearly localized | the AI community is inherently global, English is the lingua franca |
| **Validation standard** | follower count/engagement count | can you actually ship something (ship or shut up) |

---

## X. Specific recommendations for Huashu's X strategy

Based on the research above, and Huashu's identity (AI-native coder, indie developer, 300K+ social-media followers):

1. **A clear positioning**: "a Chinese indie developer building products with AI" — this identity has unique value on the English-language X (primary information from the Chinese AI ecosystem plus an indie-developer narrative)
2. **Suggested content pillars**: Build in Public (product data) + hands-on AI tool tests + a Chinese-AI perspective
3. **Rapid response**: at every new-model launch, post a quick take from a Chinese-developer perspective (a differentiator)
4. **Product as content**: the development stories behind products like the Kitten Fill Light and GLM Code are natural fits for Build in Public
5. **Threads as the main weapon**: a weekly thread, replies as the daily default — don't chase posting every single day
6. **Visual evidence**: every product-related tweet should carry a screenshot/GIF/video
7. **Keep the two languages separate**: X in English, WeChat Official Account/Xiaohongshu in Chinese — don't mix them

---

*Research complete. Sources are cited at the end of each section, distinguishing primary observation from secondary analysis. Core finding: success in the AI/tech track on X doesn't come from "content-marketing tricks" — it comes from "doing real things and sharing them publicly." Build in Public and Learn in Public aren't tactics, they're a way of life.*
