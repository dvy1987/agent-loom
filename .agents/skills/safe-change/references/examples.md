# Safe Change — Examples

## Ex.1 — Kept change

**Input:** "Safely add a null check to `parseConfig` in `lib/config.ts`"

**Output:**
```markdown
## Safe change run — parseConfig-null-guard

Snapshot: stash@{0}
Impact risk: low (2 callers, 1 test)

Verify:
- typecheck: pass — npm run typecheck
- tests: pass — npm test
- behaviorVerified: true

Outcome: KEPT
Next: `fix: guard parseConfig against null input`
```

## Ex.2 — Reverted change

**Input:** "Rename `UserDTO` to `UserRecord` across the API"

**Output:**
```markdown
## Safe change run — user-dto-rename

Snapshot: branch safe-change/user-dto
Impact risk: high (14 importers)

Verify:
- typecheck: fail — npx tsc --noEmit
- tests: skip (not reached)
- behaviorVerified: false

Outcome: REVERTED
Evidence: error TS2345 at api/users/route.ts:22 — property 'email' missing on type

Next: split rename into export-alias cycle + consumer updates per incremental-implementation
```
