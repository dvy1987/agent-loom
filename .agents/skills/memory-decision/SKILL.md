---
name: memory-decision
description: >
  Record durable project decisions with rationale, alternatives, assumptions,
  status, and revisit triggers. Load when the user says record this decision,
  we decided, decision log, why did we choose, revisit this later, capture
  architectural rationale, log this tradeoff, or document why we picked X.
  Also triggers on "what did we decide about", "ADR without full template",
  or when a debate concludes with a clear choice.
license: MIT
metadata:
  author: dvy1987
  version: "1.1"
  category: project-specific
---

# Memory Decision

You are a decision recorder for agent continuity. You capture not just what was chosen, but why it was valid at the time, what alternatives existed, and when to reopen the decision.

## Workflow

1. State the decision in one sentence.
2. Capture context: constraints, repo state, user preference, and date.
3. List alternatives considered, including deferred options.
4. Record rationale and tradeoffs.
5. Define revisit triggers with concrete conditions.
6. Set status: active, deferred, superseded, or retired.
7. Append to `docs/memory/decision-log.md`.
8. Update `docs/memory/project-index.md`.
9. If architecture-wide, offer `architectural-decision-log` for an ADR.
10. Log file outputs in `docs/skill-outputs/SKILL-OUTPUTS.md`.

## Decision Template

```markdown
## YYYY-MM-DD - <decision title>
Status: active | deferred | superseded | retired
Scope: project
Confidence: high | medium | low
Tags: <comma-separated>

### Decision
<what was chosen>

### Context
<what was true when this decision was made>

### Rationale
<why this is the right tradeoff now>

### Alternatives Considered
- <alternative>: <accepted/rejected/deferred and why>

### Revisit When
- <specific condition>

### Consequences
- <expected effect or risk>
```

## Hard Rules

- Never record a decision without at least one revisit trigger or "revisit not expected because <reason>".
- Do not overwrite old decisions; mark them superseded and link the replacement.
- Do not confuse deferred with rejected.
- If the user is still debating, write to `deferred.md` instead.

## Gotchas

- **Debating ≠ decided.** If the user is still weighing options, use `deferred.md` or `open-questions.md` — not `decision-log.md`.
- **Supersede, don't delete.** Old decisions explain history; mark `superseded` and link the replacement entry.
- **"Revisit never" needs a reason.** Absence of triggers is only valid with explicit justification (e.g., irreversible deploy).
- **Architecture-wide decisions may need an ADR.** Offer `architectural-decision-log` when the choice affects system structure.

## Common Rationalizations

| "Reason to skip recording" | Reality |
|--------------------------|---------|
| "The choice is in the commit message" | Commits lack alternatives and revisit triggers — decision-log is the rationale home |
| "We'll remember why later" | Agents rotate — without a decision entry, the next agent re-debates from scratch |
| "It's temporary" | Temporary choices become permanent habits — record with `deferred` status if unsure |
| "Too small for a decision log" | Small decisions compound — one-line decisions with revisit triggers are valid |

## Output Format

```markdown
Decision recorded: <title>
Location: docs/memory/decision-log.md
Status: <status>
Revisit triggers: <count>
ADR suggested: yes/no
```

## Examples

<examples>
  <example>
    <input>We decided to use repo memory plus global memory, but global must stay tiny.</input>
    <output>
Decision recorded: Repo memory primary; global memory strictly budgeted
Location: docs/memory/decision-log.md
Status: active
Revisit triggers: 1 — another cross-platform standard path adopted
ADR suggested: no
Indexed in `docs/memory/project-index.md`. Logged in `docs/skill-outputs/SKILL-OUTPUTS.md`.
    </output>
  </example>
</examples>

## Verification

- [ ] Entry appended to `docs/memory/decision-log.md` with all template sections
- [ ] At least one revisit trigger or explicit "revisit not expected" reason
- [ ] `docs/memory/project-index.md` updated with decision row
- [ ] Prior conflicting decision marked `superseded` if applicable

## Prune Log
Last pruned: 2026-06-29
- No prunes — content verified current

## Impact Report

```
Decision recorded: <title>
Status: <status> | Revisit triggers: <count>
ADR suggested: yes/no
```
