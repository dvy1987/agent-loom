# Design System — Full Worked Examples

Skill: `design-system` | Load when producing output for this workflow.

## Example 1 — Typical invocation

**Input:** "Run `design-system` for [concrete task]"

**Output:**
```
Invoked `design-system`.
Step 1: Read inputs
Step 2: Seed from the recipe
Step 3: Build color tokens (state-level)
Design system built: [feature]
```

## Example 2 — Success criteria

**Input:** "Use `design-system` on this project"

**Output:**
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

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
