# X Platform Algorithm Quick Reference + AI/Tech-Niche Specialization

> Load on demand: read when dealing with algorithm rules, posting parameters, AI-niche
> positioning, or going-global strategy.

---

## X platform algorithm quick reference (April 2026)

### Engagement weight formula (confirmed from open-source code)

| Engagement type | Weight multiplier (vs. Like) | Meaning | Source |
|----------|-------------------|------|------|
| Conversation reply (reply + author engages back) | **150x** | Your reply gets replied to/liked by the original poster | open-source code |
| Ordinary reply | **27x** | A regular reply | open-source code |
| Profile click | **24x** | A user clicks into your profile and engages | open-source code |
| Dwell time (>2min) | **20x** | A user spends 2+ minutes on your post/conversation | open-source code |
| Bookmark | **~20x** | Community-estimated value, not exact | community estimate |
| Retweet | **2x** | Weight cut significantly in the 2026 version | open-source code |
| Like | **1x** | Baseline | open-source code |

### Negative signals

| Signal | Penalty |
|------|------|
| Report | -369x, near-instant removal |
| Block/mute | -74x |
| External link | reach down 30-50%, near zero for non-Premium |
| >2 hashtags | reach down ~40%, flagged as spam |
| Duplicate content | gradually suppressed, severe cases trigger shadowban |

### Key rules

- **Engagement velocity**: the engagement rate in the first 15-30 minutes decides a tweet's fate.
  10+ engagements within 15 minutes -> exponential spread; <3 engagements -> the tweet dies
- **Time decay**: visibility halves every 6 hours
- **Why Premium matters**: 4x boost in the following-users feed + 2x boost in the
  non-following-users feed + an instant +100 TweepCred. Non-Premium posts with a link have a
  median engagement of zero (March 2026 data)
- **Grok tone scoring**: added in 2025 — positive/constructive content gets more distribution
- **The external-link workaround**: no link in the main tweet, put the link in the first reply

### Best posting parameters

| Parameter | Recommendation |
|------|------|
| Time window | weekdays 9AM-2PM local time |
| Best days | Tuesday, Wednesday |
| Frequency | 3-5 tweets/day, 2-3 hours apart |
| Thread length | 8-12 tweets (47% more engagement than short threads) |
| Video length | 15-30 seconds (maximizes completion rate) |
| Tweet length | 120-130 characters is optimal (for short tweets) |

### TweepCred (account reputation score)

- Range: -128 to +100
- New account: starts at -128
- Normal-distribution threshold: +17
- Premium subscription: instant +100 boost
- Contributing factors: following/follower ratio, engagement quality, account history, profile
  completeness, content tone (Grok score)

---

## AI/tech-niche specialization

### Account archetypes

| Type | Representative | Core strategy | Who it fits |
|------|------|---------|--------|
| Build-in-Public | levelsio | publicly shares revenue/process/failures | developers currently building a product |
| Learn-in-Public | swyx | makes learning notes public | technical learners/content creators |
| Technical-education | Karpathy | low-frequency, high-quality deep tutorials | domain authorities |
| AI agent/tooling | steipete | product iteration + technical opinions | tool builders |
| Open-source project | Exa | viral side-projects | open-source maintainers |
| AI-news aggregation | Rowan Cheung | daily tool recommendations/quick updates | content curators |

### Content-performance matrix

| Content type | Engagement | Frequency | Key factor |
|---------|--------|------|------|
| Quick takes on new models/products | Extremely high | whenever there's a hot topic | speed > polish, within 0-1h |
| Build-in-Public updates | High | 2-3x/week | MRR screenshots, feature launches |
| Technical tutorial threads | High | 1x/week | 8-12 tweets, with code/screenshots |
| Demo videos/GIFs | High | whenever there's a result to show | 15-30 seconds, assume muted playback |
| Hot takes (controversial opinions) | Medium-high | use sparingly | needs solid reasoning behind it |
| Paper breakdown threads | Medium | 1x/week | plain-language breakdown |
| Tool comparison reviews | Medium | 2-3x/month | screenshots + test results |

### Positioning recommendation for Huashu

Based on the research, Huashu's best differentiated positioning on X:

**"A Chinese indie developer building with AI, narrating the process for the whole world"**

Rationale:
1. **A unique vantage point**: firsthand information about the Chinese AI ecosystem (DeepSeek,
   GLM, etc.) has unique value for an international audience
2. **A natural fit for Build in Public**: the story of the Kitten Fill Light app hitting #1 on the
   App Store paid-app chart has huge viral potential on English-language X
3. **Layering in Learn in Public**: content-creation experience built from 300,000+ Chinese
   followers can be distilled into English-language methodology
4. **Product proof**: ship or shut up — the AI niche cares whether you can actually build
   something, and Huashu has products to back it up

**Content-strategy recommendation**:
- 60% English (the main battlefield), 40% Chinese (serving the existing audience)
- Don't translate Chinese content into English — rewrite it (the context is different)
- Respond in both languages simultaneously when a new model launches (a quick Chinese take +
  a deep English thread)

### Notes for Chinese developers going global

1. English writing doesn't need to be perfect — the AI niche is more forgiving of non-native
   speakers
2. Time posts to match a North American audience: 8-10 AM Pacific Time (11 PM-1 AM Beijing time)
3. Open-source contributions are the best asset for building international trust
4. Run the two languages as separate operations — don't mix them
5. Firsthand Chinese-AI information is a differentiation weapon
