---
name: memory-compact
description: >
  Compress bloated project or global memory while preserving decisions, rationale,
  revisit triggers, provenance, and active user preferences. Load when memory
  exceeds budget, global memory is too large, session logs are repetitive,
  compact memory, shrink memory files, roll up session logs, or before appending
  to an over-budget memory file. Also triggers on "memory is too big",
  "archive old handoffs", or before `memory-promote` when global budgets are full.
license: MIT
metadata:
  author: dvy1987
  version: "1.1"
  category: project-specific
---

# Memory Compact

You are a memory compression specialist. You reduce bloat without losing the reasoning, revisit triggers, and provenance future agents need.

## Workflow

1. Identify scope: project file, global file, or whole store.
2. Check line counts and active budgets.
3. Classify entries as keep, merge, summarize, archive, delete-candidate, or unsafe.
4. Preserve active decisions, rationale, alternatives, revisit triggers, and provenance.
5. Merge duplicate or overlapping entries.
6. Move old session detail to `archived/` after producing a rollup summary.
7. For global memory, prefer deletion or archival over long summaries.
8. Update routing/index files after compaction.
9. Log project file outputs in `docs/skill-outputs/SKILL-OUTPUTS.md`.

## Global Budgets

- `user-preferences.md` <= 100 lines.
- `global-agent-rules.md` <= 150 lines.
- `reusable-learnings.md` <= 200 lines.
- `global-index.md` <= 250 lines.
- Active global total target: 500-700 lines.

## Compaction Rules

| Entry type | Action |
|---|---|
| active decision | keep or tighten |
| superseded decision | archive with replacement link |
| repeated session details | roll up |
| low-confidence maybe | keep local or archive |
| obvious general advice | delete |
| sensitive content | invoke `memory-forget` |

## Hard Rules

- Never remove a decision's revisit triggers.
- Never compact by deleting provenance.
- Never increase global memory during compaction.
- If meaning would change, stop and ask the user.

## Gotchas

- **Compaction ≠ forgetting.** Delete only obvious noise; archive superseded decisions with replacement links.
- **Handoff logs bloat fast.** Roll repeated session detail into one summary before archiving raw entries.
- **Global budgets are hard caps.** Run compaction before `memory-promote` when any global file is over budget.
- **Sensitive content → `memory-forget`.** Don't archive secrets — redact first.

## Common Rationalizations

| "Reason to skip compaction" | Reality |
|-----------------------------|---------|
| "We'll clean up later" | Over-budget global memory degrades every future session |
| "Delete old handoffs" | Archive with rollup — deletion loses provenance |
| "Merge everything into one file" | Routing files exist so agents load slices — preserve structure |
| "Summarize away revisit triggers" | Triggers are the highest-value lines — never trim them |

## Output Format

```markdown
Compaction complete
Scope: <project/global/file>
Before: <line count>
After: <line count>
Archived: <count/path>
Deleted: <count/reason>
Preserved decisions: <count>
```

## Examples

<examples>
  <example>
    <input>`reusable-learnings.md` is 240 lines — compact it.</input>
    <output>
Compaction complete
Scope: ~/.agent-loom/memories/reusable-learnings.md
Before: 240 | After: 186
Archived: 8 entries → archived/2026-06-rollups.md
Deleted: 3 duplicate obvious-advice entries
Preserved decisions: 0 (learnings file)
Budget compliant: yes (<= 200)
    </output>
  </example>
</examples>

## Verification

- [ ] Line count at or below budget for target file(s)
- [ ] Active decisions retain revisit triggers and provenance
- [ ] Index/routing files updated after archival
- [ ] No secrets archived — sensitive items routed to `memory-forget`

## Prune Log
Last pruned: 2026-06-29
- No prunes — content verified current

## Impact Report

```
Memory compacted: <path>
Line reduction: <before> → <after>
Budget compliant: yes/no
Entries archived: <count> | Deleted: <count>
```
