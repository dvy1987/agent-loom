# Exploration Method — Generating Genuinely Distinct Directions

The single biggest cause of generic AI design is committing to the first idea. Models
converge on the corpus mean. The fix is to generate **2-3 deliberately different
directions and compare them before any code exists** — you choose from options instead
of accepting the average.

This file is the core of `design-direction`. The archetype catalog is the *starting
palette*; this method is how you push off-center and diverge.

---

## Rule 1 — Pick a deliberate posture, not the safe center

Before generating directions, choose a point of view on purpose. The archetype gives the
audience/job fit; the posture gives the *attitude*. State it in one sentence:

> "Confident editorial-tech — looks like a product with an opinion, not a template."

Posture axes to set explicitly (each direction can sit differently on these):
- Restraint ↔ Expression (minimal vs maximal)
- Warm ↔ Cool (paper/ink vs clinical)
- Classic ↔ Experimental (familiar patterns vs grid-breaking)
- Quiet ↔ Loud color (monochrome + 1 accent vs saturated)
- Calm ↔ Kinetic motion

Never let all three directions cluster at the center of every axis. If they do, they are
the same direction in three palettes.

---

## Rule 2 — Make the three directions actually different

Generate 2-3 directions that differ on **at least 3 of these dimensions**, not just color:

1. Typography system (e.g. editorial serif display vs geometric mono vs humanist sans)
2. Color story (e.g. warm paper + ink vs dark-first jewel vs high-key monochrome)
3. Layout signature (e.g. asymmetric editorial grid vs dense dashboard vs centered calm)
4. Motion character (e.g. near-instant vs weighted/physical vs playful spring)
5. Density (dense vs generous)
6. The "one bold move" each direction commits to (a signature element)

Anti-pattern: "Direction A: blue. Direction B: green. Direction C: purple." That is one
direction. Reject and regenerate.

---

## Rule 3 — Each direction is concrete, named, and referenced

For each direction produce:
- A **name** ("Field Notes", "Control Room", "Soft Studio") — not "Option 1"
- A one-line **"feels like X"** naming a real, current product
- Type pair (display + body, real families)
- Color story (background, ink, the ONE accent, light + dark intent)
- Layout signature (the recurring move)
- Motion character (duration + curve intent)
- The single bold move
- One-line trade-off ("most distinctive but riskiest for enterprise buyers")

Vague adjectives ("clean", "modern", "premium") are banned — they do not converge.

---

## Rule 4 — Compare side-by-side, then commit to ONE

Present the directions in a single comparison table so the choice is between concrete
options, not re-prompted one at a time. Then commit to exactly one (hybrids look
vibecoded). Carry the runner-up's best single idea as an "influence" note only.

### Who chooses
- Technical / design-capable owner → present all directions, let them pick.
- Non-technical owner (`owner_mode: non-technical`) → recommend ONE with a plain-language
  rationale ("I recommend Field Notes: it reads as credible and editorial, which suits a
  research audience, and it is the least likely to look like a generic template"), and
  name the safe alternative. Decide; do not force a technical choice on them.

---

## Rule 5 — Ground in product reality

Pull the audience, emotional goal, brand hints, and constraints from `docs/product-soul.md`,
the PRD, and specs before inventing directions. A direction that ignores the product's job
is just decoration. If those docs are absent, ask one question (purpose + a reference
product) and proceed.

---

## Output

Write the chosen direction (plus the rejected options as an appendix) to
`.design/<feature>/DIRECTION.md`. `design-system` reads it to build the DESIGN.md and
tokens. Keep the rejected options recorded — they are the audit trail that proves
exploration happened.
