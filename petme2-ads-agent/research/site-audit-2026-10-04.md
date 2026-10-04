# PETME2 store audit (petme2.com), 2026-10-04

Read-only audit. Sources: Shopify Admin API (products, variants, collections, pages, blog, menus, policies, discounts, shipping, themes), the local source of the new theme (`shopify-theme-tech/`), its preview images, and Ahrefs. Nothing was changed.

Note: the preview PNGs are from earlier builds. They use placeholder photos and show old copy ("free shipping on orders $50+", camera feeder at $59.99). Before you publish, check the real theme preview on a phone.

---

## Scorecard

| Area | Score | Why |
|---|---|---|
| Design | 7/10 | The new "Smart Tech" theme looks clean, modern and consistent. But the guarantee and free-shipping message appears 5 to 6 times on the product page, which is clutter. |
| Mobile | 7/10 | Good: a sticky add-to-cart bar, a bottom-sheet popup (not full screen), and 2-column grids. But the homepage has 11 sections and is very long. The camera feeder shows a wrong "5 Liters" size button. |
| SEO | 4/10 | Product SEO titles, meta descriptions and alt text are good, and 6 solid blog posts are live. But: Domain Rating 0 with 0 ranking keywords, about 1,165 spam referring domains, no homepage meta description, the black and white feeders have identical text, and 2 thin articles make health claims. |
| Conversion | 5/10 | The offer is clear: free U.S. shipping, a 30-day guarantee and 10% off. But the site has zero reviews, every product is on "sale" all the time, there is no delivery-date estimate, and stock is capped at 10 units per product. |
| Trust | 3/10 | The live theme shows fake contact details and a fake "John Smith" founder quote. The Privacy Policy and Terms pages contain accessibility text. Only the privacy policy is set in Shopify. There is no visible email or business address. |
| Tech | 6/10 | Good: Dawn base, lazy-loaded images, an eager hero image, FAQPage + Organization + Product schema, and reduced-motion support. But inventory is not synced with Amazon, an international zone is active, there are 5 domestic shipping rates, an old Bundler app discount is active, and there are 5 themes. |

---

## TOP 15 recommendations (ranked by impact)

### 1. Replace the wrong legal pages and set all store policies
- **Wrong:** `/pages/privacy-policy` and `/pages/term-of-services` contain the accessibility statement, word for word. In Settings → Policies, only the Privacy policy is filled in. The Refund, Shipping, Terms of service and Contact information policies are empty. The footer "Information" menu links to the wrong pages.
- **Why:** This is a legal risk. Google Merchant Center and Shopping ads need a clear refund and shipping policy, and shoppers check these pages before they pay. The checkout footer also shows no refund or terms links.
- **Fix:**
  - Paste the Refund and Shipping drafts from `research/policy-drafts-2026-10-04.md` into Settings → Policies.
  - Generate Terms of service from Shopify's template.
  - Fill in Contact information: a business name and a real address or email.
  - In the `information` menu, point "Privacy Policy" to `/policies/privacy-policy` and "Terms of Service" to `/policies/terms-of-service`. Add "Refund policy" (`/policies/refund-policy`).
  - Then unpublish the two wrong pages.
  - Also fix the menu label "Term of Service" → "Terms of Service".
- **Who:** Claude via the API (`shopPolicyUpdate`, `menuUpdate`, `pageUpdate`), after the owner approves the wording. The owner fills in the business address.
- **Effort:** 30 min.

### 2. Publish the new theme (and with it, remove the fake details on the live theme)
- **Wrong:** The live "Horizon" theme shows made-up contact details: care@petme.com, +1 (800) 555-PAWS, a Boston "Suite 450" address, "4–8 business hours" replies, and "warranty claims". It also shows a "John Smith" founder quote (4 times) and "650+ pet parents".
- **Why:** Fake details destroy trust, can count as deceptive under FTC rules, and can get Google Merchant Center suspended for "misrepresentation".
- **Fix:** Publish "PETME2 — Smart Tech (Oct 2026)" (gid …188804432084) after fixes #3, #5 and #8. If you wait, at least delete those blocks in Customize → Contact and Customize → About on Horizon now.
- **Who:** The owner clicks Publish. Claude can do the pre-publish fixes in the theme.
- **Effort:** 15 min (plus the fixes).

### 3. Fix the camera feeder's size: "3L" in the title, "5 Liters" in the variant
- **Wrong:** "Automatic Cat Feeder with 1080P Camera – 3L" has one variant named **"5 Liters"**. The product page shows a "5 Liters" size button, and the cart and order emails also say 5 Liters. The compare table, FAQ and description all say 3L.
- **Why:** This confuses buyers and sets up returns ("I thought it was 5L"). It is also a wrong claim in Google Shopping feeds.
- **Fix:** Rename the option value to "3 Liters". Better: remove the size option from all 8 single-variant products so Dawn hides the picker.
- **Who:** Claude via the API (`productOptionUpdate`).
- **Effort:** 10 min.

### 4. Add real reviews (the site has none)
- **Wrong:** There are no review stars or review blocks on any product, collection or the homepage. The product template has no reviews section.
- **Why:** For a new brand, reviews are the #1 trust signal. Going from 0 to 5 reviews can raise purchase likelihood a lot (Spiegel Research). Paid ad traffic also leaves faster when a page has no proof.
- **Fix:**
  - Install a reviews app (Judge.me free or Shopify Product Reviews) and turn on post-purchase review emails.
  - Add the app block under the product title (stars) and above "You may also like".
  - Optional: a line like "Rated 4.x/5 on Amazon → see reviews", linking to the same ASIN, only if the rating is current. Do not copy Amazon review text.
  - Dawn shows stars automatically from `reviews.rating`, which also adds `aggregateRating` to the Product schema.
- **Who:** The owner installs the app. Claude places the blocks in the theme.
- **Effort:** 1 hour.

### 5. Make inventory match Amazon, or the store will "sell out" after 10 orders
- **Wrong:** Every variant tracks inventory at "100 Powell Pl" with quantity **10** and "Deny" (stop selling at 0). No Amazon fulfillment-service location is connected, so stock never syncs with FBA.
- **Why:** After 10 sales per product, the page shows "Sold out" even though Amazon has stock. Ads keep paying for clicks on sold-out pages. The opposite risk exists too: Shopify can sell stock that Amazon no longer has.
- **Fix:** Connect Amazon MCF through an MCF app (for example Amazon's "Multi-Channel Fulfillment" app or a similar app) so it syncs stock and creates fulfillment orders automatically. Until then, set realistic quantities each week, or turn off tracking with "Continue selling" and watch FBA stock.
- **Who:** The owner (app install and choice). Claude can set the quantities via the API if asked.
- **Effort:** 1–2 hours.

### 6. Make every "sale" price honest, or remove compare-at prices
- **Wrong:** All 8 products are "on sale" all the time:
  - Compare-at prices: 45.99, 29.99, 21.99, 29.99, 59.99, 65.99, 65.99, 54.99.
  - The hero says "Sale · Save up to 33%" and the ticker says "Sale: save up to 33%".
  - The 2L Classic shows a strange 9% discount (21.99 → 19.99).
- **Why:** The FTC (16 CFR 233) and state laws (California, for example) require a "was" price to be a real price you actually sold at for a meaningful time. A permanent sale also trains people to ignore it. Google Shopping can reject sale prices without proof.
- **Fix:** Keep a compare-at price only if it equals a real, recent selling price (for example the Amazon list price you really charged). Otherwise clear it. If you remove them, change the hero eyebrow to "Free U.S. shipping · 30-day guarantee" and drop the "Sale" ticker item.
- **Who:** The owner decides which prices are real. Claude updates the variants and theme copy.
- **Effort:** 30 min.

### 7. Clean up shipping settings so checkout matches "free shipping on every order"
- **Wrong:**
  - The Domestic zone has 5 rates: Economy $0 (only for orders of $50+), Economy $4.90, Economy $19.90, Standard $6.90 and Standard $9.90. They are only made free by an automatic discount, "Free U.S. shipping on every order".
  - An **International** zone (27 countries, USPS and DHL calculated rates) is active, but orders are fulfilled by Amazon in the U.S.
  - An extra "US Only" group has a rate named **"Amazon Prime"**.
- **Why:**
  - If the discount is ever paused or fails to combine with another discount, shoppers see $4.90–$19.90 shipping. Surprise costs are the #1 reason carts are abandoned.
  - Showing two "Free" options with no delivery times is confusing.
  - International orders may not be shippable with MCF.
  - Calling a rate "Amazon Prime" misuses a trademark.
- **Fix:**
  - Delete the paid domestic rates. Keep one rate: "Free Standard Shipping (3–5 business days)" at $0, no conditions.
  - Turn off the International zone unless MCF international is set up.
  - Rename or delete the "Amazon Prime" rate.
  - The free-shipping discount can then stay as a backup, or be removed.
- **Who:** The owner in Settings → Shipping (Claude can do it via the API if asked).
- **Effort:** 20 min.

### 8. Delete or rewrite the 2 old blog posts with health claims
- **Wrong:**
  - "Demystifying Cat Hydration: Why Standing Water Hurts Feline Kidneys" is 37 words and says "Our research vets…". PETME2 has no vets.
  - "Structuring Dynamic Feeding Routines for Adult Canines" is 20 words and talks about "insulin spikes" and "stomach dilation".
  - Neither has image alt text, a summary or links.
- **Why:** These are unsupported health claims and a fake-expert claim. They are thin content that drags down site quality (Google's helpful-content rules). The dog article is also off-topic.
- **Fix:** Delete both. Add 301 redirects:
  - kidney article → `/blogs/news/why-do-cats-like-running-water`
  - canine article → `/blogs/news/automatic-cat-feeder-for-two-cats`
- **Who:** Claude via the API (`articleDelete` + `urlRedirectCreate`), after the owner says OK.
- **Effort:** 10 min.

### 9. Merge the black and white dual feeder (duplicate content)
- **Wrong:** `2-in-1-smart-feeder` (Black) and `2-in-1-smart-feeder-white` have **100% identical descriptions**, the same price and the same specs. They are two separate products.
- **Why:** Google sees duplicate pages and splits ranking signals between them. Shoppers see the "same" product twice in the grid. Reviews will also be split.
- **Fix (best):** Make one product, "Dual Bowl Automatic Cat Feeder – 3L", with a Color option (Black / White), each variant with its own images and SKU. 301-redirect `/products/2-in-1-smart-feeder-white` to the merged product, and update ad final URLs (or keep both URLs pointing to the right `?variant=` link).
- **Fix (quick):** Rewrite the white product's first paragraph and meta, and remove the white product from the collection grid (keep it reachable by link).
- **Who:** Claude via the API, after the owner agrees (ads URLs are affected).
- **Effort:** 1–2 hours.

### 10. Add a homepage meta description and fix weak homepage/collection SEO
- **Wrong:**
  - The shop description (homepage meta) is **empty**.
  - The "frontpage" collection is public, titled "Feeder 2-in-1", has 1 product, and appears in the footer "Products" menu.
  - Collections have no image (so no og:image when shared).
- **Why:** Without a meta description, Google writes its own snippet for the most important page. A thin 1-product collection is a weak, duplicate page.
- **Fix:**
  - In Online Store → Preferences, set the title to "PETME2 – Automatic Cat Feeders & Cat Water Fountains" and the description to: "Smart automatic cat feeders and quiet cat water fountains. App control, 1080P camera, stainless steel. Free U.S. shipping + 30-day money-back guarantee." (about 150 characters)
  - Remove "Feeder 2-in-1" from the footer menu, or rename the collection "Feeders for 2 Cats" and add the 3L dual feeder to it.
  - Add a collection image to each collection.
- **Who:** The owner sets Preferences (no Admin API for it). Claude does the menu and collections.
- **Effort:** 20 min.

### 11. Cut repetition on the product page and add a delivery estimate
- **Wrong:**
  - "Free U.S. shipping · 30-day guarantee" shows in: the text block under the price, the "Free shipping & 30-day guarantee" tab, the trust badges, the story CTA note, the guarantee section, the extras FAQ, and the sticky bar.
  - The product page has 9 sections. The FAQ is repeated on the homepage, the collection page, the product page and the FAQ page.
  - "How fast is shipping?" never says how fast.
- **Why:** Repetition hides the important info (what it does, size, price). No delivery date is a top reason people abandon carts.
- **Fix:**
  - Keep only one trust row under Add to cart. Remove the text block and the shipping tab, and remove the guarantee section (or the story CTA note).
  - Change the text block to "Free U.S. shipping · Arrives in 3–5 business days" (use real MCF transit times).
  - Answer the FAQ: "Orders ship from Amazon within 1–2 days and arrive in about 3–5 business days."
- **Who:** Claude in the theme (`build_v3.py` / `product.json`).
- **Effort:** 30 min.

### 12. Shorten the homepage
- **Wrong:** The homepage has 11 sections: hero, ticker, shop tabs, quiz, bento, 2 compare tables, guarantee, FAQ, FAQ schema and CTA. On a phone that is roughly 8,000 px of scroll. The 38 KB quiz plus the two tables say much the same thing.
- **Why:** Most visitors never reach the lower half. More sections also mean slower mobile load and more layout shift.
- **Fix:**
  - Keep: hero → product tabs → bento → one compare (feeders, with a link to the fountains compare) → reviews (once installed) → FAQ → CTA.
  - Move the quiz to `/pages/how-to-choose`, and move the fountains compare to the fountains collection page.
  - Keep the FAQ schema (it matches the visible FAQ).
- **Who:** Claude in the theme.
- **Effort:** 30 min.

### 13. Prevent the "Shipping calculated at checkout" line after adding a shipping policy
- **Wrong:** Dawn's price block prints "Shipping calculated at checkout" as soon as `shop.shipping_policy` is filled in, which you will do in #1.
- **Why:** It contradicts "Free U.S. shipping on every order", right next to the price.
- **Fix:** In the theme, override the locale key `products.product.shipping_policy_html` to "Free U.S. shipping. <a href='{{ link }}'>Shipping policy</a>". Or hide `.product__tax` with CSS.
- **Who:** Claude in the theme (`locales/en.default.json`).
- **Effort:** 5 min.

### 14. Check the discounts: the old Bundler app discount plus WELCOME10
- **Wrong:** Three discounts are active:
  - "Volume discount" (Bundler app, since July 2026)
  - WELCOME10 (10%, once per customer)
  - automatic free shipping

  The new theme has no Bundler app block, so the volume offer is not shown, but it may still apply or stack with other discounts.
- **Why:** Hidden discount stacking can cut margin, and a discount shoppers can't see doesn't help sales.
- **Fix:** Decide: either remove the Bundler discount and app, or add its block to the new product template. In each discount, check "Combinations" so WELCOME10 combines with free shipping but not with the volume discount.
- **Who:** The owner (app decision). Claude can read the settings and remove it via the API if asked.
- **Effort:** 15 min.

### 15. Build real links and give the blog images, plus product copy polish
- **Wrong:**
  - Ahrefs: DR 0, 0 organic keywords, 0 traffic. The 2,181 "backlinks" from 1,165 domains are almost all **spam** ("SEOExpress", "Premium PBN Network", "Buy Backlinks" anchors). This is negative-SEO / link-seller spam, not real links.
  - The 6 new articles have **no featured image**, so they show blank cards and no social image.
  - Product descriptions contain stuffed Amazon-style phrases, for example "Many cat automatic feeders have no camera", "With WiFi automatic cat feeder app control", "Turn on the cat food dispenser automatic schedule".
- **Why:** With no real links, product pages can't rank for "cat water fountain" (45K/mo, KD 10) or "automatic cat feeder" (30K, KD 20). Stuffed phrases read badly and hurt conversion.
- **Fix:**
  - Add a featured image with alt text to each article (use existing lifestyle photos).
  - Get 5–10 real links: the Amazon brand store, pet bloggers who review fountains, "best cat fountain" roundups, a Google Business/Merchant profile, and social profiles. Add those social URLs in theme settings so the Organization schema gets `sameAs`.
  - No disavow is needed for now; Google mostly ignores this kind of spam. Watch it monthly.
  - Rewrite the stuffed sentences in plain English.
  - Next keyword targets: "stainless steel cat water fountain" (2.3K, KD 0) on the 3.2L product page, "cat feeder with camera" (450, KD 2) on the camera page, "best cat water fountain" (10K, KD 0) as a buyer's-guide article.
- **Who:** Claude for the images, copy and theme. The owner for outreach and profiles.
- **Effort:** 2–4 hours, then ongoing.

---

## Smaller items (do when convenient)
- **Dual feeder connection:** the compare table says the 3L Dual is "App" while the others say "WiFi app", but the FAQ and How-to-choose page say "all feeders work over WiFi". Check what the dual feeder really uses (WiFi or Bluetooth) and make all pages match.
- **Camera feeder tags:** the camera feeder has no tags (the others do). Add them for search and filtering.
- **Footer menu:** has only Search and Your Privacy Choices. Fine, but the "information" menu does the real work, so it must be correct (see #1).
- **Contact page:** has a form but no email address. Show a support email, for example support@petme2.com, not a personal Gmail.
- **Old themes:** delete the 3 old unpublished themes ("Draft (Claude edits)", "CRO Draft (Aug 18)", "Premium Minimal") after publishing, to avoid confusion. The Premium Minimal theme still says "$50+".
- **Shop email:** Shopify's sender and contact email is a personal Gmail. Use a domain email (support@petme2.com) for better deliverability and trust.
- **Accessibility statement:** it promises WCAG 2.1 AA but gives no contact method. Add the email.

## Ads alignment (Shopify vs Amazon)
All Shopify prices match the Amazon prices you gave:

| Product | Price |
|---|---|
| Camera feeder | $52.99 |
| Dual feeders | $49.99 |
| 5L | $45.99 |
| Stainless | $39.99 |
| Three small fountains | $19.99 |

So ads can use one price everywhere. The only gap is the compare-at "was" prices (#6): make sure they match the Amazon "List Price" if you show one.

---

## Already good
- Every product has an SEO title of 55–58 characters, a meta description of 140–157 characters, a clear product title, and alt text on every image.
- 6 useful blog articles of about 1,000 words each, with 5–10 internal links to products and collections each.
- Collection SEO titles and descriptions are set, and collection intros are about 100 words.
- Clear offer, used the same way everywhere: free U.S. shipping, a 30-day money-back guarantee, and WELCOME10 (active, one use per customer).
- The new theme is a strong upgrade:
  - sticky add-to-cart bar
  - honest "Complete the setup" cross-sell
  - compare tables and FAQ with valid FAQPage schema
  - popup shown as a phone bottom sheet with exit intent on desktop, hidden for past buyers, with a focus trap and Esc to close
  - images lazy-loaded with a high-priority hero
  - reduced-motion support
  - Dawn's Product + Organization + WebSite schema
- The About, FAQ, Shipping, Returns and How-to-choose pages are clear, simple and honest (fulfilled by Amazon, dry food only).
- Menus have no broken links. All 8 products are active and in the right collection.
