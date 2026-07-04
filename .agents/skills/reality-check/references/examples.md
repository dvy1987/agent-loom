# Reality Check — Full Worked Examples

Skill: `reality-check` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

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

## Example 2 — Step-by-step execution

**Input:** "Run `reality-check` on [concrete task]"

**Agent actions:**
1. Discover What the Project Claims to Be
2. Gather Evidence (Silent Scan)
3. Extract Claims
4. Score Each Claim
5. Identify Architectural Gaps
6. Competitive Positioning
7. Creative Solutions
8. Adversarial Pressure Test

**Impact Report shape:**
```
Reality check complete: [project/product name]
Claims evaluated: [N]
Composite score: [N]/10
Gaps found: [N] fatal, [N] significant, [N] minor
Competitors compared: [N]
Solutions proposed: [N]
Findings: docs/YYYY-MM-DD-reality-check-findings.md
Roadmap: docs/YYYY-MM-DD-roadmap-and-implementation-plan.md
```

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- **Best agent configurations achieve <65% on production benchmarks** (AlphaEval 2026: 94 real-world tasks from 7 companies, top score 64.41/100). Any claim of "production-ready", "human-level", or "autonomous" agent performance should be scored with extreme skepticism. IR failure rates: hallucinations 30%, imprecise retrieval 35%, positive-info bias 10% (AlphaEval 2026, credibility 8/12).
- Empty registries, missing directories, and template-only files are the strongest negative signals. "Designed but not populated" ≠ "works."
- README examples that describe what WOULD happen (aspirational flow diagrams) are not evidence of capability. Check for actual execution artifacts.
- Cross-platform claims require per-platform verification. "Installed everywhere" ≠ "works equally everywhere."

---

See `SKILL.md` for hard rules and verification checklist.
