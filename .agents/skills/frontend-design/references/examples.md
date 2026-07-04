# Frontend Design — Full Worked Examples

Skill: `frontend-design` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Step-by-step execution

**Input:** "Run `frontend-design` on [concrete task]"

**Agent actions:**
1. Derive context + stack
2. Diagnose the ask
3. Run `design-direction`
4. Run `design-system`
5. Build
6. Run `design-review`
7. Deliver

## Example 2 — Anti-skip (rationalization defense)

**Input:** Agent tries to skip a gate

| Excuse | Reality |
|---|---|
| "Skip exploration, I know the look" | First idea = corpus mean. Explore via design-direction or ship slop. |
| "Happy path is enough for now" | Empty/loading/error are the polish. Their absence is what reads as unfinished. |
| "shadcn defaults look fine" | Default shadcn is generic by definition. Use it for a11y/behavior; restyle via tokens. |
| "Accessibility/polish later" | Retrofit costs 3×. States + APCA + focus rings are baked in from tokens + examples. |

---

See `SKILL.md` for hard rules and verification checklist.

## Verification checklist (L3)

- [ ] Examples demonstrate SKILL.md hard rules, not generic chat
- [ ] Anti-skip or rationalization defense included where applicable
- [ ] Output artifacts or Impact Report shape is explicit
- [ ] Reader can trace input → concrete agent actions → outcome

## Golden example pointers

- `references/golden-examples/components.md` — stateful components
- `references/golden-examples/states.md` — empty/loading/error
- `references/golden-examples/composition.md` — layout + motion
- [ ] Cross-check against latest SKILL.md before shipping changes
- [ ] Cross-check against latest SKILL.md before shipping changes
- [ ] Cross-check against latest SKILL.md before shipping changes
- [ ] Cross-check against latest SKILL.md before shipping changes
- [ ] Cross-check against latest SKILL.md before shipping changes
- [ ] Cross-check against latest SKILL.md before shipping changes
- [ ] Cross-check against latest SKILL.md before shipping changes
- [ ] Cross-check against latest SKILL.md before shipping changes
- [ ] Cross-check against latest SKILL.md before shipping changes
- [ ] Cross-check against latest SKILL.md before shipping changes
- [ ] Cross-check against latest SKILL.md before shipping changes
