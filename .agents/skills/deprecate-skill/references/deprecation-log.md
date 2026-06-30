# Deprecation Log

Running record of all deprecated skills. Updated by deprecate-skill after every deprecation.
Read when the user asks what has been deprecated and why, or when researching whether a skill was previously tried and removed.

---

## Active Deprecations

### design-archetype — deprecated 2026-06-30

**Reason:** Fully subsumed (trigger 2) — replaced by `design-direction` in the design suite rebuild.
**Evidence:** design-skills-rebuild plan; old skill picked one archetype instantly and skipped exploring distinct directions (the #1 cause of generic output).
**Migration:** `design-direction` (absorbs the 12-archetype catalog + selection rubric as a starting posture palette).
**Callers updated:** frontend-design, project-setup, AGENTS.md, docs/SKILL-INDEX.md, docs/skill-graph.md, README.md.
**Archive path:** `.agents/skills/.deprecated/design-archetype-deprecated-2026-06-30/`
**Recovery command:**
mv .agents/skills/.deprecated/design-archetype-deprecated-2026-06-30/ .agents/skills/design-archetype/

### design-tokens-craft — deprecated 2026-06-30

**Reason:** Fully subsumed (trigger 2) — merged with `icon-craft` into `design-system`.
**Evidence:** design-skills-rebuild plan; design intent was scattered across 4 docs and tokens lacked state-level depth (states, 8-step ramp, focus ring, APCA).
**Migration:** `design-system` (canonical DESIGN.md + state-level tokens + icons + component contracts).
**Callers updated:** frontend-design, project-setup, AGENTS.md, docs/SKILL-INDEX.md, docs/skill-graph.md, README.md.
**Archive path:** `.agents/skills/.deprecated/design-tokens-craft-deprecated-2026-06-30/`
**Recovery command:**
mv .agents/skills/.deprecated/design-tokens-craft-deprecated-2026-06-30/ .agents/skills/design-tokens-craft/

### icon-craft — deprecated 2026-06-30

**Reason:** Fully subsumed (trigger 2) — folded into `design-system`.
**Evidence:** design-skills-rebuild plan; icon strategy is one facet of a coherent system, not a standalone step.
**Migration:** `design-system` (icon strategy = Step 6 + salvaged icon-strategies/svg-craft references).
**Callers updated:** frontend-design, project-setup, AGENTS.md, docs/SKILL-INDEX.md, docs/skill-graph.md, README.md.
**Archive path:** `.agents/skills/.deprecated/icon-craft-deprecated-2026-06-30/`
**Recovery command:**
mv .agents/skills/.deprecated/icon-craft-deprecated-2026-06-30/ .agents/skills/icon-craft/

---

## Log Format

Each entry follows this structure:

```markdown
### [skill-name] — deprecated YYYY-MM-DD

**Reason:** [trigger condition that justified deprecation]
**Evidence:** [specific source with date]
**Migration:** [what replaced this skill, or "model-native"]
**Callers updated:** [list of skills that were modified, or "none"]
**Archive path:** `.agents/skills/.deprecated/[skill-name]-deprecated-YYYY-MM-DD/`
**Recovery command:**
mv .agents/skills/.deprecated/[skill-name]-deprecated-YYYY-MM-DD/ .agents/skills/[skill-name]/
```
