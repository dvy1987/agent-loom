---
name: app-security-hardening
description: >
  Harden an application against common security risks — validate inputs at
  boundaries, least-privilege access, safe secrets handling, dependency hygiene,
  and secure defaults. Load when shipping user-facing code, adding auth/session
  flows, handling untrusted data, exposing APIs, or the user asks for "security
  hardening", "OWASP hardening", "secure this feature". Not for skill-library
  security gates (use secure-skill family).
license: MIT
metadata:
  author: dvy1987
  version: "1.0"
  category: project-specific
  sources: addyosmani/agent-skills security-and-hardening (11/12, 2026-05-29)
---

# App Security Hardening

You reduce the chance and blast radius of security failures in **application code**. You focus on boundary validation, safe defaults, and least privilege — not theoretical checklists.

## Hard Rules

- Treat **all external inputs as untrusted**: HTTP requests, headers, query params, cookies, env vars, webhooks, third-party APIs, user-generated content.
- Validate at **boundaries** (routes/controllers/handlers) and at **trust transitions** (external API responses, deserialization).
- Never log secrets or credentials. Redact by default.
- Prefer **deny-by-default** authorization checks; make allow-lists explicit.
- Security changes must include a **verification step** (test, repro, or scanner run).

---

## Workflow

### Step 1 — Define the surface

Write down:
- Entry points (endpoints, jobs, webhooks, CLI, UI forms)
- Data types crossing trust boundaries
- High-value assets (accounts, money, tokens, PII)

### Step 2 — Boundary validation

For each entry point:
- Validate shape/types (schema/DTO)
- Validate constraints (length, ranges, enum allow-lists)
- Normalize (trim, lowercase where appropriate, Unicode normalization when relevant)
- Reject unknown fields (where feasible) to reduce ambiguity

### Step 3 — AuthN/AuthZ hardening (when applicable)

- AuthN: secure session/token storage; rotation; expiration; CSRF strategy if cookie-based
- AuthZ: check permissions on **every** sensitive action; avoid "frontend-only" gating
- Multi-tenant: enforce tenant scoping on queries and writes (no implicit tenant)

### Step 4 — Injection and unsafe execution

- SQL/NoSQL: parameterize queries; avoid string concatenation
- Command execution: avoid shelling out; if unavoidable, strict allow-list
- Template rendering: escape by default; avoid dangerouslySetInnerHTML-style patterns

### Step 5 — Secrets, config, and logging

- Load secrets from secret manager / env (never commit)
- Redact tokens, emails, IDs where appropriate
- Fail closed on missing security-critical config (e.g., auth secret)

### Step 6 — Dependency and supply-chain hygiene

- Prefer pinned lockfiles
- Minimize new deps; scrutinize transitive deps
- Run a vulnerability scan tool if available in the project

### Step 7 — Verify and document

Pick the cheapest credible verification:
- Unit/integration tests for validators and authZ
- Repro steps for common attacks (IDOR, privilege escalation)
- Static analysis / dependency audit command

---

## When NOT to use

- Skill-library security scanning or external content ingestion (use `secure-skill*`)
- Pure refactors with no change in security-relevant behavior (unless risk is suspected)

---

## Gotchas

- “We validated on the frontend” is not validation.
- Multi-tenant bugs are often missing constraints, not fancy exploits.
- External API JSON can contain unexpected types; validate before trusting.
- Logging is an exfiltration channel; redact by default.

---

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "We’ll add security later" | Retrofits are expensive; boundary validation is cheapest at creation time. |
| "Frontend already checks this" | Attackers don’t use your UI. Validate server-side. |
| "It’s internal, not public" | “Internal” systems still get breached; least privilege still matters. |
| "We can just block obvious bad inputs" | Allow-lists beat deny-lists; constraints must be explicit. |
| "Logging helps debug" | Logging secrets creates permanent incident blast radius. Redact. |

---

## Output Format

```markdown
## App security hardening — [scope]

Surfaces reviewed: [list]
High-value assets: [list]
Hardening changes: [numbered list]
Verification: [tests/repro/scans] → [result]
Open risks: [remaining items + rationale]
```

---

## Examples

<examples>
  <example>
    <input>“Add a new endpoint that updates a user profile.”</input>
    <output>
Validate request DTO at the route boundary, enforce authZ (user can only update self unless admin), normalize strings, reject unknown fields, ensure CSRF strategy matches session model, and add tests for IDOR and invalid payloads.
    </output>
  </example>
</examples>

---

## Verification

- [ ] Every external entry point has boundary validation (shape + constraints)
- [ ] AuthZ checks exist for every sensitive action (no frontend-only gating)
- [ ] Secrets are never logged; logs are redacted by default
- [ ] At least one verification step was run (tests/repro/scanner)
- [ ] Remaining risks (if any) are explicitly listed with rationale

---

## Impact Report

```
Scope: [endpoints/modules] | Surfaces: N
Validators added: [yes/no] | AuthZ checks: [yes/no]
Verification: [what] | Open risks: N
```
