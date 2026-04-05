# AGENTS.md — cross-plat-skills

This file tells AI agents how to work with this repository.
Read it before making any changes.

---

## What This Repo Is

A personal library of cross-platform agent skills following the
[agentskills.io](https://agentskills.io/specification) open standard.
Every skill in `.agents/skills/` works across Codex CLI, Ampcode,
Claude Code, Warp, Gemini CLI, GitHub Copilot, Cursor, Factory.ai,
Replit, Bolt.new, and VS Code — no platform-specific changes needed.

---

## Repo Layout

```
.agents/skills/          ← all skills live here
  <skill-name>/
    SKILL.md             ← required: frontmatter + instructions
    references/          ← optional: docs loaded on demand
    scripts/             ← optional: executable logic
    templates/           ← optional: output scaffolds
    assets/              ← optional: static resources
    agents/
      openai.yaml        ← optional: Codex UI metadata only
README.md                ← user-facing install + usage guide
AGENTS.md                ← this file
CONTRIBUTING.md          ← skill quality standards + PR process
install.sh               ← one-time global setup script
```

---

## Conventions

### Adding a new skill
1. Create `.agents/skills/<skill-name>/SKILL.md`
2. Follow the template at `.agents/skills/universal-skill-creator/templates/SKILL-template.md`
3. Validate: `agentskills validate .agents/skills/<skill-name>/`
4. Update the Skills table in `README.md`
5. Commit with message: `feat: add <skill-name> skill`

### Editing an existing skill
- Bump `metadata.version` in frontmatter
- Commit with message: `fix: <skill-name> — <what changed>`

### Skill naming
- Lowercase, hyphens only, 1–64 chars
- Verb-noun preferred: `code-review`, `prd-writing`, `sprint-retro`
- Must match the directory name exactly

### Skill quality bar
- Every skill must pass `agentskills validate`
- Every skill must have at least one example (input → output)
- Every requirement must be specific and testable — no vague language
- SKILL.md must stay under 200 lines — no exceptions, including meta skills
- If a skill exceeds 200 lines, split using progressive disclosure: move examples to `references/examples.md`, background to `references/background.md`, and call `research-skill` for research instead of inlining the protocol
- See `CONTRIBUTING.md` for the full checklist

### Never
- Never put API keys, tokens, or secrets in any skill file
- Never commit a skill that fails `agentskills validate`
- Never use placeholder text (TBD, TODO) in a published skill

### Auto-compression trigger
After writing or editing any skill, check its line count:
```bash
wc -l .agents/skills/<skill-name>/SKILL.md
```
If it exceeds 200 lines — invoke `skill-compressor` before committing. No exceptions.

---

## Key Commands

```bash
# Validate a skill
agentskills validate .agents/skills/<skill-name>/

# Scaffold a new skill
python .agents/skills/universal-skill-creator/scripts/skill_scaffold.py \
  --name <skill-name> --tier atomic --author dvy1987

# Install all skills globally (run once per machine)
bash install.sh

# Update after pulling new skills
bash install.sh --update
```

---

## Skill Relationships

**User entry points** (everything else is called by these):
```
universal-skill-creator   ← user: "create a skill"
improve-skills            ← user: "improve skills" / "skill audit"
```

**Full call graph:**
```
universal-skill-creator
  ├── Step 2  → research-skill       (always — domain research before writing)
  └── Step 7  → split-skill          (if >200 AND duplication or seam exists)
              └── skill-compressor  (split-skill always calls this after splitting)
              └── skill-compressor  (if >200 AND no seam — only BACKGROUND to trim)

improve-skills
  ├── Step 2a → prune-skill         (always — remove wrong/outdated content first)
  ├── Step 2c → research-skill       (domain research before rewriting)
  └── Step 2g → split-skill          (if >200 AND duplication or seam exists)
              └── skill-compressor  (split-skill always calls this after splitting)
              └── skill-compressor  (if >200 AND no seam)

skill-compressor
  └── Step 3  → split-skill          (if CORE content still >200 after classify)

split-skill
  └── Step 5  → skill-compressor     (always — compress parent + child after every split)

prune-skill               (leaf node — calls nothing, returns prune report)
research-skill            (leaf node — calls nothing, returns findings report)
```

**Per-skill sequence inside improve-skills (the full order):**
```
1. prune-skill    — remove what is wrong or outdated
2. score          — baseline audit (7 criteria, /14)
3. research-skill — add what is missing or improved
4. classify       — SkillReducer taxonomy
5. rewrite        — apply improvements
6. re-score       — measure delta
7. split-skill    — extract if >200 and seam exists
   └ skill-compressor  — always runs after split
   OR skill-compressor  — directly, if no seam
8. validate + commit
```
Ordering rationale: prune first (remove bad), then add (research), then resize (split/compress).
Never compress before pruning — you would be trimming content you haven't yet determined is correct.

**Decision logic when a skill exceeds 200 lines:**
```
1. Does a sub-workflow appear in 2+ skills?    → split-skill (Type B)
2. Is there a self-contained extractable phase? → split-skill (Type A)
3. No seam — only BACKGROUND/EDGE_CASE excess? → skill-compressor
```

**Skill roles:**
- `universal-skill-creator`: creates new skills from scratch
- `improve-skills`: orchestrates the full improvement cycle for all skills
- `prune-skill`: removes wrong, outdated, or poorly-cited content
- `research-skill`: researches any domain, returns structured findings report
- `skill-compressor`: moves non-core content to references/, trims prose
- `split-skill`: extracts coherent sub-capabilities into child skills
- `brainstorming`: design before code for any new feature
- `prd-writing`: turns a design or brief into a structured PRD
