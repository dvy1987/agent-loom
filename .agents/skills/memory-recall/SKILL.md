---
name: memory-recall
description: >
  Retrieve task-relevant project and global memory without loading everything.
  Load when the user asks what we decided, recall prior context, find memory
  about a feature, explain past rationale, resume a task, check deferred ideas,
  or what happened last time on this topic. Also triggers on "what's in memory
  about", "pull up the decision on", or "any open questions about".
license: MIT
metadata:
  author: dvy1987
  version: "1.1"
  category: project-specific
---

# Memory Recall

You are a targeted memory retrieval specialist. You return the smallest useful slice — relevance over exhaustive history.

## Workflow

1. Identify the recall target: feature, decision, bug, user preference, deferred option, learning, or session.
2. Read `docs/memory/MEMORY-ROUTING.md` and `docs/memory/project-index.md`.
3. Select candidate files and sections by tags, status, date, and scope.
4. Read only selected sections from project memory.
5. If user preferences or global process rules may matter, read `~/.agent-loom/memories/MEMORY-ROUTING.md` and `global-index.md`.
6. Pull only applicable global entries.
7. Return a concise summary with source paths.
8. Flag contradictions, stale entries, and triggered revisit conditions.

## Retrieval Priority

1. Current state and latest handoff.
2. Active decisions with matching tags.
3. Deferred items and open questions.
4. Learnings relevant to the task.
5. Session history only if the above is insufficient.
6. Global preferences/rules only if task-relevant.

## Hard Rules

- Do not load full logs by default.
- Do not treat archived or superseded memory as current.
- Do not hide uncertainty; if memory is stale, say so.
- Do not write memory during recall unless the user also asks to update it.

## Gotchas

- **Superseded ≠ deleted.** Report superseded decisions as historical with link to replacement.
- **Index before bulk read.** `project-index.md` filters by tag — don't read every memory file.
- **Recall is read-only.** Don't capture or handoff unless the user also requests it.
- **Contradictions need flagging.** If memory conflicts with current repo files, prefer repo evidence and note the drift.

## Common Rationalizations

| "Reason to load everything" | Reality |
|-----------------------------|---------|
| "Might miss something" | Routing + index exist to bound reads — flooding context defeats memory |
| "Superseded is still useful" | Cite it as historical only — don't treat as current policy |
| "Global always matters" | Global has tight budgets — load only task-relevant global entries |
| "I'll update memory while recalling" | Recall is read-only unless user explicitly asks to capture |

## Output Format

```markdown
Memory recalled for: <topic>
Sources: <paths/sections>
Relevant context:
- <fact with source>
Decisions:
- <decision/status/revisit trigger>
Deferred / open:
- <item or none>
Staleness / contradictions:
- <issue or none>
```

## Examples

<examples>
  <example>
    <input>Why did we choose local and global memory?</input>
    <output>
Memory recalled for: memory architecture
Sources: docs/memory/decision-log.md (2026-05-11 entry)
Decisions:
- Repo memory primary; global strictly budgeted — Status: active
- Revisit when: cross-platform standard path changes
Deferred / open: none
Staleness / contradictions: none
    </output>
  </example>
</examples>

## Verification

- [ ] Read `MEMORY-ROUTING.md` and `project-index.md` before content files
- [ ] Only selected sections loaded — not full logs
- [ ] Superseded/archived entries flagged as historical
- [ ] No writes performed unless user also requested capture

## Prune Log
Last pruned: 2026-06-29
- No prunes — content verified current

## Impact Report

```
Recall complete: <topic>
Files read: <count> | Relevant entries: <count>
Stale entries: <count> | Writes performed: none
```
