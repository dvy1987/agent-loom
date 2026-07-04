# App Security Hardening — Full Worked Examples

Skill: `app-security-hardening` | Load when producing output for this workflow.

## Example 1 — From skill workflow

**Input:** “Add a new endpoint that updates a user profile.”

**Output:**
```
Validate request DTO at the route boundary, enforce authZ (user can only update self unless admin), normalize strings, reject unknown fields, ensure CSRF strategy matches session model, and add tests for IDOR and invalid payloads.
```

## Example 2 — Typical invocation

**Input:** "Run `app-security-hardening` for [concrete task]"

**Output:**
```
Invoked `app-security-hardening`.
Step 1: Define the surface
Step 2: Boundary validation
Step 3: AuthN/AuthZ hardening (when applicable)
Scope: [endpoints/modules] | Surfaces: N
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
