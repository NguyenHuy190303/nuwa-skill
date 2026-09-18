# Research: X/Twitter Platform Algorithm Mechanics

> Research date: 2026-04-06
> Data coverage: the full evolution from the first open-source release in 2023 through the second open-source release in January 2026
> Confidence tiers: 🟢 officially published/verifiable in open-source code | 🟡 reported by authoritative media/data analysis | 🔴 community testing/speculation

---

## I. The evolution of the recommendation-algorithm architecture

### 1.1 The three-stage pipeline

🟢 **Source: GitHub open-source code**

X's recommendation system uses a three-stage pipeline architecture, consistent from its first open-source release in 2023 (`twitter/the-algorithm`) through the 2026 Grok version (`xai-org/x-algorithm`):

| Stage | Function | Implementation |
|------|------|----------|
| **Candidate Sourcing** | narrows hundreds of millions of posts down to ~1,500 candidates | in-network (content from people you follow) + out-of-network (ML retrieval) |
| **Ranking** | predicts engagement probability for each candidate and scores it | Phoenix (a Grok transformer model) |
| **Filtering & Blending** | dedup, diversity guarantees, ad insertion | the Home Mixer orchestration layer |

- Source: [GitHub - xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) | [GitHub - twitter/the-algorithm](https://github.com/twitter/the-algorithm)

### 1.2 Grok fully takes over the recommendation engine (October 2025 -> open-sourced January 2026)

🟢 **Source: Elon Musk's tweets + GitHub releases**

**Timeline:**
- **September 2025**: Musk announced "the algorithm will be purely AI by November," promising to open-source updates every two weeks
- **October 2025**: Grok began fully replacing traditional heuristic rules
- **November 2025**: the Following feed also switched to Grok-based ranking
- **January 20, 2026**: xAI published `xai-org/x-algorithm` on GitHub, formally open-sourcing the Rust-rewritten version

**Key changes:**
- Rewritten from Scala to a **Rust (62.9%) + Python (37.1%)** hybrid architecture
- The core transformer architecture comes from Grok-1, adapted for the recommendation use case
- Grok "reads every post and watches every video" (processing 100M+ pieces of content per day)
- Committed to pushing code updates + developer notes every 4 weeks

- Source: [Elon Musk's tweet](https://x.com/elonmusk/status/1969081066578149547) | [@XEng's tweet](https://x.com/XEng/status/2013471689087086804) | [TechCrunch coverage](https://techcrunch.com/2026/01/20/x-open-sources-its-algorithm-while-facing-a-transparency-fine-and-grok-controversies/) | [Social Media Today](https://www.socialmediatoday.com/news/x-formerly-twitter-switching-to-fully-ai-powered-grok-algorithm/803174/)

### 1.3 The four core modules (2026 open-source version)

🟢 **Source: GitHub repo code and README**

| Module | Language | Function |
|------|------|------|
| **Home Mixer** | Rust | the orchestration layer, receives gRPC requests, coordinates the whole pipeline |
| **Thunder** | Rust | in-memory post storage, consumes Kafka events, serves sub-millisecond in-network content lookups |
| **Phoenix** | Python/JAX | the Grok transformer ranking engine, predicts engagement probability |
| **Candidate Pipeline** | Rust | a reusable framework: Sources fetch -> Hydrators enrich -> Filters filter -> Scorers score -> Selector returns the top N |

- Source: [xai-org/x-algorithm README](https://github.com/xai-org/x-algorithm/blob/main/README.md) | [Phoenix README](https://github.com/xai-org/x-algorithm/blob/main/phoenix/README.md) | [DeepWiki analysis](https://deepwiki.com/xai-org/x-algorithm)

### 1.4 Promptable Feeds

🟡 **Source: Musk's tweets + media coverage**

Users can adjust their feed with natural-language instructions, e.g. typing "Show me more tech innovations, less politics." This is a direct product of embedding Grok into the recommendation engine.

- Musk announced this feature in September 2025
- The January 2026 open-source release includes the promptable-feeds interface
- Source: [WebProNews](https://www.webpronews.com/xs-promptable-algorithm-musks-bid-to-hand-users-the-feed-controls/) | [Social Media Today](https://www.socialmediatoday.com/news/x-formerly-twitter-moving-to-personalized-ai-powered-algorithm/760698/)

---

## II. The engagement-weight formula

### 2.1 The exact weights (verifiable in the open-source code)

🟢 **Source: xai-org/x-algorithm open-source code + confirmed by Social Media Today**

X is the only mainstream social platform to have open-sourced its recommendation algorithm twice, and the engagement weights are fully public:

| Engagement type | Weight | Relative multiple (vs. a Like) | Notes |
|----------|------|---------------------|------|
| **Conversation reply** (a reply the author engages with) | +75 | **150x** | your reply gets replied to/liked by the original post's author |
| **Reply** | +13.5 | **27x** | an ordinary reply |
| **Profile click** | +12.0 | **24x** | a user clicks into your profile and likes or replies |
| **Deep-conversation click** | +11.0 | **22x** | a user clicks into the conversation and replies or likes |
| **Dwell time (> 2 min)** | +10.0 | **20x** | a user clicks into the conversation and stays over 2 minutes |
| **Retweet** | +1.0 | **2x** | a retweet |
| **Like** | +0.5 | **1x (baseline)** | the baseline value |
| **Bookmark** | ~+10 | **~20x** | a community-analysis estimate, not an official exact figure |

**Core insight: conversation depth crushes everything else.** A reply chain that draws the author's engagement is worth more than 150 likes.

⚠️ **On differences between versions**:
- The weights in the first 2023 open-source release differ slightly from the 2026 version
- The commonly cited "Reply 27x, Retweet 40x" figures from early community analyses come from simplified calculations based on the 2023 version
- In the 2026 version, the retweet weight dropped significantly (from ~20x down to ~2x), while conversation weight rose further
- This document uses the 2026 open-source version as the reference

- Source: [Social Media Today](https://www.socialmediatoday.com/news/x-formerly-twitter-open-source-algorithm-ranking-factors/759702/) | [posteverywhere.ai source-code analysis](https://posteverywhere.ai/blog/how-the-x-twitter-algorithm-works) | [Typefully analysis](https://typefully.com/blog/x-algorithm-open-source)

### 2.2 Negative signals (penalty mechanisms)

🟢 **Source: open-source code**

| Negative signal | Penalty weight | Effect |
|----------|----------|------|
| **Report** | -369x | essentially removes it from distribution outright |
| **Block/mute/Show Less** | -74x | heavily reduces future recommendations of that user to you |

🟡 **Source: media analysis**

| Negative signal | Penalty effect |
|----------|----------|
| **An outbound link** | 30-50% lower reach; since March 2025, non-Premium accounts' link posts have a median engagement of zero |
| **More than 2 hashtags** | reach drops ~40%, flagged as a spam signal |
| **Duplicate content/links** | visibility drops progressively, can trigger a shadow ban in severe cases |

- Source: [posteverywhere.ai](https://posteverywhere.ai/blog/how-the-x-twitter-algorithm-works) | [Tweet Archivist](https://www.tweetarchivist.com/how-twitter-algorithm-works-2025)

---

## III. Premium subscription's visibility boost

### 3.1 The algorithmic boost multiplier

🟢 **Source: confirmed in open-source code**

| Scenario | Premium boost | Notes |
|------|-------------|------|
| **In-network (your followers' feeds)** | **4x** | your post is 4x more likely to appear in the feeds of people who follow you |
| **Out-of-network (non-followers' feeds)** | **2x** | your post is 2x more likely to appear in the feeds of people who don't follow you |

### 3.2 Real-world effect data

🟡 **Source: Buffer's analysis of 18.8 million posts + media coverage**

- Premium accounts get roughly **10x** the reach per post compared to regular accounts
- The gap widened further for Premium+ accounts after 2025
- Premium replies rank higher by default in discussions under popular posts (Q1 2026 data shows 30-40% higher reply impressions)
- For non-Premium accounts, posts with outbound links have had a median engagement of zero since March 2026

### 3.3 The relationship between TweepCred and Premium

🟡 **Source: Circleboom analysis**

Premium subscribers get an instant +100 TweepCred boost, moving their starting point from -128 to -28, drastically shortening the account's cold-start period.

- Source: [Circleboom](https://blog-content.circleboom.com/does-x-premium-boost-algorithm/) | [posteverywhere.ai](https://posteverywhere.ai/blog/how-the-x-twitter-algorithm-works) | [Buffer data](https://buffer.com/resources/data-best-content-format-social-media/)

---

## IV. TweepCred: the account-reputation score

🟢 **Source: the TweepCred module in the open-source code**

### 4.1 Basic mechanics

- Every X account has an invisible reputation score: **TweepCred**
- Range: **-128 to +100**
- A new account starts at: **-128**
- The minimum threshold for normal distribution: **+17** (content below this is throttled)
- Premium subscribers get an instant **+100 boost**

### 4.2 Contributing factors

🟡 **Source: community reverse-engineering analysis**

TweepCred is a PageRank-like weighted composite score, determined by:

| Factor | Direction |
|------|------|
| Following/follower ratio | following far more than your follower count -> negative |
| Engagement quality | high-quality conversation -> positive |
| Account history | an older account with consistent behavior -> positive |
| Tweet language and bio | a complete profile -> positive |
| Consistency of posting style | a sudden major change -> negative |
| **Grok sentiment score (new in 2025)** | positive/constructive content -> positive |

⚠️ **New in 2025**: Grok AI now scores the **sentiment** of every post, and positive, constructive content gets more distribution.

- Source: [Circleboom's TweepCred analysis](https://circleboom.com/blog/tweepcred-what-it-is-why-it-matters-and-how-to-increase-your-score-on-x-twitter/) | [Radaar](https://www.radaar.io/resources-121/blog-388/are-you-ready-to-discover-the-hidden-x-algorithm-secrets-behind-tweepcred-shadow-hierarchy-and-dwell-time-in-2025-15361/)

---

## V. How content types are treated

### 5.1 Text vs. video: is X the only platform where text beats video?

🟡 **Source: Buffer's analysis of 45M+ posts + multiple media outlets**

**Conclusion: the picture is more complicated, and the data is contradictory.**

| Data source | Conclusion |
|----------|----------|
| Buffer 2025-2026 data | text posts have a slightly higher median engagement rate (0.48%) than video |
| Multiple SEO/marketing agencies | native video gets roughly 10x more engagement + the algorithm favors distributing it |
| A 2026 social-media strategy report | short video (37%) and text (36%) user preference are nearly tied |

**A more accurate framing**: X is the mainstream social platform where **text posts perform closest to, or even better than, video** — but it's not accurate to simply say "text crushes video." At the algorithmic level, native video does get a distribution boost; but in actual engagement rate, high-quality text posts hold their own against video.

### 5.2 Algorithmic preference by content type

🟡 **Source: a synthesis of multiple analyses**

| Content type | Algorithmic treatment |
|----------|----------|
| **Pure text posts** | consistently the highest engagement rate, especially good at sparking conversation |
| **Native video (< 2:20)** | gets a distribution boost, completion rate is the key signal |
| **Image posts** | increases dwell time, a positive signal |
| **Posts with outbound links** | ⚠️ heavily penalized: 30-50% lower reach, nearly invisible for non-Premium accounts |
| **Quote Tweets** | weighted higher than a plain retweet |
| **Threads (long tweet chains)** | engagement accumulates across multiple tweets, strong overall effect |

- Source: [Buffer](https://buffer.com/resources/data-best-content-format-social-media/) | [Sprout Social](https://sproutsocial.com/insights/twitter-algorithm/) | [SocialBee](https://socialbee.com/blog/twitter-algorithm/)

---

## VI. Key time windows

### 6.1 The golden 30 minutes and Engagement Velocity

🟡 **Source: consensus across multiple analytics firms**

- **The first 30 minutes** is the decisive window: the engagement speed during this window determines whether the algorithm pushes the post into a bigger distribution pool
- The broader **first 2 hours** also matters
- **Speed beats total volume**: 100 likes within 10 minutes beats 500 likes accumulated over 3 days
- The algorithm's core logic: early engagement = a quality stamp

### 6.2 Dwell time

🟢 **Source: the weight definitions in the open-source code**

- A user staying on your post/conversation over 2 minutes = +10 weight (about 20x a Like)
- Short dwell time is treated as a low-quality-content signal, causing the algorithm to suppress it
- This means **long-form writing that makes people want to finish reading** is favored by the algorithm over **short content people scroll past**

### 6.3 Optimal posting times

🟡 **Source: Buffer's analysis of 1M posts + Sprout Social + SocialPilot's analysis of 50K accounts**

| Dimension | Recommendation |
|------|------|
| **Best time window** | weekdays 9AM-2PM (local time), second-best 12PM-6PM |
| **Best days** | Tuesday, Wednesday, Thursday (Tuesday is best) |
| **Worst day** | Saturday |
| **Posting frequency** | **3-5 posts/day** is the optimal range, 2-3 hours apart |
| **Frequency ceiling** | >5 posts/day, growth actually slows |
| **Frequency floor** | <1 post/day, growth is significantly insufficient |

⚠️ The above is based on global English-speaking-user data. Creators posting in Chinese need to adjust to their target audience's time zone (e.g. for readers in China, this corresponds to roughly 9PM-2AM EST in Beijing time).

- Source: [Buffer](https://buffer.com/resources/best-time-to-post-on-twitter-x/) | [Sprout Social](https://sproutsocial.com/insights/best-times-to-post-on-twitter/) | [SocialPilot](https://www.socialpilot.co/insights/best-time-to-post-on-twitter) | [Tweet Archivist](https://www.tweetarchivist.com/twitter-posting-frequency-guide-2025)

---

## VII. Shadow banning

### 7.1 Four types

🟡 **Source: shadowban-detection tools + community analysis**

| Type | Symptom |
|------|------|
| **Search Suggestion Ban** | your username doesn't appear in search suggestions |
| **Search Ban** | your posts don't appear in search results |
| **Ghost Ban** | your replies are invisible to others |
| **Reply Deboosting** | your replies get collapsed into "Show more replies" |

### 7.2 Triggers

🟡 **Source: Pixelscan + multiple guides**

| Behavior | Risk level |
|------|----------|
| Mass following/unfollowing in a short window | 🔴 high (mass unfollowing can trigger a 3-month shadowban) |
| Liking 200+ posts within 1 hour | 🔴 high (triggers automated detection) |
| Replying heavily to people who don't follow you | 🟡 medium |
| Repeatedly posting the same link/hashtag | 🟡 medium |
| Using suspicious third-party tools | 🔴 high |
| Posting content that gets reported by many people | 🔴 high (-369x penalty) |

### 7.3 How to check

- An online tool: [shadowban.yuzurisa.com](https://shadowban.yuzurisa.com/) — enter a username to check all 4 restriction types
- Manual verification: have someone who doesn't follow you search for your username or look up your replies

### 7.4 How to recover

🟡 **Source: consensus across multiple guides**

1. **Stop immediately** whatever triggered it (not gradually reduce — stop completely)
2. Delete duplicate, low-quality posts, or ones with too many links/hashtags
3. Revoke authorization for any suspicious third-party apps
4. **Wait 48-72 hours** (automatic shadowbans are usually lifted within this window)
5. Full recovery cycle: **2-14 days**
6. Keep posting normally, at low frequency and high quality, during the recovery period

- Source: [Pixelscan's guide](https://pixelscan.net/blog/twitter-shadowban-2025-guide/) | [Tweet Archivist](https://www.tweetarchivist.com/twitter-shadowban-complete-guide-2025) | [Multilogin](https://multilogin.com/blog/twitter-shadow-bans/)

---

## VIII. The relationship between ads and organic growth

### 8.1 Paid vs. organic performance

🟡 **Source: WebFX + media coverage**

| Metric | Paid promotion | Organic posting |
|------|----------|----------|
| Average CTR | 1-3% | 0.5-1.5% |
| Premium account reach | — | ~10x that of a regular account |
| Non-Premium link-post engagement | — | 0 (after March 2026) |

### 8.2 Key findings

🟡 **Source: multiple analyses**

- Paid and organic algorithms **run independently** — there is no penalty for "spending money reduces your organic reach"
- But the structural trend is: organic reach keeps declining (a platform-wide phenomenon, not unique to X)
- New followers gained through ads **do** affect the performance of later organic posts (more followers -> more in-network distribution)
- A Premium subscription is essentially **the lowest-cost form of "ad spend"**: the 4x/2x visibility boost far outperforms equivalent ad spend at the same price

- Source: [WebFX](https://www.webfx.com/blog/social-media/x-twitter-marketing-benchmarks/) | [Avenue Z](https://avenuez.com/blog/2025-2026-x-twitter-organic-social-media-guide-for-brands/)

---

## IX. The impact of Community Notes

### 9.1 Impact on post performance

🟢 **Source: a University of Washington study (September 2025)**

| Metric | Change after receiving a Community Note |
|------|--------------------------|
| Retweets | **down 46%** |
| Likes | **down 44%** |
| Views | a smaller effect (the feed algorithm doesn't actively demote noted posts) |

### 9.2 Key details

- X does **not** actively demote noted posts at the algorithmic level
- The decline mainly comes from **a change in user behavior**: after seeing the note, users retweet and like less
- **Timing matters enormously**: a note added more than 48 hours later has almost no effect (the content has already finished spreading)
- Notes are **most effective against manipulated media** (fake photos/videos)

### 9.3 Implications for creators

🔴 **Speculation/strategic recommendation**

- When posting a factual claim that could be controversial, make sure you have a source
- A Community Note doesn't directly hurt algorithmic weight, but it **indirectly kills engagement** (retweets -46%)
- A noted post keeps its view count but has its spread cut in half
- Constructive, well-sourced content is less likely to get noted

- Source: [University of Washington study](https://www.washington.edu/news/2025/09/18/community-notes-x-false-information-viral/) | [Wikipedia - Community Notes](https://en.wikipedia.org/wiki/Community_Notes)

---

## X. Core takeaways for content creators

### 10.1 Algorithm-optimization priorities (ranked by ROI)

| Priority | Strategy | Basis |
|--------|------|------|
| **P0** | spark conversation, reply to every comment | conversation replies carry 150x weight |
| **P0** | subscribe to Premium | 4x/2x visibility + TweepCred boost + link-post visibility |
| **P1** | ignite engagement in the first 30 minutes | engagement speed determines distribution volume |
| **P1** | write long-form content that makes people stop and read | dwell time carries 20x weight |
| **P2** | post on weekdays 9AM-2PM | the data-verified best window |
| **P2** | avoid outbound links (or put them in the comments) | a 30-50% reach penalty |
| **P3** | keep a positive/constructive tone | Grok's sentiment score affects distribution |
| **P3** | keep hashtags to 2 or fewer | more than 2 triggers a spam classification |

### 10.2 Absolute no-gos

| Behavior | Consequence |
|------|------|
| Mass following/unfollowing in a short window | a 3-month shadowban |
| Using automation tools to fake engagement | permanent damage to account reputation |
| Frequently posting outbound links (non-Premium) | posts become almost invisible |
| Posting content that gets reported | -369x penalty, content vanishes outright |
| Suddenly changing your posting pattern | TweepCred drops |

### 10.3 X's unique advantages (compared to other platforms)

- **The only mainstream platform to have open-sourced its algorithm twice**: allows precise optimization
- **Text-friendly**: doesn't force you into video the way other platforms do
- **Conversation-driven**: genuinely rewards deep exchange rather than surface-level engagement
- **Promptable Feeds**: users can customize their recommendations, meaning high-quality niche content has long-tail value

---

## Appendix: source list

### Official/primary sources
- [xai-org/x-algorithm GitHub](https://github.com/xai-org/x-algorithm) — the Grok-based algorithm open-sourced in January 2026
- [twitter/the-algorithm GitHub](https://github.com/twitter/the-algorithm) — the first open-source release, 2023
- [Elon Musk's tweet (Sept. 2025)](https://x.com/elonmusk/status/1969081066578149547) — announcing the algorithm would go fully AI
- [@XEng's tweet (Jan. 2026)](https://x.com/XEng/status/2013471689087086804) — announcing the new open-source algorithm

### Authoritative media coverage
- [TechCrunch: X open sources its algorithm](https://techcrunch.com/2026/01/20/x-open-sources-its-algorithm-while-facing-a-transparency-fine-and-grok-controversies/)
- [Social Media Today: Key ranking factors](https://www.socialmediatoday.com/news/x-formerly-twitter-open-source-algorithm-ranking-factors/759702/)
- [Social Media Today: Grok algorithm shift](https://www.socialmediatoday.com/news/x-formerly-twitter-switching-to-fully-ai-powered-grok-algorithm/803174/)

### Data analysis
- [Buffer: Best content format 2026 (an analysis of 45M+ posts)](https://buffer.com/resources/data-best-content-format-social-media/)
- [Buffer: Best time to post (an analysis of 1M posts)](https://buffer.com/resources/best-time-to-post-on-twitter-x/)
- [Sprout Social: Twitter algorithm 2026](https://sproutsocial.com/insights/twitter-algorithm/)
- [University of Washington: Community Notes study](https://www.washington.edu/news/2025/09/18/community-notes-x-false-information-viral/)

### In-depth community analysis
- [posteverywhere.ai: a source-code breakdown](https://posteverywhere.ai/blog/how-the-x-twitter-algorithm-works)
- [Typefully: algorithm-update analysis](https://typefully.com/blog/x-algorithm-open-source)
- [Circleboom: an in-depth TweepCred breakdown](https://circleboom.com/blog/tweepcred-what-it-is-why-it-matters-and-how-to-increase-your-score-on-x-twitter/)
- [nibzard: a Rust+Python architecture analysis](https://nibzard.github.io/twitter-algorithm-tufte/)
- [ByteByteGo: an illustrated algorithm-architecture breakdown](https://blog.bytebytego.com/p/the-algorithm-that-powers-your-x)
- [Pixelscan: a shadowban guide](https://pixelscan.net/blog/twitter-shadowban-2025-guide/)
- [DeepWiki: an analysis of the x-algorithm repo](https://deepwiki.com/xai-org/x-algorithm)
