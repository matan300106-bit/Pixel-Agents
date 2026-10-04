# PETME2 Shopify SEO plan (2026-10-04)

Applied by API on 2026-10-04: product SEO titles/metas (8), image alt text (56), collection SEO + descriptions (feeders, water-fountains). Backup: `shopify-seo-backup-2026-10-04.json`.

The items below are NOT applied. They are for the owner to do by hand.

## 1. Homepage title and meta description

The Admin API cannot set the homepage title/meta. Paste these in **Shopify admin → Online Store → Preferences → Title and meta description**:

- **Homepage title (51 chars):** `Automatic Cat Feeders & Cat Water Fountains | PETME2`
- **Homepage meta description (151 chars):** `Smart automatic cat feeders for 1 or 2 cats, a feeder with camera, and quiet cat water fountains in stainless steel. Free U.S. shipping on orders $50+.`

Also worth checking in the same screen: the social sharing image. Use a clean product photo, 1200 x 628 px.

## 2. Blog post ideas (Online Store → Blog posts)

Write helpful guides. Use only true product facts and no health or vet claims. Link to the matching product or collection 2 or 3 times in each post.

| # | Working title | Main keyword | Supporting keywords | Link to |
|---|---|---|---|---|
| 1 | How to Choose an Automatic Cat Feeder for 2 Cats | automatic cat feeder for 2 cats | dual bowl cat feeder, automatic cat feeder 2 cats, cat feeding station | /products/2-in-1-smart-feeder, /products/2-in-1-feeder-1 |
| 2 | Automatic Cat Feeder with Camera: What to Look For | automatic cat feeder with camera | wifi cat feeder, cat feeder with camera and app, 1080P | /products/smart-feeder |
| 3 | Stainless Steel vs Plastic Cat Water Fountains | stainless steel cat water fountain | cat water fountain stainless steel, metal cat water fountain | /products/water-fountain, /products/water-fountain-4 |
| 4 | How to Clean a Cat Water Fountain and When to Change the Filter | cat water fountain | cat fountain filter, pet water fountain cleaning | /collections/water-fountains |
| 5 | WiFi Cat Feeder Setup: Scheduling Meals from Your Phone | wifi cat feeder | automatic cat feeder app, smart pet feeder | /collections/feeders |
| 6 | Automatic Dog Feeder Guide for Small Dogs | automatic dog feeder | dog food dispenser, small dog feeder | /products/2-in-1-smart-feeder-white, /products/2-in-1-feeder-1 |

Tips: each post should be 900 to 1,500 words, with an H1 that matches the title, H2s that answer real questions, one short FAQ block at the end, and alt text on every image.

## 3. Technical SEO checks for the new theme

**Structured data**
- Product JSON-LD on every product page: name, image, description, brand "PETME2", sku, offers (price, priceCurrency USD, availability). Do not add aggregateRating or review markup unless real reviews are shown on the page.
- BreadcrumbList schema: Home → Collection → Product.
- Organization + WebSite schema on the homepage (logo, URL, sameAs for social profiles).
- FAQPage schema only where the FAQ is visible on the page, for example a product-page FAQ about filter changes or app setup. Use true answers only.
- Test with Google Rich Results Test and the Schema.org validator.

**Images**
- Product images: about 2048 x 2048 px source. Let Shopify serve sizes with `image_url: width:` and `srcset` / `sizes`.
- Serve WebP/AVIF through Shopify's CDN (automatic with `image_url`). Keep source files under about 500 KB.
- `loading="lazy"` on images below the fold. The first product image and hero image should use `loading="eager"` and `fetchpriority="high"`.
- Set width and height attributes on images so the layout does not shift (CLS).
- Keep alt text filled in for new uploads: product name plus what the image shows, 125 chars or less.
- Rename new image files descriptively before upload (e.g. `petme2-stainless-steel-cat-water-fountain-3-2l.jpg`, not `ChatGPT_Image_...png`).

**Page speed (Core Web Vitals targets: LCP < 2.5 s, INP < 200 ms, CLS < 0.1)**
- Run PageSpeed Insights on home, a collection page and a product page, on mobile.
- Remove unused apps and their leftover script snippets in `theme.liquid`.
- Defer non-critical JS. Avoid large sliders and auto-playing video in the hero.
- Limit web fonts to 1 or 2 families, use `font-display: swap`, and preload the main font.
- Do not lazy-load the LCP image.

**Crawl and indexing**
- Use one H1 per page: the product title on product pages and the collection title on collection pages.
- Canonicals: product links inside collections should point to `/products/handle`, not `/collections/x/products/handle`. Check the theme's product-card links.
- Submit `https://www.petme2.com/sitemap.xml` in Google Search Console and check Pages → Not indexed.
- Leave the default `robots.txt.liquid` unless there is a clear reason to change it.
- Check that petme2.com redirects to www.petme2.com with a single 301 (Domains settings).
- Check for 404s after the theme switch and add URL redirects (Navigation → URL Redirects) for any old URLs.
- Mobile: tap targets of 48 px or more, readable text of 16 px or more, and no horizontal scroll.

**On-page**
- Show the collection description (already written) on the collection template, above or below the product grid.
- Add internal links: homepage sections linking to /collections/feeders and /collections/water-fountains, and a "related products" block on product pages.
- Footer: links to Shipping policy and Contact pages.
- Review the "Feeder 2-in-1" collection (handle `frontpage`). It has no description or SEO. Hide it from search or give it its own meta if it is public.
