# PETME2 blog expansion (Ahrefs-driven), 2026-10-04

Scope: blog `news`, 6 articles. Only `body` was updated, in 2 batched `articleUpdate` mutations (3 aliases each). Summaries were left unchanged.
Backups of the previous live bodies and summaries: `research/seo/blog/backup-before-expand/`.
Local copies (header comments kept): `research/seo/blog/*.html`.

## Method and data sources (Ahrefs, country US)
- `keywords-explorer-matching-terms` with `terms=questions` for each topic (real search questions + volume).
- `keywords-explorer-matching-terms` (all terms) for the camera-feeder keyword.
- `serp-overview` for each target keyword (top 5–6 positions incl. SERP features).
- `content-helper-topics` (top 5 competitors) for gap analysis. It returns the subtopics the ranking pages cover. For "automatic cat feeder for two cats" it returned no topics.
- **Competitor word counts:** these could not be measured. Ahrefs `serp-overview` has no word-count field, and the sandbox egress proxy blocks direct fetches of competitor domains (petcube, happyandpolly, petlibro, rover, kowaligavet, worldsbestcatlitter). Below, "competitor depth" means each page's Ahrefs content-helper coverage score instead. Most of these SERPs are led by Reddit threads, retailer listings (Amazon, Walmart, Kohl's, PetSmart, Target) and brand collection pages. Long editorial articles are rare, so a 2,000-word guide is already deeper than most of what ranks.
- All existing tables were also wrapped in `<div style="overflow-x:auto">` so they scroll on mobile.

## Summary table

| Article | Words before → after (live) | FAQ items | Tables |
|---|---|---|---|
| how-often-to-clean-cat-water-fountain | 1,319 → 2,274 | 8 | 2 (new) |
| cat-water-fountain-filter-guide | 1,137 → 2,005 | 8 | 2 (1 new) |
| stainless-steel-cat-water-fountain-vs-plastic-ceramic | 1,077 → 1,879 | 8 | 2 (1 new) |
| why-do-cats-like-running-water | 1,185 → 2,034 | 8 | 1 (new) |
| automatic-cat-feeder-for-two-cats | 1,224 → 2,191 | 8 | 3 (2 new) |
| automatic-cat-feeder-with-camera-guide | 1,202 → 1,975 | 8 | 2 (1 new) |

---

## 1. how-often-to-clean-cat-water-fountain (target: how often to clean cat water fountain, 200/KD0)
**Top SERP:** AI overview (sources: reddit r/catcare, happyandpolly, thirstycatfountains, petcube, aitakon, petlibro "maintenance 101"), then reddit r/CatAdvice (#2), happyandpolly (#4), consumerreports/news items (#5) and Facebook groups (#6).
**Competitor depth (content-helper):** happyandpolly scores 88–100 on all 4 topics (general guidelines, health and hydration, number of cats, signs water needs changing). thirstycatfountains scores 69–94, with a per-cat-count schedule and the "persistent bubbles/foam" cue. Reddit, Facebook and Quora score 0.
**Ahrefs questions used:** how to clean cat water fountain pump (100); how often to change water in cat fountain (100); how often should you replace cat water fountain (80); why does my cat keep knocking over his water fountain (60); why is my cat water fountain not working / why did it stop working (40/30); why is my cat water fountain so loud (30); how to clean stainless steel cat water fountain (30); how to keep cat water fountain clean (30).
**Sections added:** H3 "How the number of cats changes the schedule" with a table (one cat, long-haired, multi-pet, hot or hard water) and the foam/bubbles cue. H2 "Full cleaning schedule at a glance" (task/frequency/tip table). H2 "How to clean a stainless steel cat water fountain". H2 "Troubleshooting: loud, weak, or not working" (H3s: loud, stopped working, knocking over). H2 "Common cleaning mistakes to avoid" (7). "Weekly cleaning checklist" box (8). 3 new FAQs (pump, loud, when to replace).

## 2. cat-water-fountain-filter-guide (target: cat water fountain filter, 600/KD0)
**Top SERP:** AI overview, Amazon filters listing (#2), reddit "do I really need these filters" (#3), shopping pack, Walmart (#6), PetSmart Catit filters, Target.
**Competitor depth:** no editorial article in the top 5. Topic coverage is low across the SERP: replacement frequency 30.8, necessity 28.6, installation 7.8, compatible filters 6.2, filter technology 0, where to buy 0.
**Ahrefs questions used:** how often to change (60/50/50/40, already covered); how to clean cat (water) fountain filter (30/20); how to put filter in cat water fountain (30); which way does the filter go in a cat fountain (20/10); can you use cat fountain without filter (10); how to replace/change filter (10).
**Sections added:** H2 "Filter layers compared" (table: mesh/foam/carbon/resin, rinse, replace). H2 "Do you really need a filter?". H2 "Which way does the filter go in a cat fountain?". H2 "How to clean a cat fountain filter between changes" (6 steps). H2 "Buying replacement filters". H2 "Common filter mistakes" (7). "Filter change checklist" (7). 4 new FAQs (clean, orientation, pre-soak, signs of wrong install).

## 3. stainless-steel-cat-water-fountain-vs-plastic-ceramic (target: stainless steel cat water fountain, 2,300/KD0)
**Top SERP:** AI overview (reddit, cats.com best fountains, pawspik product, PetSafe Seaside), shopping pack, Amazon Petlipo (#3), Kohl's 3.2L product (#4), reddit r/cats (#5), PAA.
**Competitor depth:** the SERP is product and retail pages, with low topic coverage: capacity 18, ease of cleaning 13.8, filtration 13. Material benefits, multi-pet compatibility, water-flow mechanism and user recommendations all score 0.
**Ahrefs questions used:** how to clean stainless steel cat (water) fountain (40/30); is stainless steel better for cat water fountain (20); how often to clean stainless steel cat fountain (10); which is better, ceramic or stainless steel; how to scrub ceramic fountain with hard water stains; how to disinfect/clean plastic cat water fountain; how to set up a stainless steel fountain.
**Sections added:** H2 "PETME2 fountains compared" (table: model/drinking surface/capacity/features). H2 "What size fountain do you need?" (one cat, multi-pet, cats + dogs). H2 "How to clean a stainless steel cat water fountain" (8 steps) plus H3 "Cleaning ceramic and plastic fountains". H2 "Is stainless steel worth the extra cost?". H2 "Common mistakes when choosing a fountain material" (6). "Before you buy" checklist (7). 4 new FAQs (cleaning, hard water stains, rust, cats + dogs sharing).

## 4. why-do-cats-like-running-water (target: why do cats like running water, 250/KD0)
**Top SERP:** AI overview (kowaligavet vet blog, rover.com), Petco vet Q&A (#2), PAA, reddit (#4), worldsbestcatlitter "Cat Hydration 101" (#5), hola.com "cats hate water" (#6).
**Competitor depth:** worldsbestcatlitter scores 77–100 on hydration, fountains, evolutionary background and ways to encourage drinking. hola.com scores 64–100 on "cats and water" and ancestry. Petco and Reddit score 0.
**Ahrefs questions used:** do cats prefer running water (150); why do cats prefer running water (100); do cats like running water (90); why is my cat obsessed with running water (30); do cats need running water (30); is a cat water fountain worth it (30); is running water better for cats (20); why does my cat only drink running water (10).
**Sections added:** H2 "Why do cats love running water but hate baths?" plus H3 "What about their wild ancestors?" (hedged as a popular explanation, not a fact). H2 "Do cats need running water?" plus H3 "Why is my cat obsessed with the tap?". H2 "Fountain vs bowl: side by side" (table). H2 "Other simple ways to help your cat drink" (vet-referral wording, no health claims). H2 "Common mistakes when switching to a fountain" (7). "New fountain checklist" (7). 4 new FAQs.
Note: worldsbestcatlitter cites a Cornell Feline Health Center intake figure. It was not independently verified, so no statistic was added.

## 5. automatic-cat-feeder-for-two-cats (target: automatic cat feeder for two cats, 500/KD0)
**Top SERP:** AI overview (reddit x2, oneisall 5L product, cats.com best automatic feeders), Amazon DUMOS (#2), Walmart (#3), shopping pack, PAA, reddit (#6).
**Competitor depth:** content-helper returned no topics for this keyword. The SERP is product listings plus Reddit, and cats.com is the only long editorial page (see #6 analysis: types of feeders, RFID/microchip, scheduling, reliability).
**Ahrefs questions used:** how to feed two cats when one overeats (80); how to feed two cats separately (60); how to feed two cats (50); how to clean automatic cat feeder (30); how to feed two cats with automatic feeder (30); how often to clean automatic cat feeder (20); how to feed two cats at the same time (20); how does an automatic cat feeder work (20); what times should I set my automatic cat feeder (10); how to get cat used to automatic feeder (10); how to feed two cats different food (10).
**Sections added:** H2 "Dual bowl vs two feeders vs microchip feeder" (table, clearly stating that microchip feeders are not part of the PETME2 range). H2 "How to feed two cats when one overeats" plus H3 "How to feed two cats different food". H2 "What times should you set? Example schedules" (table). H2 "How to get your cats used to the feeder" (5 steps). H2 "How to clean an automatic cat feeder" (5 steps). H2 "Common mistakes when feeding two cats" (7). "Two-cat feeder setup checklist" (7). 4 new FAQs.

## 6. automatic-cat-feeder-with-camera-guide (target: automatic cat feeder with camera, 600/KD5)
**Top SERP:** shopping pack, AI overview (Walmart, Amazon PETULTRA, hholove blog, YouTube, petkit collection), petlibro collection (#3), PAA, reddit (#5), news/video (#6).
**Competitor depth:** camera/monitoring features 64.4 (4 pages), scheduling/portion 54.2, feeder types 50.6, safety 46, Wi-Fi/app 35.2, pricing 34.4, best models 33, design/reliability 29.2. cats.com "13 Best Automatic Cat Feeders" is the deepest page (scores 63–100).
**Ahrefs questions used:** how to choose a pet camera (300); how to clean pet camera (300); what features are important for a pet camera (150); how much does an electronic cat feeder cost (70); which automatic pet feeder is most reliable (40); how to keep pet food fresh in feeder (30); should I talk to my cat through camera / is it bad to talk to your cat through a camera (20/20).
**Sections added:** H2 "Camera feeder or a feeder plus a pet camera?" (table). H2 "How much does a camera feeder cost?" (no prices invented). H2 "Reliability: what keeps meals on time". H2 "How to keep food fresh in the feeder". H2 "Should you talk to your cat through the camera?". H2 "How to clean a camera feeder, including the lens" (6 steps). H2 "Common camera feeder mistakes" (7). "Before you leave home checklist" (8). 3 new FAQs.

---

## Fact and safety guardrails applied
- Product facts are limited to the approved list and the existing product-card copy (for example, the 3.2L fountain's "two flow modes" and "dishwasher-safe detachable parts" come from its live card). No new specs were invented, no prices, and the Classic 2L is not claimed to have a filter.
- No health or disease claims and no statistics. Health questions are always referred to a vet.
- Free U.S. shipping and the 30-day money-back guarantee are mentioned only as already stated.

## Verification
After the update, the live bodies were re-queried. For all 6 articles, the plain text and tag sequence match the local files exactly. Word counts are as in the summary table. Images: 5–6 per article, all kept. Product cards, the quick-answer box and internal links are all kept. Neither mutation returned userErrors.
