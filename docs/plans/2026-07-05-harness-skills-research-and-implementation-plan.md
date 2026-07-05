# Harness Skills — Research Digest & Implementation Plan

**Date:** 2026-07-05  
**Status:** Approved for execution (research saved; build not started)  
**Author:** agent session (user-directed research)  
**Scope:** Add harness-generation and harness-evolution capabilities to agent-loom; wire them into project lifecycle at the correct stages.

---

## Executive summary

A **harness** is the executable scaffold around a model — prompts, tools, memory, orchestration, sandboxes, verification, and governance. **Self-improving harnesses** close the loop: execute → capture traces → diagnose failure layer → propose bounded edits → regression-validate → promote or reject.

agent-loom today bootstraps projects (`project-setup`, `retroactive-project-setup`) and routes work (`project-orchestrator`) but does **not** generate harness artifacts as a first-class concern, nor evolve them. `reality-check` and `setup-evaluation` already flag missing eval harnesses as a credibility gap.

**Recommended deliverable:** a **3-skill suite** created only via `universal-skill-creator`:

| Skill | Job |
|-------|-----|
| `harness-generation` | Seed minimal harness v0 from repo context (AGENTS.md, skills, tools, eval interface, governance) |
| `harness-evolution` | Observe → diagnose → propose → regression-gate → promote harness vN+1 |
| `harness-engineering` | Orchestrator — routes “build/improve my harness” to generation vs evolution |

**Build order:** learn-from papers + repos → design ADR → create child skills → create orchestrator → patch 8 existing skills → library sync.

---

## Part 1 — Research digest

### 1.1 What “harness” means (2026 consensus)

| Layer | Examples | Failure when missing |
|-------|----------|----------------------|
| **Execution** | sandbox, terminal, filesystem, isolation | agent can't verify its own work |
| **Tools** | MCP, APIs, skill registry | model hallucinates capabilities |
| **Context** | AGENTS.md, memory, retrieval, compaction | wrong or stale ground truth |
| **Lifecycle** | session start/end, hooks, handoffs | context rot between sessions |
| **Orchestration** | routing, subagents, parallelism | wrong skill or duplicate work |
| **Verification** | eval harness, regression gates | self-improvement unfalsifiable |
| **Governance** | permissions, forbidden paths, audit | unsafe or irreversible actions |

HarnessFix (arXiv:2606.06324) names these **ETCLOVG** layers — a useful diagnosis taxonomy for `harness-evolution`.

### 1.2 Unified self-improvement loop (all major 2026 work)

```
Minimal seed harness (v0)
    → execute on task set
    → capture traces + scores
    → diagnose failure layer (which ETCLOVG component?)
    → propose minimal bounded edit
    → regression validate (held-out set)
    → accept → promote vN+1  |  reject → revise diagnosis
```

Every credible system adds at least one of:

- **Component observability** — harness files git-tracked, revertible (AHE)
- **Experience observability** — trace distillation, not raw 10M tokens (AHE, Meta-Harness)
- **Decision observability** — edit predicts impact; next round falsifies (AHE)
- **Regression gates** — held-out tasks never used for proposal (Self-Harness, HarnessFix, RHO)

### 1.3 Top 5 repos (generation + self-improvement)

Ranked for harness **scaffolding** and/or **evolution loops**, not stars alone.

#### 1. [ruvnet/agent-harness-generator](https://github.com/ruvnet/agent-harness-generator) — MetaHarness factory

- **Role:** Generate a full branded harness from a GitHub URL or blank slate.
- **Output:** npm-publishable package — own `npx` CLI, MCP server, memory, governance, witness-signed releases.
- **Learn-from verdict (predicted):** APPLY patterns for factory CLI, release pipeline, governance policy — PARTIAL on npm-specific packaging for agent-loom (library ships skills, not npm CLIs).
- **Maps to:** `harness-generation` references (factory patterns), not wholesale copy.

#### 2. [jcaiagent7143-ui/harnessforge](https://github.com/jcaiagent7143-ui/harnessforge) (~2★, high signal)

- **Role:** `uvx harnessforge init` → deterministic `AGENTS.md`, `SOUL.md`, `TOOLS.md`, `MEMORY.md`, `SKILLS/`, per-IDE adapters in ~3s, fully local.
- **Learn-from verdict (predicted):** APPLY — repo-walker blueprint set, forbidden-path rules, model-neutral ground truth.
- **Maps to:** `harness-generation` core workflow; complements `project-setup` (interview-driven) with deterministic scaffold.

#### 3. [china-qijizhifeng/agentic-harness-engineering](https://github.com/china-qijizhifeng/agentic-harness-engineering) (685★)

- **Role:** Observability-driven harness evolution for coding agents.
- **Mechanism:** 7 orthogonal git-tracked components; `evaluate → analyze → improve`; trace distillation; falsifiable edit predictions.
- **Results:** Terminal-Bench 2 pass@1 69.7% → 77.0%; frozen harness transfers cross-model.
- **Paper:** [arXiv:2604.25850](https://arxiv.org/abs/2604.25850)
- **Learn-from verdict (predicted):** APPLY — component decomposition, three observability pillars, decision contracts.
- **Maps to:** `harness-evolution` primary reference.

#### 4. [neosigmaai/auto-harness](https://github.com/neosigmaai/auto-harness) (520★)

- **Role:** Bring your own agent; mine benchmark failures; iteratively edit harness; regression-gate.
- **Pattern:** Human writes `PROGRAM.md`; agent runs meta-loop. Terminal-Bench 2.0, tau-bench, Harbor/Docker eval backends.
- **Learn-from verdict (predicted):** APPLY — accessible meta-loop, PROGRAM.md directive pattern, regression gates.
- **Maps to:** `harness-evolution` references (practical entry), `harness-engineering` orchestration.

#### 5. [hexo-ai/sia](https://github.com/hexo-ai/sia) (1,956★)

- **Role:** Feedback-Agent co-evolves harness scaffold **and** LoRA weights.
- **Paper:** [arXiv:2605.27276](https://arxiv.org/abs/2605.27276)
- **Learn-from verdict (predicted):** PARTIAL — harness-update loop APPLY; weight-update SKIP for agent-loom (skill library, not model training).
- **Maps to:** `harness-evolution` gotcha: “harness-only vs harness+weights — agent-loom is harness-only.”

#### Runners-up (Phase 1b learn-from, lower priority)

| Repo | Focus | Stars | Predicted verdict |
|------|-------|-------|-------------------|
| [greyhaven-ai/autocontext](https://github.com/greyhaven-ai/autocontext) | Multi-gen eval → playbooks + trace datasets | ~1,230 | PARTIAL — playbook distillation |
| [Darwin-Agent/HarnessX](https://github.com/Darwin-Agent/HarnessX) | Composable foundry + SFT/RL bridge | ~127 | PARTIAL — composition algebra |
| [SuperagenticAI/metaharness](https://github.com/SuperagenticAI/metaharness) | Meta-Harness paper implementation | ~134 | APPLY — filesystem run store, scoped writes |
| [wbopan/retro-harness](https://github.com/wbopan/retro-harness) | RHO official code | ~34 | APPLY — label-free self-preference |
| [sethkarten/continual-harness](https://github.com/sethkarten/continual-harness) | Online mid-episode `evolve_harness` | ~239 | PARTIAL — online vs batch evolution |
| [raphaelchristi/harness-evolver](https://github.com/raphaelchristi/harness-evolver) | Claude Code plugin, worktree isolation | ~34 | PARTIAL — worktree regression pattern |
| [UnicomAI/UniHarness](https://github.com/UnicomAI/UniHarness) | Runtime: agent + computer separation | ~125 | SKIP for skill lib — runtime product, not scaffold |

#### Meta-curators (taxonomy only — no URL embed in skills)

| List | Stars | Use |
|------|-------|-----|
| [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) | 2,712 | Category map, self-improving harness section |
| [Picrew/awesome-agent-harness](https://github.com/Picrew/awesome-agent-harness) | 1,413 | Implementation-first catalog |
| [RyanAlberts/best-of-Agent-Harnesses](https://github.com/RyanAlberts/best-of-Agent-Harnesses) | 240 | Ranked JSON + MCP for harness picking |

Per `learn-from-repo` gotcha: extract taxonomy and workflow patterns only; distill into local `references/` — never embed external URLs in SKILL.md.

### 1.4 Top 5 papers (self-improving harnesses)

#### 1. [Self-Harness](https://arxiv.org/abs/2606.09498) (Jun 2026)

- **Loop:** Weakness Mining → Harness Proposal → Proposal Validation (regression-gated).
- **Key idea:** Agent improves its own harness without stronger external agents.
- **Results:** Terminal-Bench-2 held-out gains up to +21pp across three model families.
- **Skill takeaway:** Minimal seed + model-specific failure mining + bounded auditable edits.

#### 2. [Agentic Harness Engineering (AHE)](https://arxiv.org/abs/2604.25850) (Apr 2026)

- **Loop:** Component + experience + decision observability; every edit is a falsifiable contract.
- **Results:** Beats Codex-CLI; frozen harness generalizes cross-model.
- **Skill takeaway:** File-level harness components + prediction-verification per iteration.

#### 3. [RHO: Retrospective Harness Optimization](https://arxiv.org/abs/2606.05922) (Jun 2026) · [code](https://github.com/wbopan/retro-harness)

- **Loop:** Coreset of past tasks → parallel re-solve → self-validation + self-consistency → pairwise self-preference.
- **Key idea:** No ground-truth labels — fully self-supervised from past trajectories.
- **Results:** SWE-Bench Pro 59% → 78% in one round.
- **Skill takeaway:** Label-free harness improvement when eval sets don't exist in production.

#### 4. [HarnessFix](https://arxiv.org/abs/2606.06324) (Jun 2026)

- **Loop:** Traces → HTIR → attribute failure to harness layer → scoped repair operators → regression acceptance.
- **Results:** +15.2% to +50.0% across SWE-Bench Verified, Terminal-Bench 2, GAIA, AppWorld.
- **Skill takeaway:** Layer-attributed diagnosis before any harness edit (ETCLOVG).

#### 5. [Meta-Harness](https://arxiv.org/abs/2603.28052) (Mar 2026) · [code](https://github.com/stanford-iris-lab/meta-harness)

- **Loop:** Coding-agent proposer navigates filesystem of all prior harness code + scores + full traces (grep/cat, not compressed summaries).
- **Results:** +7.7pp text classification at 4× fewer tokens; beats hand-engineered Terminal-Bench baselines.
- **Skill takeaway:** Harness search history as first-class navigable artifact.

#### Honorable mentions (Phase 1b)

| Paper | ID | Relevance |
|-------|-----|-----------|
| SIA: Harness & Weight Updates | [2605.27276](https://arxiv.org/abs/2605.27276) | Harness+weights co-evolution — PARTIAL for agent-loom |
| Continual Harness | [2605.09998](https://arxiv.org/html/2605.09998) | Online mid-episode adaptation |
| The Last Harness You'll Ever Build | [2604.21003](https://arxiv.org/pdf/2604.21003) | Meta-evolution of the evolution blueprint |
| Live-SWE-agent | [2511.13646](https://arxiv.org/html/2511.13646v3) | Production self-evolving scaffold (2025) |

### 1.5 Gap vs existing agent-loom skills

| Existing skill | What it does | Harness gap |
|----------------|--------------|-------------|
| `project-setup` | Interview → tailored AGENTS.md + Orchestration Map | One-shot bootstrap; no harness artifact checklist or eval interface |
| `retroactive-project-setup` | Infer + backfill AGENTS.md for legacy repos | Same — no harness v0 contract |
| `project-orchestrator` | Route tasks to skills | Doesn't route harness build/improve requests |
| `agent-builder` | Multi-agent topology from process | Designs agents, not harness files/tools/evals |
| `agent-system-architecture` | Orchestration patterns | State management for agents, not harness evolution |
| `setup-evaluation` | Validate decomposition + architecture | Mentions eval harness in rationalizations; no structural check |
| `reality-check` | Claims vs implementation | Flags missing eval harness for self-improvement claims |
| `eval-output` suite | Score outputs | Not wired as harness regression gate |
| `memory-*` suite | Session continuity | Not harness-level self-improvement |

`docs/architecture.md` line 13: *"The repo is not a full agent harness."* — accurate today; this plan adds harness **skills** without turning agent-loom into a runtime harness product.

---

## Part 2 — Proposed skill suite design

### 2.1 Three-skill split (mirrors svg / gsap / motion)

```
harness-engineering (orchestrator)
├── harness-generation     — seed harness v0
└── harness-evolution      — improve harness vN → vN+1
```

**Why three, not one:** Generation (deterministic scaffold from repo) and evolution (trace-driven edit loop) have different triggers, failure modes, and prerequisites. Merging would blow past 200 lines or produce a vague mega-skill.

**Why an orchestrator:** User says "set up my harness" vs "my agent keeps failing on X" — different entry points, same family. Matches `eval-output`, `learn-from`, `frontend-design` patterns.

### 2.2 `harness-generation` — scope sketch

**Triggers:** "generate harness", "scaffold agent harness", "bootstrap harness", "harness from this repo", "AGENTS.md + skills + eval interface"

**Hard rules (from research):**
- Never generate harness without `viewBox`-equivalent contract: declare harness version, component manifest, eval interface path.
- Never skip forbidden-path / governance block.
- Never claim self-improving without pointing to `harness-evolution` + eval harness.
- Seed minimal v0 — evolution adds complexity, not generation.

**Workflow (high level):**
1. Classify delivery context (coding agent product vs skill-library project vs consumer repo).
2. Inventory repo (manifests, existing AGENTS.md, `.agents/skills/`, CI).
3. Emit harness component manifest (7 AHE components adapted for agent-loom).
4. Generate or merge: AGENTS.md blocks, skill routing, eval interface stub, governance.
5. Hand off: if `project-setup` ran → merge; if greenfield → pair with `project-setup`.

**References (L3):** harnessforge blueprint patterns, MetaHarness factory checklist, AHE component list, ETCLOVG layer map.

### 2.3 `harness-evolution` — scope sketch

**Triggers:** "improve harness", "evolve harness", "harness keeps failing", "self-improving harness", "optimize agent scaffold"

**Hard rules:**
- Never propose harness edit without trace evidence.
- Never accept edit without regression gate (held-out tasks).
- Never edit without attributing failure to an ETCLOVG layer.
- Never run evolution round without eval harness (route to `eval-pipeline` / `eval-rubric-design` first).
- Bounded edits only — auditable diffs, revertible files.

**Workflow (high level):**
1. Preconditions: harness vN exists; eval harness exists (or FAIL with setup path).
2. Capture: execution traces from last N runs or benchmark slice.
3. Diagnose: HTIR-style layer attribution (HarnessFix pattern).
4. Propose: 1–3 minimal candidate edits tied to diagnosed failures.
5. Validate: regression on held-out set; accept/reject per Self-Harness rule.
6. Promote: git-tagged harness vN+1; log in `docs/memory/learnings.md` + harness changelog.

**References (L3):** AHE three pillars, RHO self-preference (label-free path), HarnessFix HTIR, Meta-Harness filesystem navigation, auto-harness PROGRAM.md pattern.

### 2.4 `harness-engineering` — orchestrator scope sketch

**Triggers:** "harness engineering", "build/improve harness", "agent harness", "harness setup"

**Routes:**

| User intent | Route |
|-------------|-------|
| New project / no harness artifacts | `harness-generation` (may chain after `project-setup`) |
| Legacy repo / missing infra | `retroactive-project-setup` → `harness-generation` |
| Failures / plateau / "make it better" | `harness-evolution` (requires eval harness) |
| Claims audit / "is it self-improving?" | `reality-check` |
| Agent topology design | `agent-builder` (explicitly NOT harness) |

---

## Part 3 — Lifecycle: when harness skills fire

### 3.1 Project lifecycle map

```
┌─────────────────────────────────────────────────────────────────────────┐
│ GREENFIELD                                                              │
│   project-setup (interview, AGENTS.md)                                  │
│       → harness-generation (harness v0 manifest + eval interface stub)  │
│       → [optional] eval-rubric-design + eval-pipeline for harness evals │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ LEGACY / EXISTING CODE                                                  │
│   retroactive-project-setup (infer, backfill)                           │
│       → harness-generation (gap-fill harness components only)           │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ MULTI-AGENT WORK (orthogonal to harness generation)                     │
│   process-decomposer → agent-builder → setup-evaluation                 │
│   setup-evaluation MUST check: harness artifacts + eval path exist      │
│       → agent-launcher → project-orchestrator                           │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ IMPROVEMENT LOOP (post-bootstrap, recurring)                            │
│   harness-evolution (trace → diagnose → propose → regress → promote)    │
│   Requires: harness vN + eval harness + held-out task set               │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ CREDIBILITY AUDIT                                                       │
│   reality-check — self-improvement claims require eval harness proof    │
└─────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Stage gates (mandatory)

| Stage | Gate | Enforced by |
|-------|------|-------------|
| Bootstrap complete | Harness v0 manifest exists; eval interface stub documented | `harness-generation` verification checklist |
| Agent chain execution | Harness artifacts present; eval path defined | `setup-evaluation` (new checks) |
| Evolution round 1 | Eval harness operational; held-out set defined | `harness-evolution` Step 0 precondition |
| Self-improvement claim | Regression trajectory logged | `reality-check` Step 3 scoring |
| Library release | validate-skills ≥10/14 on all harness skills | `universal-skill-creator` Step 9 |

### 3.3 Explicit non-overlap with agent-builder

| Concern | `agent-builder` | `harness-*` skills |
|---------|-----------------|------------------|
| Unit of design | Agent roles, topology, handoffs | Harness files, tools, prompts, eval interface |
| Input | Process decomposition | Repo context + execution traces |
| Output | `docs/architecture/*-arch.md` | Harness component manifest + versioned artifacts |
| When | Multi-step agent-chain tasks | Project bootstrap + ongoing improvement |

**Rule for cross-linking:** `agent-builder` Step 2+ should say: *"Harness artifacts are out of scope — invoke `harness-generation` before setup-evaluation if no harness v0 exists."*

---

## Part 4 — Cross-linking matrix (existing skills to patch)

After the three harness skills exist, patch these skills via `improve-skills TARGET=<skill>` using insights from Phase 1 learn-from runs. Do **not** patch bodies during ingestion — queue per learn-from-repo Step 4b.

| Skill | Patch | Trigger / call site |
|-------|-------|-------------------|
| **`project-setup`** | Add Orchestration Map phase **"Harness bootstrap"**: after AGENTS.md save → invoke `harness-generation` for v0 manifest + eval stub. Add to Step 6 post-save chain. | New project bootstrap |
| **`project-setup` template** | Add optional Harness Bootstrap bullet in Orchestration Map template (`agents-md-template.md`). | Propagates to all new projects |
| **`retroactive-project-setup`** | After AGENTS.md backfill → invoke `harness-generation` in gap-fill mode (only missing components). Add to Step 7 completion chain. | Legacy repos |
| **`project-orchestrator`** | Route table: "harness" / "improve harness" / "agent scaffold" → `harness-engineering`. Never conflate with `agent-builder`. | User intent routing |
| **`agent-builder`** | Hard rule + gotcha: topology ≠ harness; if no harness v0, call `harness-generation` before `setup-evaluation`. | agent-chain path |
| **`setup-evaluation`** | New Step 3b **Harness checks**: (1) harness manifest or AGENTS.md harness section exists, (2) eval interface path documented, (3) for evolution claims, regression gate defined. FAIL with fix path to `harness-generation` or `eval-pipeline`. | Pre-execution gate |
| **`reality-check`** | Expand self-improvement claim scoring: require `docs/harness/` or eval artifacts; link to `harness-evolution` as remediation. | Claim audits |
| **`eval-pipeline`** | Add harness-eval variant: regression suite for harness edits (not just output quality). Cross-call from `harness-evolution` Step 5. | Evolution validation |
| **`eval-rubric-design`** | Add optional dimension set: harness reliability (layer attribution, regression delta, held-out pass rate). | Harness eval design |
| **`AGENTS.md`** (repo root) | User Entry Points: `harness engineering` → `harness-engineering`; `generate harness` → `harness-generation`; `improve harness` → `harness-evolution`. | Discovery |
| **`docs/SKILL-INDEX.md`** | Three entries + call graph edges. | Library sync |
| **`skill-routing`** | Disambiguation: harness-engineering vs project-setup vs agent-builder (ambiguity 6–8 range). | Routing conflicts |

**Deferred (ingest queue only):**
- `memory-capture` / `memory-handoff` — log harness version promotions as producer events (after harness-evolution ships).
- `ci-cd-and-automation` — optional harness regression workflow in consumer projects (Phase 3+).

---

## Part 5 — Implementation plan (skill invocation sequence)

### Phase 0 — Planning ✅

| Step | Skill / action | Output |
|------|----------------|--------|
| 0.1 | User research session | This document |
| 0.2 | Append `docs/skill-outputs/SKILL-OUTPUTS.md` | Log entry |

---

### Phase 1 — Learn-from ingestion (read-only; no SKILL.md writes)

**Global rules for every ingestion:**
- Entry: `learn-from` → sub-skill
- Security: ALL `secure-*` before content informs decisions (`secure-skill-repo-ingestion` mandatory for repos)
- Credibility gate: ≥7/12 or STOP
- No direct SKILL.md edits — insights → `docs/learnings/research-learnings.md` + application plan per insight
- Overlap with existing skills → append `docs/comparisons/INGEST-QUEUE.md`

#### Batch 1A — Foundational papers (sequential; synthesize after)

| Order | Invocation | Source | Expected insights |
|-------|------------|--------|-------------------|
| 1 | `learn-from` → `learn-from-paper` | [Self-Harness 2606.09498](https://arxiv.org/abs/2606.09498) | 3-stage loop, minimal seed, regression acceptance |
| 2 | `learn-from` → `learn-from-paper` | [AHE 2604.25850](https://arxiv.org/abs/2604.25850) | 7 components, 3 observability pillars, falsifiable edits |
| 3 | `learn-from` → `learn-from-paper` | [HarnessFix 2606.06324](https://arxiv.org/abs/2606.06324) | HTIR, ETCLOVG layers, scoped repair operators |
| 4 | `learn-from` → `learn-from-paper` | [Meta-Harness 2603.28052](https://arxiv.org/abs/2603.28052) | Filesystem feedback channel, coding-agent proposer |
| 5 | `learn-from` → `learn-from-paper` | [RHO 2606.05922](https://arxiv.org/abs/2606.05922) | Label-free self-preference, coreset selection |

**After Batch 1A:** Human checkpoint — approve insight application plan before Phase 2.

#### Batch 1B — Secondary papers (parallel OK)

| Invocation | Source | Predicted verdict |
|------------|--------|-------------------|
| `learn-from-paper` | [SIA 2605.27276](https://arxiv.org/abs/2605.27276) | PARTIAL (harness only) |
| `learn-from-paper` | [Continual Harness 2605.09998](https://arxiv.org/html/2605.09998) | PARTIAL (online adaptation) |
| `learn-from-paper` | [Last Harness 2604.21003](https://arxiv.org/pdf/2604.21003) | BACKGROUND / meta-evolution reference |

#### Batch 2A — Generation repos (parallel OK)

| Invocation | Repo | Focus extraction |
|------------|------|------------------|
| `learn-from-repo` | `jcaiagent7143-ui/harnessforge` | Blueprint set, repo walker, forbidden paths |
| `learn-from-repo` | `ruvnet/agent-harness-generator` | Factory output contract, governance, release |
| `learn-from-repo` | `Darwin-Agent/HarnessX` | Composition dimensions, processor pipeline |

#### Batch 2B — Evolution repos (parallel OK)

| Invocation | Repo | Focus extraction |
|------------|------|------------------|
| `learn-from-repo` | `china-qijizhifeng/agentic-harness-engineering` | NexAU component split, evolve agent loop |
| `learn-from-repo` | `neosigmaai/auto-harness` | PROGRAM.md, failure mining, regression gates |
| `learn-from-repo` | `wbopan/retro-harness` | RHO implementation, self-preference selection |

#### Batch 2C — Runners-up (parallel OK; lower priority)

| Invocation | Repo |
|------------|------|
| `learn-from-repo` | `SuperagenticAI/metaharness` |
| `learn-from-repo` | `greyhaven-ai/autocontext` |
| `learn-from-repo` | `sethkarten/continual-harness` |
| `learn-from-repo` | `raphaelchristi/harness-evolver` |

#### Batch 3 — Curator taxonomy (PARTIAL only)

| Invocation | Repo | Rule |
|------------|------|------|
| `learn-from-repo` | `ai-boost/awesome-harness-engineering` | Taxonomy + category names only; no URL embed |
| `learn-from-repo` | `RyanAlberts/best-of-Agent-Harnesses` | Capability tags + ranking axes for references |

**Phase 1 deliverables:**
- `docs/learnings/research-learnings.md` — new section `2026-07-05 harness-engineering`
- `docs/learnings/papers/` — optional per-paper notes (if learn-from-paper produces them)
- `docs/comparisons/INGEST-QUEUE.md` — rows for overlaps with `project-setup`, `setup-evaluation`, `eval-pipeline`
- Synthesis memo: `docs/plans/harness-skill-design-synthesis.md` (create in Phase 2)

**Phase 1 checkpoint:** User approves APPLY/PARTIAL/SKIP matrix before any skill creation.

---

### Phase 2 — Design & deconflict (pre-build)

| Order | Skill | Purpose |
|-------|-------|---------|
| 2.1 | `process-decomposer` | Decompose "build harness skill suite" into ordered steps with parallelism markers |
| 2.2 | `architectural-decision-log` | ADR: 3-skill split vs monolith; harness-only vs harness+weights; eval harness as hard gate |
| 2.3 | `skill-finder` | Confirm no existing skill covers harness generation/evolution |
| 2.4 | `skill-deconflict` | Pre-flight trigger/name check for `harness-generation`, `harness-evolution`, `harness-engineering` |
| 2.5 | Human review | Approve ADR + synthesis memo |

---

### Phase 3 — Skill creation (strict order)

**Invariant:** Every skill via `universal-skill-creator` only. Each creation runs the full Step 1–11 chain.

| Order | Skill invoked | Creates | Notes |
|-------|---------------|---------|-------|
| 3.1 | `universal-skill-creator` | `harness-generation` | Step 2: `research-skill` on harness scaffold domain; L3 refs from Batch 2A |
| 3.2 | `universal-skill-creator` | `harness-evolution` | Step 2: research-skill; L3 refs from Batch 1A + 2B; calls `eval-pipeline` in workflow |
| 3.3 | `universal-skill-creator` | `harness-engineering` | Orchestrator; calls generation + evolution; routes away from `agent-builder` |
| 3.4 | `cross-link-skills` | — | Trigger: `created — harness-engineering` (repairs all three + downstream) |
| 3.5 | `validate-skills` | — | Full library or at minimum all harness skills ≥10/14 |

**Per-skill creator chain (automatic):**
```
universal-skill-creator
  → research-skill (Step 2, secure-* on inputs)
  → skill-deconflict (Step 8)
  → validate-skills + secure-* on output (Step 9)
  → cross-link-skills (Step 10)
  → library-skill (Step 11) — run once after all three exist
  → memory-capture (Step 13)
```

---

### Phase 4 — Patch existing skills (post-create)

Use `improve-skills TARGET=<skill>` for each row in §4 cross-link matrix. One target per run to keep diffs reviewable.

**Recommended patch order:**

1. `setup-evaluation` — harness checks (highest leverage gate)
2. `project-setup` + template — bootstrap chain
3. `retroactive-project-setup` — legacy chain
4. `project-orchestrator` — routing table
5. `agent-builder` — scope boundary
6. `reality-check` — claim scoring
7. `eval-pipeline` + `eval-rubric-design` — harness eval variant
8. `skill-routing` — disambiguation

**Each patch cycle:**
```
improve-skills TARGET=<skill>
  → [edits from approved learn-from insights]
  → secure-* on modified skill
  → validate-skills ≥10/14
  → wc -l ≤200 (compress-skill if needed)
```

**After all patches:**
- `cross-link-skills` — trigger: `improve cycle complete — harness suite`
- `library-skill` — final sync (AGENTS.md, SKILL-INDEX, README, architecture.md)

---

### Phase 5 — Verification & memory

| Order | Skill | Purpose |
|-------|-------|---------|
| 5.1 | `validate-skills` | Library-wide sweep |
| 5.2 | `reality-check` | Re-score "self-improving" claim for agent-loom after harness skills land |
| 5.3 | `setup-evaluation` | Dry-run against a fixture architecture spec with harness checks |
| 5.4 | `generate-changelog` | MINOR: harness skill suite |
| 5.5 | `memory-capture` + `memory-handoff` | Session end; handoff for first real harness-evolution exercise |
| 5.6 | `memory-decision` | Record ADR outcome if not already in `docs/adr/` |

---

## Part 6 — Eval harness requirement (cross-cutting)

Self-improving harness research is unanimous: **no regression gate = no credible evolution.**

agent-loom already has `eval-output` → `eval-rubric-design` | `eval-judge` | `eval-pipeline`. The plan wires them as **hard prerequisites** for `harness-evolution`:

| When | Skill chain |
|------|-------------|
| First-time harness bootstrap | `harness-generation` emits eval interface **stub** → user or agent fills via `eval-rubric-design` |
| Before evolution round 1 | `harness-evolution` Step 0: verify eval harness exists; else route `eval-pipeline` |
| During evolution | `eval-pipeline` runs held-out regression; results feed accept/reject |
| Claim audit | `reality-check` scores self-improvement against eval trajectory |

**Minimum viable harness eval (from papers):**
- Held-out task set (never used for proposal)
- Deterministic checks where possible (pass/fail gates)
- LLM-as-judge only for dimensions without deterministic oracles
- Per-edit delta logged (decision observability — AHE)

This directly addresses `docs/2026-04-13-vc-due-diligence-findings.md` Phase 3 "Eval harness with rubric-graded LLM scoring."

---

## Part 7 — Risk register

| Risk | Mitigation |
|------|------------|
| Skill sprawl / trigger overlap with `project-setup` | `skill-deconflict` pre-flight; orchestrator routes by intent |
| SKILL.md >200 lines | L3 references for loops, HTIR, examples; compress-skill if needed |
| External URL rot in skills | learn-from-repo rule: distill patterns locally, no URL embed |
| Repo code execution during learn-from | Read-only ingestion; never run untrusted harness repos |
| Self-improvement theater | `harness-evolution` hard-fails without eval harness |
| Consumer vs library origin | `metadata.origin: project-local` only in consumer repos; omit in agent-loom |
| Partial paper replication | Preprints flagged; APPLY only after credibility ≥7/12 |

---

## Part 8 — Execution checklist (copy for session tracking)

```
Phase 1 — Learn-from
[ ] Batch 1A: 5 foundational papers (learn-from-paper)
[ ] Batch 1B: 3 secondary papers
[ ] Batch 2A: 3 generation repos (learn-from-repo)
[ ] Batch 2B: 3 evolution repos
[ ] Batch 2C: 4 runner-up repos
[ ] Batch 3: 2 curator lists (taxonomy only)
[ ] research-learnings.md updated
[ ] INGEST-QUEUE.md updated
[ ] User approved APPLY matrix

Phase 2 — Design
[ ] process-decomposer output saved
[ ] ADR written
[ ] skill-finder + skill-deconflict pre-flight PASS

Phase 3 — Create
[ ] harness-generation (universal-skill-creator)
[ ] harness-evolution (universal-skill-creator)
[ ] harness-engineering (universal-skill-creator)
[ ] cross-link-skills (harness suite)
[ ] library-skill sync

Phase 4 — Patch
[ ] setup-evaluation harness checks
[ ] project-setup + template chain
[ ] retroactive-project-setup chain
[ ] project-orchestrator routing
[ ] agent-builder scope boundary
[ ] reality-check claim wiring
[ ] eval-pipeline + eval-rubric-design harness variant
[ ] skill-routing disambiguation

Phase 5 — Close
[ ] validate-skills library sweep
[ ] reality-check re-score
[ ] generate-changelog
[ ] memory-handoff
```

---

## Part 9 — Quick reference: skill call graph (target state)

```
User: "set up project"
  → project-setup
      → harness-generation (v0)
      → [optional] eval-rubric-design → eval-pipeline

User: "backfill legacy repo"
  → retroactive-project-setup
      → harness-generation (gap-fill)

User: "design multi-agent system"
  → process-decomposer → agent-builder
      → harness-generation (if no v0)
      → setup-evaluation (harness + eval checks)
          → PASS → agent-launcher → project-orchestrator

User: "improve my harness" / "agent keeps failing"
  → harness-engineering
      → harness-evolution
          → eval-pipeline (regression)
          → memory-capture (on promote)

User: "is this self-improving?"
  → reality-check
      → [gap] harness-evolution + eval-pipeline

User: "learn from harness paper/repo"
  → learn-from → learn-from-paper | learn-from-repo
      → [approved] improve-skills | universal-skill-creator
```

---

## Appendix A — Resource URL index

### Papers
- Self-Harness: https://arxiv.org/abs/2606.09498
- AHE: https://arxiv.org/abs/2604.25850
- RHO: https://arxiv.org/abs/2606.05922
- HarnessFix: https://arxiv.org/abs/2606.06324
- Meta-Harness: https://arxiv.org/abs/2603.28052
- SIA: https://arxiv.org/abs/2605.27276
- Continual Harness: https://arxiv.org/html/2605.09998
- Last Harness: https://arxiv.org/pdf/2604.21003
- Live-SWE-agent: https://arxiv.org/html/2511.13646v3

### Repos
- agent-harness-generator: https://github.com/ruvnet/agent-harness-generator
- harnessforge: https://github.com/jcaiagent7143-ui/harnessforge
- agentic-harness-engineering: https://github.com/china-qijizhifeng/agentic-harness-engineering
- auto-harness: https://github.com/neosigmaai/auto-harness
- sia: https://github.com/hexo-ai/sia
- HarnessX: https://github.com/Darwin-Agent/HarnessX
- metaharness: https://github.com/SuperagenticAI/metaharness
- retro-harness: https://github.com/wbopan/retro-harness
- continual-harness: https://github.com/sethkarten/continual-harness
- autocontext: https://github.com/greyhaven-ai/autocontext
- harness-evolver: https://github.com/raphaelchristi/harness-evolver
- awesome-harness-engineering: https://github.com/ai-boost/awesome-harness-engineering
- awesome-agent-harness: https://github.com/Picrew/awesome-agent-harness
- best-of-Agent-Harnesses: https://github.com/RyanAlberts/best-of-Agent-Harnesses
- meta-harness (Stanford): https://github.com/stanford-iris-lab/meta-harness

### Internal
- VC due diligence (eval harness gap): `docs/2026-04-13-vc-due-diligence-findings.md`
- Roadmap Phase 3 eval: `docs/2026-04-13-roadmap-and-implementation-plan.md`
- Architecture boundary: `docs/architecture.md`
