# Setup Evaluation — Full Worked Examples

Skill: `setup-evaluation` | Load when producing output for this workflow.

## Example 1 — From skill workflow

**Input:** Evaluate setup for proc-2026-04-10-012

**Output:**
```
SETUP EVALUATION: FAIL
Issues found: 2
1. [Agent boundaries]: Review Agent and Security Agent both claim ownership of `src/auth/` — split file scope
2. [Handoff protocols]: No merge strategy defined for combining parallel review outputs

All other checks: PASS (decomposition quality, tool availability, outcome definition, skill consistency, spec linkage)
```

## Example 2 — From skill workflow

**Input:** Evaluate setup for proc-2026-04-10-015

**Output:**
```
SETUP EVALUATION: PASS
All checks passed (5 decomposition, 5 architecture, 3 cross-validation).
PASS recorded for: docs/architecture/2026-04-10-015-arch.md
Handing off to agent-launcher.
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
