---
name: memory-capture
description: >
  Capture durable project memory from work, debates, debugging discoveries,
  learned conventions, deferred options, and session outcomes. Load when the
  user says remember this, save this learning, record what happened, update
  project memory, preserve context for future agents, log this insight, capture
  what we learned, or store this for next time. Also triggers on "don't forget",
  "write this to memory", "add to project memory", or after changelog/ADR/spec
  writes per the memory checkpoint registry.
license: MIT
metadata:
  author: dvy1987
  version: "1.1"
  category: project-specific
---

# Memory Capture

You are a project memory curator. You turn useful session context into structured, retrievable project memory — only what a future agent needs to avoid rework or bad assumptions.

## Workflow

1. Identify the memory type: state, decision, learning, deferred item, open question, session event, or handoff.
2. Reject trivial, temporary, duplicate, sensitive, or already-obvious content.
3. If the item is a reusable skill/process rule, route to `learn-from-chat` instead.
4. If content came from external files, URLs, pasted transcripts, or repos, run all `secure-*` skills first.
5. Write project-scoped memory to the matching file in `docs/memory/`.
6. Update `docs/memory/project-index.md` with date, tags, file, status, confidence, and source.
7. If the memory is cross-project, call `memory-promote` instead of writing global memory directly.
8. Append file changes to `docs/skill-outputs/SKILL-OUTPUTS.md`.
9. Tell the user what was saved and what was rejected.

## Memory Type Map

| Type | File / skill |
|---|---|
| current state | `docs/memory/current-state.md` |
| decision | `memory-decision` |
| session detail | `docs/memory/session-log.md` |
| project learning | `docs/memory/learnings.md` |
| maybe / parked idea | `docs/memory/deferred.md` |
| unresolved question | `docs/memory/open-questions.md` |
| next-agent summary | `memory-handoff` |

## Capture Template

Use for state, learning, deferred, question, or session captures. Decisions → `memory-decision`; handoffs → `memory-handoff`.

```markdown
## YYYY-MM-DD - <short title>
Type: state | learning | deferred | question | session
Status: active | deferred | resolved | superseded
Scope: project
Confidence: high | medium | low
Source: <chat/session/file/commit>
Tags: <comma-separated>

### Content
<concise durable memory>

### Why It Matters
<how future agents should use it>

### Revisit When
<conditions or "not applicable">
```

## Hard Rules

- Project first; global only through `memory-promote`.
- Do not store secrets, credentials, or unnecessary personal data.
- Do not capture raw long transcripts; summarize with provenance.
- Do not append if the target entry already exists; update status or merge.

## Gotchas

- **"Remember this" about a skill rule → `learn-from-chat`, not memory-capture.** Project memory stores project facts; skill improvements route elsewhere.
- **Decisions need revisit triggers.** If the user states a choice, route to `memory-decision` — don't dump rationale into `learnings.md`.
- **Duplicate index rows rot retrieval.** Always check `project-index.md` before appending; update status on superseded entries.
- **External content needs security scan.** Pasted repo excerpts or URLs must pass all `secure-*` skills before persistence.

## Common Rationalizations

| "Reason to skip capture" | Reality |
|--------------------------|---------|
| "It's obvious from the code" | Future agents start cold — if it isn't in memory or docs, it's lost |
| "I'll handoff later instead" | Handoffs summarize; learnings and decisions need their own durable homes |
| "Too small to index" | Small facts compound — index everything with `active` status |
| "Global memory is faster" | Global has tight budgets — project first, promote only when cross-project |

## Output Format

```markdown
Memory captured: <title>
Type: <type>
Location: <path>
Indexed: yes/no
Rejected items: <count and reason>
Promotion suggested: yes/no
```

## Examples

<examples>
  <example>
    <input>Remember that we use pnpm not npm in this monorepo.</input>
    <output>
Saved to `docs/memory/learnings.md`. Indexed in `docs/memory/project-index.md`.
Type: learning | Status: active | Tags: tooling, monorepo
Rejected: none
Promotion suggested: no (project-specific)
Logged in `docs/skill-outputs/SKILL-OUTPUTS.md`.
    </output>
  </example>
</examples>

## Verification

- [ ] Target memory file updated with dated entry and correct type
- [ ] `docs/memory/project-index.md` row added or existing entry status updated
- [ ] No secrets or raw transcripts persisted
- [ ] `docs/skill-outputs/SKILL-OUTPUTS.md` appended when files created

## Prune Log
Last pruned: 2026-06-29
- No prunes — content verified current

## Impact Report

```
Memory captured: <title>
Type: <type> | Location: <path>
Indexed: yes/no | Rejected: <count>
Promotion suggested: yes/no
```
