# AGENTS.md — cross-plat-skills

Agent instructions for working in this repo.
**Skill reference:** `docs/SKILL-INDEX.md` — read before invoking any skill.

---

## What This Repo Is

Cross-platform agent skills (agentskills.io standard). Skills in `.agents/skills/` work across Codex, Ampcode, Claude Code, Warp, Gemini, Copilot, Cursor, Factory.ai, Replit, Bolt.new, VS Code.

---

## Repo Layout

```
.agents/skills/<name>/SKILL.md   ← skill entry point (≤200 lines, no exceptions)
docs/SKILL-INDEX.md              ← full skill reference (read this first)
docs/skill-outputs/SKILL-OUTPUTS.md  ← auto-log of all project files generated
AGENTS.md                        ← this file (keep lean)
README.md                        ← user-facing install + usage guide
CONTRIBUTING.md                  ← skill quality standards
install.sh                       ← one-time global setup
```

---

## Conventions

```
name:    lowercase, hyphens only, 1–64 chars, matches directory
quality: agentskills validate must pass | score ≥10/14 | ≤200 lines
commit:  feat: add <name> | fix: <name> — <what> | compress: <name> | improve: <name>
never:   API keys in skill files | placeholder text | failing validate
```

---

## Skill Quality Gate

After writing or editing any skill:
```bash
wc -l .agents/skills/<name>/SKILL.md      # must be ≤200
agentskills validate .agents/skills/<name>/
```

If >200 lines → check `docs/SKILL-INDEX.md` for split vs compress decision:
- Duplication across 2+ skills or natural seam → `split-skill`
- Only BACKGROUND/EDGE_CASE excess → `skill-compressor`

---

## Skill Types (see docs/SKILL-INDEX.md for full details)

```
meta            | manage the skill library | install globally (~/.agents/skills/)
domain          | reusable workflows       | install globally
project-specific| one project's conventions| stay in this repo's .agents/skills/
```

---

## User Entry Points

```
"create a skill"     → universal-skill-creator
"improve skills"     → improve-skills
```

All other meta skills are called automatically. See `docs/SKILL-INDEX.md` → Call Graph.

---

## File Output Convention

Skills that generate project files:
1. Write file to appropriate `docs/` subdirectory
2. Append to `docs/skill-outputs/SKILL-OUTPUTS.md`
3. Tell user: "Saved to `[path]`. Logged in `docs/skill-outputs/SKILL-OUTPUTS.md`."

Bootstrap: `cp .agents/skills/universal-skill-creator/templates/SKILL-OUTPUTS-template.md docs/skill-outputs/SKILL-OUTPUTS.md`
