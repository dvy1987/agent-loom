---
name: project-constitution
description: >
  Author the project's non-negotiable engineering rules — the constitution
  that every feature spec, plan, and implementation must satisfy. Load when
  the user asks to write a constitution, define project rules, set engineering
  invariants, write project standards, define non-negotiables, capture
  agent guardrails as policy, or when spec-driven-development orchestrator
  routes here. Also triggers on "project constitution", "engineering
  invariants", "non-negotiable rules", "project policy", "set our standards",
  "/constitution". Output: docs/constitution.md. The third strategic
  artifact alongside AGENTS.md (agent behavior) and product-soul (strategy).
license: MIT
metadata:
  author: dvy1987
  version: "1.0"
  category: project-specific
  sources: GitHub Spec Kit (constitution command), AWS Kiro (specs-first), agentskills.io
---

# Project Constitution

You are a Principal Engineer. You write the project's irreducible engineering invariants — the rules that NEVER bend, regardless of feature, sprint, or PR. Specs reference the constitution. Plans cannot violate it. Implementations are rejected if they break it.

## Hard Rules

Never write a constitution longer than ~120 lines — it must fit in every agent's context.
Never write rules without IDs — every rule needs `C-N` so specs and plans can cite them.
Never write aspirational rules — every rule must be enforceable in code review or CI.
Never duplicate AGENTS.md (agent behavior) or product-soul (strategy) — constitution is engineering invariants only.
Never amend silently — every change bumps the version and gets an Amendment line.

---

## Workflow

### Step 1 — Check existing context

Read in priority order:
1. Existing `docs/constitution.md` (if updating — preserve IDs).
2. `AGENTS.md` (don't duplicate agent behavior rules).
3. `docs/product-soul.md` (don't duplicate strategy).
4. `package.json` / `pyproject.toml` / `Cargo.toml` / `go.mod` / `Makefile` (extract de-facto current standards: lint, test, type-check, coverage thresholds).

### Step 2 — Interview (max 5 questions, one at a time)

For each constitution category below, ask only what cannot be inferred:

1. **Testing** — required coverage, types of tests, what's untested-allowed
2. **Security/Privacy** — credentials, PII, dependency audit posture, threat model
3. **Performance** — latency budgets, bundle size limits, p95/p99 targets
4. **Accessibility** — WCAG level, supported languages (skip if no UI)
5. **Dependencies** — license rules, version pinning, vendor allowlist
6. **Observability** — logs, metrics, traces, error tracking required
7. **Migration/Rollback** — DB migrations, feature flags, blast radius
8. **Documentation** — what must be documented before merge

Skip categories that don't apply.

### Step 3 — Write the constitution

Use the schema below. Each rule:
- Has a stable ID (`C-1.1`)
- Is normative (MUST / MUST NOT / SHOULD)
- Is enforceable (a reviewer or linter can detect violations)
- Has at most a 1-line rationale

### Step 4 — Self-review

- [ ] Each rule has a unique ID
- [ ] No "should consider" / "try to" / "where possible" — vague = unenforceable
- [ ] No rule duplicates AGENTS.md or product-soul
- [ ] Total length < 120 lines
- [ ] Versioned (header has Version + Date)

### Step 5 — Save and notify

Save to `docs/constitution.md`.
Append to `docs/skill-outputs/SKILL-OUTPUTS.md`:
```
| YYYY-MM-DD HH:MM | project-constitution | docs/constitution.md | Constitution v<N> |
```

Tell the user:
> "Constitution saved to `docs/constitution.md` (v<N>). Every feature-spec must reference this version. Re-run when rules need to change — never amend silently."

---

## Output Format

```md
# Project Constitution
Version: 1 | Date: YYYY-MM-DD | Status: Active

## C-1 Testing
- C-1.1 Every PR MUST include unit tests for new logic. Rationale: regression protection.
- C-1.2 ...

## C-2 Security/Privacy
- C-2.1 Credentials MUST come from env vars or secret manager — never committed.
- C-2.2 ...

## C-3 Performance
- C-3.1 ...

## C-4 Accessibility (only if UI)
- C-4.1 ...

## C-5 Dependencies
- C-5.1 New runtime deps require ADR if they add > 100KB to bundle.

## C-6 Observability
- C-6.1 Every API endpoint MUST emit a request-id correlated log line.

## C-7 Migration & Rollback
- C-7.1 Every DB migration MUST be reversible OR shipped behind a feature flag.

## C-8 Documentation
- C-8.1 Public API changes MUST update docs in same PR.

## Amendments
- 2026-05-02: Initial draft.
```

---

## Gotchas

- Constitution rules are NOT preferences — they bend for nobody. If a team consistently waives a rule, remove it instead of letting it rot.
- Each rule must point at a single observable behavior. "Code should be clean" is not a rule. "Functions MUST be < 50 lines OR have a `# noqa: complexity` comment" is.
- Version bumps: any rule change is a major bump. Add to Amendments. Specs cite the version they were written against (e.g. `constitution: docs/constitution.md@2`).
- AGENTS.md vs constitution: AGENTS.md tells the agent HOW to work. Constitution tells the project WHAT must always be true. Don't confuse them.
- A waiver mechanism exists in `feature-spec` (a `## Constitution Waivers` section). Don't try to encode waivers here.

---

## Example

<examples>
  <example>
    <input>Set up a constitution for our SaaS app — Next.js + Postgres + Vercel.</input>
    <output>
[Interview: 4 questions — testing posture (90% on services, no UI snapshot), perf budget (LCP < 2s), GDPR (yes, EU users), DB migration policy (always reversible)]

Wrote 8 categories, 19 rules, 94 lines. Top rules:
- C-1.1 Service layer code MUST have ≥ 90% coverage (Vitest)
- C-2.2 PII fields MUST be marked in Prisma schema with `@encrypted`
- C-3.1 LCP MUST be < 2s on p75 (Vercel Analytics)
- C-7.1 Every Prisma migration MUST be backwards-compatible across one deploy

Saved to `docs/constitution.md` v1. Every feature-spec must now reference `constitution: docs/constitution.md@1`.
    </output>
  </example>
</examples>

---

## Impact Report

```
Constitution complete: v<N>
Categories: <N> populated, <M> skipped (with reason)
Rules: <N> total
Lines: <N>/120
Saved: docs/constitution.md
Logged: docs/skill-outputs/SKILL-OUTPUTS.md
Cited by: feature-spec, implementation-plan, spec-crosscheck
```
