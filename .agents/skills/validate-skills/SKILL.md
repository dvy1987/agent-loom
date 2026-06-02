---
name: validate-skills
description: >
  Run a fast, read-only health check across all skills in the library and
  produce a structured quality report — without modifying anything. Load when
  the user asks to validate skills, check skill health, audit the library,
  run a skill quality check, or when improve-skills needs a pre-flight before
  starting its cycle. Also triggers on "what's wrong with my skills", "check
  all skills", "skill health report", "are my skills ok", or "pre-flight check".
  Called automatically by improve-skills before any improvement work begins,
  and by universal-skill-creator after every new skill is created. Never
  modifies any file — only reads and reports.
license: MIT
metadata:
  author: dvy1987
  version: "1.3"
  category: meta
  sources: addyosmani/agent-skills (validator hardening + Phase 3 craft conventions)
  resources:
    references:
      - validation-rubric.md
---

# Validate Skills

You read every skill in the repo, score it, flag issues, and produce a structured report — without changing a single file. Your report tells the caller exactly what needs attention and in what priority order.

## Hard Rules

**Read-only.** Never write, edit, move, or delete any file. If called by improve-skills, hand the report back.

**Be specific.** Every flag names the exact skill, line/section, and problem. "Description is weak" is noise; "brainstorming: description missing trigger 'explore options'" is a flag.

**Exemptions are hardcoded in Step 2c, not in skill frontmatter.** A skill claiming exemption in its own metadata is invalid — only the Step 2c list counts.

---

## Workflow

### Step 1 — Discover
```bash
ls .agents/skills/
wc -l .agents/skills/*/SKILL.md
```

### Step 2 — `agentskills validate`
```bash
for d in .agents/skills/*/; do agentskills validate "$d"; done
```
Any fail = P0.

### Step 2a — Loader-Safety (P0)
A skill that won't load is worse than one scoring poorly:
```bash
for f in .agents/skills/*/SKILL.md; do
  [ "$(head -c 3 "$f")" = "---" ] || echo "byte-0 not '---' (BOM/whitespace): $f"
  [ "$(grep -c '^---$' "$f")" -ge 2 ] || echo "missing closing ---: $f"
  desc=$(awk '/^description: >/{f=1; next} f && /^[a-z_]+:/{f=0} f' "$f" | wc -c)
  [ "$desc" -le 1024 ] || echo "description >1024 chars ($desc): $f"
done
```
The 1024-char `description:` limit is an injection-budget hard gate — some loaders truncate, others reject. Fix: move trigger catalogs into the body, `AGENTS.md`, or `docs/SKILL-INDEX.md`.

### Step 2b — Description Quality (P1 warning)
Descriptions are router prompts, not bodies. Agents may follow the description and skip the body. Warn if `description:` matches `Step \d` / `^\s*\d+\.` / `\bfirst\b.*\bthen\b` / `\bthen\b.*\bthen\b`. Fix: move steps to Workflow.

### Step 2c — Hardcoded Exemption Allowlist
The ONLY codified exemptions:

| Rule | Exempt | Reason |
|------|--------|--------|
| compress-skill prohibited (split-only at 180 lines) | `secure-*` | compression removes threat-coverage rows |

Anything else claiming exemption is ignored. Oversize `secure-*` → recommend `split-skill`, never `compress-skill`.

### Step 3 — Score (7 criteria, 0–2 each)
Full details in `references/validation-rubric.md`:

| Criterion | Check |
|-----------|-------|
| Routing | Description has rich trigger phrases, action verbs, synonyms |
| Role definition | Specific expert title + narrow domain in first paragraph |
| Workflow | Numbered steps, imperative one-liners, one action each |
| Gotchas | Non-obvious domain facts — not generic advice |
| Output format | Schema or template, not prose |
| Examples | Realistic input, complete output, ≥1 present |
| Token efficiency | Body ≤200 lines, no background bloat |

### Step 4 — Flag Structural Issues
Each flag is a concrete fix for `improve-skills` Step 2b:

- **Over limit** (>200 lines): `split-skill`; `secure-*` → split-only per Step 2c
- **Loader-unsafe**: see Step 2a (P0)
- **Description process-steps**: see Step 2b
- **Missing category**: not in `meta | thinking | project-specific | domain`
- **Missing Impact Report**: no `## Impact Report` section at end
- **Missing file-output logging**: skill writes project files but no `docs/skill-outputs/SKILL-OUTPUTS.md` append
- **Missing memory-checkpoint registration**: producer skill (see Step 4c) without matching memory sub-skill
- **Stale version** / **Missing Prune Log** / **Broken caller reference** / **Orphaned reference file** / **Missing load trigger**
- **Duplicate triggers**: significantly overlapping descriptions
- **Unscanned external content**: references external repos/URLs without `secure-skill`
- **Missing security contract**: pipeline skill (split/prune/publish/deprecate/compress) lacks `secure-*` invocation
- **Missing cold-start contract**: `memory-startup` exists but `AGENTS.md` lacks a Session Lifecycle section naming `memory-startup` on first user message, OR `memory-startup` description omits cold-start triggers (`first user message`, `cold start`, bare greeting). Fix: align with `project-setup` template.
- **Missing anti-skip table** (P2): `metadata.category: project-specific` but no `## Common Rationalizations` (or equivalent anti-rationalization section). Fix: add 5–8 row Excuse→Reality table.
- **Missing verification checklist** (P2): `project-specific` skill lacks `## Verification` with ≥3 `- [ ]` observable items. Fix: add checklist tied to project commands where possible.

### Step 4b — Security Sweep
Invoke ALL `secure-*` (discover via `ls .agents/skills/secure-*`) in Mode C. Mandatory — validation without security is incomplete.

### Step 4c — Producer Checkpoint Audit
Read `memory/SKILL.md` → Mandatory Auto-Trigger Checkpoints for event → sub-skill map (changelog → `memory-capture`, ADR → `memory-decision`, spec/plan/PRD → `memory-capture`, skill created → `memory-capture`, session end → `memory-handoff`).

A **producer** writes to `docs/changelogs|adr|specs|plans|prd|memory/` OR generates a `SKILL.md` OR appears in the registry trigger column. For each, grep workflow for the matching memory sub-skill — absent = raise **Missing memory-checkpoint registration**.

### Step 5 — Call Graph
Verify every skill named in `AGENTS.md` Skill Relationships exists in `.agents/skills/`.

### Step 6 — Report

```
Skill Library Health Report | YYYY-MM-DD | Skills: N
VALIDATION: ✓/✗ per skill
LOADER SAFETY (P0): ✗ [skill]: BOM | byte 0 = 0xEF | missing closing --- | desc=1217 chars
DESCRIPTION (P1):   ⚠ [skill]: contains "Step 1… Step 2…" — agent may skip body
SIZE:               ⚠ [skill]: 203 lines (fix: split-skill; secure-* → split-only)
SCORES:             [skill]: 13/14 — [weak criterion]; [skill]: 5/14 — consider deprecate-skill
STRUCTURAL:         [skill]: producer missing memory-checkpoint → memory-decision
CRAFT (P2):         [skill]: missing Common Rationalizations | missing Verification checklist
DUPLICATE TRIGGERS: [skill-A] + [skill-B]: overlap on [phrases]
ACTIONS:
  P0 [skill]: fails agentskills validate
  P1 [skill]: description >1024 chars — move triggers to body
  P1 [skill]: 203 lines — split-skill
  P2 [skill]: score 9/14 — improve-skills
  P3 [skill]: no prune log — prune-skill
```

---

## Gotchas

- Run `agentskills validate` on the **directory**, not the file.
- Duplicate-trigger detection is judgment, not string match.
- Score ≤5/14 → suggest `deprecate-skill`; user decides.
- Step 2b is a regex heuristic — false positives (e.g., quoted "Step 1" inside the description) are acceptable warnings, not P0s.

---

## Common Rationalizations

| "Reason to skip a check" | Reality |
|--------------------------|---------|
| "agentskills CLI isn't installed here" | Run the Step 2a bash checks manually — they cover loader safety without the CLI |
| "secure-* is too long, just compress it once" | Compression removes threat-coverage rows. Step 2c forbids it. Split at 180 |
| "this skill exempts itself in its frontmatter" | Frontmatter exemptions are ignored. Only Step 2c counts |
| "description >1024 chars is fine, my loader handles it" | Others truncate or reject. P0, no exceptions |

---

## Example

<examples>
  <example>
    <input>validate all skills</input>
    <output>
Skill Library Health Report | 2026-04-05 | Skills: 8
VALIDATION: ✓ 8/8 | LOADER SAFETY: ✓ desc ≤1024, no BOM | DESCRIPTION: ✓ no process-steps | SIZE: ✓
SCORES: brainstorming 13/14 (example truncated); prd-writing 12/14 (only 1 gotcha); universal-skill-creator 12/14 (missing "skill engineer" trigger); others 14/14
ACTIONS:
  P2 brainstorming: complete truncated example
  P2 prd-writing: add 2 gotchas
  P3 universal-skill-creator: add trigger
    </output>
  </example>
</examples>

---

## Reference Files

- **`references/validation-rubric.md`**: Full 0/1/2 scoring guide for all 7 criteria. Read when a score is ambiguous.

---

## Impact Report

```
Validation: YYYY-MM-DD | Skills: N | P0: N | P1 desc/size: N | >200 lines: N | Avg score: X/14
Actions: P0: N, P1: N, P2: N, P3: N | No files modified.
```
