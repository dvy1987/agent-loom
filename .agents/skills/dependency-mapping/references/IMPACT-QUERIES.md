# Impact Queries — Mandatory Gate

**No non-trivial edit until all three rows are answered with evidence.** Modeled on Synapse Farsight `what_depends_on` / `what_breaks_if_i_change` and Cartograph blast-radius queries.

---

## The three questions

| # | Question | What to list | Done when |
|---|----------|--------------|-----------|
| 1 | **What depends on this symbol?** | Direct importers, callers, re-exporters, config references, route handlers | Every dependency has a `path:line` or `[INFERRED]` tag |
| 2 | **What breaks if I change it?** | Signature mismatches, behavior changes, deleted exports, schema/API drift | Each breaking surface tied to a consumer from Q1 |
| 3 | **Which tests cover it?** | Unit/integration/e2e files that import or name the symbol | List paths, or `NONE` + note `behaviorVerified: false` |

---

## Query ladder (capability detection)

Run top-to-bottom; stop at the highest available:

1. **LSP** — `findReferences`, `goToDefinition`, workspace symbol search.
2. **Semantic** — tree-sitter, ts-morph, pyright, gopls graph exports when CLI available.
3. **Structural text** — ripgrep for symbol, qualified imports, string literals (URLs, env keys, CLI flags).
4. **Co-change heuristic** — git log `-L` or `git log --follow` on the file (Cartograph-style); mark `[INFERRED]`.

Document the highest rung used in the impact report header.

---

## Risk rubric

| Risk | Signals |
|------|---------|
| **low** | ≤2 direct callers, tests cover change surface, internal module |
| **medium** | 3–10 callers, partial test coverage, or public API surface |
| **high** | >10 callers, no tests, exported API, cross-package boundary, or dynamic dispatch unknowns |

---

## Hidden coupling checks (agentic-codebase pattern)

Before marking Q2 complete, scan for:

- Stringly-typed references (magic strings matching symbol name)
- Reflection / `getattr` / registry maps
- Duplicate implementations (same logic in two files)
- Docs/examples that embed the old API
