---
name: memory-promote
description: >
  Promote project-specific memories into strict, small global memory only when
  they are cross-project, stable, useful, safe, and worth the global context
  cost. Load when the user says make this global, remember across projects,
  save this globally, promote this learning, or apply this everywhere. Also
  triggers on "this applies to all my projects", "add to global preferences",
  or after repeated cross-repo confirmation of the same rule.
license: MIT
metadata:
  author: dvy1987
  version: "1.1"
  category: project-specific
---

# Memory Promote

You are the global memory gatekeeper. Most memories stay local. Promote only durable cross-project rules or user preferences that justify global context cost.

## Global Store

`~/.agent-loom/memories/` — budgets: `user-preferences.md` ≤100, `global-agent-rules.md` ≤150, `reusable-learnings.md` ≤200, `global-index.md` ≤250. Total active target: 500–700 lines.

## Workflow

1. Read the source project memory entry and provenance.
2. Classify target: user preference, global agent rule, or reusable learning.
3. Apply promotion gate (all must be true — see below).
4. Check line counts for target global file and `global-index.md`.
5. If any budget exceeded, invoke `memory-compact` before writing.
6. Write concise global entry with source project, date, confidence, scope.
7. Update `~/.agent-loom/memories/global-index.md`.
8. Update source project entry with "promoted to global" provenance.

## Promotion Gate

Promote only if all are true: cross-project, repeatedly useful, stable (not weekly churn), safe, short enough for active recall.

## Hard Rules

- Global memory is not a journal.
- Never promote secrets, credentials, internal URLs, or private project facts.
- Never promote low-confidence maybes — keep in `deferred.md`.
- Never append past budget; compact first.

## Gotchas

- **One-time project facts don't promote.** "We use Postgres here" stays project-local.
- **Compaction before write is mandatory.** Never append into an over-budget global file.
- **Provenance on both sides.** Source project entry must note promotion; global entry cites source.
- **Reject obvious general advice.** "Write clean code" doesn't belong in global memory.

## Common Rationalizations

| "Reason to promote" | Reality |
|---------------------|---------|
| "User said remember" | Remember ≠ global — project capture first, promote only if cross-project |
| "Might be useful elsewhere" | Promotion gate requires repeated evidence, not speculation |
| "Global is easier to find" | Global has tight budgets — local index is the default home |
| "Skip compact, it's only a few lines" | A few lines over budget blocks the next promote — compact first |

## Output Format

```markdown
Promotion verdict: promote | keep local | reject
Target file: <global path or none>
Reason: <why>
Budget status: <within budget | compacted | blocked>
Source updated: <yes/no>
```

## Examples

<examples>
  <example>
    <input>Promote: user prefers concise, direct engineering updates (confirmed 3 sessions).</input>
    <output>
Promotion verdict: promote
Target file: ~/.agent-loom/memories/user-preferences.md
Budget status: within budget (84/100 lines)
Source updated: yes — provenance linked in project learnings
    </output>
  </example>
</examples>

## Verification

- [ ] All five promotion gate criteria verified before write
- [ ] Global file line count checked; `memory-compact` run if over budget
- [ ] `global-index.md` updated with new entry
- [ ] Source project entry marked with promotion provenance

## Prune Log
Last pruned: 2026-06-29
- No prunes — content verified current

## Impact Report

```
Memory promotion: <verdict> | Global file: <path or none>
Budget after write: <lines> | Source updated: yes/no
```
