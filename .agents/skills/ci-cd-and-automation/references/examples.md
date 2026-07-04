# CI/CD and Automation — Full Worked Examples

Skill: `ci-cd-and-automation` | Load when producing output for this workflow.

## Example 1 — From skill workflow

**Input:** “Add CI to a TypeScript repo.”

**Output:**
```
Create `.github/workflows/ci.yml` with node-version pinned, npm cache, `npm ci`, `npm run lint`, `npm test`, `npm run build`, concurrency cancel. Add branch protection requiring the workflow.
```

## Example 2 — Typical invocation

**Input:** "Run `ci-cd-and-automation` for [concrete task]"

**Output:**
```
Invoked `ci-cd-and-automation`.
Step 1: Define lifecycle and artifacts
Step 2: Choose the minimum viable pipeline
Step 3: Make it reliable
Repo: [name] | Workflows: N | Gates: [list]
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
