# Stack Selection — Derive It From the Product

The stack is not a default to assume; derive it from `docs/product-soul.md`, the PRD, and
specs (and any existing manifests). State the recommendation with a one-line rationale, then
build with that stack's strong, opinionated system.

If the repo already has a stack (manifest present), use it — do not migrate. This guide is
for greenfield or when the user asks what to use.

---

## Step 1 — Read product signals
From product-soul/PRD/specs extract: product type (web app / marketing site / dashboard /
mobile / content), interactivity level, SEO need, team skill, target platforms, existing code.

## Step 2 — Map to a recommended stack

| Product signal | Recommended stack | Why |
|---|---|---|
| Interactive web app / SaaS / dashboard (default) | **React + Next.js + Tailwind v4 + shadcn/ui** | Strongest component ecosystem; what v0/Lovable/Claude optimize for; shadcn = accessible Radix primitives you restyle |
| Marketing / landing / mostly static + SEO | **Astro + Tailwind** (islands for interactivity) | Ship near-zero JS; best LCP; content-first |
| Content / blog / docs | **Astro** or **Next.js MDX** | Editorial layouts, MDX, fast |
| Mobile app | **Expo + React Native + NativeWind** | Token-shared RN; same mental model |
| Design-light internal tool | **Next.js + Tailwind + shadcn/ui** | Speed over bespoke |
| Existing repo with a stack | **Match it** | Never migrate for a design task |

Default when ambiguous and it's an app: React + Next + Tailwind v4 + shadcn/ui.

## Step 3 — shadcn is a primitives layer, not a look

shadcn/ui gives accessible, unstyled-ish primitives (Radix under the hood). A shadcn
**drop-in looks generic** — that is the trap. The non-generic path:
1. Install primitives for behavior/accessibility (dialog, popover, select, etc.).
2. Drive ALL their styling from the DESIGN.md tokens (override the default theme vars).
3. Restyle the visible surface per the chosen direction; never ship default shadcn styling.

So: shadcn for *behavior + a11y*, DESIGN.md tokens + golden examples for *the look*.

## Step 4 — Token format per stack
- shadcn/ui → HSL channel vars (`--background: 240 33% 14%;`, consumed via `hsl(var(--background))`).
- Tailwind v4 (no shadcn) → `@theme` with `oklch()` custom properties.
- Astro / plain → `:root` + `[data-theme="dark"]` custom properties (`oklch`).
Pass the chosen format to `design-system` so tokens emit correctly.

## Step 5 — Record it
State in the DESIGN.md header: `Stack: [...]. Token format: [...].` and a one-line rationale
the user (including a non-technical owner) can understand.

---

## Anti-patterns
- Assuming a stack without reading product docs.
- Migrating an existing repo's stack for a design pass.
- Shipping default shadcn styling (generic by definition).
- Picking a heavy SPA for a static marketing site (kills LCP).
