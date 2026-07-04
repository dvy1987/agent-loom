# Design System — Full Worked Examples

Skill: `design-system` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Step-by-step execution

**Input:** "Run `design-system` on [concrete task]"

**Agent actions:**
1. Read inputs
2. Seed from the recipe
3. Build color tokens (state-level)
4. Typography, spatial, motion, elevation
5. APCA pass
6. Icon strategy
7. Component contracts
8. Emit

**Impact Report shape:**
```
Design system built: [feature]
Direction: [name]
Token format: [shadcn HSL / oklch / @theme]
Color slots (with states): [count] | Neutral ramp: 8-step
APCA: [all pass / fixes applied]
Icon strategy: [name] | Component contracts: [count]
Files: DESIGN.md, src/styles/tokens.css[, tokens.ts]
Handoff to: frontend-design (build)
```

## Example 2 — Anti-skip (rationalization defense)

**Input:** Agent tries to skip a gate

| Excuse | Reality |
|---|---|
| "Accent + a few greys is enough" | The slop lives in the unstated 95% — define every state or the model guesses the mean. |
| "Invert light mode for dark" | Inverted lightness reads cheap. Dark is a separate hand-set story. |
| "WCAG 4.5:1 is fine" | WCAG misreads dark themes and thin type. Use APCA Lc targets. |
| "Skip DESIGN.md, just write CSS" | DESIGN.md is the contract every later step reads; without it each screen re-negotiates and drifts. |

---

See `SKILL.md` for hard rules and verification checklist.
