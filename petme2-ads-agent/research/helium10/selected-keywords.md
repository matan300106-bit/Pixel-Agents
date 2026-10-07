# Selected keywords for wide phrase-match test (2026-10-04)

Source: research/helium10/candidates.json (2,406 Helium 10 Cerebro keywords). Full list: `selected-keywords.json`.

Start bid = min(H10 suggested min bid, 60% of profit max CPC); floor 0.20; WiFi cap 0.25; basic cap 0.24; no H10 min -> 0.35 (dual/camera/stainless) or 0.20 (WiFi/basic).

| Group | Keywords | Total monthly SV | Already in campaigns | Shared with WiFi |
|---|---|---|---|---|
| dual | 40 | 348,949 | 8 | 0 |
| camera | 33 | 24,666 | 15 | 21 |
| wifi | 25 | 14,892 | 8 | 0 |
| stainless | 40 | 782,620 | 17 | 0 |
| basic | 25 | 151,626 | 13 | 0 |

Rules used: every feature word true for every ASIN in the group; competitor brands and wrong product types removed (birds/squirrels, microchip/RFID, wet food, gravity, filters, large dog, outdoor, heated, ceramic, wireless/battery fountains, slow/stand/mat/toy and similar); phrase-covered near-duplicates and reorders under 2,000 SV dropped.

Group assignment (no overlap except as noted): generic feeder terms -> Dual (best feeder margin). Camera/video/1080p/battery-backup terms -> Camera. WiFi/smart/app/elevated/large-capacity terms -> WiFi. The Camera feeder also has WiFi and an app, so Camera also lists 21 WiFi/smart/app terms (`also_in: wifi`). If both ad groups run them in one campaign, the Camera bid (0.35-0.74) wins over the WiFi bid (0.20). Keep each term in only one of the two groups. Generic fountain terms -> Stainless; quiet/small/kitten/kitty/plastic/dispenser terms -> Basic. Terms already in a Test-* ad group stay in that group.

## Dual Feeders (B0GHLSQMJ9, B0GHMCG8Q9) - max CPC 1.13

| # | Keyword | SV | H10 bid | H10 min | Start bid | Existing |
|---|---|---|---|---|---|---|
| 1 | automatic cat feeder | 187,032 | 1.39 | 1.19 | 0.68 | PETME2-SP-Feeders/Feeders-Exact (exact); PETME2-SP-Feeders/Feeders-Broad (broad) |
| 2 | automatic dog feeder | 32,356 | 1.34 | 1.02 | 0.68 | PETME2-SP-KeywordTest/Test-DualFeeders (phrase) |
| 3 | cat food dispenser | 23,065 | 0.79 | 0.63 | 0.63 | PETME2-SP-KeywordTest/Test-DualFeeders (phrase) |
| 4 | cat feeder automatic | 20,495 | 0.97 | 0.89 | 0.68 |  |
| 5 | cat automatic feeders | 14,453 | 0.92 | 0.8 | 0.68 |  |
| 6 | auto cat feeder | 8,838 | 1.52 | 1.17 | 0.68 | PETME2-SP-KeywordTest/Test-DualFeeders (phrase) |
| 7 | automatic cat feeder 2 cats | 4,741 | 1.46 | 1.13 | 0.68 | PETME2-SP-KeywordTest/Test-DualFeeders (phrase) |
| 8 | dog feeder automatic | 4,515 | 1.44 | 1.13 | 0.68 |  |
| 9 | automatic pet feeder | 4,241 | 1.48 | 1.29 | 0.68 | PETME2-SP-Feeders/Feeders-Exact (exact) |
| 10 | dog automatic feeders | 3,335 | 1.84 | 1.42 | 0.68 |  |

## Camera Feeder (B0GTCGYZDM) - max CPC 1.24

| # | Keyword | SV | H10 bid | H10 min | Start bid | Existing |
|---|---|---|---|---|---|---|
| 1 | automatic cat feeder with camera | 6,417 | 1.66 | 1.32 | 0.74 | PETME2-SP-Feeders/CameraFeeder-Exact (exact) |
| 2 | cat feeder with camera | 2,519 | 2.21 | 1.45 | 0.74 | PETME2-SP-Feeders/CameraFeeder-Exact (exact) |
| 3 | wifi automatic cat feeder app control | 1,244 | 1.76 | 1.45 | 0.74 |  |
| 4 | automatic dog feeder with camera | 977 | 1.91 | 1.36 | 0.74 |  |
| 5 | smart cat feeder | 882 | 1.79 | 1.55 | 0.74 | PETME2-SP-KeywordTest/Test-WiFiFeeder (phrase) |
| 6 | smart pet feeder | 880 | 1.79 | 1.37 | 0.74 | PETME2-SP-KeywordTest/Test-WiFiFeeder (phrase) |
| 7 | pet feeder with camera | 782 | 1.88 | 1.46 | 0.74 | PETME2-SP-Feeders/CameraFeeder-Exact (exact) |
| 8 | wifi cat feeder | 666 | 1.7 | 1.33 | 0.74 | PETME2-SP-Feeders/Feeders-Exact (exact) |
| 9 | automatic feeder with camera | 639 | 2.07 | 1.7 | 0.74 | PETME2-SP-KeywordTest/Test-CameraFeeder (phrase) |
| 10 | smart automatic dog feeder wifi app control | 632 | 1.79 | 1.7 | 0.74 |  |

## WiFi Feeder (B0GHH8L59K) - max CPC 0.26

| # | Keyword | SV | H10 bid | H10 min | Start bid | Existing |
|---|---|---|---|---|---|---|
| 1 | automatic cat feeder with app | 1,768 | 1.5 | 1.3 | 0.20 |  |
| 2 | wifi automatic cat feeder app control | 1,244 | 1.76 | 1.45 | 0.20 |  |
| 3 | smart cat feeder | 882 | 1.79 | 1.55 | 0.20 | PETME2-SP-KeywordTest/Test-WiFiFeeder (phrase) |
| 4 | smart pet feeder | 880 | 1.79 | 1.37 | 0.20 | PETME2-SP-KeywordTest/Test-WiFiFeeder (phrase) |
| 5 | large capacity automatic dog feeder | 880 | 1.57 | 1.22 | 0.20 |  |
| 6 | wifi cat feeder | 666 | 1.7 | 1.33 | 0.20 | PETME2-SP-Feeders/Feeders-Exact (exact) |
| 7 | smart automatic dog feeder wifi app control | 632 | 1.79 | 1.7 | 0.20 |  |
| 8 | automatic cat feeder wifi | 603 | 1.95 | 1.68 | 0.20 | PETME2-SP-KeywordTest/Test-WiFiFeeder (phrase) |
| 9 | smart feeder for cats | 593 | 1.71 | 1.26 | 0.20 |  |
| 10 | elevated cat feeder | 593 | 0.81 | 0.53 | 0.20 |  |

## Stainless Fountain (B0DR7FCLZR) - max CPC 1.39

| # | Keyword | SV | H10 bid | H10 min | Start bid | Existing |
|---|---|---|---|---|---|---|
| 1 | cat water fountain | 319,141 | 0.86 | 0.68 | 0.68 | PETME2-SP-Fountains/Fountains-Exact (exact); PETME2-SP-Fountains/Fountains-Broad (broad) |
| 2 | dog water fountain | 97,595 | 0.88 | 0.64 | 0.64 | PETME2-SP-KeywordTest/Test-StainlessFountain (phrase) |
| 3 | cat water fountain stainless steel | 79,303 | 0.88 | 0.78 | 0.78 | PETME2-SP-Fountains/Stainless-Exact (exact) |
| 4 | stainless steel cat water fountain | 70,227 | 1.05 | 0.81 | 0.81 | PETME2-SP-Fountains/Stainless-Exact (exact) |
| 5 | water fountains for cats indoor | 49,512 | 0.87 | 0.71 | 0.71 |  |
| 6 | pet water fountain | 42,109 | 0.81 | 0.61 | 0.61 | PETME2-SP-Fountains/Fountains-Exact (exact); PETME2-SP-Fountains/Fountains-Broad (broad) |
| 7 | cat fountain stainless steel | 15,361 | 1.27 | 0.86 | 0.83 |  |
| 8 | water fountain for dogs inside | 14,057 | 0.97 | 0.7 | 0.70 |  |
| 9 | stainless steel water fountain for cats | 8,816 | 1.23 | 1.08 | 0.83 | PETME2-SP-KeywordTest/Test-StainlessFountain (phrase) |
| 10 | stainless steel dog water fountain | 8,814 | 0.97 | 0.8 | 0.80 | PETME2-SP-KeywordTest/Test-StainlessFountain (phrase) |

## Basic Fountains (B0GHKN9DBR, B0GHLBGCP3, B0GHKRYV6W) - max CPC ~0.24-0.30

| # | Keyword | SV | H10 bid | H10 min | Start bid | Existing |
|---|---|---|---|---|---|---|
| 1 | cat fountain | 83,521 | 0.91 | 0.73 | 0.20 | PETME2-SP-KeywordTest/Test-BasicFountains (phrase) |
| 2 | cat water dispenser | 17,542 | 0.78 | 0.66 | 0.20 | PETME2-SP-KeywordTest/Test-BasicFountains (phrase) |
| 3 | pet fountain | 11,094 | 0.97 | 0.76 | 0.20 | PETME2-SP-KeywordTest/Test-BasicFountains (phrase) |
| 4 | pet water dispenser | 8,821 | 0.87 | 0.78 | 0.20 | PETME2-SP-KeywordTest/Test-BasicFountains (phrase) |
| 5 | cat drinking fountain | 5,948 | 1.14 | 0.87 | 0.20 | PETME2-SP-KeywordTest/Test-BasicFountains (phrase) |
| 6 | water dispenser for cats | 4,736 | 0.71 | 0.66 | 0.20 |  |
| 7 | kitten water fountain | 2,502 | 1.12 | 0.83 | 0.20 | PETME2-SP-KeywordTest/Test-BasicFountains (phrase) |
| 8 | plastic cat water fountain | 1,883 | 1.23 | 1.1 | 0.20 | PETME2-SP-KeywordTest/Test-BasicFountains (phrase) |
| 9 | kitty water fountain | 1,870 | 1.31 | 1.2 | 0.20 | PETME2-SP-KeywordTest/Test-BasicFountains (phrase) |
| 10 | small cat water fountain | 1,768 | 1.22 | 0.85 | 0.20 | PETME2-SP-AllProducts/More-Fountains22 (exact) |
