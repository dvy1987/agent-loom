# Research Learnings

This file stores reusable learnings captured from external sources such as papers, repositories, and articles.

Use one dated entry per learning. Keep entries concise and action-oriented so they can later be turned into skill updates or new skills. When a new skill is created from an entry here, update that same entry instead of creating a separate note.

Template:

```markdown
## YYYY-MM-DD - One-line summary
- Source:
- Type: paper | repo | article
- Credibility:
- Security:
- Classification:
- Insight:
- Recommended action:
- Skills modified:
- Skills created from this learning: none yet
- Notes:
```

## 2026-04-20 - AlphaEval: Production agent evaluation reveals scaffold dominance, value-score disconnect, and cascade fragility
- Source: Lu, Xu, Zhang et al. (2026). "AlphaEval: Evaluating Agents in Production". arXiv preprint.
- Type: paper
- Credibility: 8/12 (PASS — Moderate). Breakdown:
    - Author expertise: 2/2 — large team including Pengfei Liu (established NLP researcher)
    - Publication venue: 1/2 — arXiv preprint, no peer review yet
    - Evidence type: 2/2 — production data from 94 tasks across 7 companies
    - Reproducibility: 1/2 — benchmark described but dataset not publicly released
    - Recency: 2/2 — 2026, current models and scaffolds
    - Cross-reference: 0/2 — no independent replication at time of ingestion
- Security: SAFE (local PDF, text-only, no executable content)
- Classification: GOTCHA × 3, FAILURE_MODE × 5, TECHNIQUE × 2, METRIC × 2
- Insights:
  - GOTCHA: Scaffold choice is a first-order performance driver — same model (Opus 4.6) varies 11+ points across scaffolds (Claude Code 64.41 vs Codex 53.45)
  - GOTCHA: High aggregate scores ≠ high economic value — Gemini 3 Pro delivers more USD value than higher-scoring configs because it wins on high-value domains
  - GOTCHA: Search persistence is elicitable via scaffold strategy, not a fixed model property (GPT-5.2: 0.0 via Claude Code, 0.4 via Codex on same task)
  - FAILURE_MODE: Cascade dependency — early-stage errors invalidate all downstream steps. #1 pipeline killer.
  - FAILURE_MODE: Cross-section logical inconsistency — contradictory statements within long-form deliverables (e.g., different market sizes on different pages)
  - FAILURE_MODE: Constraint misinterpretation — agents optimize explicit goals while violating implicit domain-specific constraints
  - FAILURE_MODE: Format compliance failure — correct analysis fails because output format is incompatible with downstream systems
  - FAILURE_MODE: Synergy blindness — agents optimize components independently, producing 26% cost overruns vs jointly optimal solutions
  - TECHNIQUE: Compose multiple evaluation paradigms per task (avg 2.8 per task) — no single paradigm sufficient
  - TECHNIQUE: Requirement-to-benchmark framework (4 stages: partner engagement → requirement elicitation → task formalization → iterative evaluation)
  - METRIC: Best agent config achieves only 64.41/100 on production tasks (Claude Code + Opus 4.6)
  - METRIC: IR failure breakdown — hallucinations 30%, imprecise retrieval 35%, positive-info bias 10%
- Recommended action: Apply 8 skill improvements (see below)
- Skills modified: eval-rubric-design (×2), eval-judge, eval-pipeline, agent-builder (×2), process-decomposer, reality-check
- Skills created from this learning: none
- Notes: Format compliance finding validates existing eval-rubric-design hard gate. Multi-paradigm composition finding validates existing eval-pipeline 3-layer approach. Both KEEP CURRENT.

## 2026-07-03 - awesome-ui: ethics + UX heuristics gap in design suite; no link imports
- Source: kevindeasis/awesome-ui (Markdown awesome list). Credibility 7/12 BORDERLINE.
- Type: repo
- Security: SAFE
- Classification: GOTCHA × 1, TECHNIQUE × 3, FAILURE_MODE × 1, BACKGROUND × 2, SKIP × 3
- Insight: Design review lacked ethical-pattern and UX-heuristic gates; direction lacked pre-build context capture. Awesome-list links rot — patterns only, no URL embedding.
- Recommended action: Applied — design-review v2.1 (ethical-patterns.md, ux-heuristics.md), design-direction v1.1 (ux-context-checklist.md), learn-from-repo gotcha on link imports.
- Skills modified: design-review, design-direction, learn-from-repo
- Skills created from this learning: none
- Notes: Erik Kennedy 7-rules and text-over-image kept current (already stronger). Tool/inspiration link directories skipped per security policy.

## 2026-07-03 - graphify: native knowledge-graph skill + consumer integration
- Source: safishamsi/graphify (Python CLI + agent skill). Credibility 11/12 PASS.
- Type: repo
- Security: SAFE (patterns extracted; no vendored graphify pip install)
- Classification: GOTCHA × 2, TECHNIQUE × 4, FAILURE_MODE × 2
- Insight: Query-before-rebuild, EXTRACTED/INFERRED labeling, corpus gates, shrink guard, handoff-sync graph — implemented as native stdlib `knowledge-graph` skill.
- Recommended action: Applied — new `knowledge-graph` skill; wired to memory-handoff, memory-startup, memory-recall, codebase-understanding, context-engineering, debug-and-fix; graphify learnings in memory-capture/compact.
- Skills modified: knowledge-graph (new), memory-handoff, memory, memory-startup, memory-recall, codebase-understanding, context-engineering, debug-and-fix, memory-capture, memory-compact, learn-from-repo (prior)
- Skills created from this learning: knowledge-graph
- Notes: User declined external Graphify install; graph at `docs/knowledge-graph/graph.json`.

## 2026-07-03 - graphify: knowledge-graph v2 gap fixes
- Source: safishamsi/graphify patterns + adversarial review of v1 graph
- Type: repo (patterns only)
- Classification: TECHNIQUE × 6, FAILURE_MODE × 3, GOTCHA × 2
- Insight: v1 was ~79% INFERRED noise; v2 ingests authoritative `skill-graph.md` + SKILL-INDEX **Calls:**, real communities, GRAPH_REPORT, call-graph.json, graph_health audit, path/explain query, project-setup bootstrap.
- Recommended action: Applied — knowledge-graph v2.0; wired project-setup, retroactive-project-setup, library-skill, validate-skills Step 4d, cross-link-skills, learn-from confidence rubric.
- Skills modified: knowledge-graph, project-setup, retroactive-project-setup, memory-startup, library-skill, validate-skills, cross-link-skills, learn-from, universal-skill-creator, SKILL-INDEX
- Notes: Dual-mode (skill-library in agent-loom, application in consumer repos). No pip install.

## 2026-07-03 - L3 examples backfill (addyosmani + ingestion skills)
- Source: addyosmani/agent-skills snapshots (secure-* structural scan SAFE 2026-07-03)
- Type: improve-skills mandate
- Insight: Examples were deleted during compress, not relocated; 21 skills now have references/examples.md
- Recommended action: Applied — backfill + never-discard invariant in AGENTS.md, creator, compress, improve, learn-from, validate
- Skills modified: 17 example backfills + 8 policy skills
- Notes: Index at docs/SKILL-EXAMPLES-INDEX.md; regenerate via build_examples_index.py

## 2026-07-04 - Full library L3 examples backfill
- Source: improve-skills mandate (all remaining skills)
- Type: batch backfill via backfill_examples.py
- Insight: 77 skills had inline-only examples; all 98 now have references/examples.md
- Recommended action: Applied — auto-extract inline + workflow synthesis; 17 prior hand-curated AO examples retained
- Skills modified: 77 new L3 files + SKILL.md resource/pointer wiring
- Notes: enrich thin auto-backfills via improve-skills TARGET=<skill> over time

## 2026-07-04 - SVG creation and animation craft from community repos
- Source: supermemoryai/skills svg-animations, seeb4coding/SVG-ORA-Studio, orsinium-labs/svg.py, visioncortex/vtracer (learn-from repo sweep)
- Type: repo
- Credibility: 8/12 (supermemory skill), 6/12 (SVG-ORA prompts), 9/12 (svg.py), 11/12 (vtracer)
- Security: SAFE — patterns distilled; no external URLs embedded in skill body
- Classification: GOTCHA (SMIL vs CSS by delivery context), TECHNIQUE (stroke-dash draw, morph rules), FAILURE_MODE (guessed dash lengths, script in SVG)
- Insight: agent-loom had static svg-craft only; trash animations come from wrong animation tech for context and unmeasured path lengths
- Recommended action: Applied — new `svg-creation` skill with static-craft, animation-craft, ai-svg-prompts, examples L3
- Skills modified: design-system (caller to svg-creation for animated SVG), library docs
- Skills created from this learning: svg-creation (`.agents/skills/svg-creation/`), gsap-animation, motion-animation

### Primary sources (user-named)
| Repo | Verdict | Applied to |
|------|---------|------------|
| supermemoryai/skills `svg-animations` | **APPLY** | `svg-creation` — delivery matrix, recipes, morph/freeze rules |
| visioncortex/vtracer | **PARTIAL** | `svg-tooling.md` — bitmap→vector presets |
| orsinium-labs/svg.py | **SKIP** | `svg-tooling.md` taxonomy row only (Python codegen, not agent markup) |
| willianjusten/awesome-svg | **PARTIAL** | `svg-tooling.md` — category taxonomy, no embedded URLs |
| seeb4coding/SVG-ORA-Studio | **PARTIAL** | `ai-svg-prompts.md` — prompt dimensions + review gate |

### Additional high-signal repos
| Repo | Verdict | Applied to |
|------|---------|------------|
| greensock/GSAP | **APPLY** | `gsap-animation` skill — timelines, ScrollTrigger, SVG plugins |
| motiondivision/motion | **APPLY** | `motion-animation` skill — variants, AnimatePresence, pathLength |
| svg/svgo | **PARTIAL** | `static-craft.md` multipass + prefixIds; `svg-tooling.md` CLI |
| rough-stuff/rough | **PARTIAL** | `svg-tooling.md` — `rough.svg()` API + when to use |
| maxwellito/vivus | **PARTIAL** | `svg-tooling.md` — prerequisites, types, `recalc`, `data-ignore` |
| shshaw/lengthy-svg | **PARTIAL** | `animation-craft.md` — WebKit attribute + `-webkit-keyframes` calc px workaround |
| williamzujkowski/svg-terminal | **PARTIAL** | `github-safe-smil.md` tiered reduced motion; `svg-tooling.md` CLI row |
| BlinkZer0/Ai-Generated-SVG-Examples | **PARTIAL** | `github-safe-smil.md` recipes; `examples.md` Ex.7 typing dots |
| jorisperrenet/VectorMation | **SKIP** | Python time-based codegen — same class as svg.py |
| tympanus.net Codrops SVG Drawing | **SKIP** | Foundational tutorial; techniques already in `animation-craft.md` line-draw |

- Notes: 2026-07-05 runtime split complete; 2026-07-05 lengthy-svg + vivus L3 gaps closed in animation-craft + svg-tooling

## 2026-07-05 - Learn-from batch: 8 additional SVG animation repos
- Source: greensock/GSAP, maxwellito/vivus, shshaw/lengthy-svg, williamzujkowski/svg-terminal, BlinkZer0/Ai-Generated-SVG-Examples, svg/svgo, rough-stuff/rough, jorisperrenet/VectorMation (+ motiondivision/motion already applied)
- Type: repo batch (learn-from-repo)
- Security: SAFE — tutorial/code patterns only; no URLs embedded in skill bodies
- Classification: TECHNIQUE (github-safe SMIL, vivus prereqs, lengthy-svg WebKit keyframes, SVGO multipass), GOTCHA (tiered reduced motion, vivus hidden paths), TOOLING (rough.js, svg-terminal CLI)
- Insight: primary five repos covered core FAILURE_MODEs; additional repos add tooling depth and README-specific recipes
- Recommended action: Applied — `github-safe-smil.md` L3; expanded animation-craft, static-craft, svg-tooling; examples Ex.7–10 + 20-catalog; svg-creation v1.3 polish pass
- Skills modified: svg-creation (v1.2)
- Skills created from this learning: none (depth pass on existing skill)
- Repo verdicts applied:
  - GSAP → already `gsap-animation`
  - motion → already `motion-animation`
  - vivus → PARTIAL applied (`svg-tooling.md` prerequisites + recalc)
  - lengthy-svg → PARTIAL applied (`animation-craft.md` WebKit keyframes)
  - svg-terminal → PARTIAL applied (`github-safe-smil.md` tiered reduced motion + tool row)
  - Ai-Generated-SVG-Examples → PARTIAL applied (`github-safe-smil.md` recipes + examples Ex.7)
  - svgo → PARTIAL applied (`static-craft.md` + `svg-tooling.md`)
  - rough → PARTIAL applied (`svg-tooling.md` API snippet)
  - VectorMation → SKIP (Python codegen)
  - Codrops SVG Drawing → SKIP (superseded by animation-craft line-draw)
