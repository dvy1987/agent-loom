# Git Workflow and Versioning — Full Worked Examples

Skill: `git-workflow-and-versioning` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** I'm done with the validation endpoint. Ready to commit.

**Output:**
```
Staged review: one logical change (POST /validate + tests).
Message:
```
feat: add skill validation endpoint

Exposes validate-skills checks for CI; refs task validate-api.
```
Run: `npm test` → pass, then commit.
```

## Example 2 — Step-by-step execution

**Input:** "Run `git-workflow-and-versioning` on [concrete task]"

**Agent actions:**
1. Review what's changing
2. Pre-commit hygiene
3. Write the message
4. Commit or advise the user
5. Summarize for reviewers

## Example 3 — Anti-skip (rationalization defense)

**Input:** Agent tries to skip a gate

| Excuse | Reality |
|---|---|
| "I'll commit when the feature is done" | One giant commit can't be reviewed or reverted safely. |
| "Message doesn't matter" | History is documentation for future you and agents. |
| "I'll squash later" | Prefer clean incremental commits from the start. |
| "Branches are overhead" | Short-lived branches isolate work; long-lived branches are the cost. |

## Example 4 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- Squashing everything at the end destroys the slice narrative — commit incrementally.
- Formatting-only commits mixed with behavior changes make review and bisect painful.
- Missing `.gitignore` until `.env` lands in history.
- `git reset --hard` on shared branches loses others' work — warn first.

---

See `SKILL.md` for hard rules and verification checklist.
