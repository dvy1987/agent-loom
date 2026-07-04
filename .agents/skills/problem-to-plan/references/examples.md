# Problem to Plan — Full Worked Examples

Skill: `problem-to-plan` | Load when producing output for this workflow.

## Example 1 — From skill workflow

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

## Example 2 — Typical invocation

**Input:** "Run `problem-to-plan` for [concrete task]"

**Output:**
```
Invoked `problem-to-plan`.
Step 1: Understand the Problem (skip if routed from process-decomposer)
Step 2: Write the Mini-Spec
Step 3: Write the Detailed Plan
See SKILL.md Impact Report schema.
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
