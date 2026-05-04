# Prioritisation Rubric

ICE scoring + feasibility gate for experiment-backlog. Use this for every backlog candidate. The feasibility gate is BINARY and BLOCKING — a high-ICE candidate that fails feasibility is REJECTED, not deprioritised.

---

## ICE Scoring (1–10 each, average → ICE)

### Impact

How big is the win if the hypothesis is correct?

| Score | Anchor |
|---|---|
| 1–2 | Tiny effect on a low-leverage metric. Easy to absorb as noise. |
| 3–4 | Modest effect on a secondary metric, or large effect on a low-leverage surface. |
| 5–6 | Material effect on a primary funnel metric (5–10% relative on activation, conversion, or retention). |
| 7–8 | Large effect on a primary funnel metric (10–20% relative) OR meaningful revenue impact. |
| 9–10 | Step-change on revenue, retention, or PMF — the kind of result that reshapes the roadmap. |

**Calibration tip:** most experiments deliver 0–5% lift, not 20%. Score generously, but be honest. If everything is a "9", the rubric is broken.

---

### Confidence

How strong is the prior that the hypothesis will work?

| Score | Anchor |
|---|---|
| 1–2 | Wild guess. No supporting data, no analogous result. |
| 3–4 | Plausible. Surface has known issues but no specific evidence the change helps. |
| 5–6 | User research, qualitative signals, OR analogous results from other surfaces support it. |
| 7–8 | Strong: prior win on similar surface, clean funnel data showing the pain point. |
| 9–10 | Near-certain — but at this level, ask whether the test is worth running vs just shipping. |

**Calibration tip:** if Confidence is 9–10, you may not need an experiment — consider direct ship + monitor, especially for low-risk changes.

---

### Ease

How cheap to design, instrument, and run?

| Score | Anchor |
|---|---|
| 1–2 | New schema / new infra / new platform integration required. Multi-week setup. |
| 3–4 | New events to instrument, dashboard work, ramp coordination. ~1 week. |
| 5–6 | Existing instrumentation; flag wiring + variant build only. 2–3 days. |
| 7–8 | Surface already instrumented; copy / minor UI change behind existing flag. <1 day. |
| 9–10 | Trivial: config change, content update, copy swap. |

---

## ICE Computation

`ICE = (Impact + Confidence + Ease) / 3`

Some teams use `ICE = Impact × Confidence × Ease`. Pick one and stay consistent across the backlog. Avoid mixing additive and multiplicative ICE.

---

## Feasibility Gate (BINARY, BLOCKING)

A candidate must pass ALL four to enter the active backlog.

### 1. Traffic

Does the surface have enough volume to detect the planned MDE in ≤ 8 weeks at 80% power?

- **PASS:** sample plan from `experiment-spec/references/mde-heuristics.md` is achievable.
- **FAIL → REJECT** (or downgrade to Directional, label explicitly).

Quick rule of thumb: if the surface gets fewer than ~3,000 weekly exposed units AND the baseline conversion is < 10%, most A/B tests will be underpowered.

---

### 2. Metric Latency

Does the primary metric mature within the test window?

- **Activation (Day 7):** OK for 14–28-day tests.
- **Retention (Day 30+):** requires longer test OR Phase-2 holdout.
- **Revenue lag (60+ days for SaaS):** requires Phase-2 holdout, not a fixed-horizon A/B.

- **PASS:** primary matures inside the planned window.
- **FAIL → REJECT** unless paired with a planned Phase-2 holdout.

---

### 3. Method Fit

Does `experimentation/references/method-selector.md` point at a clean method for this surface?

- **PASS:** A/B, Holdout, Switchback, Quasi-experiment, or MAB cleanly applies.
- **FAIL → REJECT** if the surface has interference + no clean cluster / switchback pattern, or if randomisation is impossible AND no quasi-experimental design exists.

---

### 4. Population Stability

Is the test population stable during the planned window?

- **Stable:** no major paid campaign launches, no big seasonality cliffs, no ongoing migrations.
- **FAIL → REJECT or SCHEDULE** for a stable window.

---

## Backlog File Format

```markdown
# Experiment Backlog

Living portfolio. Status: idea | designed | running | readout | archived.
Most recent first within each status.

---

## Active

| Rank | Surface | Hypothesis | Method | Class | ICE | Feasibility | Status | Owner |
|------|---------|-----------|--------|-------|-----|-------------|--------|-------|

## Rejected (with reason)

| Surface | Hypothesis | Reject reason |
|---------|-----------|---------------|

## Archived

| Surface | Hypothesis | Final decision | Date |
|---------|-----------|----------------|------|
```

---

## Anti-Patterns

- Treating feasibility as a tiebreaker instead of a gate.
- Inflating Impact scores to keep favourite ideas in the running.
- Reusing a stale ICE score after the surface's traffic profile changed.
- Carrying REJECTED items forever without re-evaluating whether feasibility has improved.
- Ranking by Ease alone (the "shipping the easy stuff" trap).
- Letting Confidence drive everything (the "shipping what feels safe" trap).
