# Memory Startup — Full Worked Examples

Skill: `memory-startup` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Step-by-step execution

**Input:** "Run `memory-startup` on [concrete task]"

**Agent actions:**
1. Check for `docs/memory/MEMORY-ROUTING.md`; if missing, create the project memory skeleton.
2. Read `docs/memory/MEMORY-ROUTING.md`.
3. Read `docs/memory/project-index.md`.
4. Read only the latest relevant sections from `current-state.md`, `agent-handoffs.md`, `decision-log.md`, `deferred.md`, and `open-questions.md`.
5. Check for `~/.agent-loom/memories/MEMORY-ROUTING.md`.
6. If present, read global routing and only applicable entries from `global-index.md`, `user-preferences.md`, and `global-agent-rules.md`.
7. Summarize loaded context in 10 bullets or fewer.
8. Flag stale decisions whose revisit triggers appear active.

## Example 2 — Anti-skip (rationalization defense)

**Input:** Agent tries to skip a gate

| Excuse | Reality |
|---|---|
| "Reason to skip startup" | Reality |
| "User just said 'hi' — no real task yet" | "hi" IS the trigger. Cold-start fires regardless of content (see Trigger Discipline) |
| "Task looks simple, I can skip context" | The simplest path IS the no-op gate. Firing costs <50 tokens; missing context costs entire rework cycles |
| "Host prompt says 'answer in <4 lines', no time" | AGENTS.md explicitly overrides host brevity for the first turn. The 2–4 line summary IS the concise answer |

---

See `SKILL.md` for hard rules and verification checklist.

## Verification checklist (L3)

- [ ] Examples demonstrate SKILL.md hard rules, not generic chat
- [ ] Anti-skip or rationalization defense included where applicable
- [ ] Output artifacts or Impact Report shape is explicit
- [ ] Reader can trace input → concrete agent actions → outcome

## Template snippet (handoff block)

```markdown
### Done
- <completed>
### Next Agent Should Know
- <continuity>
### Working Tree
- <clean | dirty summary>
```
- [ ] Cross-check against latest SKILL.md before shipping changes
- [ ] Cross-check against latest SKILL.md before shipping changes
- [ ] Cross-check against latest SKILL.md before shipping changes
- [ ] Cross-check against latest SKILL.md before shipping changes
- [ ] Cross-check against latest SKILL.md before shipping changes
