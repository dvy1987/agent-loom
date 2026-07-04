# Reality Check — Full Worked Examples

Skill: `reality-check` | Load when producing output for this workflow.

## Example 1 — From skill workflow

**Input:** Reality-check this agent skill library. It claims it can handle any coding or business process.

**Output:**
```
[Step 1: Read README, PRD, architecture.md, all skill files, process registry, git log, changelogs]

## Claim Assessment (sample)
| Claim | Verdict | Score | Key Evidence |
|-------|---------|:---:|--------------|
| "Complete any process" | False | 1/10 | Process registry empty. No end-to-end execution proof. |
| "Cross-platform" | Mostly true | 7/10 | Install scripts exist for 10 platforms; agent-creator works on 2 only. |
| "Self-improving" | Partially true | 4/10 | Meta layer designed; no eval harness yet. |

## Top Gap: No persistent memory (Fatal)
"Learning from past chats" requires storage + retrieval. Neither exists. Lightweight: markdown run ledger. Medium: local SQLite + FTS5. Heavyweight: hosted memory API.

## Verdict
Composite: 2/10 for headline claim. Skill library: 7/10. Control plane: 4/10. Autonomous execution: 1/10.

[Findings: docs/2026-04-13-reality-check-findings.md | Roadmap: docs/2026-04-13-roadmap-and-implementation-plan.md]
```

## Example 2 — Typical invocation

**Input:** "Run `reality-check` for [concrete task]"

**Output:**
```
Invoked `reality-check`.
Step 1: Discover What the Project Claims to Be
Step 2: Gather Evidence (Silent Scan)
Step 3: Extract Claims
Reality check complete: [project/product name]
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
