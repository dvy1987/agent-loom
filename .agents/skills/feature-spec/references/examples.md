# Feature Spec — Full Worked Examples

Source: addyosmani/agent-skills `spec-driven-development` spec patterns (2026-05-29 snapshot). Security-scanned SAFE.

---

## Example 1 — Assumptions block before draft

**Input:** "Spec out dark mode"

```markdown
## Assumptions I'm Making
- Users toggle in settings (not system-only) — **confirm?**
- Scope: web app only, not marketing site
- Existing design tokens in DESIGN.md are source of truth
- Out of scope: per-component overrides

→ User confirms or corrects before FR/NFR draft.
```

---

## Example 2 — Vague requirement reframe

**Input:** "Make it fast and intuitive"

**Reframe:**
- "Fast" → NFR: LCP < 2.5s on 4G (measurable)
- "Intuitive" → FR: user completes primary flow in ≤3 clicks without help doc

---

## Example 3 — Given/When/Then acceptance criteria

**FR-3:** User can enable dark mode

```gherkin
Given the user is on Settings
When they toggle "Dark mode"
Then the UI uses dark tokens and preference persists across reload
And contrast meets APCA thresholds per design-system
```

---

## Example 4 — Clarify mode output

**Input:** `/clarify` on draft spec

```markdown
Open clarifications (max 3):
1. Persist preference per-device or per-account?
2. Default: system preference or light?
3. Email templates included in scope?
```
