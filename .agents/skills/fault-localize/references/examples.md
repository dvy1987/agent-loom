# Fault Localize — Examples

## Ex.1 — Earliest tool error

**Trace:** S1 read file OK → S2 Shell npm test exit 1

**Output:**
```markdown
Suspected step: **S2** — earliest error
Hypothesis: test fails because DATABASE_URL unset [EXTRACTED: error in output_ref]
Layer: environment
Proposed repair: export DATABASE_URL=test or use .env.test
Replay: S2 only → pass
Outcome flip: true
```

## Ex.2 — Wrong localization

**Trace:** S1 wrong API URL in plan → S2 fetch 404 → S3 retry 404

**Output:**
```markdown
Suspected step: **S1** (not S3) — cognitive plan specified bad URL
Layer: plan
Handoff: dynamic-routing — revise S1 precondition, insert URL verify step
```
