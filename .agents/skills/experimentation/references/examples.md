# Experimentation — Full Worked Examples

Skill: `experimentation` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Step-by-step execution

**Input:** "Run `experimentation` on [concrete task]"

**Agent actions:**
1. Diagnose the Lifecycle Stage
2. Pre-Route Hooks (Optional)
3. Route to Child Skill
4. Enforce Lifecycle Completeness
5. Surface the Funnel-ROI Map
6. Hand Off Downstream

**Impact Report shape:**
```
Experiment: [name or "TBD"]
Lifecycle stage: [backlog | spec | runbook | readout]
Decision class: [Causal | Directional | Instrumentation]
Routed to: [child skill]
Upstream skills called: [list or none]
Downstream handoff: [list or none]
Next recommended step: [exact next action]
```

## Example 2 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- **A/B is not the universal answer.** Persistent treatments, lifecycle email, recommendations, and notification programs default to **holdouts**. Marketplaces / feeds / scheduling default to **switchbacks**. SEO / content default to **quasi-experiments**. Routing the user to the wrong method is the single biggest avoidable mistake.
- **Decision class declared up front, never retrofitted.** A Directional test cannot become "Causal" after the fact because the lift looked nice. Once tagged Directional, claims are forever stripped of significance language.
- **The orchestrator never analyses results itself.** Always route to `experiment-readout`. SRM and exposure-parity checks live there and are mandatory before any metric is reported.
- **Skipping a stage is allowed, but only with a recorded justification.** If the user wants to launch without a spec ("just a copy tweak"), force a one-line note in the artefact — silent skips break the learnings log later.

---

See `SKILL.md` for hard rules and verification checklist.

## Verification checklist (L3)

- [ ] Examples demonstrate SKILL.md hard rules, not generic chat
- [ ] Anti-skip or rationalization defense included where applicable
- [ ] Output artifacts or Impact Report shape is explicit
- [ ] Reader can trace input → concrete agent actions → outcome

## Suite note

See orchestrator skill and sibling references for full suite walkthrough.
- [ ] Cross-check against latest SKILL.md before shipping changes
- [ ] Cross-check against latest SKILL.md before shipping changes
- [ ] Cross-check against latest SKILL.md before shipping changes
- [ ] Cross-check against latest SKILL.md before shipping changes
