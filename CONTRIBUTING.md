# Contributing to cross-plat-skills

---

## The One Rule

Every skill must work on the first try in at least three platforms.
If it only works in Claude Code, it doesn't belong here.

---

## Adding a Skill

### 1. Scaffold it

```bash
python .agents/skills/universal-skill-creator/scripts/skill_scaffold.py \
  --name your-skill-name \
  --tier atomic \
  --author your-name
```

Or copy the template manually:
```bash
mkdir -p .agents/skills/your-skill-name
cp .agents/skills/universal-skill-creator/templates/SKILL-template.md \
   .agents/skills/your-skill-name/SKILL.md
```

### 2. Write it

Open `.agents/skills/your-skill-name/SKILL.md` and fill in:

- **`description`** — the most important field. Write it to answer: "When should an agent load this?" Include trigger phrases, domain keywords, and synonyms. Use the full 1024 characters for public skills.
- **Role definition** — "You are a [specific expert] specializing in [narrow domain]"
- **Numbered workflow** — one action per step, action verbs only
- **Gotchas** — non-obvious facts the agent will get wrong without being told
- **2+ examples** — realistic input → complete (non-truncated) output
- **Verification checklist** — what the agent checks before presenting output

**Quality standards (enforced):**
- No vague language: "fast", "easy", "intuitive", "modern", "robust" → replace with specific, testable criteria
- No negative constraints: "don't do X" → rewrite as "do Y instead"
- No placeholder text in published skills: TBD, TODO, `[fill in]`
- SKILL.md body under 500 lines — move large reference material to `references/`

### 3. Validate it

```bash
pip install -q skills-ref
agentskills validate .agents/skills/your-skill-name/
```

Must pass with zero errors before committing.

### 4. Test it

Before submitting, test with at least one trigger prompt in a real agent. Include that test prompt in your PR description:

```
Test prompt: "help me write a sprint retrospective for last week's sprint"
Expected: sprint-retro skill loads, asks for team size and sprint duration
```

### 5. Update the README

Add a row to the Skills table in `README.md`:

```markdown
| [`your-skill-name`](.agents/skills/your-skill-name/) | What it does | "trigger phrase 1", "trigger phrase 2" |
```

### 6. Commit

```bash
git add .agents/skills/your-skill-name/ README.md
git commit -m "feat: add your-skill-name skill"
```

---

## Skill Tiers

Choose the right complexity for the job:

| Tier | Structure | When to Use |
|------|-----------|-------------|
| **Atomic** | `SKILL.md` only | Self-contained task, no external reference needed |
| **Standard** | + `references/` | Task needs lookup tables, API docs, or long examples |
| **Advanced** | + `scripts/` | Needs deterministic automation or validation |
| **System** | + `assets/` + `agents/openai.yaml` | Full workflow with output templates + Codex UI |

Start Atomic. Promote only when SKILL.md exceeds 400 lines or the agent consistently needs reference material.

---

## Skill Author Checklist

Before every commit:

**Frontmatter**
- [ ] File starts with `---` on line 1 (no blank lines before it)
- [ ] `name` is lowercase, hyphens-only, matches directory name exactly
- [ ] `description` has trigger keywords, action verbs, synonyms
- [ ] No unknown top-level fields (custom fields go under `metadata:`)

**Body**
- [ ] Expert role defined in first paragraph
- [ ] Workflow steps numbered, one action each, action verbs
- [ ] Gotchas section with specific non-obvious facts
- [ ] At least 2 examples with realistic inputs and complete outputs
- [ ] Output format defined as schema or template (not prose)
- [ ] Verification checklist included
- [ ] All constraints phrased positively
- [ ] Under 500 lines

**Cross-platform**
- [ ] Installs in `.agents/skills/` (universal location)
- [ ] `agentskills validate` passes with zero errors
- [ ] Test prompt confirmed working in at least one real agent

---

## Skill Relationships

When adding a skill, consider how it chains with existing ones:

```
brainstorming → prd-writing → [your planning/execution skill here]
```

If your skill naturally follows or precedes an existing skill, add a handoff note at the end of your SKILL.md — e.g., "Once the plan is approved, invoke the `prd-writing` skill."

---

## Resources

- [agentskills.io specification](https://agentskills.io/specification)
- [agentskills.io best practices](https://agentskills.io/skill-creation/best-practices)
- [anthropics/skills](https://github.com/anthropics/skills) — reference quality bar
- [openai/skills](https://github.com/openai/skills) — Codex patterns
- [warpdotdev/oz-skills](https://github.com/warpdotdev/oz-skills) — parameterized skill patterns
- [obra/superpowers](https://github.com/obra/superpowers) — workflow enforcement patterns
