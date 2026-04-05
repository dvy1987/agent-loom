# Skill Index

Complete reference for all skills in this repo. Referenced by AGENTS.md.
Read this when deciding which skill to invoke or when checking what a skill produces.

Last updated: 2026-04-05

---

## Skill Categories

| Category | Description |
|----------|-------------|
| **Meta** | Skills that manage the skill library itself. Available globally via `~/.agents/skills/`. |
| **Domain** | Reusable workflow skills for common product/engineering tasks. Available globally. |
| **Project-specific** | Skills scoped to one project's conventions, stack, or codebase. Live in `.agents/skills/` of that repo only. |

---

## Meta Skills

Skills that create, improve, validate, and manage other skills. Install globally — they work across all projects.

### `universal-skill-creator`
**Type:** Meta | **Scope:** Global
**Triggers:** "create a skill", "build a skill that does X", "skill creator", "write a SKILL.md"
**What it does:** Creates new cross-platform skills. Runs live domain research (papers + blogs + GitHub repos), writes the skill, validates quality (≥10/14), splits/compresses if needed, optionally publishes to skills.sh.
**Output:** `.agents/skills/<name>/SKILL.md` + optional references/, scripts/, templates/
**Impact report delivered:** Yes — tier, score, install path, test trigger, files created
**File logged to:** Not logged (skill files go to `.agents/skills/`, not `docs/skill-outputs/`)

---

### `improve-skills`
**Type:** Meta | **Scope:** Global
**Triggers:** "improve all skills", "skill audit", "upgrade skills with latest research", "run improvement pass"
**What it does:** Orchestrates the full improvement cycle for every skill. Runs validate → prune → research → rewrite → split/compress → commit. Processes all skills or a user-specified subset.
**Sequence:** validate-skills → (deprecate-skill if score 0–5) → prune-skill → research-skill → rewrite → split-skill/skill-compressor → validate + commit
**Output:** Modified SKILL.md files (every skill improved)
**Impact report delivered:** Yes — per-skill score deltas, sources used, all files modified

---

### `validate-skills`
**Type:** Meta | **Scope:** Global
**Triggers:** "validate skills", "skill health check", "check all skills", "pre-flight check"
**What it does:** Read-only health audit. Scores every skill on 7 criteria (0–2 each, max 14/14). Flags P0 failures, >200-line violations, broken caller references, orphaned reference files, duplicate triggers.
**Output:** No files modified. Structured quality report in chat.
**Impact report delivered:** Yes — skills checked, P0 failures, average score, recommended actions
**Scoring rubric:** `.agents/skills/validate-skills/references/validation-rubric.md`

---

### `prune-skill`
**Type:** Meta | **Scope:** Global
**Triggers:** "prune skills", "check for outdated techniques", "verify skill citations", "update for new model"
**What it does:** Evidence-only removal of wrong, outdated, or poorly-cited content. Audits every citation (trust tier: High=NeurIPS/ICML, Medium=arXiv 50+ citations, Low=blogs, Zero=unverifiable). Checks obsolete techniques list. Never prunes without a citable source.
**Output:** Target SKILL.md pruned + Prune Log section appended
**Impact report delivered:** Yes — items pruned, corrected, flagged, source for each
**Citation standards:** `.agents/skills/prune-skill/references/citation-standards.md`
**Obsolete techniques list:** `.agents/skills/prune-skill/references/obsolete-techniques.md`

---

### `research-skill`
**Type:** Meta | **Scope:** Global (leaf node — called by other skills)
**Triggers:** "research the domain for a skill", "find existing skills on X", "what research exists for Y"
**What it does:** Searches academic papers (arXiv, NeurIPS, ICML), practitioner blogs (Vercel, Stripe, Linear eng, HN, Substack), and GitHub skill repos (anthropics/skills, openai/skills, warpdotdev/oz-skills, VoltAgent/awesome-agent-skills) in parallel. Returns structured findings report.
**Output:** No files modified. Returns findings report: GOTCHAS, WORKFLOW PATTERNS, FAILURE MODES, EXISTING SKILLS.
**Impact report delivered:** Yes — sources consulted, gotchas found, existing skills found

---

### `skill-compressor`
**Type:** Meta | **Scope:** Global
**Triggers:** "compress this skill", "skill is over 200 lines", called by split-skill and improve-skills
**What it does:** Brings a SKILL.md under 200 lines by classifying content (CORE/WORKFLOW/FORMAT/EXAMPLE/BACKGROUND/EDGE_CASE/DUPLICATE) and moving non-core content to references/ with specific load triggers. Invokes split-skill if CORE content alone exceeds 200 lines.
**Output:** SKILL.md trimmed + new references/background.md or references/examples.md created
**Impact report delivered:** Yes — lines before/after, files created, regression check result
**Theory:** `.agents/skills/skill-compressor/references/compression-theory.md`

---

### `split-skill`
**Type:** Meta | **Scope:** Global
**Triggers:** "split this skill", "extract a sub-skill", "skill is doing too much"
**What it does:** Extracts a coherent sub-capability from a parent skill into a new child skill. Handles Type A (natural phase seam) and Type B (duplicated across 2+ skills). Always calls skill-compressor on both parent and child after splitting. Updates AGENTS.md and all callers.
**Output:** New `.agents/skills/<child>/SKILL.md` created. Parent SKILL.md and AGENTS.md modified.
**Impact report delivered:** Yes — parent/child line counts, callers updated, regression check
**Split patterns:** `.agents/skills/split-skill/references/split-patterns.md`

---

### `deprecate-skill`
**Type:** Meta | **Scope:** Global
**Triggers:** "deprecate this skill", "retire this skill", called by improve-skills when score 0–5/14
**What it does:** Gracefully retires a skill — requires evidence (not age alone), gets user confirmation, moves to `.agents/skills/.deprecated/`, writes DEPRECATION.md, updates all callers, AGENTS.md, README, and deprecation log.
**Output:** Skill moved to `.agents/skills/.deprecated/<name>-deprecated-YYYY-MM-DD/`. AGENTS.md, README, callers modified.
**Impact report delivered:** Yes — archive path, recovery command, callers updated
**Deprecation log:** `.agents/skills/deprecate-skill/references/deprecation-log.md`

---

### `publish-skill`
**Type:** Meta | **Scope:** Global
**Triggers:** "publish this skill", "share this skill publicly", "submit to skills.sh"
**What it does:** Validates quality (≥10/14 score required), scans for proprietary content, packages correctly (.md for Atomic, .zip for Standard+), writes README if missing, publishes to skills.sh via `npx skills publish`.
**Output:** Skill live on skills.sh registry. Optional git commit if pushing to GitHub.
**Impact report delivered:** Yes — registry URL, install command, score at publish
**Pre-publish checklist:** `.agents/skills/publish-skill/references/publish-checklist.md`

---

## Domain Skills

Reusable workflow skills for common product/engineering tasks. Install globally.

### `brainstorming`
**Type:** Domain | **Scope:** Global
**Triggers:** "brainstorm", "design this feature", "what's the best approach for", "let's think through", "before we build"
**What it does:** Turns a rough idea into an approved design through structured dialogue. One question at a time. Hard gate: no code or implementation until the user has reviewed and approved a written design doc.
**Output file:** `docs/specs/YYYY-MM-DD-<topic>-design.md` (committed to git)
**Logged to:** `docs/skill-outputs/SKILL-OUTPUTS.md`
**Terminal notification:** "Design doc saved to `docs/specs/...`. Logged in `docs/skill-outputs/SKILL-OUTPUTS.md`."
**Impact report delivered:** Yes — approach chosen, key decisions, open questions resolved, ready for next step

---

### `prd-writing`
**Type:** Domain | **Scope:** Global
**Triggers:** "write a PRD", "document requirements", "create a spec", "I need a PRD for", "turn this into a spec"
**What it does:** Runs a discovery interview (minimum 2 questions) then produces a structured PRD. Supports Full PRD, Lean PRD, One-Pager, and Technical PRD formats. Reads brainstorming design docs as foundation if present.
**Output file:** `docs/prd/YYYY-MM-DD-<feature>-prd.md`
**Logged to:** `docs/skill-outputs/SKILL-OUTPUTS.md`
**Terminal notification:** "PRD saved to `docs/prd/...`. Logged in `docs/skill-outputs/SKILL-OUTPUTS.md`."
**Impact report delivered:** Yes — format, sections written, open questions remaining, success metrics defined
**PRD schemas:** `.agents/skills/prd-writing/references/prd-schemas.md`
**Metrics frameworks:** `.agents/skills/prd-writing/references/metrics-frameworks.md`

---

## Project-Specific Skills

Skills scoped to a single project's conventions, stack, or domain. These live in `.agents/skills/` inside the project repo — not installed globally. They reference project-specific paths, APIs, database schemas, naming conventions, or tooling that would be meaningless outside that project.

**When to create a project-specific skill:**
- The skill references your project's specific file paths, API endpoints, or database schema
- The skill encodes your team's naming conventions or branching strategy
- The skill would produce wrong output if run in a different project without modification
- The output files land in project-specific directories

**Examples of project-specific skills** (not yet built — add as needed):
- `write-impl-plan` — generates `docs/plans/YYYY-MM-DD-<feature>-plan.md` with task breakdown from a PRD, following your project's ticket format
- `write-changelog` — generates `CHANGELOG.md` entries from git log, following your project's changelog conventions
- `write-adr` — generates Architecture Decision Records in `docs/adr/NNNN-<title>.md`
- `run-retro` — generates `docs/retros/YYYY-MM-DD-sprint-N-retro.md` from the sprint's git history and tickets

**How to create one:**
```
"create a project-specific skill for writing implementation plans"
```
`universal-skill-creator` will ask clarifying questions about your project's conventions, then build and save the skill to `.agents/skills/` in the current project.

---

## Skill Output Log Convention

Every skill that generates a project file appends to `docs/skill-outputs/SKILL-OUTPUTS.md`.

**Bootstrap (one time per project):**
```bash
mkdir -p docs/skill-outputs
cp .agents/skills/universal-skill-creator/templates/SKILL-OUTPUTS-template.md \
   docs/skill-outputs/SKILL-OUTPUTS.md
```

**Log format:**
```
| YYYY-MM-DD HH:MM | skill-name | file/path.md | One-line description |
```

---

## Call Graph (quick reference)

```
universal-skill-creator → research-skill, validate-skills, publish-skill (opt)
improve-skills          → validate-skills, prune-skill, research-skill,
                          split-skill, skill-compressor, deprecate-skill
skill-compressor        → split-skill (if CORE still >200)
split-skill             → skill-compressor (always after split)
validate-skills         leaf — read only
prune-skill             leaf — modifies target skill only
research-skill          leaf — returns findings report
deprecate-skill         leaf — archives skill
publish-skill           leaf — external action (skills.sh)
```
