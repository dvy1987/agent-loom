# Brainstorming — Full Session Examples

Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.

---

## Example 1 — Feature design (dark mode)

**Input:** "I want to add dark mode to our React app"

**Phase 1 — Frame (How Might We)**
```
How Might We let users switch between light and dark themes without breaking
existing custom components or increasing bundle size significantly?
```

**Clarifying question (one at a time):**
> Do you have an existing design system or component library (Tailwind, MUI, styled-components), or are styles written manually?

**User:** "Tailwind v4 + a few custom CSS modules for charts."

**Phase 2 — Options (3 divergent approaches)**

| Option | Summary | Trade-off |
|---|---|---|
| A. CSS variables + `class="dark"` on `<html>` | Token swap at root | Fast; chart CSS modules need manual vars |
| B. Tailwind `dark:` variant only | No extra runtime | Verbose; easy to miss a component |
| C. User preference in localStorage + system sync | Best UX | More state logic; flash-of-wrong-theme risk |

**Phase 3 — Converge**
Recommend **A + C**: CSS variables for charts, Tailwind dark: for app shell, `prefers-color-scheme` default with override.

**Design doc sections produced:**
- How Might We statement
- Target user: power users who work evenings; success = readable charts in both modes
- **Not Doing:** Per-component theme props (scope creep); auto-detect without manual toggle (accessibility concern)
- Key assumptions: chart library supports CSS color vars (validate in spike)
- HYPOTHESIS: 80% of screens themable via tokens alone — CONFIDENCE: 65%

**Output path:** `docs/specs/YYYY-MM-DD-dark-mode-design.md` — **no code until user approves.**

---

## Example 2 — Route to venture-exploration

**Input:** "I'm thinking of building a SaaS for freelance invoicing"

**Step 1 detect:** Business idea, not feature design → invoke `venture-exploration` instead of continuing brainstorming.

**Handoff message:**
> This sounds like a business validation question, not a feature design session. I'll route to venture-exploration for idea cards, Lean Canvas, and Mom Test interviews. Want to continue there?

---

## Example 3 — Anti-pattern recovery

**Input:** "Just pick the best architecture and implement auth"

**Response (Hard Gate):**
> Brainstorming blocks implementation until an approved design doc exists. I can either (1) run a 10-minute design pass on auth approach options, or (2) route directly to `feature-spec` if you already have an approved spec. Which?

---

## Verification checklist (full session)

- [ ] How Might We statement is clear
- [ ] Target user and success criteria defined
- [ ] Not Doing list makes trade-offs explicit
- [ ] Key assumptions listed with validation approach
- [ ] User approved design before implementation handoff
