---
name: git-workflow-and-versioning
description: >
  Structure git work with atomic commits, conventional messages, short-lived
  branches, and pre-commit hygiene. Load when committing, branching, resolving
  merge conflicts, organizing parallel work, or reviewing git history. Also
  triggers on "git workflow", "commit message", "conventional commits", "atomic
  commit", "branch strategy", "git worktree", "how should I commit this". Does
  not replace project-specific hook policies — complements them.
license: MIT
metadata:
  author: dvy1987
  version: "1.0"
  category: project-specific
  sources: addyosmani/agent-skills git-workflow-and-versioning (11/12, 2026-05-29)
---

# Git Workflow and Versioning

You keep git history reviewable, reversible, and honest. Commits are save points; messages document intent.

## Hard Rules

One logical change per commit — never mix feature + refactor + formatting.
Commit messages explain **why**, not only what the diff shows.
Never commit secrets — scan staged diff for password, secret, api_key, token patterns.
Never force-push to shared `main`/`master` without explicit user request.
Tests should pass before commit when the project has a test command.

---

## Workflow

### Step 1 — Review what's changing

Run `git status` and `git diff` (staged if committing). Confirm scope matches one logical change.

### Step 2 — Pre-commit hygiene

Run project tests/lint if applicable. Reject staged secrets. Split if mixed concerns.

### Step 3 — Write the message

```
<type>: <short imperative description>

<optional body — why, tradeoffs, links to spec/task>
```

Types: `feat` | `fix` | `refactor` | `test` | `docs` | `chore`

### Step 4 — Commit or advise the user

If the user's environment allows commits, commit. Otherwise output the exact message for them to run.

### Step 5 — Summarize for reviewers

Emit a short change summary (see Output Format).

---

## Branching defaults

- **Trunk-based:** keep default branch deployable; merge feature branches within 1–3 days.
- **Naming:** `feature/<slug>`, `fix/<slug>`, `chore/<slug>`, `refactor/<slug>`
- **Parallel agents:** prefer `git worktree add` over constant branch switching.
- **Incomplete features:** feature flags on main beat month-long branches.

---

## Gotchas

- Squashing everything at the end destroys the slice narrative — commit incrementally.
- Formatting-only commits mixed with behavior changes make review and bisect painful.
- Missing `.gitignore` until `.env` lands in history.
- `git reset --hard` on shared branches loses others' work — warn first.

---

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "I'll commit when the feature is done" | One giant commit can't be reviewed or reverted safely. |
| "Message doesn't matter" | History is documentation for future you and agents. |
| "I'll squash later" | Prefer clean incremental commits from the start. |
| "Branches are overhead" | Short-lived branches isolate work; long-lived branches are the cost. |

---

## Output Format

```markdown
## Git summary

Commits recommended:
- `<type>: <description>`

CHANGES:
- path: one-line what/why

NOT TOUCHED (intentional):
- path: reason out of scope

CONCERNS:
- [risk or question for human]
```

---

## Examples

<examples>
  <example>
    <input>I'm done with the validation endpoint. Ready to commit.</input>
    <output>
Staged review: one logical change (POST /validate + tests).
Message:
```
feat: add skill validation endpoint

Exposes validate-skills checks for CI; refs task validate-api.
```
Run: `npm test` → pass, then commit.
    </output>
  </example>
</examples>

---

## Impact Report

```
Git workflow: [commit advised / committed / review-only]
Commits: N | Concerns flagged: N
```
