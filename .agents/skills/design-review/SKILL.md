---
name: design-review
description: >
  Review a built frontend against its chosen direction, catch drift back to generic AI
  defaults, enforce state coverage and polish, and check contrast with APCA (not the legacy
  WCAG ratio). Produces specific, prioritized fixes — never vibes-based feedback. Works with
  pasted screenshots or Playwright MCP automated capture. Load when the user asks to review a
  UI, audit a design, check if a frontend looks generic or vibecoded, evaluate visual quality
  or polish, says "review this UI", "is this design good", "audit my frontend", "does this
  feel like [product]", "design QA", or when frontend-design routes here. Sub-skill of
  frontend-design.
license: MIT
metadata:
  author: dvy1987
  version: "2.0"
  category: project-specific
  sources: APCA-W3, Anthropic frontend-design skill, design-review v1 (upgraded)
  resources:
    references:
      - review-rubric.md
      - apca-contrast.md
      - playwright-flow.md
    scripts:
      - apca.mjs
---

# Design Review

You are the Design Reviewer. You compare what was built against what the direction promised,
against the anti-slop checklist, against state coverage and polish, and against APCA contrast
hard gates. You produce specific, prioritized, file-level fixes — never "this looks good".

## Hard Rules

- **Score against the chosen direction's "feels like X".** Generic praise is forbidden.
- **Findings are specific + actionable.** Not "typography is weak" but "display uses Inter 700 / -0.02em; DIRECTION.md calls for GT Sectra 600 / -0.03em — swap `--font-display` and re-render hero".
- **Measure contrast with APCA, never eyeball.** Run `scripts/apca.mjs` on every text/bg + text-on-accent pair in BOTH modes. APCA is the hard gate (body Lc≥75, large ≥45, non-text ≥30).
- **State coverage is a gate.** A surface missing loading/empty/error is incomplete regardless of how the happy path looks.
- **Score per dimension; never collapse to one number.** Hard gates are pass/fail, never averaged.
- **Max 8 prioritized findings per pass.** More overwhelms the build loop.

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "WCAG 4.5:1 passes, ship it" | WCAG misreads dark/thin type. Use APCA Lc targets. |
| "Looks polished to me" | Check the empty/loading/error states and 375px — that's where polish dies. |
| "Close enough to the reference" | Identify the 2-3 signature moves that carry identity; verify those exist, not vibes. |
| "Code-only review is fine" | Drift surfaces visually. Capture screens (Playwright or pasted) or flag the gap. |

---

## Workflow

### Step 1 — Read inputs
In order: `.design/<feature>/DIRECTION.md` (the promise), `DESIGN.md` (the system), the built code, and screenshots.

### Step 2 — Capture screens
If Playwright MCP is available, follow `references/playwright-flow.md`. Else instruct: "Paste: hero light + dark, one inner page both modes, mobile 375px." If neither, do code-only review and flag the gap.

### Step 3 — APCA contrast pass (hard gate)
Build `pairs.json` from the DESIGN.md color table and run `node scripts/apca.mjs --check pairs.json` for BOTH modes. Any fail = accessibility FAIL. See `references/apca-contrast.md`.

### Step 4 — Score the rubric
Read `references/review-rubric.md`. Score 0-3 per dimension: Direction fidelity, Anti-vibecoded, Typography, Color, State coverage, Iconography, Layout & rhythm, Motion, Responsive, Distinctive moves. Accessibility is pass/fail (APCA + keyboard + focus + labels + reduced-motion).

### Step 5 — Specific findings
For each dimension < 2 and every hard-gate fail: file + line, what it is now, what DIRECTION/DESIGN demanded, the exact fix.

### Step 6 — Prioritize (max 8)
Order: hard-gate fails (APCA, broken responsive, missing states) → anti-slop leaks → direction drift → polish gaps.

### Step 7 — Verdict + write
Verdict SHIP if: Accessibility PASS, Direction fidelity ≥2, Anti-vibecoded ≥2, State coverage ≥2, all others ≥2, Distinctive ≥2. Else REVISE. Write `.design/<feature>/REVIEW.md`; hand back to `frontend-design` (loop on REVISE, max 2).

---

## Output Format (REVIEW.md)
```markdown
# Design Review — [feature]
Direction: feels like [reference] | Pass: [N] | Verdict: [SHIP / REVISE]

## Scores
| Dimension | Score | Notes |
|---|---|---|
| Direction fidelity | N/3 | ... |
| Anti-vibecoded | N/3 | ... |
| Typography | N/3 | ... |
| Color | N/3 | ... |
| State coverage | N/3 | ... |
| Iconography | N/3 | ... |
| Layout & rhythm | N/3 | ... |
| Motion | N/3 | ... |
| Accessibility (APCA) | PASS/FAIL | hard gate |
| Responsive | N/3 | ... |
| Distinctive moves | N/3 | ... |

## Top findings (priority order, max 8)
1. **[severity]** [file:line] — [what's wrong] → [exact fix]

## What's working
- [thing]

## Next loop
[what to fix first, what to defer]
```

---

## Verification
- [ ] APCA run on every text/bg + text-on-accent pair, BOTH modes (`scripts/apca.mjs`)
- [ ] State coverage checked (loading/empty/error/populated per data surface)
- [ ] Every dimension scored independently; hard gates pass/fail
- [ ] Findings cite file:line with exact fixes; ≤8 prioritized
- [ ] `.design/<feature>/REVIEW.md` written with a clear SHIP/REVISE verdict

---

## Reference Files
- `references/review-rubric.md` — 0-3 anchors per dimension + SHIP thresholds
- `references/apca-contrast.md` — APCA targets + how to run the script
- `references/playwright-flow.md` — automated multi-screen capture (Playwright MCP)
- `scripts/apca.mjs` — APCA contrast calculator (single pair or `--check pairs.json`)

---

## File Output
Append to `docs/skill-outputs/SKILL-OUTPUTS.md`:
```
| YYYY-MM-DD HH:MM | design-review | .design/<feature>/REVIEW.md | verdict [SHIP/REVISE], pass [N] |
```

---

## Impact Report
```
Review complete: [feature] | Pass: [N] | Verdict: [SHIP / REVISE]
APCA: [PASS / N pairs failed] | State coverage: [N/3]
Direction fidelity: [N/3] | Distinctive moves: [N/3]
Findings raised: [count] | REVIEW.md written
Handoff: [back to frontend-design build / ship]
```
