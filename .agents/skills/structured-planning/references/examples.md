# Structured Planning — Examples

## Ex.1 — Plan-ahead API feature

**Input:** "Add user settings endpoint — DB, API, and tests"

**Output:**
```markdown
## Structured plan — user-settings-endpoint

Plan file: `.agent-loom/plans/user-settings-endpoint.md`
Steps: 4 total | done: 0 | pending: 4

Steps drafted:
- S1 migration | S2 route handler | S3 service layer | S4 tests

Next: execute **S1** only — commit-one per ReCAP
```

## Ex.2 — Trivial bypass

**Input:** "Fix typo in README line 12"

**Output:**
```markdown
Trivial — plan skipped (single file, no dependencies).
Proceeding to direct edit via safe-change if needed.
```
