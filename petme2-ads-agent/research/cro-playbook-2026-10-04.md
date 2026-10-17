# PETME2 CRO Playbook (ethical persuasion) — 2026-10-04

Store: petme2.com (Shopify). Feeders cost $50–66 and fountains $22–40. Every U.S. order ships free and is fulfilled by Amazon. Every order has a 30-day money-back guarantee (owner confirmed).
Ground rule: every claim must be **true and checkable**. The FTC treats fake countdown timers and false scarcity as dark patterns ([FTC "Bringing Dark Patterns to Light", 2022](https://www.venable.com/insights/blogs/2022/09/the-ftc-brings-more-light-to-dark-patterns-in-new)). Under the 2024 FTC rule, each fake or misattributed review can cost about $52k ([WSGR summary](https://wsgr.com/en/insights/ftc-issues-final-rule-banning-fake-and-misleading-consumer-reviews-and-testimonials.html)).

---

## 1. Top 12 ethical levers, ranked by expected impact

Most cart abandonment comes from surprise costs (48%), slow delivery (~23%), trust worries (~19–25%) and long checkouts (~18%) ([Baymard survey via OptinMonster](https://optinmonster.com/cart-abandonment-statistics/); [Baymard](https://baymard.com/lists/cart-abandonment-rate)). The levers below target those reasons first.

| # | Lever | What to show + wording | Where / mobile | Do NOT |
|---|---|---|---|---|
| 1 | **Free shipping, said early and often** | "Free U.S. shipping on every order" | Announcement bar, under the price, in the cart. On mobile, keep the bar to one line. | Don't write "Free shipping over $X" (there's no threshold). Don't let tax or fees appear for the first time at checkout. |
| 2 | **Risk reversal (30-day guarantee)** | "Try it for 30 days. Not happy? Full refund." Link to the policy. The FTC says a "money-back guarantee" must mean a full refund and must clearly state any conditions ([16 CFR 239.3](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-239)) | Directly under the Add to cart (ATC) button, plus the cart and FAQ | Don't hide conditions (return shipping, original box). If you have any, write them in the same line: "…Full refund — just send it back within 30 days." |
| 3 | **Delivery-date estimate** | "Order today, get it by **Thu, Oct 9**". Calculate the date from real Amazon Multi-Channel Fulfillment (MCF) transit times. 64% of shoppers look for a delivery date on the product page ([Baymard](https://baymard.com/blog/shipping-speed-vs-delivery-date)) | Under the price, above ATC | Don't promise a date MCF can't meet. Give a range ("Oct 8–10") if you're unsure. Don't add a countdown ("order in 2h 13m") unless it is the real fulfillment cutoff. |
| 4 | **Fast checkout (Shop Pay, Apple Pay, Google Pay, PayPal)** | Turn on the express checkout buttons and guest checkout. Shopify's claim of up to +50% is unaudited. Its own case study showed about +1–4% ([analysis](https://cleancommit.io/blog/shop-pay-conversion-rate/)). Still cheap and worth it. | Product page below ATC, cart drawer | Don't force account creation. 26% abandon over it ([Baymard](https://optinmonster.com/cart-abandonment-statistics/)). |
| 5 | **Real social proof** | Collect **your own** verified reviews with a Shopify reviews app and post-purchase emails. Five reviews raise purchase likelihood by about 270% compared with none, and 4.0–4.7 stars look more credible than 5.0 ([Spiegel/Northwestern](https://spiegel.medill.northwestern.edu/wp-content/uploads/sites/2/2021/04/Spiegel-research-reveals-4.5-stars-are-better-than-5-The-Medill-IMC-Spiegel-Research-Center.pdf)). Only show an Amazon rating if it's for the **same ASIN**, current, and linked: "Rated 4.3/5 by 212 Amazon buyers — see reviews". | Stars under the title, review block lower on the page | Don't copy or paste Amazon review text (Amazon's terms and copyright). Don't borrow ratings from other products. Don't pay for positive reviews. Show nothing until the data is real. |
| 6 | **Trust row near ATC** | 3 icons + text: "Free shipping · 30-day refund · Secure checkout". Small brands benefit most from security cues placed where doubt arises ([Baymard perceived security](https://baymard.com/blog/perceived-security-of-payment-form)) | Directly under ATC. On mobile, wrap to two lines rather than shrinking the text. | Don't use fake "McAfee/Norton secure" seals you don't license. Don't show a wall of 10 badges. |
| 7 | **Welcome offer pop-up (10%)** | "Get 10% off your first order" (details in §2) | Bottom sheet on mobile, centered modal or exit-intent on desktop | Don't show it full-screen on mobile on page load. Don't attach a "today only" timer. |
| 8 | **Benefit-first titles + bullets** | Short title (§3) plus 3–5 bullets, each a benefit with its proof: "Feed on schedule from your phone (app control)" | Above the fold | Don't use keyword-stuffed Amazon-style titles. Don't claim features the product lacks. |
| 9 | **Sticky ATC on mobile** | A bar showing price and "Add to cart" once the main button scrolls out of view | Bottom of the screen on mobile only | Don't cover the chat or cookie bar, and don't place it on top of the pop-up. |
| 10 | **Bundle: "Complete the setup"** | Feeder + fountain: "Food and water, sorted. Add the fountain →". Offer replacement filters for fountains. | Below ATC or in the cart drawer. Use 1 product with a one-tap add. | Don't pre-check add-ons. Don't show a fake "bundle savings" amount. Only show a discount if it's real. |
| 11 | **Real anchoring (compare-at price)** | Show a compare-at price **only** if you openly sold at that price for a substantial period ([16 CFR 233.1](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-233)). Otherwise anchor on value: "Less than $X/month over a year of feeding" (simple math only). | Next to the price | Don't inflate the "was" price, and don't keep a permanent "sale". |
| 12 | **Real low-stock + "Which feeder?" quiz** | Low stock: "Only 4 left" **only** when it's synced to live inventory. A 3-question quiz (how many cats? want a camera? prefer stainless?) leads to one recommended product. | Low stock goes near ATC. The quiz goes in the homepage hero or collection page. | Don't show static or fake stock counts or "12 people are viewing". Don't put an email gate before the quiz result. |

---

## 2. Pop-up best practices

- **Mobile rule (Google):** Google penalizes interstitials on mobile that cover the main content right after someone arrives from search. Small banners that use a reasonable amount of screen space are fine ([Google guidance summary](https://www.smashingmagazine.com/2017/05/intrusive-interstitials-guidelines-avoid-google-penalty/); [Google Search Central](https://developers.google.com/search/docs/appearance/avoid-intrusive-interstitials)). → On mobile use a **bottom sheet that covers no more than ~30% of the screen**, or a small teaser tab ("10% off") that opens the form on tap.
- **Timing:** Immediate pop-ups do worst. Pop-ups shown at 6–15 seconds perform best, at ~2.1–2.3% ([Omnisend data via CrazyEgg](https://www.crazyegg.com/blog/popup-statistics/); [Omnisend](https://www.omnisend.com/blog/email-popup-statistics/)). NN/g lists early interruption as the top pop-up mistake ([NN/g](https://nngroup.com/articles/popups/)).
  - Mobile: trigger after 10–15 seconds **or** a 40–50% scroll, whichever comes first, and only from the 2nd page view on landing pages from ads.
  - Desktop: **exit intent**, with a fallback after 20–30 seconds.
  - Never show it in the cart or checkout ([NN/g](https://nngroup.com/articles/popups/)).
- **Frequency capping:**
  - Show once per session.
  - If dismissed, don't show again for 7–14 days.
  - Never show it again to subscribers or customers (use the Klaviyo/Shopify segment).
  - Suppress it for visitors arriving from email links.
- **Form:** Use 1 field (email). Optionally add a second step for SMS, since multi-step forms do slightly better (2.3% vs 2.0%, Omnisend). Klaviyo's baseline is about a 3% submit rate ([Klaviyo](https://www.klaviyo.com/blog/sign-up-form-best-practices)).
- **Copy:**
  - Headline: "Get 10% off your first order"
  - Sub: "Plus feeding tips. Unsubscribe anytime."
  - Button: "Send my 10%"
  - Decline: "No thanks" (neutral wording, never a guilt-trip like "No, I hate saving money")
- **Success state:** Show the code on screen (**WELCOME10**) with a "Copy code" button, and **apply it automatically** to the cart via a discount link. Also email it. Message: "You're in! 10% off is applied at checkout."
- **Accessibility:**
  - Make it a real dialog (`role="dialog"`, `aria-modal`, labelled title).
  - Move focus into the dialog, trap focus while it's open, and close it on Esc.
  - Use a visible close button of at least 44×44px.
  - Give the input a label (not just placeholder text), keep 4.5:1 contrast, and announce errors.
  - Return focus to where it was on close, and respect reduced motion.
- **Honesty:** The code must work every time it's advertised. Don't add an expiry timer unless the expiry is real and stated ("Code valid 7 days").

---

## 3. Product titles

Guidance: put the product type and the key differentiator first. Keep titles under ~70 characters, because longer ones get cut off in Shopping and listings. Leave out promo text and ALL CAPS ([Google Merchant Center](https://support.google.com/merchants/answer/6098378)). Put specs (size, color) in the variant or bullets, not the title. Keep the Google Shopping feed title the same as the on-site title (use a feed app if you want an SEO variant).

Suggested titles (true facts only):

1. **Dual Bowl Automatic Cat Feeder – 3L, App Control & 2-Way Audio** (color variants: Black / White)
2. **Two-Cat Automatic Feeder – 2 Stainless Bowls, App Control, 3L**
3. **Elevated WiFi Cat Feeder – 5L, 2 Bowls, Voice Recording**
4. **Camera Cat Feeder – 1080P Live View, 2-Way Audio, WiFi, 3L**
5. **Stainless Steel Cat Water Fountain – 3.2L (108oz), 4-Layer Filter, LED Light**
6. **Steel-Tray Cat Water Fountain – 2.2L, 4-Layer Filter**
7. **Clear Cat Water Fountain – 2.2L, See-Through Tank, Filter Included**
8. **Classic Cat Water Fountain – 2L, Low-Water Light**

(#1 and #2 are alternatives for the same 3L dual-bowl feeder. A/B test them, or keep #2 as the SEO or ad-feed version. Before publishing #7, confirm that one filter cartridge ships in the box.)

Subtitle or first bullet ideas: "Meals on time, even when you're out" (feeders); "Fresh, filtered water that cats want to drink" (fountains). Keep these as benefit language, not medical claims.

---

## 4. Top 10 actions (prioritized)

| # | Action | Impact | Effort |
|---|---|---|---|
| 1 | Announcement bar + "Free U.S. shipping" under every price and in the cart | High | Low |
| 2 | Trust row under ATC: free shipping · 30-day full refund · secure checkout, plus a clear refund policy page | High | Low |
| 3 | Turn on Shop Pay, Apple Pay, Google Pay and PayPal express buttons and guest checkout | High | Low |
| 4 | Delivery-date estimate on product pages, using MCF transit times (range if unsure) | High | Med |
| 5 | Welcome pop-up: mobile bottom sheet after 10–15 seconds or 40% scroll, desktop exit intent, auto-applied WELCOME10, capped frequency | High | Low |
| 6 | Install a reviews app and automate review requests 10–14 days after delivery. Link to the real Amazon listing rating only if it's the same ASIN and verified. | High (over time) | Med |
| 7 | Rewrite titles and bullets to be benefit-first (§3) and match the ad feed | Med | Low |
| 8 | Sticky ATC on mobile product pages | Med | Low |
| 9 | Cart-drawer "Complete the setup" (feeder ↔ fountain, filters) | Med (AOV) | Med |
| 10 | "Which feeder?" quiz + inventory-synced low-stock note (only when real) | Low–Med | Med |

**Measure:** Use Shopify Analytics to track product-page→cart rate, cart→checkout rate and checkout completion, split by device. Change one thing per week, or A/B test each change with a test app, and check results after about 2 weeks or once there's enough traffic.

**Never:** fake timers, invented stock or "people viewing" counters, fabricated or borrowed reviews, inflated "was" prices, pre-checked add-ons, guilt-trip decline buttons, or full-screen mobile pop-ups on page load.
