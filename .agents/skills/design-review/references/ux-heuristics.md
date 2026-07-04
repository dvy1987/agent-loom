# UX Heuristics (supplement to visual rubric)

Lightweight usability checks beyond polish. Score as part of review; flag in findings
when any fail. No external link dependencies — patterns only.

## Navigation & wayfinding

- Current location is visible (breadcrumb, active nav, page title)
- Primary task reachable in ≤3 clicks from landing
- Back/exit paths exist on every modal and multi-step flow
- Destructive actions are not adjacent to primary actions without confirmation

## Forms & input

- Every field has a visible label (not placeholder-only)
- Required fields marked; optional fields marked when most are required
- Inline validation on blur or submit — not only on server round-trip
- Error messages name the field and the fix ("Email must include @")
- Password fields offer show/hide toggle

## Feedback & recovery

- Actions that take >400ms show loading state
- Success confirmations for irreversible or high-stakes actions
- Errors offer a recovery path (retry, edit, contact support) — not a dead end
- Empty states explain what belongs here and offer one next action

## Content & clarity

- Headings describe page purpose in plain language
- Jargon and abbreviations defined on first use (or avoided)
- Legal/consent copy is readable size; not buried in gray 10px text
- Pricing tiers compare features without hiding exclusions in footnotes

## Delight (micro-interactions + micro-copy)

- Transitions confirm causality (button press → result appears)
- Micro-copy matches product voice — not generic system strings
- One intentional delight moment per primary flow (not animation everywhere)
- `prefers-reduced-motion` honored (see accessibility gate)

## Scan method

Walk the three primary user flows from DIRECTION.md. For each screen, check the
sections above. Any clear fail → finding with `file:line` and specific fix.
