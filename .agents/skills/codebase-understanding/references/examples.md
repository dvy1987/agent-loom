# Codebase Understanding — Full Worked Examples

Skill: `codebase-understanding` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** Help me understand this repo before I start working on it.

**Output:**
```
[Scanned root: Next.js app with Prisma ORM, 3 main directories]

## Architecture Overview
Tech stack: TypeScript, Next.js 14, Prisma, PostgreSQL, Tailwind
Entry points: `src/app/layout.tsx` (UI), `src/app/api/` (API routes)
Layers: UI (src/app/), API (src/app/api/), Services (src/lib/), DB (prisma/)

## Key Flows
1. User signup: `app/signup/page.tsx` → `api/auth/register/route.ts` → `lib/auth.ts` → Prisma → DB
2. Dashboard load: `app/dashboard/page.tsx` → `api/projects/route.ts` → `lib/projects.ts` → DB

## Component Map
| Component | Path | Responsibility | Dependencies |
|-----------|------|----------------|--------------|
| Auth | src/lib/auth.ts | JWT + session management | prisma, jose |
| Projects | src/lib/projects.ts | CRUD for projects | prisma |

## Hotspots
- `src/lib/auth.ts:45-120` — 75-line function handling both login and registration
- `prisma/schema.prisma` — 3 TODO comments for missing indexes

## Recommendations
- Split auth.ts login/register into separate functions before adding features
- Add the missing DB indexes flagged in the schema

Want me to deep-dive into any of these components?
```

## Example 2 — Documented workflow

**Input:** How does the payment flow work in this codebase?

**Output:**
```
[Searched for payment/billing/stripe across the codebase]

## Key Flow: Payment Processing
`app/billing/page.tsx` → `api/billing/checkout/route.ts` → `lib/stripe.ts` → Stripe API → webhook at `api/webhooks/stripe/route.ts` → `lib/subscriptions.ts` → DB

## Component Map
| Component | Path | Responsibility | Dependencies |
|-----------|------|----------------|--------------|
| Checkout | api/billing/checkout/ | Creates Stripe session | stripe, lib/stripe |
| Webhook | api/webhooks/stripe/ | Handles payment events | stripe, lib/subscriptions |
| Subscriptions | lib/subscriptions.ts | Updates user plan in DB | prisma |

## Hotspots
- `lib/stripe.ts:30` — Stripe secret key loaded from env, verified
- `api/webhooks/stripe/route.ts:15` — Webhook signature verification present

Want me to trace another flow or go deeper on any component?
```

## Example 3 — Step-by-step execution

**Input:** "Run `codebase-understanding` on [concrete task]"

**Agent actions:**
1. Query knowledge graph (if present)
2. Scope the Request
3. Scan Project Structure
4. Map Architecture
5. Trace Key Flows
6. Surface Hotspots and Risks
7. Deliver the Mental Model

## Example 4 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- Directory names like `utils/` or `helpers/` reveal nothing about responsibility — always read the files inside.
- Monorepos have multiple entry points — check for workspace configs (`pnpm-workspace.yaml`, `lerna.json`, Cargo workspace).
- Generated files (build output, lockfiles, compiled assets) pollute architecture maps — identify and exclude them early.
- A `README.md` may be outdated — cross-reference claims against actual file structure.

---

See `SKILL.md` for hard rules and verification checklist.
