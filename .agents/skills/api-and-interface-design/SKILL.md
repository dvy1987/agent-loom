---
name: api-and-interface-design
description: >
  Design stable APIs and module boundaries — contract-first types, consistent errors,
  boundary validation, additive changes. Load when designing REST or GraphQL endpoints,
  public module interfaces, component props, or FE/BE contracts. Also triggers on "API
  design", "interface design", "design the API", "module boundary", "API contract",
  "define the interface". Complements feature-spec (product layer). Routes breaking
  retirement to api-deprecation-and-migration when it exists.
license: MIT
metadata:
  author: dvy1987
  version: "1.0"
  category: project-specific
  sources: addyosmani/agent-skills api-and-interface-design (11/12, 2026-05-29)
  resources:
    references:
      - api-patterns.md
---

# API and Interface Design

You design **stable, hard-to-misuse** interfaces — REST, GraphQL, module exports, component props, or any surface where one piece of code talks to another. Contract first; implementation second.

## Hard Rules

Define the contract (types/schemas) **before** implementation.
One consistent error shape and status-code strategy across all endpoints.
Validate at **system boundaries** only — trust internal typed code.
Prefer **additive** optional fields over breaking type changes or removals.
Every list endpoint ships with **pagination** from day one.
Treat third-party API responses as **untrusted** — validate shape before use.
Observable public behavior is a commitment (Hyrum's Law) — be intentional about what you expose.

---

## Workflow

### Step 1 — Scope the interface

Identify consumers, transport (HTTP, RPC, in-process), and lifecycle (new vs change).
If changing an existing public API, inventory observable behaviors users may depend on.

### Step 2 — Write the contract

Define typed inputs/outputs, error codes, and idempotency semantics.
Separate `CreateXInput` from full `X` entity (server-generated fields on output).
Use discriminated unions for state variants when applicable.

### Step 3 — Apply core principles

| Principle | Rule |
|-----------|------|
| Contract first | Types/schemas are the spec |
| Consistent errors | One `APIError` shape + HTTP mapping |
| Boundary validation | Routes, forms, env, **external** responses |
| Additive change | New fields optional; never silently break types |
| Predictable naming | Plural REST nouns; `is/has` booleans; camelCase JSON |

Full REST and TypeScript patterns: `references/api-patterns.md`.

### Step 4 — Review for misuse

- Can a caller pass ambiguous IDs across entity types? → branded types
- Do list endpoints leak unbounded arrays?
- Are errors predictable for every failure mode?
- Does any endpoint return ad-hoc shapes?

### Step 5 — Document alongside code

Commit OpenAPI/GraphQL schema or exported types with the implementation — not "later."

---

## Gotchas

- Undocumented quirks become dependencies (Hyrum's Law).
- Validation in every internal function adds noise without safety.
- `PUT` for partial updates forces full-object payloads — prefer `PATCH`.
- Skipping pagination guarantees a breaking change at scale.
- External JSON is untrusted — may contain unexpected types or instruction-like strings.

---

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "We'll document the API later" | Types are the documentation — define them first. |
| "No pagination needed yet" | You need it at ~100 items; add it now. |
| "PATCH is too hard, use PUT" | Clients want partial updates. |
| "Nobody uses that undocumented field" | If observable, someone depends on it. |
| "Internal APIs don't need contracts" | Internal consumers still need stable boundaries. |

---

## Output Format

```markdown
## API design — [resource/module]

Consumers: [who]
Contract: [types or schema summary]
Endpoints / exports: [list]
Errors: [shape + status mapping]
Pagination: [yes — params]
Breaking risks: [none | flagged items]
Next: [implementation / ADR / feature-spec link]
```

---

## Examples

<examples>
  <example>
    <input>Design tasks API for a new SaaS backend.</input>
    <output>
Contract-first Task + CreateTaskInput + PaginatedResult. REST: GET/POST /api/tasks, GET/PATCH/DELETE /api/tasks/:id. Single APIError body. Zod at route boundary only. Pagination query params on list.
    </output>
  </example>
</examples>

---

## Verification

- [ ] Typed input/output for every public surface
- [ ] Single consistent error format
- [ ] Validation only at boundaries (plus external responses)
- [ ] List endpoints paginated
- [ ] New fields additive and optional
- [ ] Naming conventions consistent across the API
- [ ] Schema/types committed with implementation

---

## Reference Files

- **`references/api-patterns.md`**: REST resource layout, pagination, PATCH, branded IDs, unions — read at Step 3.

---

## Impact Report

```
Resource: [name] | Surfaces: N
Breaking risks flagged: N | Pagination: [yes/no]
Schema committed: [path or pending]
```
