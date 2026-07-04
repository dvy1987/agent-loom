# Frontend Design — Workflow Examples

Source: addyosmani/agent-skills `frontend-ui-engineering` workflow patterns (2026-05-29 snapshot). Security-scanned SAFE. Component craft: see `golden-examples/`.

---

## Example 1 — Full suite routing

**Input:** "Build a settings page for our SaaS"

```markdown
Route: design-direction → design-system → frontend-design build → design-review
Stage 0: Read product-soul / PRD for audience + stack
Output: DESIGN.md + working code; all states (loading/empty/error/populated)
```

---

## Example 2 — Anti-vibecoded rejection

**Input:** "Just use a centered hero, Inter, purple gradient"

**Output:** Reject default stack — run design-direction; require ≥1 distinctive move per DESIGN.md; match `golden-examples/` craft.

---

## Example 3 — State coverage gate

Before "done", verify each interactive component has:
- Default, hover, focus-visible, disabled, loading, error
See `golden-examples/states.md` for patterns.

---

## Example 4 — One-shot vs full path

| Ask | Route |
|---|---|
| "Quick landing tweak" | design-direction lite → build with existing DESIGN.md |
| "New product surface" | Full chain + design-review with APCA script |
