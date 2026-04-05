# cross-plat-skills

> A personal library of agent skills that work across every major AI coding tool — write once, run everywhere.

Skills follow the [agentskills.io](https://agentskills.io/specification) open standard and work with Codex CLI, Ampcode, Claude Code, Warp, Gemini CLI, GitHub Copilot, Cursor, VS Code, Replit, Factory.ai, and Bolt.new.

---

## Installation (One Time, Any Machine)

Clone the repo once and run the install script. Your skills become globally available in every tool, in every project — no per-project setup needed.

```bash
git clone https://github.com/dvy1987/cross-plat-skills.git ~/.cross-plat-skills
cd ~/.cross-plat-skills
bash install.sh
```

That's it. Open any project in Codex, Warp, Claude Code, Gemini — your skills are already there.

### Updating Later

When new skills are added to this repo:

```bash
bash ~/.cross-plat-skills/install.sh --update
```

This pulls the latest from git and refreshes all links. No reinstall, no restart (except Codex CLI which needs one restart if already running).

---

## How It Works

Every platform reads `~/.agents/skills/` as the global user-level skills folder. The install script symlinks each skill there once:

```
~/.agents/skills/
├── universal-skill-creator/   → ~/.cross-plat-skills/.agents/skills/universal-skill-creator/
├── brainstorming/             → ~/.cross-plat-skills/.agents/skills/brainstorming/
└── prd-writing/               → ~/.cross-plat-skills/.agents/skills/prd-writing/
```

A symlink means `git pull` is all you ever need — the platform sees the updated skill immediately.

| Platform | Reads global skills from |
|----------|--------------------------|
| Codex CLI | `~/.agents/skills/` |
| Ampcode | `~/.agents/skills/` |
| Claude Code | `~/.claude/skills/` or `~/.agents/skills/` |
| Warp | `~/.agents/skills/` |
| Gemini CLI | `~/.agents/skills/` |
| GitHub Copilot CLI | `~/.agents/skills/` |
| Cursor | `~/.agents/skills/` |
| Factory.ai | `~/.factory/skills/` or `~/.agents/skills/` |
| Replit | Project-level only (`/.agents/skills/`) |
| Bolt.new | Project-level only (`/.agents/skills/`) |

---

## Using Skills

### Codex CLI

```bash
codex                        # start Codex in any project
/skills                      # list all available skills
$brainstorming               # invoke explicitly
$prd-writing                 # invoke explicitly

# Or just describe your task — Codex matches automatically:
"brainstorm ideas for our onboarding flow"
"write a PRD for the payments feature"
```

### Ampcode / Claude Code

```bash
claude   # or amp
# Skills activate automatically when your message matches the description
"help me brainstorm approaches for this refactor"
"create a PRD for dark mode"
```

### Warp

```bash
/brainstorming
/prd-writing
/prd-writing for the new search feature    # pass context inline
```

### Gemini CLI / GitHub Copilot CLI

```bash
# Skills auto-load when your task matches — just describe what you want
"let's brainstorm the analytics dashboard design"
"write requirements for the export feature"
```

---

## The Daily Workflow

Skills enforce a repeatable product discipline **across every tool**:

```
Codex:    "build a feature for data export"
               ↓ brainstorming skill loads
          One question at a time → 2-3 approaches → design approval
          Saves design doc to docs/specs/

Warp:     /prd-writing
               ↓ prd-writing skill loads
          Discovery interview → structured PRD (Problem → Stories → Metrics → Risks)

Ampcode:  "implement the PRD we just wrote"
               ↓ agent reads spec, builds from it
          No vibe coding — builds from an approved spec
```

Same skills, chained across tools. Your entire product workflow — idea → design → spec → code — is version-controlled and works on any machine.

---

## Skills in This Repo

| Skill | What it does | Trigger phrases |
|-------|-------------|-----------------|
| [`universal-skill-creator`](.agents/skills/universal-skill-creator/) | Creates new cross-platform skills | "create a skill", "write a SKILL.md" |
| [`brainstorming`](.agents/skills/brainstorming/) | Turns ideas into approved designs before any code is written | "brainstorm", "design this feature", "explore approaches" |
| [`prd-writing`](.agents/skills/prd-writing/) | Runs a discovery interview and outputs a structured PRD | "write a PRD", "document requirements", "create a spec" |

---

## Adding Skills to a Specific Project

If you want teammates to get a skill automatically (without running the install script):

```bash
cd your-project/
cp -r ~/.agents/skills/prd-writing .agents/skills/
git add .agents/skills/prd-writing
git commit -m "chore: add prd-writing skill for team"
```

Any teammate using Codex, Warp, Ampcode etc. in that repo gets the skill — no setup required on their end.

---

## Adding New Skills to This Repo

Use the `universal-skill-creator` skill to build new ones:

```bash
# In any AI tool with the skill installed:
"create a skill for writing sprint retrospectives"
"build a skill for code review"
"make a skill for writing changelog entries"
```

Or scaffold manually:

```bash
python .agents/skills/universal-skill-creator/scripts/skill_scaffold.py \
  --name my-skill \
  --tier atomic \
  --author dvy1987
```

Then commit to this repo and run `install.sh --update` on any machine.

---

## Resources

- [agentskills.io specification](https://agentskills.io/specification)
- [agentskills.io best practices](https://agentskills.io/skill-creation/best-practices)
- [anthropics/skills](https://github.com/anthropics/skills) — Anthropic reference skills
- [openai/skills](https://github.com/openai/skills) — Official Codex skills catalog
- [warpdotdev/oz-skills](https://github.com/warpdotdev/oz-skills) — Warp curated skills
- [github/awesome-copilot](https://github.com/github/awesome-copilot) — Community skills collection
- [obra/superpowers](https://github.com/obra/superpowers) — Battle-tested brainstorming + dev workflow skills

---

*MIT licensed — fork, adapt, use freely.*
