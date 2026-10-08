# PETME2 Shopify redesign: Premium Minimal (2026-10-04)

Theme: **"PETME2 — Premium Minimal (Oct 2026)"**. It is a copy of the live theme and is **NOT published**. Only you can publish it.
The live store did not change. Product data changes (metafields, collection, product type) show on the live store too, but they look the same until you publish.

## How to see it
Shopify admin → Online Store → Themes → "PETME2 — Premium Minimal (Oct 2026)" → **Preview** (or **Customize**).
If you like it: **Publish**. If not: tell me what to change.

## What changed
| Area | Change |
|---|---|
| Colors | Orange removed everywhere. Black (#111) buttons, stone (#f6f5f3) backgrounds, square corners. The top bar is black now. |
| Homepage | New order: hero → trust bar → categories → product showcase (6 products) → **feeder comparison chart** → fountains → **fountain comparison chart** → video → slider → feature banner → before/after → feed |
| True copy only | Removed "Integrated Smart Feeder **Scale**" (no feeder has a scale) and "Feeding Calculator". Replaced placeholder text with real facts from the Amazon listings |
| Comparison charts | Feeders: 3L Dual / 5L WiFi / 3L Camera. Fountains: Stainless 3.2L / Steel Tray 2.2L / Transparent 2.2L / Classic 2L. Prices and photos update live from the product |
| Product page | Removed 7 sections that were wrong for most products: lorem-ipsum FAQ, "freeze-dried 39mm channel", "three feeding steps" on fountain pages, the "treats, toys, beds" banner, and more. Added: 4 feature icons, **What's in the box**, a real **FAQ** (feeder FAQ on feeders, fountain FAQ on fountains), and **Complete the setup** (feeder pages show the stainless fountain, fountain pages show the dual feeder). Turned on "You may also like" and the service row |
| Service row | "30-Days Return" → "Also on Amazon" (I don't know your return policy). Shipping now says $50+ (it said $49 before; the rest of the site says $50) |
| Footer | "© 2026 Petme2 by 2026." → "© 2026 PETME2. All rights reserved." |
| Products | The camera feeder product type is now "Automatic Pet Feeders" (it was empty). The 5L feeder was added to the **Feeders** collection (it was missing). "What's in the box" was added to 5 products |

## Your to-do (only you can do these)
1. **Preview, then Publish** the theme.
2. **Filters**: install the free **Shopify Search & Discovery** app → Filters → add: Product type, Price, Availability. They then show on the collection pages.
3. **Return policy**: tell me your real policy (30 days?). Then I'll add it back to the service row.
4. **Bundles**: the "Complete the setup" box is ready. Do you want a discount for buying feeder + fountain together (for example 10% off with the code SETUP10)? Say yes/no and the %.
5. **Prices on Shopify are higher than Amazon** ($65.99 / $54.99 / $29.99). Match Amazon? yes/no.
6. "What's in the box" is missing for the camera feeder, the stainless fountain and the steel-tray fountain. The Amazon data is unclear. Send me the box contents and I'll add them.

## Files
`shopify-theme/`: new sections (`sections/petme2-*.liquid`), the new templates (`index.json`, `product.json`, `settings_data.json`, `footer-group.json`), the `*-original.json` backups, and `build_index.py`.
