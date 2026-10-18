# Plan: 2 new Sponsored Products campaigns (Feeders + Fountains)

Status: **suggested**. Nothing is created yet. Waiting for the owner's answers (bottom of this file).
Date: 2026-10-03

## Why this setup

- In Sponsored Products, **auto or manual is chosen per campaign**. You want only 2 campaigns, so both are **Manual**.
  Inside each campaign, one **Broad** ad group does the "discovery" job that an auto campaign usually does.
- Separate ad groups for **Exact** and **Broad**. Then we see clearly which search terms sell, and we can move
  winners to Exact (harvesting).
- Products with a special feature (camera, WiFi, stainless steel) get their **own ad group**. Then a "camera"
  search only shows the camera feeder.
- Bidding strategy: **Dynamic bids – down only** (safe for a start). Top-of-search placement: **+0%** for the first 14 days,
  then we test +25% (Experiment Lab).
- Ignore the first 14 days for big decisions. New campaigns need data (about 15–30 clicks per day).

## Money check (per unit, before product cost)

| Product | Price | Amazon fees | Left before product cost |
|---|---|---|---|
| B0DR7FCLZR Stainless fountain 3.2L | $39.99 | $12.90 | $27.09 |
| B0GHKN9DBR Fountain | $19.99 | $9.76 | $10.23 |
| Other fountains / feeders | $19.99–$52.99 | FBA fee missing in API | unknown |

**The $19.99 fountains have very little margin.** If the product cost is about $5, break-even ACOS is only about 25%.
So the fountain bids must be low. We need the **product cost for each ASIN** to set exact targets.

## Campaign 1: `PETME2 | SP | Feeders | Manual`

- Daily budget: **$25** (suggested)
- Start: **PAUSED**, enable after you approve.

| Ad group | Products (ads) | Match | Keywords | Start bid |
|---|---|---|---|---|
| Feeders – Exact | B0GHH8L59K, B0GHLSQMJ9, B0GHMCG8Q9 | Exact | automatic cat feeder · automatic pet feeder · cat feeder automatic · timed cat feeder · automatic cat feeder for 2 cats · dual bowl automatic cat feeder · automatic cat food dispenser | $1.10 |
| Camera Feeder – Exact | B0GTCGYZDM | Exact | automatic cat feeder with camera · cat feeder with camera · pet feeder with camera · automatic pet feeder with camera | $1.20 |
| WiFi Feeder – Exact | B0GHH8L59K | Exact | wifi cat feeder · automatic cat feeder with app · smart cat feeder · automatic cat feeder wifi | $1.10 |
| Feeders – Broad | all 4 feeders | Broad | automatic cat feeder · pet feeder · cat food dispenser | $0.80 |

Negative keywords (campaign level, phrase): `water`, `fountain`, `bird`, `fish`, `horse`, `chicken`, `slow feeder`, `bowl only`, `replacement`.
Treat dispenser (B0GHMCG8Q9): check if it is really a feeder. If it is a treat toy, give it its own ad group with treat keywords.

## Campaign 2: `PETME2 | SP | Fountains | Manual`

- Daily budget: **$20** (suggested)
- Start: **PAUSED**, enable after you approve.

| Ad group | Products (ads) | Match | Keywords | Start bid |
|---|---|---|---|---|
| Stainless Fountain – Exact | B0DR7FCLZR | Exact | stainless steel cat water fountain · cat water fountain stainless steel · metal cat water fountain · large cat water fountain · stainless steel pet water fountain | $1.00 |
| Fountains – Exact | B0GHKN9DBR (hero) | Exact | cat water fountain · pet water fountain · water fountain for cats · cat fountain · cat water fountain for drinking · quiet cat water fountain | $0.60 |
| Fountains – Broad | B0DR7FCLZR, B0GHKN9DBR | Broad | cat water fountain · pet water fountain · dog water fountain | $0.50 |

Negative keywords (campaign level, phrase): `filter`, `filters`, `replacement`, `pump`, `feeder`, `bird`, `outdoor`, `garden`, `ceramic` (only if the product is not ceramic).

**Only one $19.99 fountain in the ads at first.** The 3 $19.99 fountains (B0GHKN9DBR, B0GHLBGCP3, B0GHKRYV6W) look very similar.
If all three are in one ad group, they compete with each other and split the data. B0GHKN9DBR sells best, so it starts alone.
Later we can test the others (Experiment Lab).

## Total

About **$45/day** (about $1,350/month) for both campaigns. Inventory is fine. Every product has more than 100 days of stock.

## What I need from you

1. **Do you already have campaigns** for these products? If yes, I must see them first. New campaigns could compete with the old ones.
2. **Product cost per unit** (and shipping to Amazon) for each ASIN, so I can set target ACOS.
3. **OK with the budgets** ($25 feeders, $20 fountains) and **max bid** (suggested: $2.00)?
4. Is **B0GHMCG8Q9** a feeder or a treat dispenser? Is the 3.2L fountain really stainless steel inside?
5. **Mode**: creating campaigns is a change. The project is in `audit` mode (read only). Only you can change it (to `supervised`).
