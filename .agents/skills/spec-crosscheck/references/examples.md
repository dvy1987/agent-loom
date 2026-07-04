# Spec Crosscheck — Full Worked Examples

Skill: `spec-crosscheck` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** /analyze the magic-link feature.

**Output:**
```
Loaded:
- docs/constitution.md@2
- docs/specs/2026-05-02-magic-link-feature-spec.md (Approved)
- docs/plans/2026-05-02-magic-link-plan.md
- docs/plans/2026-05-02-magic-link-tasks.md (12 tasks)

Verdict: FAIL (3 findings)

A. Spec readiness: PASS
B. Constitution coverage: FAIL — C-2.4 (token TTL ≤15min) referenced in spec but no task enforces it. Add server-side TTL check task.
C. Spec→Plan traceability: PASS
D. Plan→Spec traceability: FAIL — Task T-9 ("send analytics event on login") not in spec FRs. Either add FR or remove task.
E. Task quality: PASS
F. Out-of-Scope adherence: FAIL — Task T-11 ("add Google OAuth fallback") violates spec out-of-scope ("no SSO/OAuth").

Required:
- [ ] Add task enforcing token TTL ≤15min (or waive C-2.4 with rationale)
- [ ] Resolve T-9 (add FR or drop task)
- [ ] Remove T-11

Saved to `docs/reviews/2026-05-02-magic-link-spec-crosscheck.md`.
```

## Example 2 — Step-by-step execution

**Input:** "Run `spec-crosscheck` on [concrete task]"

**Agent actions:**
1. Locate inputs
2. Run six checks
3. Write the report
4. Save, log, present

**Impact Report shape:**
```
Crosscheck: <slug>
Verdict: PASS | FAIL
Checks: A=<v> B=<v> C=<v> D=<v> E=<v> F=<v>
Findings: <N> (severity breakdown)
Saved: docs/reviews/YYYY-MM-DD-<slug>-spec-crosscheck.md
Logged: docs/skill-outputs/SKILL-OUTPUTS.md
Implementation: gated|unblocked
```

## Example 3 — Anti-skip (rationalization defense)

**Input:** Agent tries to skip a gate

| Excuse | Reality |
|---|---|
| "Reason to PASS anyway" | Reality |
| "Only 1 `[NEEDS CLARIFICATION]` left — close enough" | Hard rule: PASS forbidden while ANY marker remains. The single remaining one is usually the riskiest |
| "Constitution rule is small, an implicit waiver is fine" | Implicit waivers fail crosscheck. Force the spec to spell it out in `## Constitution Waivers` with rule ID + rationale |
| "Task lacks a DoD but the team knows what's meant" | Tribal knowledge fails the next agent. No DoD = FAIL, fix in the artefact not in the head |

## Example 4 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- A PASS doesn't mean the implementation is correct — it means the spec, plan, and tasks are mutually consistent and the spec is unambiguous. Correctness is verified by tests after implementation.
- "Constitutional waivers" are real — sometimes a feature legitimately needs to break a rule. Require explicit `## Constitution Waivers` in the spec with rule ID and rationale; never let a waiver be implicit.
- This skill is read-only. Do not edit any spec/plan/task to make checks pass — instruct the user to fix and re-run.
- Re-runs are cheap. After the user fixes findings, re-run rather than guessing.

---

See `SKILL.md` for hard rules and verification checklist.
