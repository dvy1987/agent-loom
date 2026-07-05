# Open Questions

Blocking or strategic questions needing human decision before implementation.

---

## COMPATIBILITY.md and the One Rule (2026-07-05)

**Context:** High-leverage spec proposed per-skill `references/COMPATIBILITY.md` documenting verified platforms (Cursor, Claude Code, Copilot, etc.) for the "works first try on ≥3 platforms" rule.

**Open:**

1. Is COMPATIBILITY a **release artifact** (marketing/audit) or an **enforced quality gate** (blocks ship like `validate-skills`)?
2. One shared `docs/COMPATIBILITY.md` vs per-skill files vs generated from a test matrix?
3. Who runs and updates platform checks — manual smoke, CI, or honor-system?
4. Does `agentskills.io` `compatibility` frontmatter field replace markdown files?
5. Minimum bar before claiming cross-platform in README?

**Status:** Deferred as #13 in `deferred.md` until strategy is decided.

**Related:** `agentskills validate` should run when CLI available; independent of COMPATIBILITY policy.
