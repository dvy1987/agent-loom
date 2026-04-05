---
name: improve-skills
description: >
  Audit, improve, and optionally compress every non-meta skill in the repo.
  Load when the user asks to improve skills, audit the skill library, upgrade
  existing skills, refresh skills with new research, review all skills, do a
  skill health check, or update skills with latest best practices. Also triggers
  on "improve all skills", "update the skill library", "make skills better",
  "skill audit", or "run an improvement pass". Applies live domain research,
  practitioner blogs, and GitHub repo patterns to each skill — same research
  depth as universal-skill-creator — then rewrites the skill body to be more
  effective, and invokes skill-compressor if the result exceeds 200 lines.
  Meta skills (universal-skill-creator, skill-compressor, improve-skills) are
  never modified by this skill.
license: MIT
metadata:
  author: dvy1987
  version: "1.0"
  sources: arXiv:2602.12430, arXiv:2603.29919, agentskills.io best practices
---

# Improve Skills

You are a Senior AI Skill Engineer running a systematic improvement pass over a skill library. For each non-meta skill you audit, research, rewrite, and compress — in that order. The goal is skills that are more effective, not just shorter. Compression without improved quality is failure.

## Meta Skill Exemption

**Never modify:** `universal-skill-creator`, `skill-compressor`, `improve-skills` (this skill).
If the user asks you to improve a meta skill, explain the exemption and skip it.

---

## Workflow

### Step 1 — Discover All Non-Meta Skills

```bash
ls .agents/skills/
```

Build the work queue: every directory except `universal-skill-creator`, `skill-compressor`, `improve-skills`.

Report the queue before starting:
```
Skills to improve: brainstorming, prd-writing, [others...]
Meta skills (skipping): universal-skill-creator, skill-compressor, improve-skills
```

Ask the user: "Improve all of these, or specific ones?" Proceed once confirmed.

---

### Step 2 — For Each Skill, Run the Full Improvement Cycle

Process one skill at a time. For each skill:

#### 2a — Baseline Audit

Read the skill's `SKILL.md` and score it against these criteria:

| Criterion | Question | Score |
|-----------|----------|-------|
| Routing | Does the description contain rich trigger keywords? | 0–2 |
| Role definition | Is the expert role specific and narrow? | 0–2 |
| Workflow | Are steps numbered, imperative, one-action-each? | 0–2 |
| Gotchas | Are there non-obvious domain facts the agent needs? | 0–2 |
| Output format | Is there a schema or template (not prose)? | 0–2 |
| Examples | Are examples realistic and complete (not truncated)? | 0–2 |
| Token efficiency | Is 60%+ of the body actionable (not background)? | 0–2 |

Maximum score: 14. Report score before improving.

#### 2b — Live Domain Research

Same research protocol as `universal-skill-creator` Step 2. Do not skip this — the improvement is only as good as the research backing it.

Search in parallel:

**1. Academic / Research papers**
Search: `[skill-domain] best practices 2025 2026`, `[skill-domain] LLM workflow arxiv`, `[skill-domain] agent automation research`
- Extract: empirical workflow findings, documented failure modes, anti-patterns

**2. Practitioner blogs and articles**
Search: `[skill-domain] best practices expert guide`, `[skill-domain] workflow tips 2025`, `[skill-domain] common mistakes`
- Target: engineering blogs (Vercel, Linear, Stripe, Shopify), Substack, HN top posts, dev.to
- Extract: specific gotchas, non-obvious steps, conventions the agent won't know from training

**3. GitHub skill repos**
Search: `SKILL.md [skill-domain]` on GitHub, check `anthropics/skills`, `openai/skills`, `warpdotdev/oz-skills`, `VoltAgent/awesome-agent-skills`
- Extract: trigger phrases that work, gotchas in existing skills, structural patterns
- Note: what existing skills get right and what they're missing

Document findings before rewriting:
```
Research for [skill-name]:
- [Source]: [specific finding]
- [Source]: [specific finding]
New gotchas found: [list]
Workflow improvements identified: [list]
```

#### 2c — Classify Existing Content (SkillReducer Taxonomy)

Tag every block of the current skill body:

| Tag | Destination |
|-----|-------------|
| `CORE` — hard gates, MUST/NEVER rules, gotchas | Keep in SKILL.md |
| `WORKFLOW` — numbered steps | Keep, compress to one-liners |
| `FORMAT` — output schema or template | Keep |
| `EXAMPLE` — input → output pairs | Keep 1–2 shortest, rest → `references/examples.md` |
| `BACKGROUND` — rationale, "why", verbose context | Move → `references/background.md` |
| `EDGE_CASE` — applies to <20% of invocations | Move → `references/edge-cases.md` |
| `DUPLICATE` — already stated elsewhere | Delete |
| `STALE` — contradicts current research findings | Replace with researched version |

#### 2d — Rewrite the Skill

Apply improvements in this priority order:

1. **Fix routing first.** If the description doesn't trigger on common user phrases, rewrite it. Test mentally against 5 real user prompts. The description is always-loaded — it has the highest ROI.

2. **Add gotchas from research.** Every non-obvious fact discovered in Step 2b that isn't already in the skill goes into a `## Gotchas` section. These must stay in the body, not references/.

3. **Sharpen the workflow.** Replace vague steps ("think through the requirements") with imperative one-liners ("ask one clarifying question per message, wait for answer"). Apply rule-based patterns: MUST/NEVER over soft suggestions.

4. **Replace generic examples with better ones.** Per NeurIPS 2025: real, domain-specific examples outperform generic ones. If the existing examples feel synthetic, rewrite with realistic inputs and complete outputs.

5. **Add or tighten the output format.** If the skill describes output in prose, replace with a concrete schema or template the agent can pattern-match against.

6. **Move BACKGROUND and EDGE_CASE to references/.** For each moved block, write a specific load trigger in the body: "Read `references/edge-cases.md` if the user mentions [X]." Generic "see references/ for more" is not acceptable.

7. **Bump version** in frontmatter metadata.

#### 2e — Post-Rewrite Score

Re-score against the same 7 criteria. Report:
```
[skill-name]: 8/14 → 13/14
Improvements made:
- Added 3 gotchas from [source]
- Replaced vague step 2 with imperative one-liner
- Rewrote description — added 4 trigger phrases
- Moved 2 background sections to references/
```

#### 2f — Compression Check

```bash
wc -l .agents/skills/<skill-name>/SKILL.md
```

If over 200 lines: invoke `skill-compressor` on the skill before committing.
If under 200 lines: validate and commit directly.

#### 2g — Validate and Commit

```bash
agentskills validate .agents/skills/<skill-name>/
```

Must pass. Then commit:
```bash
git add .agents/skills/<skill-name>/
git commit -m "improve: <skill-name> — score <before>/14 → <after>/14

- [improvement 1]
- [improvement 2]
- [improvement 3]
Sources: [source 1], [source 2]"
```

---

### Step 3 — Library Summary Report

After processing all skills, report:

```
Skill Library Improvement Summary
==================================
Skills improved: N
Meta skills skipped: universal-skill-creator, skill-compressor, improve-skills

Results:
  brainstorming:  10/14 → 13/14  (+3)  148 lines
  prd-writing:    9/14  → 12/14  (+3)  176 lines
  [others]

Top improvements across library:
- [Pattern 1 — e.g., "Added gotchas sections to 3 skills"]
- [Pattern 2]

Research sources used:
- [Source 1] — applied to [skill]
- [Source 2] — applied to [skill]
```

---

## Gotchas

- **Never compress before improving.** Compressing a weak skill just makes it a smaller weak skill. Always improve first, compress second.
- **Never move gotchas to references/.** Gotchas must be in the body — the agent reads them before encountering the situation, not after deciding to look.
- **Description rewrites must preserve all existing trigger phrases.** Adding new ones is fine. Removing working ones breaks routing for existing users.
- **Score honestly before and after.** The point isn't to report a high score — it's to identify what actually needs fixing.

---

## Example

<examples>
  <example>
    <input>Improve all skills in the repo</input>
    <output>
Skills to improve: brainstorming, prd-writing
Meta skills (skipping): universal-skill-creator, skill-compressor, improve-skills

Confirm improvement pass on: brainstorming, prd-writing?

[After confirmation]

--- brainstorming (1/2) ---
Baseline score: 10/14
  Routing: 2/2 ✓
  Role definition: 2/2 ✓
  Workflow: 1/2 — steps have prose explanations, not one-liners
  Gotchas: 1/2 — only 1 gotcha, research suggests 3 more
  Output format: 2/2 ✓
  Examples: 1/2 — example output truncated
  Token efficiency: 1/2 — 35% background content

Research for brainstorming:
- obra/superpowers (GitHub): "One question per message" is the most cited failure mode
- HN discussion 2025: LLM brainstorming sessions fail when agent proposes solutions before understanding constraints
New gotchas found: agents skip scope check for "simple" requests; agents merge approach selection with design presentation
Workflow improvements: compress 8 prose paragraphs to imperative one-liners

Rewriting... [produces improved SKILL.md]

Post-rewrite score: 13/14
  Workflow: 2/2 ✓ — all steps are imperative one-liners
  Gotchas: 2/2 ✓ — 3 new gotchas added
  Token efficiency: 2/2 ✓ — moved 2 background sections to references/
  Examples: 1/2 — kept 1 complete example, added note to references/

148 lines — under 200, no compression needed.
agentskills validate: ✓
Committed: improve: brainstorming — 10/14 → 13/14
    </output>
  </example>
</examples>

---

## Reference Files

- **`references/scoring-rubric.md`**: Full scoring rubric with examples of 0, 1, and 2 scores for each criterion. Read when scoring is ambiguous.
- **`references/research-papers.md`** (in `universal-skill-creator/`): State-of-the-art research backing the improvement criteria. Read for architectural decisions.
