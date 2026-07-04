# Setup Evaluation — Full Worked Examples

Skill: `setup-evaluation` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** Evaluate setup for proc-2026-04-10-012

**Output:**
```
SETUP EVALUATION: FAIL
Issues found: 2
1. [Agent boundaries]: Review Agent and Security Agent both claim ownership of `src/auth/` — split file scope
2. [Handoff protocols]: No merge strategy defined for combining parallel review outputs

All other checks: PASS (decomposition quality, tool availability, outcome definition, skill consistency, spec linkage)
```

## Example 2 — Documented workflow

**Input:** Evaluate setup for proc-2026-04-10-015

**Output:**
```
SETUP EVALUATION: PASS
All checks passed (5 decomposition, 5 architecture, 3 cross-validation).
PASS recorded for: docs/architecture/2026-04-10-015-arch.md
Handing off to agent-launcher.
```

## Example 3 — Step-by-step execution

**Input:** "Run `setup-evaluation` on [concrete task]"

**Agent actions:**
1. Read Artifacts
2. Evaluate Decomposition
3. Evaluate Architecture
4. Cross-Validate
5. Verdict

**Impact Report shape:**
```
Setup evaluation for: [proc-ID]
Verdict: PASS | FAIL
Issues found: [N]
Decomposition checks: [passed/total]
Architecture checks: [passed/total]
Cross-validation checks: [passed/total]
Next: agent-launcher (if PASS) | agent-builder revision (if FAIL)
```

## Example 4 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- This skill runs from a SEPARATE agent (setup-evaluator) to avoid bias. If agent-builder calls it directly, the independence is lost.
- A "partial pass" is still a FAIL — all checks must pass.
- Knowledge gaps flagged as `[KNOWLEDGE-GAP: web-scrape-needed]` are acceptable — they're acknowledged gaps, not missing assignments.
- If the same setup fails 3 times, escalate to the user instead of looping.

---

See `SKILL.md` for hard rules and verification checklist.
