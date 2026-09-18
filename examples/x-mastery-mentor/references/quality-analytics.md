# Quality Checklist + Anti-Patterns + Analytics Review + Report Template

> Load on demand: read when in scenario C (reviewing content), scenario E (account diagnosis), or during an analytics review.

---

## Quality checklist

When reviewing a written tweet/thread, check each item:

### Tweet checklist
- [ ] Does the hook grab attention within 2 lines?
- [ ] Does it answer "who's it for / what's it about / why should I read it"?
- [ ] Is it specific? (numbers, dates, names)
- [ ] Can it prompt a reply? (not just a like)
- [ ] Does it avoid an external link? (if one is needed, put it in the first reply)
- [ ] Is the posting time within the target audience's active hours?

### Thread checklist
- [ ] Does the first tweet stand alone as a complete, compelling piece?
- [ ] Does it follow the 1/3/1 rhythm?
- [ ] Does every tweet actually advance the content? (Rate of Revelation)
- [ ] Is there a TL;DR summary?
- [ ] Is there a clear CTA?
- [ ] Is the length 8-12 tweets?
- [ ] Does it use bullet points instead of dense paragraphs?

### Content-strategy checklist
- [ ] Was there at least 1 thread this week?
- [ ] Were high-quality replies left in big accounts' comment sections?
- [ ] Is there a CTA driving traffic to the newsletter?
- [ ] Did it respond to this week's AI news?
- [ ] Is the mix of short tweets to threads reasonable?

---

## Anti-patterns and pitfalls to avoid

### Growth traps (don't fall for these)

1. **Buying followers/follow-for-follow-and-like groups**: numbers look good short-term, but TweepCred (X's internal reputation score) craters long-term. The algorithm detects unnatural engagement patterns and demotes you — not worth it
2. **Pure tool-recommendation roundups**: the AI niche is already a red ocean. "10 AI tools you need" posts are everywhere with zero differentiation. If you post one, add your own test data and a unique take
3. **Just translating foreign AI news**: zero differentiation. Add your own take — "why this matters for developers here" or "I tested it, here's what actually happens..."
4. **Chasing every trend and losing your positioning**: jumping on every trend leaves followers unsure who you actually are. Filter your trends: only jump on the ones relevant to your positioning
5. **All hook, no substance**: clickbait works short-term, loses followers long-term. Hormozi's rule is "over-deliver" — promise 1, give 3
6. **Posting without replying**: conversation carries 150x weight — not replying means giving up your biggest algorithmic lever
7. **Threads that run too long**: engagement drops off past 15 tweets. The sweet spot is 8-12

### Platform-level risks (stay alert to these)

- **Overall engagement rate decline**: X's platform-wide engagement rate dropped 48% from 2024-2025. Not your problem — it's a platform trend
- **Pay-to-play intensifying**: organic reach for non-Premium users keeps shrinking, and posts with outbound links get almost none. Premium isn't optional anymore — it's a requirement
- **User migration**: some creators are spreading out to Bluesky/Threads. But X remains the main battleground for AI/tech content for now

---

## Analytics review guide

### Key metrics (by priority)

| Metric | What it measures | Healthy range |
|------|--------|-----------|
| Engagement Rate | engagements / impressions | >2% is good, >5% is excellent |
| Reply rate | replies / impressions | higher is better (heaviest algorithmic weight) |
| Profile Visit rate | profile visits / impressions | >1% means people want to know more about you |
| Follower growth | net new followers per week | cold-start stage: 5-10/day average; growth stage: 20-50/day average |
| Bookmark rate | bookmarks / impressions | high bookmarks = high-value content |
| Newsletter conversion | new subscribers/week | any is good — keep tracking the conversion rate |

### Review cadence

- **Daily**: scan yesterday's post data, flag any post with 500+ engagements
- **Weekly**: analyze this week's top 3 tweets, extract what they have in common -> update your template library
- **Monthly**: review the follower-growth curve, content-type distribution, and newsletter growth. Adjust next month's content strategy

### Diagnostic framework (when tweet performance is poor)

Check these in order:
1. **Algorithm layer**: is Premium turned on? Is the posting time right? Is there an outbound link?
2. **Hook layer**: is there a curiosity gap in the first 2 lines? Is there a credibility anchor?
3. **Content layer**: does every tweet advance the piece? Does it follow the 1/3/1 rhythm?
4. **Audience layer**: is the follower count enough to trigger Engagement Velocity? If not, borrow reach from comment sections first

---

## Report HTML template requirements

Diagnostic reports use an Economist/newspaper-style layout, and must include:
- **Visual style**: serif typeface (Georgia), a warm paper-colored background (#f5f0e8), a red accent color (#C7000A), a grid layout
- **Data visualization**: use ECharts.js (via CDN), including at minimum a topic-distribution chart, a time-distribution chart, and an engagement funnel
- **Required sections**:
  1. Banner + Masthead (one-sentence core finding as the headline)
  2. KPI Grid (4 core metrics as large numbers)
  3. Lead (a summary paragraph, italicized, with a red left border)
  4. Content ROI analysis (engagement comparison broken down by topic)
  5. Distribution funnel (like rate/bookmark rate/retweet rate/reply rate)
  6. Time analysis (best posting windows, how posting cadence has evolved)
  7. Brand narrative (distribution of narrative roles and their engagement performance)
  8. Top 5 action recommendations (numbered red circles + headline + body + supporting data)
  9. Footer (data period, sample size, analysis timestamp)
- **Reference implementation**: `user-data/AlchainHust/report_20260406.html`
