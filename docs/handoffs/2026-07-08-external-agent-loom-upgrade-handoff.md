# External Handoff — agent-loom Upgrade Plan (Phase 1 of 6 done)

**Read this file in full before asking the user anything.** It is written so a
coding agent with zero prior context — a different tool, a different session,
possibly a different AI provider entirely — can resume exactly where the last
session stopped, with no re-derivation needed.

---

## 1. Who the user is (do not re-discover this — act on it immediately)

- **Non-technical, solo PM/founder.** No formal AI-engineering training. Cannot
  parse technical jargon, but can understand the *consequences* of options when
  explained in plain language. Treat this as a hard constraint on every
  explanation you give them, not just a tone preference.
- Builds **AI-heavy consumer and enterprise products**, most of them
  **multi-agent systems**, as a solo operator. Reference projects (siblings of
  this repo, under `../`): `aegis` (a 12-agent Google ADK swarm with
  Arize-Phoenix-based self-improvement — a hackathon submission that is also a
  real product prototype), `prof-photon` (React Native/Expo mobile app),
  `Ember` (local-first Node/pnpm app with its own MCP server).
- **agent-loom is their compensating layer.** It is a portable `.agents/`
  skill library the user copies into every new or existing project, then runs
  `project-setup` (greenfield) or `retroactive-project-setup` (existing code)
  to bootstrap agent behavior for that project. **This copy-paste-then-bootstrap
  workflow is the core product.** Anything you build in agent-loom must work
  after a bare folder copy into a totally different repo — never depend on
  agent-loom-only files.
- The user is running this specific upgrade work **inside the agent-loom repo
  itself** (`/Users/divya/Projects/Building-apps/agent-loom`, branch `main`).

## 2. What this upgrade plan is for

The user described 5 concrete pain points (their own words, paraphrased):
1. They build agentic harnesses and multi-agent systems constantly but don't
   know if they're good, want them to be **self-improving during development**
   (CLI retros: what went well/poorly, ranked hypotheses, small n=1/n=2
   experiments), and don't understand **observability/tracing** at all despite
   suspecting it's important.
2. They have access to several models of different capability/cost (their
   labels: Opus 4.8, Sonnet 5, GLM 5.2, GPT 5.4, GPT 5.5, Cursor Composer 2.5)
   but cheap models get stuck in bad loops on complex tasks and make
   irreversible bad decisions. They want plans that assign the right model
   tier to each module, with a high-intelligence model doing foundational
   design first.
3. Skills in agent-loom aren't reliably invoked inside **Cursor**.
4. agent-loom hasn't ingested learnings from **obra/superpowers** (a ~243k-star
   MIT Claude Code skill library), which the user believes is state of the art.
5. They want spec-driven development (SDD) and test-driven development (TDD)
   wired together, not parallel unconnected systems.

A plan artifact exists in the conversation with **plan_id
`834ff43c-a703-4565-9b8f-2dba210002b0`**, title "Agent-loom upgrade:
triggering, model routing, agentic quality loop, superpowers, SDD×TDD". If
your tool has access to `read_plans`, read that plan in full — it is the
authoritative source. If not, this document reproduces everything needed.

**The user asked to stop after each phase to review token spend.** Do not run
multiple phases in one go without checking in.

## 3. Binding decisions from user clarification (do not re-litigate)

These came from explicit user answers, not agent inference — treat as hard
constraints on Phases 2–6:

1. **Model routing is advisory, not automatic.** Harnesses like Cursor cannot
   switch models mid-run under agent control. Any model-selection skill must
   (a) emit a model-plan table *before* execution begins, and (b) at each
   module/task boundary, announce "next module → use tier X / model Y" so the
   *human* switches manually. Never design a mechanism that assumes the skill
   itself can change the active model.
2. **Observability must not require Arize Phoenix specifically, and must never
   require self-hosting on the user's laptop** (their words: "if it needs
   hosting then my laptop will crash and it will need to be hosted in cloud...
   I have never done [that]. The architecture, the structure, I know
   nothing."). Any observability skill needs: a free-tier-first backend
   decision table (see §5 Phase 3), a plain-language explanation of what
   traces/spans even are, an explanation that the backend is a separate
   managed service reached over HTTPS (not something that runs on their
   machine), and explicit gotchas (never log secrets/PII into traces; sample
   to control cost).
3. **Runtime self-improvement must be technique-agnostic, not GEPA-only.** The
   user used GEPA in `aegis` because they wanted to learn something new, not
   because they'd validated it was optimal. Do not default to GEPA. The
   `runtime-learning-loop` skill's research pass must survey current
   alternatives and let each project pick. Additionally: **the skill must
   design and run experiments autonomously** — pre-declaring success
   definitions, guardrails, failure modes, stop conditions, and a cost/ROI
   kill-switch (stop when expected quality lift no longer justifies spend).
   Priority order when trading off: **quality > performance > cost**, with an
   explicit diminishing-returns stop rule (don't over-optimize any one
   dimension). The user approves hypotheses and promotions; the experiment
   machinery itself runs unattended.
4. **Portability is non-negotiable for every new skill and adapter.** Derive
   all state from `.agents/` contents and the *consumer* project's own `docs/`
   — never from agent-loom-only files (e.g. `docs/SKILL-INDEX.md`). Test the
   mental model: "would this work if someone copied only `.agents/` into
   `prof-photon` and ran `project-setup`?" If no, it's built wrong.

## 4. Repo conventions (must follow — these are pre-existing, not new)

- Every `SKILL.md` body ≤ 200 lines. Depth goes in `references/*.md`.
- **Never write a `.agents/skills/<name>/SKILL.md` directly.** All skill
  creation/editing routes through `universal-skill-creator`
  (`.agents/skills/universal-skill-creator/SKILL.md`) — it runs research,
  validation, security scanning, deconfliction, and library sync
  automatically. Bypassing it is an explicit AGENTS.md violation.
- `project-specific` category skills require `## Common Rationalizations`
  (≥5 rows) and `## Verification` (≥3 checks).
- External content (repos, articles) must pass ALL `secure-*` skills before
  being ingested or persisted — discover via `ls .agents/skills/secure-*`.
- After any skill add/rename/removal: `library-skill` syncs
  `docs/SKILL-INDEX.md`, `AGENTS.md`, `README.md`, `docs/skill-graph.md`,
  `docs/architecture.md`, `docs/prd/PRD.md`, then auto-invokes
  `generate-changelog`.
- L3 examples: every skill should have `references/examples.md` ≥55 lines.
- Memory checkpoints: skill creation / changelog / ADR / spec / plan / major
  commit → invoke the matching `memory-*` sub-skill (see
  `.agents/skills/memory/SKILL.md` → Mandatory Auto-Trigger Checkpoints).
- No child/parallel agents for this plan — the repo's own sequential
  governance (shared SKILL-INDEX/AGENTS.md/README writes, security gates)
  makes parallel writers conflict-prone. Execute phases sequentially,
  single-agent.
- **Never commit unless the user explicitly asks.**

## 5. Phase-by-phase plan (Phase 1 done; resume at Phase 2)

### Phase 1 — Cursor trigger reliability — ✅ DONE (2026-07-08)

- New script `.agents/skills/project-setup/scripts/gen_host_adapters.py`
  (stdlib-only Python, portable — parses `.agents/skills/*/SKILL.md`
  frontmatter directly, never reads `docs/SKILL-INDEX.md`). Generates two
  files:
  - `.cursor/rules/agent-loom-routing.mdc` — small, `alwaysApply: true`. The
    mandatory invocation protocol (session-start memory rule, "invoking = you
    must open the SKILL.md", security invariant, "task seems simple" is not
    an excuse to skip a matching skill).
  - `.cursor/rules/agent-loom-skills-index.mdc` — `alwaysApply: false`,
    on-demand full index of all installed skills (one line each), so the
    always-on rule stays small.
- Wired into the lifecycle so every project gets it automatically:
  `project-setup` (v1.3, new Step 6d), `retroactive-project-setup` (v1.2, new
  Step 7.5), `agent-loom-sync` (v1.2, regenerates post-sync).
- `docs/memory/deferred.md` item #10 updated: PARTIAL (Cursor done; native
  `.claude/commands/` and `.gemini/commands/` adapters still open — reopen
  only if the user hits the same friction on those tools).
- **To activate in an existing consumer repo** (e.g. `prof-photon`, `aegis`,
  `Ember`), the user just needs to run, from that repo's root:
  ```bash
  python3 .agents/skills/project-setup/scripts/gen_host_adapters.py
  ```
- Verification done: line counts ≤200 on all 3 edited skills, loader-safety
  byte check (`---` at byte 0) passed, generator smoke-tested (produced valid
  output for all 119 skills in this repo).
- **Not yet done for Phase 1:** committing. Working tree is dirty (see git
  status below). Do not commit unless the user asks.

### Phase 2 — Model-tier routing — NEXT (not started)

Build `model-selection` via `universal-skill-creator` (Atomic or Standard
tier). Required contents:
- `references/model-tiers.md` — an editable tier registry (models change
  fast; do not hardcode into SKILL.md body). Corrected tiering (the user's
  original guess undersold Sonnet and GPT-5.4 — correct it in the skill):
  - **High-cognition** (architecture, foundations, ambiguous problems,
    deep debugging): Opus 4.8, GPT-5.5.
  - **High-mid** (most feature implementation, given a clear spec): Sonnet 5,
    GPT-5.4. *Sonnet 5 is stronger than the user assumed — don't relegate it
    to a low tier.*
  - **Mid** (well-scoped implementation with tests as guardrails): GLM 5.2.
  - **Fast/low** (small scoped edits, renames, boilerplate — never
    multi-file design decisions): Cursor Composer 2.5.
- Task-class → tier mapping (architecture/foundations always high; routine
  CRUD/UI/tests mid-to-high-mid; mechanical edits low).
- **Advisory mechanics per §3.1 above**: a pre-execution model-plan table +
  per-module-boundary "next module → tier X" announcements. No automatic
  model switching.
- Escalation rules: if a low/mid-tier execution gets stuck in a retry loop,
  fails the same test repeatedly, or needs to make an architectural decision
  it wasn't scoped for — stop and escalate to a human-directed tier change,
  don't let it push through.
- Guardrails for low-tier execution: only run against a spec + tests written
  by a higher tier; never let low tier make unscoped design decisions.
- Edit `implementation-plan` and `problem-to-plan` (both existing skills) to
  add a `model:` tier column/field to every plan task/module, with
  architecture/foundation tasks always pinned to the high tier. Frame plan
  tasks the way obra/superpowers frames them for junior engineers (see Phase
  4) — the point is that a **lower-tier model executing a task written by a
  higher-tier model** should still succeed, because the task is
  unambiguous and fully scoped.
- Deconflict against nothing existing — grep confirmed no model-selection
  skill exists anywhere in the library.

### Phase 3 — Agentic quality loop for shipped products — biggest phase

Three new skills, each ≤200 lines, via `universal-skill-creator`, each
deconflicted against `harness-evolution` / `run-trace` / `experimentation`
(those three are scoped to the *coding agent's own* reliability — these new
skills are scoped to the *user's shipped product's own runtime agents*,
which is a currently-missing distinction in the library):

1. **`agent-observability`**
   - Plain-language primer: what a "trace" and a "span" are, why they matter
     for a multi-agent system, written for someone with zero infra
     background.
   - Backend decision table, free-tier-first, per §3.2 above. Candidates to
     research and compare at build time (do not just copy this list without
     verifying current free-tier terms, since these change): Langfuse Cloud
     free tier, Phoenix Cloud free tier, LangSmith free tier. Self-hosting in
     a cloud provider is the *last resort*, clearly labeled as requiring more
     setup, never presented as running on the user's laptop.
   - Plain-language architecture explainer: the observability backend is a
     separate managed service; the product's own code just sends trace data
     to it over HTTPS as a side effect of running; it is not a service the
     user has to build or run themselves in the common case.
   - Gotchas section: never log secrets or PII into trace payloads; sample
     traces to control cost at scale; traces are for the *shipped product*,
     distinct from `run-trace` (which logs the *coding agent's own*
     execution).
   - Wire into `agent-system-architecture` Step 4 (currently says "design for
     observability" with zero implementation guidance — point it at this new
     skill) and into `setup-evaluation` as an additional check for
     `agent-chain` complexity-class products.

2. **`agent-run-retro`**
   - The CLI interview loop the user explicitly asked for: after a dev run,
     ask in plain language what went well / what went poorly.
   - Draft ranked hypotheses about what would most improve output quality or
     performance — must be hypotheses that could plausibly move a real
     metric, never busywork experiments for their own sake.
   - Design n=1/n=2 experiments per hypothesis with pre-declared success
     criteria before running anything.
   - Priority order **quality > performance > cost**, with an explicit rule
     to stop chasing a dimension once it shows diminishing returns.
   - Runs autonomously once hypotheses are approved; only checkpoints with
     the user for approval, not for every step.

3. **`runtime-learning-loop`**
   - Technique-agnostic self-improvement for a *shipped* product's agents:
     production traces → eval/judge scoring → improvement proposals
     (prompt/playbook edits) → human approval gate → promote.
   - `references/techniques.md` should survey current options (GEPA is one;
     research at build time for current alternatives — this space moves
     fast) rather than hardcoding GEPA as the default.
   - Explicitly distinct from `harness-evolution` (improves the *coding
     agent's own* harness, not the product).
   - Same autonomous-experimentation requirement as `agent-run-retro`: the
     loop must design and run its own experiments with pre-declared success
     definitions, guardrails, failure modes, stop conditions, and a
     cost/ROI kill-switch that halts experimentation when expected quality
     lift no longer justifies the spend.

4. Plus: an `improve-skills TARGET=<skill> SKIP_RESEARCH=false` pass (i.e.
   run real research) on the existing `eval-output` suite (`eval-rubric-design`,
   `eval-judge`, `eval-pipeline`, `eval-output`) to answer the user's question
   "is my eval suite actually good?" against current best practice, and
   cross-link it to the three new skills above.

### Phase 4 — Superpowers ingestion

Run `learn-from-repo` on `github.com/obra/superpowers` (MIT, ~243k stars as
of this session — verify current numbers, this space moves fast) through the
full credibility + `secure-*` pipeline (do not skip security scanning just
because the repo is popular). Key skills in that repo worth comparing against
(confirmed via web research this session, not yet read in full or ingested):
`test-driven-development` (RED-GREEN-REFACTOR, deletes code written before
tests), `systematic-debugging`, `verification-before-completion`,
`subagent-driven-development` (two-stage review: spec compliance then code
quality), `writing-plans` (tasks scoped for "an enthusiastic junior engineer
with poor taste, no judgement... and an aversion to testing" — directly
relevant to Phase 2's low-tier-model guardrails), `brainstorming`,
`requesting-code-review`.

Pairwise-compare against this repo's existing: `brainstorming`,
`test-driven-development`, `debug-and-fix`, `code-review-crsp`,
`incremental-implementation`, `implementation-plan`,
`git-workflow-and-versioning`, `universal-skill-creator`. Merge craft where
superpowers wins, with citations, following the same evolution model already
proven in this repo for the `addyosmani/agent-skills` ingestion (see
`docs/comparisons/2026-06-01-SUMMARY.md` for the pattern to replicate: score
pairs, MERGE/KEEP verdicts, apply in small batches, cite sources inline).

### Phase 5 — SDD × TDD unification

Edits only, no new skill:
- `feature-spec`: Given/When/Then acceptance criteria should be able to emit
  failing-test skeletons.
- `spec-driven-development`: `/implement` should enforce red-green per slice
  by routing through `incremental-implementation` + `test-driven-development`
  together, not either alone.
- `spec-crosscheck`: add an acceptance-criteria ↔ test traceability check to
  its existing PASS/FAIL gate.

### Phase 6 — Remaining audit gaps (queued, not this pass)

From an earlier gap audit this session (comparing agent-loom's coverage
against the user's real projects), two gaps were identified and explicitly
deferred rather than built now: `mobile-app-development` (React
Native/Expo — navigation, EAS build/submit, native config, app-store review;
needed for `prof-photon`) and `mcp-server-authoring` (building an MCP
server's tool/resource/prompt handlers — `tool-finder` only checks *whether*
an MCP is needed, nothing helps build one; needed for `Ember`'s
`ember-mcp`). Log both to `docs/memory/deferred.md` with clear reopen
triggers; do not build them in this plan's pass.

## 6. Current working-tree state (as of Phase 1 close)

```
Modified:  .agents/skills/agent-loom-sync/SKILL.md
           .agents/skills/project-setup/SKILL.md
           .agents/skills/retroactive-project-setup/SKILL.md
           docs/knowledge-graph/{GRAPH_INDEX.md,GRAPH_REPORT.md,call-graph.json,graph.json,manifest.json}
           docs/memory/{deferred.md,current-state.md,project-index.md,agent-handoffs.md}
           docs/skill-outputs/SKILL-OUTPUTS.md
New:       .agents/skills/project-setup/scripts/gen_host_adapters.py
           .cursor/rules/agent-loom-routing.mdc
           .cursor/rules/agent-loom-skills-index.mdc
           docs/handoffs/2026-07-08-external-agent-loom-upgrade-handoff.md (this file)
```

Not committed. Do not commit unless the user asks — when they do, run
`memory-handoff` first (already done, this document + the memory files above
are the handoff), then follow `git-workflow-and-versioning` for the commit
itself.

## 7. How to resume

1. Confirm with the user that you're picking up the agent-loom upgrade plan
   (don't assume — say what you found and ask if they want to continue at
   Phase 2, or ask for something else first).
2. If your tool supports plan artifacts, `read_plans` on
   `834ff43c-a703-4565-9b8f-2dba210002b0` to cross-check against this
   document (this document should already match it in full).
3. Build Phase 2 (`model-selection` skill) via `universal-skill-creator`,
   following §5 above.
4. Stop after Phase 2 and report token spend / progress before continuing,
   per the user's standing instruction.
