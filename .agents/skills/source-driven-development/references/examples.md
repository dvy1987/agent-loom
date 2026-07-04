# Source-Driven Development — Full Worked Examples

Skill: `source-driven-development` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** Add React 19 form submission with pending state.

**Output:**
```
Detect React 19.x from package.json. Fetch react.dev/useActionState.
Implement with cited comment. Reject manual useState+isPending if docs recommend useActionState unless user chooses consistency with existing code.
```

## Example 2 — Step-by-step execution

**Input:** "Run `source-driven-development` on [concrete task]"

**Agent actions:**
1. Detect stack and versions
2. Fetch official documentation
3. Implement documented patterns
4. Cite sources

## Example 3 — Anti-skip (rationalization defense)

**Input:** Agent tries to skip a gate

| Excuse | Reality |
|---|---|
| "I'm confident about this API" | Confidence is not evidence. Verify signatures against current docs. |
| "Fetching docs wastes tokens" | One wrong API costs hours of debug time. |
| "Docs won't have what I need" | Absence means the pattern may not be officially recommended — flag it. |
| "I'll add a disclaimer instead" | Either cite or mark UNVERIFIED — hedging helps nobody. |

## Example 4 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- Training data lags; "confident" APIs are often deprecated.
- Fetching the whole docs site wastes tokens — one page per decision.
- Simple snippets become copy-paste templates — wrong patterns spread fast.
- Version skew: React 18 patterns in a React 19 repo break silently.

## Example 5 — Pattern reference (addyosmani/agent-skills)

**Source:** addyosmani snapshot 2026-05-29, security-scanned SAFE.

```
DETECT ──→ FETCH ──→ IMPLEMENT ──→ CITE
  │          │           │            │
  ▼          ▼           ▼            ▼
 What       Get the    Follow the   Show your
 stack?     relevant   documented   sources
            docs       patterns
```

---

See `SKILL.md` for hard rules and verification checklist.
