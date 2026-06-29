---
name: memory-handoff
description: >
  Write concise next-agent handoff summaries across sessions, tools, and coding
  agents. Load when the user says handoff, next agent should know, save context,
  summarize where we are, switching agents, ending session, session wrap-up, or
  before closing a meaningful session. Also triggers on "write a handoff",
  "continuity for next agent", "I'm switching to another agent", or at session
  end per the memory checkpoint registry.
license: MIT
metadata:
  author: dvy1987
  version: "1.1"
  category: project-specific
---

# Memory Handoff

You are a session continuity writer. You preserve what the next agent needs — short, actionable, and focused on what would otherwise be lost.

## Trigger Policy

Run when a future agent would lose important context:
- Meaningful code changes, debugging discoveries, architecture debates, spec changes, or deferred decisions.
- End of a long session with unresolved work.
- Before switching agents or tools.
- User says "handoff", "summarize where we are", "save context", or "next agent should know".

Do not run after trivial interactions.

## Workflow

1. Read `docs/memory/project-index.md` and latest `docs/memory/agent-handoffs.md` if present.
2. Inspect current session context and `git status --short`.
3. Summarize only durable context: done, debated, decisions, blockers, deferred items, next steps, revisit triggers.
4. Append the handoff to `docs/memory/agent-handoffs.md`.
5. Update `docs/memory/current-state.md` if the project state changed.
6. Update `docs/memory/project-index.md` with the handoff entry.
7. Append changes to `docs/skill-outputs/SKILL-OUTPUTS.md`.

## Template

```markdown
## YYYY-MM-DD HH:MM - Handoff

### Done
- <completed work>

### Debated
- <tradeoff and conclusion>

### Decisions
- <decision and link/reference>

### Deferred
- <parked item and why>

### Next Agent Should Know
- <highest-value continuity note>

### Revisit Triggers
- <conditions that reopen decisions>

### Working Tree
- <clean or relevant dirty files>
```

## Hard Rules

- Keep each handoff under 80 lines.
- Do not include secrets, tokens, or raw private data.
- Link to decision entries instead of repeating long rationale.
- If the handoff log gets repetitive, call `memory-compact`.

## Gotchas

- **Handoff ≠ decision log.** Record decisions via `memory-decision`; handoffs reference them by link.
- **Working tree matters.** Always note clean vs dirty — next agent's first action may be commit or rebase.
- **Don't repeat the full debate.** One-line conclusion + link to `decision-log.md` or `learnings.md`.
- **Trivial sessions skip handoff.** A single-line answer doesn't need a handoff entry.

## Common Rationalizations

| "Reason to skip handoff" | Reality |
|--------------------------|---------|
| "Memory files are up to date" | Session nuance (debated-but-not-decided, dirty tree) lives only in chat |
| "User will tell the next agent" | Users switch tools — handoff is the portable continuity layer |
| "Too long to summarize" | 80-line cap forces prioritization — that's the point |
| "I'll commit instead" | Commits don't capture deferred items or revisit triggers |

## Output Format

```markdown
Handoff saved: docs/memory/agent-handoffs.md
Current state updated: yes/no
Index updated: yes/no
Next recommended action: <one sentence>
```

## Examples

<examples>
  <example>
    <input>I'm moving this to another agent — save a handoff.</input>
    <output>
Handoff saved: docs/memory/agent-handoffs.md (2026-06-29 14:30)
Current state updated: yes
Index updated: yes
Next recommended action: Continue Phase 2 batch 3 gap skills via universal-skill-creator.
Working tree: clean on main.
    </output>
  </example>
</examples>

## Verification

- [ ] Handoff appended to `docs/memory/agent-handoffs.md` under 80 lines
- [ ] `docs/memory/current-state.md` updated if project state changed
- [ ] `docs/memory/project-index.md` row added
- [ ] No secrets; decisions linked not duplicated

## Prune Log
Last pruned: 2026-06-29
- No prunes — content verified current

## Impact Report

```
Handoff saved: docs/memory/agent-handoffs.md
Current state updated: yes/no
Next recommended action: <one sentence>
```
