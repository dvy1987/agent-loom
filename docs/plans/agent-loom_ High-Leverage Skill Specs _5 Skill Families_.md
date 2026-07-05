# agent-loom: High-Leverage Skill Specs

These specs describe five skill families to add to or update in agent-loom (dvy1987/agent-loom). Each one is written to be handed directly to an agent that builds agentskills.io-compliant skills.

## How to read these specs

Every skill in agent-loom is an agentskills.io package: a directory containing a `SKILL.md` (YAML frontmatter plus Markdown body) and optional `scripts/`, `references/`, and `assets/` subdirectories. Skills load in three stages — Discovery (name + description), Activation (full `SKILL.md`, keep under \~500 lines / \~5000 tokens), and Execution (follow instructions, optionally run bundled code).

Because agent-loom is provider-agnostic and self-maintaining, each spec includes:

* Reference material: real repos and papers the building agent should read and, where useful, mine for patterns or bundle into `references/`.
* Precise instructions: for areas where good public references are thin or inconsistent, deterministic step-by-step rules so the skill is valuable without depending on the agent inventing an approach.

Priority order for build: Skill 2 (codebase navigation and safe change) and Skill 1 (workflow orchestration) first — they are the strongest differentiators. Skill 4 (observability) and Skill 5 (onboarding) compound adoption. Skill 3 (deployment) broadens reach incrementally.

Portability rule (applies to all five): use only portable frontmatter fields from the agentskills.io spec (name, description, license, compatibility, metadata, allowed-tools). Do not use tool-specific frontmatter extensions. Every skill must satisfy agent-loom's One Rule — work on the first try in at least three platforms (for example Claude Code, GitHub Copilot, and Cursor or Gemini CLI).

---

# Skill 1: Workflow Orchestration and Structured Reasoning

## Product Overview

A skill family that teaches an agent to plan before it acts: decompose a task into an explicit, revisable subgoal graph, execute steps against ground truth (tool output, tests, environment feedback), and adapt the plan when a step fails. This is the core of agent-loom's stated identity — "agents that reason about process structure before execution." Primary user: a builder running an AI coding agent on a non-trivial, multi-step task where a naive one-shot attempt would be fragile.

Scope for this version:

* Included: a `structured-planning` skill (plan-ahead decomposition, checkpointing, plan revision on failure) and a `dynamic-routing` skill (outcome-based branching: if X fails, try Y).
* Later: multi-agent delegation, learned routing policies, parallel tool execution.

## Design and Visual Style

Not a UI. The "surface" is the plan artifact the skill emits. Standardize it so every platform renders it consistently:

* Emit the plan as a Markdown checklist with stable step IDs (`S1`, `S1.1`, `S2`).
* Each step records: goal, chosen action, precondition, expected observation, and status (`pending` / `in-progress` / `done` / `failed` / `revised`).
* Keep a running "plan delta log" so a human or another agent can see why the plan changed.

## Tech Stack

* Skill format: agentskills.io `SKILL.md` (YAML frontmatter + Markdown), body under \~500 lines.
* Language for bundled scripts: Python 3.11 (matches the repo's primary language) in `scripts/`, no non-stdlib dependencies unless justified.
* Persistence: plan and delta log written to a local `.agent-loom/plans/<task-id>.md` file; no external database.
* Model-agnostic: no hard dependency on a specific LLM provider.

## Pages and Navigation

Skill package layout:

* `SKILL.md` — activation instructions and the reasoning protocol.
* `references/PATTERNS.md` — the orchestration patterns distilled from the reference material below.
* `references/PLAN-SCHEMA.md` — the exact plan artifact schema and status lifecycle.
* `scripts/plan_lint.py` — validates a plan artifact against the schema (stable IDs, no orphan steps, every failed step has a revision or an explicit abort).

## Core User Flows

Flow 1: Plan-ahead decomposition (the first win)

1. Agent receives a multi-step task and activates `structured-planning`.
2. Agent generates a complete subgoal list in one pass, then commits only to executing the first subgoal (ReCAP-style plan-ahead decomposition).
3. Agent executes step S1, records the actual observation, and marks status.
4. Agent refines the remaining steps using the real result before continuing.

Flow 2: Failure-driven revision

1. A step returns an error or an unexpected observation.
2. Agent writes a short structured reflection (cause hypothesis grounded in the step's evidence).
3. `dynamic-routing` selects an alternative path or recombines the remaining plan rather than blindly retrying.
4. Plan delta log records the revision and the reason.

## Data Model and Backend

* Plan (task_id: string, created_at, steps: Step\[\], delta_log: Delta\[\])
* Step (id: string, goal: string, action: string, precondition: string, expected: string, status: enum, evidence_ref: string)
* Delta (at: timestamp, step_id: string, from_status, to_status, reason: string)

No server. State is file-based and git-friendly so runs are auditable.

## Key Components

* Reasoning protocol in `SKILL.md`: the imperative rules the agent follows (decompose, commit-one, execute-against-ground-truth, reflect-on-failure, revise-not-retry).
* `plan_lint.py`: deterministic guardrail so malformed plans are caught before execution.

## Reference Material to Learn From

* Anthropic, "Building Effective Agents" (anthropic.com/research/building-effective-agents) — orchestrator-workers pattern, workflows vs. agents, start-simple guidance. Bundle a distilled summary into `references/PATTERNS.md`.
* ReCAP: Recursive Context-Aware Reasoning and Planning (NeurIPS 2025) — plan-ahead decomposition and consistent multi-level context. Source of the "generate full plan, execute first, refine rest" rule.
* DyFlow: Dynamic Workflow Framework for Agentic Reasoning (NeurIPS 2025; code: github.com/wyf23187/DyFlow) — designer-executor split and feedback-driven subgoal revision.
* GAP: Graph-Based Agent Planning (arXiv 2510.25320) and NaviAgent (arXiv 2506.19500) — dependency-aware planning and path recombination on tool failure.

## AI Generation Notes

* Keep `SKILL.md` model-agnostic; describe the protocol in imperative prose, not provider-specific prompt syntax.
* Stub multi-agent delegation and parallel execution; note them as future work.
* Seed `references/` with the four summaries above so the skill is self-contained.
* The skill must degrade gracefully: if the task is trivial (single step), the protocol should say to skip formal planning — echo Anthropic's "add complexity only when it helps."

---

# Skill 2: Codebase Navigation and Safe Change

## Product Overview

A skill family that lets an agent understand a repository's structure and dependencies before editing, predict the blast radius of a change, apply the change, and verify it with a type-check plus tests — reverting automatically if verification fails. Primary user: a builder who wants an agent to make real edits across a codebase without breaking the build. This is the highest-leverage differentiator because most agents fail exactly here.

Scope for this version:

* Included: `dependency-mapping` (find callers, reverse dependencies, blast radius), `safe-change` (plan change, verify, auto-revert on failure), and `pr-authoring` (intent-separated commits and clear PR summaries).
* Later: cross-repo migration, learned risk scoring, hotspot analysis from git history.

## Design and Visual Style

Not a UI. Standardize the two artifacts the skill emits:

* Impact report: a table of affected symbols, files, callers, and tests, plus a plain-language risk statement.
* PR body: intent-labeled sections (what changed, why, blast radius, verification result), one intent per PR.

## Tech Stack

* Skill format: agentskills.io `SKILL.md`.
* Analysis approach: prefer the agent's native code-search plus a language server or `tree-sitter` when available; fall back to text search. Do not require a bespoke binary.
* Verification: invoke the repo's existing type-checker and test command (auto-detected); degrade to type-check-only when no tests exist and report `behaviorVerified: false`.
* Safety: use `git` for snapshots and `git restore` / branch reset for rollback.

## Pages and Navigation

Skill package layout:

* `SKILL.md` — the navigate-then-change protocol.
* `references/IMPACT-QUERIES.md` — the exact question set the agent must answer before editing (see below).
* `references/PR-CONVENTIONS.md` — commit intent separation and PR summary template.
* `scripts/verify.sh` — detects and runs type-check + tests, returns a structured pass/fail.

## Core User Flows

Flow 1: Safe change (the first win)

1. Agent activates `safe-change` for an edit request.
2. Agent answers the mandatory impact questions: what depends on this symbol, what breaks if I change it, which tests cover it.
3. Agent takes a git snapshot, applies exactly one logical change.
4. `verify.sh` runs type-check + tests. On pass, keep and continue; on fail, `git restore` and report the failure with evidence (codespine-style one-safe-edit loop).

Flow 2: Intent-separated PR authoring

1. Agent groups edits by intent (fix vs. refactor vs. feature).
2. Refactoring changes are committed separately from behavior changes (per the Agentic Refactoring study's finding that mixed PRs raise review burden).
3. PR body states intent, blast radius, and verification result explicitly.

## Data Model and Backend

* Symbol (name, file, kind, callers: string\[\], callees: string\[\], covering_tests: string\[\])
* ImpactReport (target_symbol, affected_files: string\[\], risk: enum, notes: string)
* ChangeRun (snapshot_ref, edits: Edit\[\], verify_result: {typecheck: bool, tests: bool, behaviorVerified: bool})

No server; git is the persistence and rollback layer.

## Key Components

* Mandatory impact-question gate in `SKILL.md` — the agent may not edit until these are answered.
* `verify.sh` — deterministic verification and structured result.
* Auto-revert rule — non-negotiable: a failed verification always rolls back.

## Reference Material to Learn From

* Synapse Farsight (github.com/alexsarrell/synapse-farsight) — `what_depends_on`, `what_breaks_if_i_change`, plan-then-verify with gap reporting; deterministic non-LLM core. Strong model for the impact-question gate.
* Cartograph (github.com/emberloom/cartograph) — blast radius, dependencies, co-changes, who-owns, hotspots; layered structure + git-history model.
* codespine (github.com/jeromeetienne/codespine) — one-safe-edit-per-run with type-check + test verification and automatic `git restore` on failure. Directly informs the `safe-change` loop.
* agentic-codebase (github.com/agentralabs/agentic-codebase) — pre-refactor safety checks, hidden-coupling detection, evidence-backed changes.
* "Agentic Refactoring: An Empirical Study of AI Coding Agents" (arXiv 2511.04824) — evidence that agents should separate refactoring from feature work and state intent in PRs. Bundle its recommendations into `references/PR-CONVENTIONS.md`.

## AI Generation Notes

* Do not require installing a specific graph tool. Detect capability (LSP, tree-sitter, plain search) and adapt; document the fallback ladder.
* Never skip verification. If no test command is found, run type-check and clearly report reduced confidence.
* Seed `references/IMPACT-QUERIES.md` with the exact three-question gate.
* Keep edits atomic — one logical change per verify cycle.

---

# Skill 3: Cross-Platform Deployment and Provider Abstraction

## Product Overview

A skill family that lets an agent build, test, and deploy a project with one intent ("deploy this to preview") regardless of the underlying provider, and keep issues or project boards in sync across platforms. Primary user: a builder who wants to automate once and run anywhere (GitHub Actions, Vercel, Netlify, Cloudflare, local). Reinforces agent-loom's provider-agnostic positioning.

Scope for this version:

* Included: `deploy-anywhere` (unified build/test/deploy intent with per-provider adapters) and `issue-sync` (mirror issues and status across trackers).
* Later: cloud infra provisioning, multi-region rollout, secret rotation.

## Design and Visual Style

Not a UI. Standardize a single declarative config the agent reads and writes: `.agent-loom/deploy.yml` describing target(s), build command, test command, and environment mapping. Emit a deployment summary (target, URL, status, rollback command).

## Tech Stack

* Skill format: agentskills.io `SKILL.md`.
* Adapter pattern: one adapter file per provider in `references/adapters/` (start with GitHub Actions + Vercel), each documenting the exact CLI calls and required secrets.
* No bespoke runtime; the skill orchestrates existing provider CLIs (for example `vercel pull` / `vercel build` / `vercel deploy --prebuilt`).

## Pages and Navigation

Skill package layout:

* `SKILL.md` — the deploy-intent protocol and provider-detection logic.
* `references/DEPLOY-SCHEMA.md` — the `deploy.yml` schema.
* `references/adapters/github-actions.md`, `references/adapters/vercel.md` — exact steps and secrets per provider.
* `scripts/preflight.py` — checks required secrets/env exist before any deploy is attempted.

## Core User Flows

Flow 1: Deploy anywhere (the first win)

1. Agent activates `deploy-anywhere`; reads or scaffolds `deploy.yml`.
2. Agent detects the target provider (config first, then repo signals).
3. `preflight.py` verifies required credentials exist; if missing, the agent stops and lists exactly what to add (no partial deploys).
4. Agent runs the adapter's build/deploy steps and returns URL + rollback instructions.

Flow 2: Issue sync

1. Agent reads issues/status from source tracker.
2. Agent mirrors create/update/close to the target tracker, preserving a stable external-ID mapping to avoid duplicates.

## Data Model and Backend

* DeployConfig (targets: Target\[\], build_cmd, test_cmd, env_map)
* Target (provider: enum, project_id, org_id, prod: bool)
* IssueMirror (source_id, target_id, status, last_synced_at)

Secrets are referenced by name only; never stored in the repo.

## Key Components

* Provider adapters (data-driven, one per file) modeled on ci-orchestrator's adapter pattern.
* `preflight.py` — hard gate that prevents half-configured deploys.

## Reference Material to Learn From

* Vercel GitHub Actions example (github.com/vercel/examples/tree/main/ci-cd/github-actions) and Vercel KB guide — exact CLI sequence and required secrets (VERCEL_TOKEN, VERCEL_ORG_ID, VERCEL_PROJECT_ID). Use verbatim for the Vercel adapter.
* ci-orchestrator (github.com/nikolareljin/ci-orchestrator) — single-config, adapter-based, multi-platform orchestration (BuildAdapter / DeployAdapter / GitOperations / Notifier). Model for `deploy.yml` and the adapter layout.
* universal-deploy (github.com/universal-deploy/universal-deploy) — zero-config cross-provider deployment abstraction; model for provider auto-detection and sensible defaults.

## AI Generation Notes

* Ship only GitHub Actions and Vercel adapters now; document the adapter interface so others can be added.
* Preflight must fail loudly on missing secrets — never attempt a partial deploy.
* Keep secrets as named references; the skill must never write credential values into files.

---

# Skill 4: Observability, Self-Correction, and Feedback Loops

## Product Overview

A skill family that makes an agent's work inspectable and self-correcting: capture a structured execution trace (plan steps, tool calls, observations, errors), localize the first decisive failure in a run, propose and apply a targeted repair, and record what changed and why. Primary user: a builder who needs to trust, debug, and iterate on agent runs. Increases reliability and trust — the multiplier on every other skill.

Scope for this version:

* Included: `run-trace` (structured, minimal-overhead logging of a run) and `fault-localize` (find the earliest decisive error and propose a repair grounded in evidence).
* Later: cross-run telemetry dashboards, learned repair policies, provenance graphs.

## Design and Visual Style

Not a UI. Standardize the trace and the debug report:

* Trace: append-only structured records (JSONL) across three surfaces — operational (what ran), cognitive (why, the reasoning step), contextual (inputs/environment).
* Debug report: earliest suspected step, evidence, proposed repair, and outcome after replay.

## Tech Stack

* Skill format: agentskills.io `SKILL.md`.
* Trace storage: `.agent-loom/traces/<run-id>.jsonl`, append-only, git-ignored by default.
* Language: Python 3.11 in `scripts/` for trace parsing and localization helpers; stdlib only.
* Model-agnostic.

## Pages and Navigation

Skill package layout:

* `SKILL.md` — tracing protocol and the localization/repair loop.
* `references/TRACE-SCHEMA.md` — the record schema (operational/cognitive/contextual surfaces).
* `references/LOCALIZATION.md` — the diagnose to replay to verify procedure.
* `scripts/trace_query.py` — filter a trace, list tool errors, show the step timeline.

## Core User Flows

Flow 1: Run trace (always on)

1. As the agent works, it appends a structured record per meaningful step (tool call, observation, reasoning, error).
2. Records use stable step IDs that match the plan artifact from Skill 1, so plan and trace line up.

Flow 2: Fault localization and repair (the first win)

1. On a failed or wrong-result run, the agent scans the trace for the earliest step whose output diverged.
2. It writes a structured reflection (cause hypothesis grounded in that step's evidence) — not a vague retry.
3. It applies a targeted repair and replays from the localized point; if the outcome flips to correct, it keeps the fix and records the attribution (step, intervention, outcome change).

## Data Model and Backend

* TraceRecord (run_id, step_id, surface: enum{operational,cognitive,contextual}, action, input_ref, output_ref, error: string?, ts)
* Attribution (run_id, suspected_step_id, hypothesis, repair, outcome_flip: bool)

Append-only files; no server.

## Key Components

* Structured logging protocol (three surfaces) so traces are consistent across platforms.
* Localization loop: diagnose to targeted replay to outcome-verify, keeping human-in-the-loop optional.

## Reference Material to Learn From

* REFLECT: Intervention-Supported Error Attribution (arXiv 2606.09071) — diagnose, targeted replay, verify outcome flip; the core of `fault-localize`.
* Watson: Cognitive Observability Framework (arXiv 2411.03455) — recover reasoning traces retroactively and feed them into self-reflection to improve correction.
* AgentTrace: Structured Logging for Agent Observability (arXiv 2602.10133) — the operational/cognitive/contextual three-surface log model. Use for `TRACE-SCHEMA.md`.
* LADYBUG (EDBT 2025) — interactive trace timeline, mocking, and reflection-based first-incorrect-step detection.
* "From Agent Traces to Trust" (arXiv 2606.04990) and "Failure makes the agent stronger" (ACL Findings 2026) — trace element taxonomy and structured, learnable reflection (Reflect to Call to Final).

## AI Generation Notes

* Keep logging low-overhead and append-only; never block execution to log.
* Reuse Skill 1 step IDs so plan, trace, and attribution cross-reference cleanly.
* Default traces to git-ignored; do not persist secrets in trace payloads (store refs, not raw values).

---

# Skill 5: First-Win Onboarding and Delight

## Product Overview

A skill family plus repo assets that get a new user or contributor to a real, runnable win in under five minutes, and convert that win into stars and contributions. Primary user: a builder evaluating agent-loom for the first time, and drive-by developers who could contribute. This is the growth engine for the 5,000-star goal.

Scope for this version:

* Included: a `quickstart` skill that runs a guaranteed-to-work demo automation, three real-world example skills (not hello-world), and repo onboarding assets (README hero rewrite, good-first-issue templates).
* Later: interactive playground, template gallery, contributor recognition automation.

## Design and Visual Style

* README hero: one-line value hook in the first \~10 lines, a copy-paste quickstart that produces a visible result in about 60 seconds, and a short "Not for you if..." expectations block.
* Examples folder as the product tour: three concrete, real-world example skills with expected output shown.
* Keep formatting clean and scannable; move deep docs to `docs/`.

## Tech Stack

* Skill format: agentskills.io `SKILL.md`.
* Demo: the quickstart invokes an existing agent-loom skill (ideally Skill 2's safe-change on a tiny seeded repo) so the "win" is genuine, not staged.
* No new services.

## Pages and Navigation

Repo + skill layout:

* `SKILL.md` (quickstart) — the guided first-run protocol.
* `examples/` — three runnable example skills with README and expected output each.
* `README.md` (hero rewrite), `.github/ISSUE_TEMPLATE/good-first-issue.md`, and a short `docs/why-agent-loom.md` for consistent messaging.

## Core User Flows

Flow 1: First win in five minutes (the core moment)

1. New user copies the quickstart command from the README.
2. The quickstart activates a real skill against a tiny seeded example repo and produces a visible, correct result (for example, a safe, verified edit or an impact report).
3. User sees the result plus a one-line "what just happened" explanation and a next-step link.

Flow 2: Drive-by to contributor

1. User browses `examples/` and sees three real use cases with expected output.
2. A tagged good-first-issue offers a scoped, welcoming task (for example, add one provider adapter or one example skill).

## Data Model and Backend

* Minimal. A seeded example repo/fixture lives under `examples/seed/`. No persistence beyond the example workspace.

## Key Components

* Quickstart skill with a guaranteed-success demo (idempotent, no external credentials required).
* Three example skills chosen to showcase the differentiators (structured planning, safe change, deploy-anywhere).
* README hero and issue templates as conversion surfaces.

## Reference Material to Learn From

* microsoft/apm OSS growth-hacker agent (github.com/microsoft/apm, .github/agents/oss-growth-hacker.agent.md) — the surface-to-goal conversion framework (README hero, quickstart, templates, changelog, issue templates).
* "The GitHub-Driven GTM" (datadab.com) — treat the repo as the onboarding experience; README is the value prop, examples are the product tour; include at least three real-world examples and a "Not for you if..." block.
* "How We Got 4.5K+ GitHub Stars in 6 Months" (bomberbot.com) — README structure, good-first-issue tagging, fast issue response, contributor recognition.
* "OSS Signals for Developer Launch Pages" (landings.us) — hero structure and quickstart snippet guidance; agent-loom is currently high-differentiation / low-stars, so emphasize quickstart and sample apps.

## AI Generation Notes

* The quickstart must require zero external credentials and be idempotent — it should work offline on a seeded fixture.
* Do not stage a fake result; wire the demo to a real skill so the win is trustworthy.
* Keep the README hook under \~10 lines and the quickstart runnable in about 60 seconds.
* Seed three real example skills, not toy hello-world snippets.

---

# Cross-cutting build guidance

* Validate every `SKILL.md` against the agentskills.io format (frontmatter fields, \~500-line body limit) before considering a skill done.
* Enforce the One Rule: test each skill on at least three platforms and note results in the skill's `references/COMPATIBILITY.md`.
* Where a reference repo is deterministic and non-LLM (Synapse Farsight, Cartograph, codespine), prefer mirroring its exact query/verification interface over inventing new terminology — it makes agent-loom skills interoperable with tools builders already use.
* Add each new skill to `docs/SKILL-INDEX.md` and set conflict precedence in `.agents/ROUTING.md` (Skill 4 observability should be able to wrap Skills 1–3; Skill 2's verification gate should always win over Skill 5's "make it easy" bias).