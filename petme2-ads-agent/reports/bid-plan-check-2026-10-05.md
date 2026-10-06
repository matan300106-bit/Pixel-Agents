# Bid plan check - 2026-10-05

Sheet: PETME2_bid_plan_2026-10-04 (272 rows). Read only, nothing changed.

Note on rounding: when old x1.5 lands on a half cent (e.g. 0.35 x1.5 = 0.525), the plan rounds down (0.52) so it stays "not above old x1.5". I count that as OK.

## 1. Rows per ad group, and how many follow the rules

| Campaign | Ad group | Rows | Follow rules |
|---|---|---|---|
| Keyword Test - Phrase | Test - Basic Fountains | 25 | 25 |
| Keyword Test - Phrase | Test - Camera Feeder | 44 | 43 |
| Keyword Test - Phrase | Test - Dual Feeders | 50 | 50 |
| Keyword Test - Phrase | Test - Stainless Fountain | 44 | 44 |
| Keyword Test - Phrase | Test - WiFi Feeder | 19 | 19 |
| Feeders - Exact | Camera Feeder - Exact | 6 | 6 |
| Feeders - Exact | Dual Feeders (white+black) - Exact | 8 | 8 |
| Feeders - Exact | WiFi Feeder Exact | 5 | 5 |
| Fountains - Exact | $19.99 Fountains - Exact (low margin) | 5 | 5 |
| Fountains - Exact | Stainless Fountain 3.2L - Exact | 10 | 10 |
| Brand - Exact | PETME2 Brand - Exact | 3 | 3 |
| Discovery - Auto | Auto - $19.99 Fountains | 5 | 5 |
| Discovery - Auto | Auto - 5L WiFi Feeder | 5 | 5 |
| Discovery - Auto | Auto - Camera Feeder | 5 | 5 |
| Discovery - Auto | Auto - Dual Feeders | 5 | 5 |
| Discovery - Auto | Auto - Stainless Fountain | 5 | 5 |
| Competitors - ASIN | Competitors - $19.99 Fountains | 6 | 6 |
| Competitors - ASIN | Competitors - 5L WiFi Feeder (low bids) | 4 | 4 |
| Competitors - ASIN | Competitors - Camera Feeder | 6 | 6 |
| Competitors - ASIN | Competitors - Dual Feeders | 6 | 6 |
| Competitors - ASIN | Competitors - Stainless Fountain | 6 | 6 |
| **Total** | | **272** | **271** |

No bid is above its cap. No bid is below its old bid. No bid is above old x1.5.

## 2. Rows that break a rule

Only 1, and it is a 1-cent rounding miss:

| Sheet row | Ad group | Keyword | Old | Range | Expected | Planned |
|---|---|---|---|---|---|---|
| 62 | Test - Camera Feeder | smart petfeeder | 0.35 | none | 0.44 (0.35 x1.25 = 0.4375) | 0.43 |

## 3. Planned bid still BELOW Amazon's suggested low end

241 of 272 rows (89%). These will likely still get almost no impressions.

| Ad group | Rows below | Avg gap to low end |
|---|---|---|
| Test - Basic Fountains | 25 | $0.50 |
| Test - Camera Feeder | 41 | $0.66 |
| Test - Dual Feeders | 45 | $0.44 |
| Test - Stainless Fountain | 39 | $0.49 |
| Test - WiFi Feeder | 18 | $0.89 |
| Camera Feeder - Exact | 6 | $0.55 |
| Dual Feeders (white+black) - Exact | 7 | $0.40 |
| WiFi Feeder Exact | 5 | $0.89 |
| $19.99 Fountains - Exact (low margin) | 5 | $0.53 |
| Stainless Fountain 3.2L - Exact | 6 | $0.66 |
| Auto - $19.99 Fountains | 5 | $0.28 |
| Auto - 5L WiFi Feeder | 4 | $0.37 |
| Auto - Camera Feeder | 4 | $0.14 |
| Auto - Dual Feeders | 4 | $0.18 |
| Auto - Stainless Fountain | 3 | $0.17 |
| Competitors - $19.99 Fountains | 6 | $0.48 |
| Competitors - 5L WiFi Feeder (low bids) | 4 | $0.53 |
| Competitors - Camera Feeder | 5 | $0.16 |
| Competitors - Dual Feeders | 5 | $0.19 |
| Competitors - Stainless Fountain | 4 | $0.23 |
| **Total** | **241** | |

Brand rows (3) have no suggested range, so they are not counted.
Main reasons: the x1.5 limit (WiFi and Basic Fountain bids start at $0.20, so they only reach $0.30) and the caps (many Camera/Dual low ends are $1.00-$2.70, cap is $0.85). With these caps, many keywords can never reach the low end.

## 4. Average old bid vs average new bid

| Ad group | Avg old | Avg new |
|---|---|---|
| Test - Basic Fountains | 0.200 | 0.300 |
| Test - Camera Feeder | 0.515 | 0.675 |
| Test - Dual Feeders | 0.560 | 0.739 |
| Test - Stainless Fountain | 0.608 | 0.794 |
| Test - WiFi Feeder | 0.200 | 0.297 |
| Camera Feeder - Exact | 0.675 | 0.850 |
| Dual Feeders (white+black) - Exact | 0.685 | 0.840 |
| WiFi Feeder Exact | 0.250 | 0.370 |
| $19.99 Fountains - Exact (low margin) | 0.220 | 0.330 |
| Stainless Fountain 3.2L - Exact | 0.688 | 0.844 |
| PETME2 Brand - Exact | 0.240 | 0.300 |
| Auto - $19.99 Fountains | 0.220 | 0.330 |
| Auto - 5L WiFi Feeder | 0.200 | 0.298 |
| Auto - Camera Feeder | 0.400 | 0.566 |
| Auto - Dual Feeders | 0.400 | 0.566 |
| Auto - Stainless Fountain | 0.400 | 0.566 |
| Competitors - $19.99 Fountains | 0.240 | 0.360 |
| Competitors - 5L WiFi Feeder (low bids) | 0.250 | 0.370 |
| Competitors - Camera Feeder | 0.533 | 0.768 |
| Competitors - Dual Feeders | 0.483 | 0.683 |
| Competitors - Stainless Fountain | 0.467 | 0.640 |
| **All 272 rows** | **0.460** | **0.615** (+34%) |
