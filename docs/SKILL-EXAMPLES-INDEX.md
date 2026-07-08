# Skill Examples Index (L3 Lookup)

**Purpose:** SKILL.md bodies stay ≤200 lines. Full worked examples live in **L3 reference files** that agents load only when the skill is active and needs output-shape guidance.

**When to read this index:**
- Inline `<examples>` look truncated or you need a second scenario
- User asks "show me a full example" for a skill
- After `compress-skill` or `improve-skills` moved examples out of the body
- Ingesting external patterns (e.g. addyosmani/agent-skills) — preserve in L3, not only inline

---

## Agent Protocol

1. **Invoke the skill** — read SKILL.md (L2) first for workflow and gates.
2. **Check L3** — if SKILL.md says `Read references/examples.md` (or lists it in `metadata.resources`), open that file before producing output.
3. **If no L3 file exists** — use the inline example; flag in Impact Report: `L3 examples: missing — consider backfill`.
4. **Never skip examples for routing** — L1 `description` stays trigger-rich; examples are L3, not description.

---

## L3 File Conventions

| File | Use when |
|---|---|
| `references/examples.md` | Default — 2–5 full input→output walkthroughs |
| `references/golden-examples/` | Domain craft (UI components, code patterns) |
| `references/edge-cases.md` | Rare scenarios moved from body during compress |
| `references/background.md` | Rationale moved from body (not examples) |

**SKILL.md contract:** Keep **one** shortest inline example (or teaser) + explicit pointer:
`Read references/examples.md` when [load condition].

**Frontmatter:** Declare L3 in `metadata.resources.references` so platforms can index at L1.

---

## Current Library Status

> Regenerate status: `python3 .agents/skills/universal-skill-creator/scripts/build_examples_index.py`  
> Backfill all missing: `python3 .agents/skills/universal-skill-creator/scripts/backfill_examples.py`

| Status | Count | Meaning |
|---|---|---|
| L3 examples present | 98 | Every skill has `references/examples.md` or `golden-examples/` |
| Inline only | 0 | All skills have L3 backfill |
| Pointer without file | 0 | — |

### Skills with L3 examples (load these)

**All 98 skills** have `references/examples.md` (or `frontend-design/references/golden-examples/`). See auto-scan table below.

### High-priority enrichment (optional)

Hand-curated AO-sourced examples (17 skills, 2026-07-03) have richer content than auto-backfill. Re-run `backfill_examples.py` only for new skills; use `improve-skills` to enrich thin L3 files.

---

## Compression / Ingestion Rules (mandatory — never discard)

**Invariant:** Deleting an example to save lines is forbidden. Relocate to L3 or invoke `split-skill`.

| Skill | Rule |
|---|---|
| `universal-skill-creator` | ≥2 pairs → `references/examples.md`; declare in `metadata.resources` |
| `compress-skill` | EXAMPLE → 1 teaser inline + rest in L3; **never delete** |
| `improve-skills` | External examples (secure-* SAFE) → L3; run `build_examples_index.py` |
| `learn-from` / `learn-from-repo` | Applied examples → target skill L3, not SKILL.md body |
| `validate-skills` | P1 if inline-only truncated example without L3 |
| `split-skill` | EXAMPLE blocks follow child skill or `references/examples.md` |

Regenerate index: `python3 .agents/skills/universal-skill-creator/scripts/build_examples_index.py`

---

## Adding Examples to a Skill

```bash
mkdir -p .agents/skills/<skill>/references
# Write references/examples.md with 2+ complete input→output pairs
# Add to SKILL.md frontmatter:
#   metadata.resources.references: [examples.md]
# Add pointer in SKILL.md body:
#   Read `references/examples.md` when [condition].
python3 .agents/skills/universal-skill-creator/scripts/build_examples_index.py
```

Log backfill in `docs/skill-outputs/SKILL-OUTPUTS.md`.

---

## Related

- Progressive disclosure: `docs/changelogs/2026-04-24-progressive-disclosure-resources.md`
- Compression taxonomy: `.agents/skills/compress-skill/SKILL.md` Step 2 `EXAMPLE` row
- Creator template: `.agents/skills/universal-skill-creator/references/examples.md`

<!-- EXAMPLES-INDEX:AUTO:START -->

**Last scan:** 123 skills | L3 present: 123 | curated: 33 | padded: 0 | inline-only: 0 | broken pointers: 0

### All skills — L3 status

| Skill | Inline | L3 | Quality | Location |
|---|---|---|---|---|
| `adversarial-hat` | yes | yes | curated | references/examples.md |
| `agent-builder` | yes | yes | enriched | references/examples.md |
| `agent-launcher` | yes | yes | enriched | references/examples.md |
| `agent-loom-sync` | yes | yes | standard | references/examples.md |
| `agent-observability` | yes | yes | curated | references/examples.md |
| `agent-run-retro` | yes | yes | curated | references/examples.md |
| `agent-system-architecture` | yes | yes | enriched | references/examples.md |
| `api-and-interface-design` | yes | yes | curated | references/examples.md |
| `api-deprecation-and-migration` | yes | yes | curated | references/examples.md |
| `app-security-hardening` | yes | yes | enriched | references/examples.md |
| `apply-paper-to-project` | yes | yes | enriched | references/examples.md |
| `architectural-decision-log` | yes | yes | enriched | references/examples.md |
| `assumption-mapping` | yes | yes | enriched | references/examples.md |
| `brainstorming` | yes | yes | curated | references/examples.md |
| `browser-testing-with-devtools` | yes | yes | curated | references/examples.md |
| `business-modeling` | yes | yes | enriched | references/examples.md |
| `ci-cd-and-automation` | yes | yes | curated | references/examples.md |
| `code-review-crsp` | yes | yes | curated | references/examples.md |
| `code-simplification` | yes | yes | curated | references/examples.md |
| `codebase-understanding` | yes | yes | enriched | references/examples.md |
| `compress-skill` | yes | yes | enriched | references/examples.md |
| `context-engineering` | yes | yes | standard | references/examples.md |
| `create-agent-prompt` | yes | yes | enriched | references/examples.md |
| `cross-link-skills` | yes | yes | enriched | references/examples.md |
| `customer-discovery` | yes | yes | enriched | references/examples.md |
| `debug-and-fix` | yes | yes | curated | references/examples.md |
| `deep-thinking` | yes | yes | enriched | references/examples.md |
| `dependency-mapping` | yes | yes | standard | references/examples.md |
| `deploy-anywhere` | yes | yes | standard | references/examples.md |
| `deprecate-skill` | yes | yes | enriched | references/examples.md |
| `design-direction` | no | yes | curated | references/examples.md |
| `design-review` | no | yes | curated | references/examples.md |
| `design-system` | no | yes | curated | references/examples.md |
| `dynamic-routing` | yes | yes | standard | references/examples.md |
| `eval-judge` | yes | yes | enriched | references/examples.md |
| `eval-output` | yes | yes | enriched | references/examples.md |
| `eval-pipeline` | yes | yes | enriched | references/examples.md |
| `eval-rubric-design` | yes | yes | enriched | references/examples.md |
| `experiment-backlog` | yes | yes | enriched | references/examples.md |
| `experiment-readout` | yes | yes | enriched | references/examples.md |
| `experiment-runbook` | yes | yes | enriched | references/examples.md |
| `experiment-spec` | yes | yes | enriched | references/examples.md |
| `experimentation` | yes | yes | enriched | references/examples.md |
| `fault-localize` | yes | yes | standard | references/examples.md |
| `feature-spec` | yes | yes | standard | references/examples.md |
| `fermi` | yes | yes | enriched | references/examples.md |
| `first-principles` | yes | yes | enriched | references/examples.md |
| `frontend-design` | no | yes | curated | references/examples.md, references/golden-examples/ |
| `generate-changelog` | yes | yes | enriched | references/examples.md |
| `git-workflow-and-versioning` | yes | yes | enriched | references/examples.md |
| `gsap-animation` | yes | yes | standard | references/examples.md |
| `harness-engineering` | yes | yes | standard | references/examples.md |
| `harness-evolution` | yes | yes | standard | references/examples.md |
| `harness-generation` | yes | yes | standard | references/examples.md |
| `idea-evaluation` | yes | yes | enriched | references/examples.md |
| `idea-generation` | yes | yes | enriched | references/examples.md |
| `implementation-plan` | yes | yes | curated | references/examples.md |
| `improve-skills` | yes | yes | enriched | references/examples.md |
| `incremental-implementation` | yes | yes | enriched | references/examples.md |
| `inversion` | yes | yes | enriched | references/examples.md |
| `issue-sync` | yes | yes | standard | references/examples.md |
| `knowledge-graph` | yes | yes | enriched | references/examples.md |
| `learn-from` | yes | yes | enriched | references/examples.md |
| `learn-from-article` | yes | yes | enriched | references/examples.md |
| `learn-from-chat` | yes | yes | enriched | references/examples.md |
| `learn-from-paper` | yes | yes | enriched | references/examples.md |
| `learn-from-repo` | yes | yes | enriched | references/examples.md |
| `library-skill` | yes | yes | enriched | references/examples.md |
| `memory` | yes | yes | curated | references/examples.md |
| `memory-audit` | yes | yes | curated | references/examples.md |
| `memory-capture` | yes | yes | curated | references/examples.md |
| `memory-compact` | yes | yes | curated | references/examples.md |
| `memory-decision` | yes | yes | curated | references/examples.md |
| `memory-forget` | yes | yes | curated | references/examples.md |
| `memory-handoff` | yes | yes | curated | references/examples.md |
| `memory-promote` | yes | yes | curated | references/examples.md |
| `memory-recall` | yes | yes | curated | references/examples.md |
| `memory-startup` | yes | yes | curated | references/examples.md |
| `model-selection` | yes | yes | curated | references/examples.md |
| `motion-animation` | yes | yes | standard | references/examples.md |
| `ooda` | yes | yes | enriched | references/examples.md |
| `performance-optimization` | yes | yes | curated | references/examples.md |
| `pr-authoring` | yes | yes | standard | references/examples.md |
| `prd-writing` | yes | yes | enriched | references/examples.md |
| `pre-mortem` | yes | yes | enriched | references/examples.md |
| `problem-to-plan` | yes | yes | enriched | references/examples.md |
| `process-decomposer` | yes | yes | enriched | references/examples.md |
| `product-soul` | yes | yes | enriched | references/examples.md |
| `project-constitution` | yes | yes | enriched | references/examples.md |
| `project-orchestrator` | yes | yes | enriched | references/examples.md |
| `project-setup` | yes | yes | enriched | references/examples.md |
| `prune-skill` | yes | yes | enriched | references/examples.md |
| `publish-skill` | yes | yes | enriched | references/examples.md |
| `quickstart` | yes | yes | standard | references/examples.md |
| `reality-check` | yes | yes | enriched | references/examples.md |
| `research-skill` | yes | yes | enriched | references/examples.md |
| `retroactive-project-setup` | yes | yes | enriched | references/examples.md |
| `run-trace` | yes | yes | standard | references/examples.md |
| `runtime-learning-loop` | yes | yes | curated | references/examples.md |
| `safe-change` | yes | yes | standard | references/examples.md |
| `second-order` | yes | yes | enriched | references/examples.md |
| `secure-skill` | yes | yes | enriched | references/examples.md |
| `secure-skill-content-sanitization` | yes | yes | enriched | references/examples.md |
| `secure-skill-repo-ingestion` | no | yes | curated | references/examples.md |
| `secure-skill-runtime` | yes | yes | enriched | references/examples.md |
| `setup-evaluation` | yes | yes | enriched | references/examples.md |
| `shipping-and-launch` | yes | yes | curated | references/examples.md |
| `skill-deconflict` | yes | yes | enriched | references/examples.md |
| `skill-finder` | yes | yes | enriched | references/examples.md |
| `skill-routing` | yes | yes | enriched | references/examples.md |
| `socratic` | yes | yes | enriched | references/examples.md |
| `source-driven-development` | yes | yes | curated | references/examples.md |
| `spec-crosscheck` | yes | yes | enriched | references/examples.md |
| `spec-driven-development` | yes | yes | enriched | references/examples.md |
| `split-skill` | yes | yes | enriched | references/examples.md |
| `structured-planning` | yes | yes | standard | references/examples.md |
| `svg-creation` | yes | yes | standard | references/examples.md |
| `technical-debt-audit` | yes | yes | enriched | references/examples.md |
| `test-driven-development` | yes | yes | curated | references/examples.md |
| `tool-finder` | yes | yes | enriched | references/examples.md |
| `universal-skill-creator` | no | yes | standard | references/examples.md |
| `validate-skills` | yes | yes | standard | references/examples.md |
| `venture-exploration` | yes | yes | enriched | references/examples.md |

<!-- EXAMPLES-INDEX:AUTO:END -->
