# Dependency Mapping — Examples

## Ex.1 — Rename a Python function

**Input:** "What breaks if I rename `build_graph` in `scripts/build_graph.py`?"

**Output:**
```markdown
## Impact report — build_graph in scripts/build_graph.py

Capability ladder: text-search
Risk: medium — 5 shell/docs references, 1 test file

| Question | Answer | Evidence |
|----------|--------|----------|
| What depends on this? | CLI entry, Makefile, 2 docs | Makefile:12, README.md:45, harness-engineering SKILL.md:64 |
| What breaks if I change it? | Docs commands, CI graph step | `.github/workflows` none; local scripts call by filename |
| Which tests cover it? | smoke only | NONE direct — behaviorVerified: false |

Affected files: scripts/build_graph.py, Makefile, docs/knowledge-graph/README.md
Recommended verify: python3 -m py_compile scripts/build_graph.py
```

## Ex.2 — Change a TypeScript export signature

**Input:** "Blast radius of changing `UserSchema` in `src/schemas/user.ts`"

**Output:**
```markdown
## Impact report — UserSchema in src/schemas/user.ts

Capability ladder: LSP
Risk: high — 14 importers across API + UI

| Question | Answer | Evidence |
|----------|--------|----------|
| What depends on this? | 14 imports | api/users/route.ts:3, lib/auth.ts:8, ... |
| What breaks if I change it? | Zod parse failures on 3 POST routes | api/users/route.ts:22 [EXTRACTED] |
| Which tests cover it? | 2 unit, 1 e2e | src/schemas/user.test.ts, e2e/signup.spec.ts |

Affected files: [14 paths]
Recommended verify: npm run typecheck && npm test
```
