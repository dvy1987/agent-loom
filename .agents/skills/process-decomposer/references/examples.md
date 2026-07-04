# Process Decomposer — Full Worked Examples

Skill: `process-decomposer` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** Add dark mode to the React app

**Output:**
```
Let me make sure I understand: you want a dark/light theme toggle for the React frontend. I scanned the codebase — you're using Tailwind CSS with no existing theme system.

Two quick questions:
1. **What does done look like?** e.g., toggle in settings, persists across sessions, all components themed?
2. **Should this follow the OS preference by default**, or always start in light mode?

[After user answers]

[Triage] Checked process.md — no match found.
Complexity: skill-chain (sequential, no agent specialization needed).
Proceeding to decompose...
```

## Example 2 — Documented workflow

**Input:** I want to plan out building a multi-agent code review pipeline. Can you spec it out and create tasks?

**Output:**
```
Here's my understanding: you want a pipeline where multiple specialized agents (e.g., security, code quality, test coverage) review PRs in parallel, then aggregate results. Is that right?

One question: **Should agents block the PR merge on critical findings**, or just report?

[After user confirms]

[Triage] Checked process.md — partial match found:
- proc-2026-04-08-012: "Code review automation" (single-reviewer variant)

This needs planning deliverables (spec + plan + TODO). Routing to `problem-to-plan` with confirmed problem statement.
```

## Example 3 — Step-by-step execution

**Input:** "Run `process-decomposer` on [concrete task]"

**Agent actions:**
1. Understand the Problem
2. Complexity Triage (Layer 1)
3. Define Outcome (Hard Gate)
4. Decompose Into Steps
5. Knowledge Gap Resolution
6. Write Process Entry
7. Pattern Learning

**Impact Report shape:**
```
Process decomposed: [task description]
Complexity class: exact-match | single-skill | skill-chain | agent-chain
Process entry: docs/processes/YYYY-MM-DD-<slug>.md
Registry updated: docs/processes/process.md (volume N)
Steps: [N] ([M] parallel)
Knowledge gaps: [N] flagged
Next: [execution | agent-builder | skill routing]
```

## Example 4 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- Triage must read ALL process.md volumes — not just the first one.
- "Exact match" means same outcome cluster AND same nuance — same cluster alone is partial.
- `skill-chain` tasks still execute under `project-orchestrator` so the learning loop stays intact.
- This skill does NOT replace `brainstorming` or `implementation-plan`. Brainstorming = what to build. This = how to execute.

---

See `SKILL.md` for hard rules and verification checklist.
