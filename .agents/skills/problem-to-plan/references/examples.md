# Problem to Plan — Full Worked Examples

Skill: `problem-to-plan` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** The narration agent crashes when the ElevenLabs API key is missing — instead of a clear error it just throws a raw exception. Fix this and add proper error handling.

**Output:**
```
I scanned the codebase: `agents/narration/agent.py` calls the ElevenLabs API in `generate()` at line 45 with no try/except. The API key is read from `os.environ` with no fallback.

Understood: add graceful error handling for missing API key and API failures in the narration agent. Creating deliverables...

**Spec saved:** `docs/specs/2026-04-12-narration-error-handling-spec.md`
- Problem: Raw exception on missing API key, no error handling for API failures
- Success: Missing key → clear error message, API timeout → retry once then user-facing error
- Scope: `agents/narration/agent.py` only

**Plan saved:** `docs/plans/2026-04-12-narration-error-handling-plan.md`
- Phase 1: Add API key validation at agent init (1 task)
- Phase 2: Add try/except around API calls with retry logic (2 tasks)
- Phase 3: Add unit tests for error paths (1 task)
- Effort: S (1-2 hours)

**TODO saved:** `docs/plans/2026-04-12-narration-error-handling-TODO.md`
- M1: API key validation — 1 task
- M2: Error handling — 2 tasks (depends on M1)
- M3: Tests — 1 task
- 4 tasks total, all independently executable after dependencies met

Agents can pick up tasks from the TODO.
```

## Example 2 — Step-by-step execution

**Input:** "Run `problem-to-plan` on [concrete task]"

**Agent actions:**
1. Understand the Problem (skip if routed from process-decomposer)
2. Write the Mini-Spec
3. Write the Detailed Plan
4. Generate TODO.md
5. Present and Log

**Impact Report shape:**
```
Problem planned: [title]
Deliverables: spec + plan + TODO
Spec: docs/specs/YYYY-MM-DD-<slug>-spec.md
Plan: docs/plans/YYYY-MM-DD-<slug>-plan.md
TODO: docs/plans/YYYY-MM-DD-<slug>-TODO.md
Tasks: [N] across [M] milestones
Estimated effort: [S/M/L]
Ready for: agent execution / manual pickup
```

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- TODO tasks must be self-contained — an agent reading only the TODO and the linked files should be able to execute without asking questions. If a task requires context not in the code, add it as a note on the task.
- Change-specs are NOT PRDs. They are scoped to one tactical problem. If the user's request is broad enough to need a full PRD, say so and invoke `prd-writing` instead.
- Change-specs are also NOT feature-specs. Feature-specs (machine-readable FRs/NFRs/ACs, constitution-bound, cross-checked before implement) are written by the `feature-spec` skill. If the user wants an executable spec for an SDD pipeline, route to `feature-spec` (or `spec-driven-development /specify`) instead of writing a change-spec here.
- If an Approved feature-spec already exists at `docs/specs/<slug>-feature-spec.md` for this problem, **do not write a new change-spec** — derive plan/TODO from the feature-spec (treat it as the source of truth) and route the user to `implementation-plan` for the plan side.

---

See `SKILL.md` for hard rules and verification checklist.
