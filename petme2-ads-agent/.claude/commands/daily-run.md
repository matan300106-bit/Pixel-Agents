---
description: Run the PETME2 ads team daily routine (Collector → Analyst → Guardian → Optimizer → Experiment Lab → Guardian → Reporter)
---
You are the **Manager**. Follow `CLAUDE.md` section 7. Run each step with its subagent, in order, and pass the results to the next one:

1. **collector**: fresh data (SP-API snapshot + ads files from `inbox/`). If ads files are missing, download them in the browser first (`docs/how-to-download-reports.md`).
2. **analyst**: 7 / 14 / 30 day numbers vs targets, waste, winners.
3. **guardian**: inventory check and emergency stop check.
4. **optimizer**: daily proposals.
5. **experiment-lab**: running tests, end finished ones, new proposals.
6. **guardian**: review all proposals → approve / block / send to owner. Apply items the owner marked APPROVED (bulk file only).
7. **reporter**: daily report (+ weekly on Mondays).
8. Update `changes-log.csv` and `learnings.md`.

End with a 5-line summary for the owner in simple English and the list of things waiting for approval.
