# CI/CD and Automation — Full Worked Examples

Skill: `ci-cd-and-automation` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** “Add CI to a TypeScript repo.”

**Output:**
```
Create `.github/workflows/ci.yml` with node-version pinned, npm cache, `npm ci`, `npm run lint`, `npm test`, `npm run build`, concurrency cancel. Add branch protection requiring the workflow.
```

## Example 2 — Step-by-step execution

**Input:** "Run `ci-cd-and-automation` on [concrete task]"

**Agent actions:**
1. Define lifecycle and artifacts
2. Choose the minimum viable pipeline
3. Make it reliable
4. Secrets and permissions
5. Add automation hooks (only if they pay rent)
6. Verification

## Example 3 — Anti-skip (rationalization defense)

**Input:** Agent tries to skip a gate

| Excuse | Reality |
|---|---|
| "We don’t need CI yet" | CI is cheapest when the repo is small; add the PR gates early. |
| "Let’s add every check" | Overbuilt CI becomes slow and ignored; start minimal and expand on evidence. |
| "Caching is premature optimization" | Without caching, CI becomes slow and gets bypassed. |
| "We’ll add branch protection later" | CI without enforcement is a suggestion, not a gate. |

## Example 4 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- “Green CI” that doesn’t match local commands becomes ignored.
- Unpinned runtimes cause flakey builds over time.
- Missing branch protections makes CI advisory-only.
- Long pipelines encourage skipping checks; keep PR path fast.

## Example 5 — Pattern reference (addyosmani/agent-skills)

**Source:** addyosmani snapshot 2026-05-29, security-scanned SAFE.

```
Pull Request Opened
    │
    ▼
┌─────────────────┐
│   LINT CHECK     │  eslint, prettier
│   ↓ pass         │
│   TYPE CHECK     │  tsc --noEmit
│   ↓ pass         │
│   UNIT TESTS     │  jest/vitest
│   ↓ pass         │
│   BUILD          │  npm run build
│   ↓ pass         │
│   INTEGRATION    │  API/DB tests
│   ↓ pass         │
│   E2E (optional) │  Playwright/Cypress
│   ↓ pass         │
│   SECURITY AUDIT │  npm audit
│   ↓ pass         │
│   BUNDLE SIZE    │  bundlesize check
└─────────────────┘
    │
    ▼
  Ready for review
```

---

See `SKILL.md` for hard rules and verification checklist.
