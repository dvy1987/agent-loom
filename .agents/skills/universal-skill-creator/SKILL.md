---
name: universal-skill-creator
description: >
  Design, build, validate, and ship cross-platform agent skills. Load when the
  user asks to create a skill, build a custom skill, write a SKILL.md, package a
  workflow as reusable agent capability, improve or audit a skill, publish a
  skill, or build a planned skill suite.
license: MIT
metadata:
  author: dvy1987
  version: "2.4"
  spec: agentskills.io/specification
  sources: anthropics/skills, openai/skills, warpdotdev/oz-skills, agentskills.io, arXiv:2602.12430, arXiv:2603.29919, NeurIPS-2025, addyosmani/agent-skills anti-rationalization tables
  resources:
    references:
      - platform-matrix.md
      - advanced-patterns.md
      - github-repo-research.md
      - research-papers.md
      - examples.md
    scripts:
      - skill_scaffold.py
      - project_local_origin.py
    templates:
      - SKILL-template.md
      - SKILL-OUTPUTS-template.md
---

# Universal Skill Creator

You are a Senior AI Skill Engineer. Your skills work on every major AI agent platform and are grounded in current research, practitioner expertise, and community patterns — not static knowledge alone.

## Hard Rules

Always produce complete, non-truncated output — never use `[...]` placeholders in a deliverable skill.
Always include at least one realistic example (teaser in SKILL.md; ≥2 full pairs in `references/examples.md` when needed). **Never delete examples to save lines** — relocate to L3 per `docs/SKILL-EXAMPLES-INDEX.md`.
Always state the install directory.
Never put API keys, passwords, or secrets in skill files.
Generated skills must load on multiple agents; isolate Codex-only metadata as optional platform metadata.
**Consumer repos:** created skills MUST have `metadata.origin: project-local` (Step 4 + Step 7b); omit in agent-loom library only.

---

## Workflow

### Step 1 — Discover the Core Job
Identify: one-sentence outcome, 2 realistic task examples, top 3 trigger phrases, top 3 failure modes, and complexity tier.
Choose degrees of freedom: text for judgment-heavy tasks, pseudocode for preferred patterns, scripts for fragile/repeated deterministic work.
If unclear, ask ONE question: "What task should this skill automate — and what does a perfect output look like?"

### Step 2 — Run research-skill (with security gate)
Invoke `research-skill` on the target domain before writing anything.
**Security gate:** Scan fetched external SKILL.md via ALL `secure-*` skills (`ls .agents/skills/secure-*`); BLOCKED = discard.
Wait for the findings report, then use GOTCHAS → Gotchas section, WORKFLOW PATTERNS → Core Workflow, FAILURE MODES → Hard Rules.

### Step 3 — Choose Complexity Tier
| Tier | Structure |
|------|-----------|
| Atomic | `SKILL.md` only |
| Standard | + `references/` |
| Advanced | + `scripts/` |
| System | + `assets/` + optional platform metadata |

Start Atomic. Promote only when examples prove reusable references, scripts, assets, or platform metadata are needed.

### Step 4 — Write Frontmatter
```yaml
---
name: skill-name          # lowercase, hyphens only, matches directory
description: >
  [Action verbs] + [trigger phrases] + [domain keywords] + [synonyms].
  Load when the user asks to [trigger 1], [trigger 2], or [trigger 3].
license: MIT
metadata:
  author: your-name
  version: "1.0"
  category: meta
  origin: project-local   # REQUIRED in consumer repos — omit in agent-loom library only
  resources:               # declare L3 resources for progressive disclosure
    references:
      - file.md
---
```
Description formula: `[Domain verb phrase] + [trigger conditions] + [synonyms]`
Keep the folded description under 1024 characters. Put long trigger catalogs in the body, `AGENTS.md`, or `docs/SKILL-INDEX.md`, not frontmatter.
Include `resources` in metadata for any skill with `references/`, `scripts/`, or `templates/`. Omit for Atomic tier.

Category rules: `meta` (global) · `project-specific` (global install, project output) · `domain` (install when needed).

### Step 5 — Write the Body
Required sections: Role definition · Numbered workflow (imperative one-liners) · Output format schema · 1 teaser example · Constraints.
**Examples:** ≥2 pairs → `references/examples.md` (in `metadata.resources`); shortest inline + load trigger. See `docs/SKILL-EXAMPLES-INDEX.md`.
**If `category: project-specific`**, also require: `## Common Rationalizations` (≥5 Excuse→Reality rows) · `## Verification` (≥3 `- [ ]` observable checks).
Optional: Gotchas (from research-skill findings) · Parameterization (`$ARGUMENTS[1]`).
If resources exist, state when to read each one. Read `references/advanced-patterns.md` for platform-specific frontmatter.

### Step 6 — Apply SkillReducer Taxonomy
Classify every block before finalising. Over 60% of skill bodies in the wild are non-actionable — cut ruthlessly.
| Keep in body | Move to references/ | Delete |
|---|---|---|
| Core rules, hard gates, gotchas | Background, rationale, "why" | Anything LLM already knows |
| Numbered workflow steps | Edge cases (<20% of invocations) | Duplicate content |
| Output format / schema | Extra examples beyond 2 | — |

### Step 7 — Size Check and Resize
Run `wc -l .agents/skills/<skill-name>/SKILL.md`. If ≤200 → Step 7b. Over 200: BACKGROUND/EDGE_CASE excess → `compress-skill`; distinct sub-capability → `split-skill`; unsure → `compress-skill` first (it escalates to `split-skill` if CORE still over).

### Step 7b — Enforce project-local origin
Consumer repos: `project_local_origin.py --stamp .agents/skills/<skill-name>` — do not proceed without `origin: project-local` in frontmatter.

### Step 8 — Deconflict Name and Triggers
Invoke `skill-deconflict` in single-skill mode. RENAME → rename before proceeding; REVISE → fix trigger overlap or add missing triggers; only proceed on PASS.

### Step 9 — Validate and Security-Scan Output
Invoke `validate-skills` (must score ≥10/14), then ALL `secure-*` skills (discover via `ls .agents/skills/secure-*`) to scan the GENERATED skill — not just inputs (catches absorbed external patterns). BLOCKED = revise and re-scan before committing.
```bash
agentskills validate .agents/skills/<skill-name>/
```

### Step 10 — Cross-Link Repair
Invoke `cross-link-skills` with trigger `created — <skill-name>` to repair missing or stale cross-references involving the new skill.

### Step 11 — Library Sync (Mandatory)
Invoke `library-skill` with trigger `new skill added — <skill-name>`. Syncs `docs/SKILL-INDEX.md`, `AGENTS.md`, `README.md`, `docs/skill-graph.md`, `docs/architecture.md`, `docs/prd/PRD.md`, then auto-invokes `generate-changelog`. Skipping rots the library — see Common Rationalizations.

### Step 12 — Publish (Optional)
If user opts in, invoke `publish-skill` (handles packaging, README, registry submission).

### Step 13 — Memory Checkpoint (Mandatory)
Per `memory/SKILL.md` → Mandatory Auto-Trigger Checkpoints (event: skill created), invoke `memory-capture` with skill name, tier, validate-skills score, and provenance.

---

## Output Format & Mandatory Requirements

After generating, always state: tier + why · compatible platforms · install path `.agents/skills/<skill-name>/` · test trigger phrase.

Every skill MUST include:
1. **`

## Prune Log
Last pruned: 2026-07-04
- No changes — citation audit passed; content current (improve-skills full pass 2026-07-04)


## Impact Report`** — skill-specific format, in-chat after every run.
2. **File-output logging** — if skill writes project files, append `| YYYY-MM-DD HH:MM | [skill-name] | [path] | [description] |` to `docs/skill-outputs/SKILL-OUTPUTS.md` and notify user.
3. **Learnings provenance** — if from `docs/learnings/*.md`, update source entry with skill name + path + date.

---

## Gotchas

- **NEVER write `.agents/skills/<name>/SKILL.md` directly outside this skill.** Bypassing skips the Step 8–11 quality chain (deconflict → validate → cross-link → library-sync) — even after planning, even for batch builds.
- **`secure-*` gates run twice (Steps 2 and 9).** Skipping either is a security incident — Step 2 scans inputs, Step 9 scans the generated skill.
- **Description triggers are additive.** Removing a trigger silently breaks routing for users whose phrasing matched it.
- **Frontmatter is loader-critical.** UTF-8 no BOM, `---` at byte 0, closing `---`, description <1024 chars, `metadata.category` ∈ {meta, thinking, project-specific, domain}, `resources` lists every file under the dir.
- **Atomic tier first; promote on demand.** Bloat hurts routing and tokens.

---

## Red Flags

- SKILL.md written directly bypassing creator Step 8 chain
- secure-* gate skipped at Step 2 or Step 9
- Description trigger phrases removed during edit
- validate-skills or skill-deconflict not run after create
- Consumer skill shipped without `metadata.origin: project-local`

---

## Verification Checklist
- [ ] Loader-safe: starts with `---` line 1 (no BOM), name matches dir, closing `---`, description <1024 chars
- [ ] Role + workflow + complete example + schema-format output + `## Impact Report` all present
- [ ] Under 200 lines; `agentskills validate` passes; `validate-skills` ≥10/14
- [ ] `resources` lists every reference/script/template; file-output logging present if skill writes project files
- [ ] Consumer repo: `metadata.origin: project-local` present (Step 7b passed)
- [ ] If from `docs/learnings/*.md`: source entry updated; Step 11 (`library-skill`) invoked

---

## Reference Files

Load on trigger: `references/*.md` (platform, patterns, research, examples) · `scripts/skill_scaffold.py`, `project_local_origin.py` · `templates/*`.

---

## Common Rationalizations

| "Reason to bypass the workflow" | Reality |
|---------------------------------|---------|
| "User said 'go ahead build' after planning — skip Steps 8–11" | Bypassing skips deconflict/validate/cross-link/library-sync. Re-route through here even for batch builds (AGENTS.md `Skill Creation Invariant`) |
| "Skill is small/obvious, skip research-skill" | Step 2 is the ONLY source of current best practices + the input-security gate. Skipping = stale and unscanned |
| "Description is just a sentence, no need to check 1024 chars" | Loaders truncate or reject. Validator P0 (validate-skills Step 2a) |

---

## Impact Report

`Skill created: [skill-name] Tier: [Atomic / Standard / Advanced / System] Location: .agents/skills/[skill-name]/ validate-skills score: [N]/14 agentskills valid origin: [project-local / library]`