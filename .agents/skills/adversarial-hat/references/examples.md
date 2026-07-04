# Adversarial Hat — Full Worked Examples

Source: addyosmani/agent-skills `doubt-driven-development` (2026-05-29 snapshot). Security-scanned SAFE. Adapted to agent-loom in-flight loop.

---

## Example 1 — In-flight CLAIM → STOP loop

**Input:** Agent states "This approach will scale to 10k RPS"

```markdown
CLAIM: "Scales to 10k RPS"
STOP — evidence?
- Load test cited? No
- Bottleneck analysis? No
→ Downgrade to HYPOTHESIS; require benchmark task or remove claim.
```

---

## Example 2 — Cross-model second opinion (optional)

**Input:** Large auth refactor complete

```markdown
Single-model review complete. Want cross-model second opinion?
Options: external review paste, adversarial subagent, or skip.
```

Use adversarial prompt verbatim — issues-only output, not balanced LGTM.

---

## Example 3 — Stop conditions

Stop doubt loop when:
- Findings trivial (style nits only)
- 3 cycles without new material issues
- User override: "ship it"

---

## Example 4 — Copyable adversarial prompt

```
Review ONLY for flaws, risks, and missing tests.
Do not praise. List issues with severity.
If no issues: say "No material issues" once — no filler.
```

Paste into subagent invocation; overrides persona default "balanced review" shape.
