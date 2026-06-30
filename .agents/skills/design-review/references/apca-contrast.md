# APCA Contrast — Measure, Don't Eyeball

Use APCA (perceptual) instead of the legacy WCAG 2.x ratio. WCAG misjudges dark themes and
thin type; APCA models real readability. This is a HARD GATE in review.

## Targets (`Lc`, absolute value)

| Content | Min Lc |
|---|---|
| Body text (normal weight, ≤18px) | 75 |
| Large or bold text (≥24px or ≥18px bold) | 45 |
| Non-text UI (icons, borders, focus rings, disabled affordances) | 30 |

Polarity: dark-on-light gives positive Lc, light-on-dark gives negative — compare the
absolute value to the target.

## How to run

The script lives at `scripts/apca.mjs` (Node, no deps).

Single pair:
```bash
node .agents/skills/design-review/scripts/apca.mjs "#1A1A1A" "#FAFAF7"
# -> Lc 101.1  (text on bg)
```

Batch — build a `pairs.json` from the DESIGN.md token table and check all at once:
```json
[
  { "name": "body",            "text": "#1A1A1A", "bg": "#FAFAF7", "min": 75 },
  { "name": "secondary text",  "text": "#5A5A5A", "bg": "#FAFAF7", "min": 75 },
  { "name": "text-on-accent",  "text": "#FFFFFF", "bg": "#4338CA", "min": 75 },
  { "name": "border",          "text": "#D8D6CF", "bg": "#FAFAF7", "min": 30 },
  { "name": "body (dark mode)","text": "#ECECEC", "bg": "#141414", "min": 75 }
]
```
```bash
node .agents/skills/design-review/scripts/apca.mjs --check pairs.json
# PASS/FAIL per pair; non-zero exit if any fail
```

## What to check (every review)
- Every text/background pair from the DESIGN.md color table — BOTH light and dark mode.
- `text-on-accent` against the accent (the most-missed failure).
- Secondary/tertiary text (often fails at Lc 75).
- Non-text: borders, focus ring, disabled text, icon-only buttons (Lc ≥ 30).

## Fixing failures
- Shift the text or surface lightness until the pair clears the target.
- Text over images/gradients: add a semi-transparent overlay so the worst-case pair clears.
- Do NOT lower the target. If a brand accent can't carry white text at Lc 75, darken the
  accent or use dark text on it.
