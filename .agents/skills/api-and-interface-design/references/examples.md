# API and Interface Design — Full Worked Examples

Skill: `api-and-interface-design` | Load when producing output for this workflow.

## Example 1 — From skill workflow

**Input:** Design tasks API for a new SaaS backend.

**Output:**
```
Contract-first Task + CreateTaskInput + PaginatedResult. REST: GET/POST /api/tasks, GET/PATCH/DELETE /api/tasks/:id. Single APIError body. Zod at route boundary only. Pagination query params on list.
```

## Example 2 — Typical invocation

**Input:** "Run `api-and-interface-design` for [concrete task]"

**Output:**
```
Invoked `api-and-interface-design`.
Step 1: Scope the interface
Step 2: Write the contract
Step 3: Apply core principles
Resource: [name] | Surfaces: N
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
