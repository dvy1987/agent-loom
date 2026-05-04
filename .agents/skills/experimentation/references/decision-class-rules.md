# Decision Class Rules

Every experiment must be labelled one of three decision classes before launch. The class governs which gates apply and which claims are allowed. This is the single most important discipline in the suite — it eliminates the "looks significant, ship it" failure mode without forcing rigour everyone will route around.

---

## The Three Classes

### 1. Causal Decision

**Definition:** the outcome of the experiment will directly determine a ship/keep/kill choice with material business impact.

**Examples:** new pricing structure, paywall redesign, onboarding rewrite, new core loop, model swap on a recommendation surface, removing a feature.

**Required gates (block if any fail):**
- Falsifiable hypothesis declared.
- Primary metric declared, with a direction and a minimum detectable effect (MDE).
- Guardrail metrics declared (at least 1 — typically downstream activation, retention, revenue, error rate, or user complaints).
- Sample/duration plan present and adequate for the MDE at 80% power, alpha 0.05.
- Decision rule declared pre-launch (e.g. "ship if primary +≥3% with no guardrail breach; iterate if directional positive but underpowered; kill if neutral or negative").
- Peek policy declared (default: no peeking; if early stops desired → sequential testing or alpha-spending).
- SRM check pre-registered for readout.
- Validity threats listed (novelty, primacy, interference, contamination, confounding).

**Allowed claims:** statistical significance, effect-size confidence intervals, ship/keep/kill decisions.

**Banned without explicit pre-registration:** segment-level wins, secondary-metric headlines, post-hoc subgroup discoveries.

---

### 2. Directional Exploration

**Definition:** the team wants signal to inform direction, but the experiment lacks the power, traffic, or duration to support a causal claim.

**Examples:** small-segment A/B on a low-volume page, a 5-day test on a B2B product, a multi-arm exploration of copy variants without enough sample for clean A/B/n.

**Required gates:**
- Hypothesis declared.
- Primary metric declared.
- Decision class explicitly labelled **Directional Exploration** in the spec.
- Honest acknowledgement of underpower in the spec.

**Allowed claims:** "the data is consistent with X", "directionally suggests Y", "informs further investigation". Effect size point estimates without significance claims are OK if uncertainty is shown.

**Banned:** the words "statistically significant", "winner", "lift", "uplift", or "ship". Decisions made on directional tests must be labelled as "best-guess pending further validation".

**Why this class exists:** small teams will run underpowered tests anyway. The trap is that under-powered results look like wins. Forcing the Directional label preserves rigour without blocking learning.

---

### 3. Instrumentation Shakedown

**Definition:** the experiment exists to validate that tracking, exposure, and assignment work — not to learn about user behaviour.

**Examples:** A/A test, ramp-up to 1% to verify SRM is healthy, smoke-test of a new event pipeline, end-to-end check of a new flag system.

**Required gates:**
- Purpose declared (e.g. "verify SRM under 50/50 split", "confirm exposure event fires for both variants").
- Pass/fail criteria declared (e.g. "SRM p-value ≥ 0.05, exposure parity within 1%").
- Time-bounded (typically 1–7 days).

**Allowed claims:** instrumentation works / does not work. **No business claims**, no metric movement claims, no user-behaviour conclusions.

**Banned:** any reference to lift, conversion change, or product effect. If the test surfaces an unexpected metric movement, it converts into a separate Causal Decision experiment with a fresh spec.

---

## Class Selection Cheatsheet

| Question | Answer | Class |
|---|---|---|
| Will this test directly drive a ship/keep/kill decision? | Yes, with adequate power | **Causal** |
| Same as above but underpowered or short duration? | Yes | Run as **Directional**, OR delay until power is there |
| Is the goal to validate tracking, randomisation, or pipeline? | Yes | **Instrumentation** |
| Want to ship-and-watch without a real test? | — | Not an experiment; this is a feature flag rollout. Don't dress it up. |

---

## Downgrade and Upgrade Rules

- **Downgrade Causal → Directional:** allowed if traffic shortfall is detected. The spec must be updated, the decision rule revised, and the class change recorded with a one-line reason.
- **Upgrade Directional → Causal:** never retroactively. A re-run with adequate power and a fresh spec is required.
- **Instrumentation surprise:** if instrumentation tests surface unexpected metric movement, do NOT publish it as a result. Open a fresh Causal experiment to investigate.

---

## Why This Matters

Most product teams fail at experimentation in one of two ways:

1. They run rigorous tests too rarely — and ship features blindly the rest of the time.
2. They run lots of tests with weak rigour and convince themselves underpowered results are wins — leading to phantom lifts that don't reproduce in production.

The decision-class label fixes both. Causal tests get the rigour they need; Directional tests can run without polluting the evidence base; Instrumentation tests stop pretending to be experiments. Every spec, every runbook, every readout file in `docs/experiments/` must carry the label in its first 5 lines.
