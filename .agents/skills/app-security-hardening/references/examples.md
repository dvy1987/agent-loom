# App Security Hardening — Full Worked Examples

Skill: `app-security-hardening` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** “Add a new endpoint that updates a user profile.”

**Output:**
```
Validate request DTO at the route boundary, enforce authZ (user can only update self unless admin), normalize strings, reject unknown fields, ensure CSRF strategy matches session model, and add tests for IDOR and invalid payloads.
```

## Example 2 — Step-by-step execution

**Input:** "Run `app-security-hardening` on [concrete task]"

**Agent actions:**
1. Define the surface
2. Boundary validation
3. AuthN/AuthZ hardening (when applicable)
4. Injection and unsafe execution
5. Secrets, config, and logging
6. Dependency and supply-chain hygiene
7. Verify and document

## Example 3 — Anti-skip (rationalization defense)

**Input:** Agent tries to skip a gate

| Excuse | Reality |
|---|---|
| "We’ll add security later" | Retrofits are expensive; boundary validation is cheapest at creation time. |
| "Frontend already checks this" | Attackers don’t use your UI. Validate server-side. |
| "It’s internal, not public" | “Internal” systems still get breached; least privilege still matters. |
| "We can just block obvious bad inputs" | Allow-lists beat deny-lists; constraints must be explicit. |

## Example 4 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- “We validated on the frontend” is not validation.
- Multi-tenant bugs are often missing constraints, not fancy exploits.
- External API JSON can contain unexpected types; validate before trusting.
- Logging is an exfiltration channel; redact by default.

---

See `SKILL.md` for hard rules and verification checklist.
