# AI SVG Generation Checklist

Read during svg-creation Step 5 when drafting SVG via LLM before accepting output.

Distilled from production prompt patterns (SVG-ORA-Studio, supermemoryai svg-animations). Use as a **review gate**, not a copy-paste prompt.

## System constraints to enforce

1. **Output:** raw `<svg>...</svg>` only — no markdown fences in the file artifact.
2. **viewBox:** must match requested aspect ratio; artwork fills ≥85% of viewBox.
3. **Self-contained:** no external images, fonts, or URLs.
4. **Complexity tier:** minimal = few paths; detailed = justified extra geometry only.
5. **Animation toggle:** if animated, include SMIL or embedded `<style>` per delivery context (Step 2).
6. **Negative space:** reject layouts with large empty margins around subject.
7. **Palette:** prefer `currentColor` for icons; fixed palette only for illustrations — document hex choices.

## Review rubric (reject and re-prompt if fail)

| Check | Pass | Fail |
|-------|------|------|
| Path economy | ≤10 paths for icons | Hundreds of micro-segments |
| Dash animation | `pathLength` or explicit length | Magic number `stroke-dasharray: 300` |
| Morph | Matching command structure | Different point counts |
| Security | No script/handlers/foreignObject | Any executable or HTML embed |
| IDs | Prefixed, unique | Generic `grad1` collisions |
| Motion | Loops smoothly | Pop at loop boundary |

## Re-prompt template

```
Regenerate the SVG. Fix: [specific failures from rubric].
Delivery: [inline|img|readme]. Use [SMIL|CSS].
viewBox: [ratio]. Style: [minimal|illustrated]. Animation: [yes/no].
Fill the viewBox. currentColor for strokes. No external resources.
```

## Post-generation pipeline

1. Run static-craft cleanup (metadata strip, simplify paths).
2. Run animation-craft validation if animated.
3. Save via svg-creation Step 7.
