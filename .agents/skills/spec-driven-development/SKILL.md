---
name: spec-driven-development
description: >
  Orchestrator for spec-driven development (SDD) — the discipline of writing
  executable specs before code, with a constitution above them and a hard
  cross-check gate before implementation. Mirrors GitHub Spec Kit / AWS Kiro
  slash-command shape. Routes /constitution, /specify, /clarify, /plan,
  /tasks, /analyze, /implement to the right leaf skill. Load when the user
  says "spec-driven development", "SDD", "specs-first workflow", "run the
  spec loop", "/specify a feature", "/plan from this spec", "do spec-driven
  for this", "GitHub Spec Kit workflow", "Kiro workflow", or invokes any
  SDD-style slash command. Single entry point for all SDD workflows.
license: MIT
metadata:
  author: dvy1987
  version: "1.0"
  category: project-specific
  sources: GitHub Spec Kit, AWS Kiro, agentskills.io
---

# Spec-Driven Development

You are the SDD Orchestrator. You route specs-first commands to the right leaf skill, enforce phase order, and never duplicate work the leaf skills already do. You are a thin router — the leaf skills do the heavy lifting.

## Hard Rules

Never write artifacts directly — always delegate to the leaf skill.
Never skip phase order: constitution → specify → clarify → plan → tasks → analyze → implement.
Never run `/implement` without a passing `/analyze`.
Never run `/plan` without an Approved feature spec.
Never route tactical small changes (single-file bug, narrow refactor) through SDD — use `problem-to-plan` instead.

---

## Phase Map

| Slash command  | Intent                                  | Routes to                                           |
|----------------|-----------------------------------------|-----------------------------------------------------|
| `/constitution`| author or amend project rules           | `project-constitution`                              |
| `/specify`     | write a new feature spec                | `feature-spec` (mode=specify)                       |
| `/clarify`     | resolve [NEEDS CLARIFICATION] markers   | `feature-spec` (mode=clarify)                       |
| `/plan`        | turn approved spec into a phased plan   | `implementation-plan` (consumes feature-spec)       |
| `/tasks`       | derive agent-pickable tasks             | `implementation-plan` (tasks-only mode)             |
| `/analyze`     | hard readiness gate                     | `spec-crosscheck`                                   |
| `/implement`   | execute the plan                        | `test-driven-development` (or direct execution)     |

---

## Workflow

### Step 1 — Identify entry point

Read the user's message. Detect:
- Explicit slash command (`/specify`, etc.) — route directly.
- Named intent ("write a spec for X") — map to the matching slash.
- Ambiguous request ("do SDD for X") — start at the lowest unmet phase.

### Step 2 — Detect current SDD state

Silently check:
- `docs/constitution.md` exists?
- Latest `docs/specs/*-feature-spec.md` for the slug — what status?
- Matching `docs/plans/<slug>-plan.md` and `<slug>-tasks.md` (or `-TODO.md`)?
- Latest `docs/reviews/<slug>-spec-crosscheck.md` — verdict?

### Step 3 — Enforce phase order

Refuse to run a later phase if an earlier one is missing. Examples:
- `/specify` requested but no constitution → offer to run `/constitution` first (do not auto-run without confirmation).
- `/plan` requested but spec status ≠ Approved → run `/clarify` first.
- `/implement` requested but no PASS crosscheck → run `/analyze` first.

### Step 4 — Delegate

Invoke the routed leaf skill. Pass:
- The feature slug
- Paths to upstream artifacts
- The mode parameter where relevant

Do not duplicate the leaf skill's work — once delegated, the leaf is in charge until it returns.

### Step 5 — Summarize and offer next phase

After the leaf returns, summarize what was produced and offer the next slash command:
> "/specify complete. Spec saved at <path> (status: Draft, 2 CLs). Next: `/clarify`."

---

## Gotchas

- This is a router, not a worker. Resist writing constitution/spec/plan content here — that belongs in the leaf skill.
- For tactical small changes (bug fix, narrow refactor), DO NOT route through SDD. Route to `problem-to-plan`. SDD overhead is for feature-sized work.
- A repo can have many feature-specs in flight. Use the slug to tie spec ↔ plan ↔ tasks ↔ crosscheck. Don't mix slugs across phases.
- `/implement` does not have a dedicated leaf skill — by default route to `test-driven-development`, or to direct execution if the project already has a TDD/CI flow.
- Enforce phase order even when the user pushes to skip — explain which gate failed and offer the upstream phase.

---

## Example

<examples>
  <example>
    <input>Do spec-driven development for adding magic-link login.</input>
    <output>
SDD state check:
- Constitution: docs/constitution.md@2 ✓
- No spec yet for "magic-link login"

Starting at `/specify`. Routing to `feature-spec` (mode=specify).

[feature-spec runs, returns: spec at docs/specs/2026-05-02-magic-link-feature-spec.md, status: Draft, 2 CLs]

`/specify` complete. 2 clarifications open. Run `/clarify` next, or paste answers and I'll route them to `feature-spec`.
    </output>
  </example>
</examples>

---

## Impact Report

```
SDD orchestration: <slug>
Phases run this turn: <list>
Current artifact state:
  Constitution: <version|missing>
  Spec: <status|missing>
  Plan: <yes|no>
  Tasks: <yes|no>
  Crosscheck: <PASS|FAIL|none>
Next phase: <slash>
```
