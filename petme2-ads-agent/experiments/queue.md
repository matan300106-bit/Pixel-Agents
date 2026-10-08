# Experiment queue

Owner: Experiment Lab. Status: **queued — no test is running.** Date: 2026-10-03.

## Decision

**No test starts until a campaign has 14 days of data** (CLAUDE.md section 9). The two campaigns
(Feeders, Fountains) are not live yet, so we have 0 days. During days 1–14 only the ramp-up rules
(`docs/ramp-up-rules.md`) run.

A queued test may start only when ALL are true on that day:
- The campaign has 14+ days of data.
- Fewer than 3 tests are running.
- The tested part spends 15% or less of the total daily budget (15% of $18 = about $2.70/day), or the owner says OK.
- Product has 21+ days of stock.
- The same test did not fail before (`learnings.md`).
- A file `experiments/YYYY-MM-DD-<name>.md` is written first (hypothesis, change, control, start date, end rule, metric).
- Keywords in a test are frozen: no ramp-up raises on them while the test runs (safety cuts still allowed).

**End rule for every test:** at least **14 days AND at least 100 clicks** on the test part. Then keep the winner,
undo the loser, write the result in `learnings.md`. If 100 clicks are not reached by day 28 of the test,
end it as "no result" and undo the change.

**Success metric for every test:** lower cost per sale (spend ÷ orders) with the **same or more orders** than the control.

---

## Test 1 — Lower bid on feeder exact keywords

- **Hypothesis:** a −15% bid on exact feeder keywords keeps the same orders at a lower cost per sale.
- **One change:** bid −15% on the 2 keywords in `Feeders-Exact` with the most clicks on day 14.
- **Control:** the other 2 keywords in `Feeders-Exact`, no change. Also compare with the same 2 keywords' 14 days before.
- **Start:** Feeders campaign day 15 or later, if both keywords have 50+ impressions in 3 days and at least 1 order.
- **End rule / metric:** as above.

## Test 2 — Phrase vs broad match for "cat water fountain"

- **Hypothesis:** phrase match brings fewer wrong searches than broad, so cost per sale is lower.
- **One change:** add "cat water fountain" as **phrase** in `Fountains-Broad`, same bid as the broad keyword.
- **Control:** "cat water fountain" **broad** in the same ad group (unchanged).
- **Start:** Fountains campaign day 15 or later.
- **End rule / metric:** as above, comparing the phrase keyword with the broad keyword.

## Test 3 — Top-of-search placement +25% (Feeders)

- **Hypothesis:** +25% top-of-search wins better spots that sell more, with the same or lower cost per sale.
- **One change:** top-of-search placement adjustment 0% → **+25%** on the Feeders campaign.
- **Control:** Fountains campaign stays at 0%, and Feeders' own 14 days before the test.
- **Start:** after Test 1 ends (so the two do not mix in the same campaign).
  This change covers the whole Feeders campaign ($10/day, more than 15% of the budget) → **needs owner OK**.
- **End rule / metric:** as above, plus check top-of-search cost per click does not go above $1.00.
