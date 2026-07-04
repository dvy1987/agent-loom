# Spec Crosscheck — Full Worked Examples

Skill: `spec-crosscheck` | Load when producing output for this workflow.

## Example 1 — From skill workflow

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

## Example 2 — Typical invocation

**Input:** "Run `spec-crosscheck` for [concrete task]"

**Output:**
```
Invoked `spec-crosscheck`.
Step 1: Locate inputs
Step 2: Run six checks
Step 3: Write the report
Crosscheck: <slug>
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
