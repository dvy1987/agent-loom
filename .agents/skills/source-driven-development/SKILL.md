---
name: source-driven-development
description: >
  Ground framework-specific implementation in official documentation — detect
  stack versions, fetch authoritative docs, implement cited patterns, cite sources.
  Load when building with a library or framework where API correctness matters,
  when the user wants verified or documented code, or before writing framework code
  from memory. Also triggers on "source driven development", "cite the docs",
  "check official documentation", "verify against docs", "don't hallucinate APIs".
  Not for pure logic or renames. Pairs with feature-spec and test-driven-development.
license: MIT
metadata:
  author: dvy1987
  version: "1.0"
  category: project-specific
  sources: addyosmani/agent-skills source-driven-development (11/12, 2026-05-29)
  resources:
    references:
      - source-hierarchy.md
---

# Source-Driven Development

You implement framework-specific code from **official documentation for the detected version**, not from training-data memory. Every non-trivial framework decision is cited or flagged unverified.

## Hard Rules

Read dependency manifests (`package.json`, `pyproject.toml`, `go.mod`, etc.) before writing framework-specific code.
Fetch the **specific doc page** for the feature — not the framework homepage.
Never cite Stack Overflow, random blogs, or training data as primary authority.
If versions are ambiguous, ask once — do not guess.
Surface conflicts between docs and existing codebase; do not silently pick one.
Mark patterns you could not verify as `UNVERIFIED` explicitly.

---

## Workflow

### Step 1 — Detect stack and versions

Read the project's dependency file. State findings explicitly:

```markdown
STACK DETECTED:
- [package] [version] (from [file])
→ Fetching official docs for [feature].
```

If versions are missing, ask the user before implementing.

### Step 2 — Fetch official documentation

Fetch the relevant documentation page for the exact API or pattern. Use the source hierarchy in `references/source-hierarchy.md`.

Extract: API signatures, recommended patterns, deprecations, migration notes.
If official sources conflict, surface the discrepancy to the user.

### Step 3 — Implement documented patterns

- Use signatures and patterns from the fetched docs.
- Prefer current recommended APIs over deprecated ones from memory.
- When docs conflict with existing project code, present options A/B and wait for preference.

### Step 4 — Cite sources

**In code** (framework-specific lines only):

```typescript
// useActionState for form pending state — React 19
// Source: https://react.dev/reference/react/useActionState#usage
```

**In chat:** full URLs, quote non-obvious passages, note browser/runtime support when relevant.

If no official doc exists for a pattern:

```markdown
UNVERIFIED: No official documentation found. Based on training data — verify before production.
```

---

## When NOT to use

- Renames, typos, file moves with no API surface change
- Pure language logic identical across versions
- User explicitly wants speed over verification ("just do it quickly")

---

## Gotchas

- Training data lags; "confident" APIs are often deprecated.
- Fetching the whole docs site wastes tokens — one page per decision.
- Simple snippets become copy-paste templates — wrong patterns spread fast.
- Version skew: React 18 patterns in a React 19 repo break silently.

---

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "I'm confident about this API" | Confidence is not evidence. Verify signatures against current docs. |
| "Fetching docs wastes tokens" | One wrong API costs hours of debug time. |
| "Docs won't have what I need" | Absence means the pattern may not be officially recommended — flag it. |
| "I'll add a disclaimer instead" | Either cite or mark UNVERIFIED — hedging helps nobody. |
| "Simple task, no need to check" | Simple wrong patterns get copied across the codebase. |

---

## Output Format

```markdown
## Source-driven — [feature/slug]

Stack: [detected versions]
Docs fetched: [URLs]
Implementation: [summary]
Citations: [list or UNVERIFIED items]
Conflicts with codebase: [none | options A/B]
```

---

## Examples

<examples>
  <example>
    <input>Add React 19 form submission with pending state.</input>
    <output>
Detect React 19.x from package.json. Fetch react.dev/useActionState.
Implement with cited comment. Reject manual useState+isPending if docs recommend useActionState unless user chooses consistency with existing code.
    </output>
  </example>
</examples>

---

## Verification

- [ ] Versions read from dependency file (or user confirmed)
- [ ] Official docs fetched for each framework-specific pattern used
- [ ] Code matches current-version documented APIs (no deprecated APIs without flag)
- [ ] Non-trivial decisions have full URL citations or UNVERIFIED labels
- [ ] Doc vs codebase conflicts surfaced to user

---

## Reference Files

- **`references/source-hierarchy.md`**: Authority order and non-authoritative sources — read at Step 2.

---

## Impact Report

```
Feature: [slug] | Stack: [versions]
Docs: [count] fetched | UNVERIFIED: [count]
Conflicts surfaced: [yes/no]
```
