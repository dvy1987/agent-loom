# Process Decomposer — Full Worked Examples

Skill: `process-decomposer` | Load when producing output for this workflow.

## Example 1 — From skill workflow

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

## Example 2 — From skill workflow

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

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
