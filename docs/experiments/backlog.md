# Experiment Backlog

Living portfolio. Status: idea | designed | running | readout | archived.
Most recent first within each status.

Every candidate is scored with ICE (Impact + Confidence + Ease, each 1–10) and must clear the 4-part feasibility gate before entering the Active table:

1. **Traffic** — surface has enough volume to detect planned MDE in ≤ 8 weeks at 80% power
2. **Metric latency** — primary metric matures inside the test window
3. **Method fit** — A/B / Holdout / Switchback / Quasi / MAB cleanly applies (see `experimentation/references/method-selector.md`)
4. **Population stability** — no major paid campaign / seasonality cliff / migration during window

High-ICE candidates that fail feasibility move to **Rejected** with the reason recorded. Re-evaluate when feasibility improves.

See `experiment-backlog/references/prioritization-rubric.md` for ICE 1–10 anchors.

---

## Active

| Rank | Surface | Hypothesis | Method | Class | ICE | Feasibility | Status | Owner |
|------|---------|-----------|--------|-------|-----|-------------|--------|-------|

---

## Rejected (with reason)

| Surface | Hypothesis | Reject reason |
|---------|-----------|---------------|

---

## Archived

| Surface | Hypothesis | Final decision | Date |
|---------|-----------|----------------|------|
