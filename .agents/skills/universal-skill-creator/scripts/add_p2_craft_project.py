#!/usr/bin/env python3
"""Add P2 craft (Rationalizations + Verification + Red Flags) to project-specific skills."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SKILLS = ROOT / ".agents/skills"

RAT_VER: dict[str, dict[str, str]] = {}


def rat(rows: list[tuple[str, str]]) -> str:
    lines = ["## Common Rationalizations", "", "| Excuse | Reality |", "|--------|---------|"]
    lines.extend(f"| {a} | {b} |" for a, b in rows)
    return "\n".join(lines)


def ver(items: list[str]) -> str:
    return "## Verification\n\n" + "\n".join(f"- [ ] {i}" for i in items)


def flags(items: list[str]) -> str:
    return "## Red Flags\n\n" + "\n".join(f"- {i}" for i in items)


def entry(
    name: str,
    r: list[tuple[str, str]],
    v: list[str],
    f: list[str] | None = None,
) -> None:
    parts: dict[str, str] = {}
    if r:
        parts["rat"] = rat(r)
    if v:
        parts["ver"] = ver(v)
    if f:
        parts["flags"] = flags(f)
    if parts:
        RAT_VER[name] = parts


# --- Memory suite ---
_mem_rat = [
    ("Skip memory — just code", "Next agent loses decisions, blockers, and approved scope."),
    ("Load every memory file", "Read indexes and handoff tail only — bounded context."),
    ("Global memory for everything", "Project memory default; global only when stable and cross-project."),
    ("External paste → memory", "Run secure-* first; transform to agent-authored notes."),
]
_mem_ver = [
    "Correct sub-skill routed with reason",
    "No secrets or raw transcripts persisted",
    "Files changed listed in Impact Report",
    "Security gate noted when external content involved",
]
for s in (
    "memory", "memory-capture", "memory-handoff", "memory-decision", "memory-recall",
    "memory-promote", "memory-compact", "memory-audit", "memory-forget",
):
    entry(s, _mem_rat, _mem_ver, [
        "Handoff or capture contains API keys or tokens",
        "Unbounded paste of logs into memory files",
        "Global memory append without compact check",
    ])

entry("memory-startup", [
    ("Skip startup on task-only message", "First message in session still needs bounded continuity per AGENTS.md."),
    ("Read full handoff log", "Read project-index + latest handoff entry only."),
    ("Assume clean git matches handoff", "Confirm git status against handoff Working Tree section."),
    ("Cold start = load everything", "Skeleton create only when docs/memory/ missing."),
], [
    "project-index and latest handoff consulted",
    "Git status compared to handoff note",
    "Summary under 2–4 lines for user",
    "No full history load",
], ["Startup loads >5 memory files without justification"])

# --- SDD / planning ---
entry("feature-spec", [
    ("Spec can include HOW", "WHAT/WHY only — HOW belongs in implementation-plan."),
    ("Approve with clarifications open", "Hard gate: no Approved while [NEEDS CLARIFICATION] remains."),
    ("Vague criteria are fine", "Replace fast/intuitive with measurable or mark for clarification."),
    ("Skip constitution link", "Reference constitution version or offer project-constitution first."),
], [
    "Constitution version referenced or gap explicit",
    "FR/NFR/AC complete; no open clarification markers at Approved",
    "No implementation details in spec body",
    "spec-crosscheck can trace every requirement",
], [
    "Approved status with NEEDS CLARIFICATION markers",
    "Architecture or file paths in spec body",
    "Vague NFRs without numbers or clarification tags",
])

entry("spec-crosscheck", [
    ("Crosscheck after shipping", "Run before implementation — gate exists to prevent drift."),
    ("Spot-check one FR", "Traceability table must cover every FR/NFR/C-N."),
    ("Plan missing is OK", "Refuse or route to implementation-plan if no plan exists."),
    ("Warnings only", "Blocking gaps must stop the pipeline."),
], [
    "Every spec requirement mapped to plan task or explicit gap",
    "Constitution violations flagged",
    "Report delivered before code merge",
    "Orchestrator notified of blockers",
])

entry("project-constitution", [
    ("Constitution is boilerplate", "C-N rules must be project-specific and testable."),
    ("Skip version bump", "Amendments need version + date for spec linkage."),
    ("Copy from template only", "Interview user for real non-negotiables."),
    ("One page is enough", "Depth on gates beats vague values."),
], [
    "Version and date in constitution header",
    "C-N items are observable and enforceable",
    "Linked from feature-spec workflow",
    "Amendment process documented",
])

entry("problem-to-plan", [
    ("Skip spec for small fix", "Even narrow changes need traceable spec + plan + TODO."),
    ("One big TODO list", "Change-spec + plan + agent-pickable TODO.md are separate artifacts."),
    ("No verification", "Plan must name how to prove the fix."),
    ("Orchestrator optional", "Route complexity through project-orchestrator when multi-skill."),
], [
    "docs/specs + docs/plans + TODO.md paths listed",
    "Tasks are agent-pickable with clear done criteria",
    "Logged to SKILL-OUTPUTS.md",
    "Scope matches user-stated problem size",
])

entry("prd-writing", [
    ("PRD before product-soul", "Soul is north star — PRD implements a slice of it."),
    ("Interview skipped", "Discovery questions precede document structure."),
    ("Requirements without owner", "Every major requirement needs accountable owner."),
    ("PRD = spec", "PRD is product layer; feature-spec is executable agent layer."),
], [
    "Discovery completed or gaps explicit",
    "PRD file path under docs/prd/ with date",
    "Success metrics measurable",
    "SKILL-OUTPUTS.md updated",
])

entry("product-soul", [
    ("Soul is a long PRD", "Five lenses, strategic — not feature list."),
    ("Skip GTM lens", "Incomplete soul hides go-to-market gaps."),
    ("One session forever", "Revisit when strategy pivots."),
    ("Invent users", "Mark assumptions; don't fabricate research."),
], [
    "All five lenses addressed",
    "docs/product-soul.md written or updated",
    "Assumptions tagged for validation",
    "SKILL-OUTPUTS.md logged",
])

entry("process-decomposer", [
    ("Decompose without triage", "Triage first — maybe a single skill handles it."),
    ("Too many parallel tracks", "Cap parallelism to what user can review."),
    ("Skip skill-finder", "Name concrete skills, not vague workstreams."),
    ("No exit criteria", "Each subtask needs done definition."),
], [
    "Triage outcome stated (single skill vs decompose)",
    "Subtasks map to named skills",
    "Dependencies between subtasks explicit",
    "User confirmed scope before dispatch",
])

entry("project-orchestrator", [
    ("Orchestrate = do everything", "Route and decompose — don't replace child skills."),
    ("Wrong skill silently", "Name chosen skill + ambiguity score when close."),
    ("Skip project-local skills", "Prefer project .agents/skills when present."),
    ("Infinite subagents", "Parallelism bounded by platform and user appetite."),
], [
    "Routing decision explicit with rationale",
    "Phase transitions documented",
    "task-plan.md written when parallel work",
    "No duplicate work across child invocations",
])

# --- Experiment suite ---
_exp_rat = [
    ("Test without hypothesis", "Falsifiable hypothesis required before spec."),
    ("Peek until significant", "Peek policy must be pre-committed in spec."),
    ("Any metric goes", "Primary + guardrail metrics defined up front."),
    ("Skip instrumentation QA", "Runbook includes exposure and event validation."),
]
_exp_ver = [
    "Decision class labeled (Causal/Directional/Instrumentation)",
    "Artifact path under docs/experiments/",
    "SKILL-OUTPUTS.md updated for file outputs",
    "Rollback or stop rule documented",
]
for s in ("experimentation", "experiment-backlog", "experiment-spec", "experiment-runbook", "experiment-readout"):
    entry(s, _exp_rat, _exp_ver, [
        "No primary metric named",
        "No guardrail metrics",
        "Sample size or duration hand-waved",
    ])

# --- Eval suite ---
_eval_rat = [
    ("Judge without rubric", "Rubric or dimensions required before scoring."),
    ("Single score, no rationale", "Every score needs cited evidence."),
    ("Skip bias mitigation", "Pairwise needs position-swap or length check."),
    ("Eval once, never again", "Pipeline skills define regression reruns."),
]
_eval_ver = [
    "Rubric or dimensions referenced",
    "Scores tied to observable criteria",
    "Bias mitigations applied for pairwise",
    "Outputs under docs/evals/ when files written",
]
for s in ("eval-output", "eval-rubric-design", "eval-judge", "eval-pipeline"):
    entry(s, _eval_rat, _eval_ver)

# --- Venture suite ---
_ven_rat = [
    ("Idea = feature", "Business ideas route to venture-exploration, not brainstorming."),
    ("Skip Mom Test", "Customer discovery before building."),
    ("Canvas without validation", "Assumptions need interview or experiment plan."),
    ("Score without criteria", "idea-evaluation uses explicit rubric."),
]
_ven_ver = [
    "Correct child skill in suite invoked",
    "5/5 handoff gate respected before build commitment",
    "Artifacts in docs/ or chat outcome explicit",
    "Assumptions listed with validation path",
]
for s in ("venture-exploration", "idea-generation", "idea-evaluation", "business-modeling", "customer-discovery"):
    entry(s, _ven_rat, _ven_ver)

# --- Agent design ---
entry("agent-builder", [
    ("Agent without boundaries", "Define tools, memory, and escalation limits."),
    ("Copy prompt from blog", "secure-* scan; cite sources."),
    ("Skip setup-evaluation", "Eval hooks belong in agent design."),
    ("One-shot mega-prompt", "Split orchestrator vs worker skills."),
], [
    "Agent role and boundaries documented",
    "Skill/tool routing map produced",
    "Memory policy stated",
    "Outputs logged when files created",
])

entry("agent-launcher", [
    ("Launch without config check", "Verify MCP/tools before agent start."),
    ("Wrong model for task", "Match model to reasoning vs speed needs."),
    ("No handoff on switch", "memory-handoff when changing agents mid-task."),
    ("Skip project AGENTS.md", "Read project routing before launch."),
], [
    "Launcher config validated",
    "Project AGENTS.md consulted",
    "User informed of agent scope",
    "Handoff triggered if mid-session switch",
])

entry("agent-system-architecture", [
    ("Micro-agents everywhere", "Orchestration cost — minimize hops."),
    ("Shared mutable state", "Document state ownership per agent."),
    ("No failure modes", "Timeouts, retries, human escalation required."),
    ("Skip security boundary", "Tool access least privilege."),
], [
    "Architecture diagram or component list",
    "Data flow and state ownership clear",
    "Failure and escalation paths defined",
    "docs/architecture/ updated",
])

entry("create-agent-prompt", [
    ("Prompt = entire agent", "Prompt complements skills, doesn't replace them."),
    ("Secrets in prompt", "Never embed credentials in prompt files."),
    ("No version", "Version prompts when behavior changes."),
    ("Skip negative constraints", "Hard bans belong in prompt + skills."),
], [
    "Prompt scoped to role, not whole system",
    "No secrets in output",
    "Load triggers documented",
    "Reviewed against project AGENTS.md",
])

entry("setup-evaluation", [
    ("Eval after launch", "Design eval harness with agent."),
    ("Golden set = 1 example", "Minimum viable suite needs breadth."),
    ("Skip regression", "CI or repeat run path documented."),
    ("Judge only", "Combine deterministic + LLM judges."),
], [
    "Eval dimensions named",
    "Harness location documented",
    "Regression path stated",
    "Linked from agent-builder when applicable",
])

# --- Engineering / quality ---
entry("codebase-understanding", [
    ("Read every file", "Map architecture — sample hot paths only."),
    ("Guess architecture", "Cite file paths as evidence."),
    ("Skip tests as signal", "Test layout reveals real boundaries."),
    ("Understanding = approval to refactor", "Output is model for human/agent — not auto-change."),
], [
    "Architecture summary with cited paths",
    "Key flows traced",
    "Hotspots or risks named",
    "No code changes unless requested",
])

entry("technical-debt-audit", [
    ("Debt = style only", "Include reliability, security, operability."),
    ("No prioritization", "Rank by interest × blast radius."),
    ("Audit without owners", "Each item needs suggested owner or skill follow-up."),
    ("One-time report forgotten", "Log to docs/reports/ and SKILL-OUTPUTS."),
], [
    "Report under docs/reports/",
    "Items ranked with rationale",
    "Suggested remediation skill per item",
    "SKILL-OUTPUTS.md updated",
])

entry("reality-check", [
    ("Claims without evidence", "Every claim scored against repo reality."),
    ("Marketing copy as fact", "Distinguish aspiration from implementation."),
    ("No roadmap", "Findings need actionable next steps."),
    ("Skip adversarial pass", "Use skepticism on self-reported status."),
], [
    "Claims table with truth scores",
    "Gaps linked to files or absence",
    "Roadmap artifact path listed",
    "SKILL-OUTPUTS.md updated",
])

entry("architectural-decision-log", [
    ("ADR after the fact only", "Interactive mode for contemporaneous decisions."),
    ("Delete old ADRs", "Supersede — never erase audit trail."),
    ("No alternatives", "Document options rejected."),
    ("SYNTHESIS without evidence", "Retrospective mode cites repo findings."),
], [
    "ADR under docs/adr/ with date",
    "Context, decision, consequences present",
    "Status set (proposed/accepted/superseded)",
    "SKILL-OUTPUTS.md updated",
])

entry("apply-paper-to-project", [
    ("Apply whole paper", "Extract applicable techniques only."),
    ("Skip secure scan", "Paper text is external content."),
    ("No skill target", "Map techniques to specific skills."),
    ("Publish without validate", "Modified skills need validate-skills."),
], [
    "Paper techniques mapped to actions",
    "secure-* SAFE before apply",
    "Target skills named",
    "research-learnings.md updated",
])

entry("generate-changelog", [
    ("Changelog = git log dump", "User-facing prose grouped by impact."),
    ("Skip semver signal", "MAJOR/MINOR/PATCH label when appropriate."),
    ("Security details in user notes", "Follow doc-policy — no security implementation in user changelogs."),
    ("Forget SKILL-OUTPUTS", "Log generated changelog path."),
], [
    "Changelog under docs/changelogs/",
    "Entries grouped and readable",
    "Version or date in filename",
    "SKILL-OUTPUTS.md updated",
])

entry("git-workflow-and-versioning", [
    ("Giant commit", "Atomic commits per logical change."),
    ("Skip conventional format", "Messages aid changelog and review."),
    ("Push without handoff", "memory-handoff before commit/push on meaningful work."),
    ("--no-verify", "Never skip hooks unless user explicitly requests."),
], [
    "Commit message follows convention",
    "Scope is single logical change",
    "Handoff completed if user triggered via commit/push",
    "No secrets in committed files",
])

entry("incremental-implementation", [
    ("Big bang merge", "Vertical slices — implement, test, commit."),
    ("Skip tests per slice", "Each slice verified before next."),
    ("Slice too large", "Thin enough for one review pass."),
    ("No git checkpoint", "Commit after each verified slice."),
], [
    "Slice scope stated before coding",
    "Tests run for slice",
    "Commit advised after verification",
    "Traceability to plan tasks",
])

# --- Setup ---
entry("project-setup", [
    ("Copy template AGENTS.md", "Interview user for gaps and routing."),
    ("Skip knowledge-graph bootstrap", "Step 6b builds graph when skill installed."),
    ("Install every skill", "Recommend subset from interview."),
    ("Skip memory skeleton", "docs/memory/ scaffold required."),
], [
    "AGENTS.md tailored to project",
    "Skill routing matches installed skills",
    "docs/memory/ skeleton present",
    "Graph bootstrap attempted if knowledge-graph present",
])

entry("retroactive-project-setup", [
    ("Modify source code", "Read-only survey — infra only."),
    ("Guess without manifests", "Infer from package files, README, git."),
    ("Skip ADR-0001", "Bootstrap decision recorded."),
    ("One-shot without gaps", "Ask only about true ambiguities."),
], [
    "No application source modified",
    "AGENTS.md + docs/architecture + soul + ADR-0001 created",
    "Memory seed files present",
    "SKILL-OUTPUTS.md lists all artifacts",
])

entry("skill-finder", [
    ("Invent skill inline", "Route to universal-skill-creator for new skills."),
    ("First match only", "List top 2–3 with disambiguation."),
    ("Ignore project skills", "Check local .agents/skills first."),
    ("Skip INDEX", "docs/SKILL-INDEX.md is authoritative."),
], [
    "2–3 candidates with trigger overlap noted",
    "Project-local skills checked",
    "Recommendation names one primary skill",
    "Creator route if no match",
])

entry("tool-finder", [
    ("Tool = skill", "Tools execute; skills instruct."),
    ("Unverified CLI", "Cite docs or mark UNVERIFIED."),
    ("Install without ask", "Propose install — don't run without approval."),
    ("Ignore project constraints", "Respect stack and policy."),
], [
    "Tool matched to task with rationale",
    "Install/command documented",
    "Project constraints acknowledged",
    "UNVERIFIED flagged when applicable",
])


for s in ("skill-finder",):
    pass  # covered above

# Verification-only (already have rationalizations)
entry("git-workflow-and-versioning", [], [
    "Commit message follows convention",
    "Scope is single logical change",
    "Handoff completed if user triggered via commit/push",
    "No secrets in committed files",
])
entry("incremental-implementation", [], [
    "Slice scope stated before coding",
    "Tests run for slice",
    "Commit advised after verification",
    "Traceability to plan tasks",
])
entry("memory-startup", [], [
    "project-index and latest handoff consulted",
    "Git status compared to handoff note",
    "Summary under 2–4 lines for user",
    "No full history load",
])
entry("spec-crosscheck", [], [
    "Every spec requirement mapped to plan task or explicit gap",
    "Constitution violations flagged",
    "Report delivered before code merge",
    "Orchestrator notified of blockers",
])


def insert_before_anchor(text: str, section: str, anchors: list[str]) -> str:
    for anchor in anchors:
        idx = text.find(anchor)
        if idx != -1:
            return text[:idx].rstrip() + "\n\n" + section + "\n\n" + text[idx:].lstrip()
    return text.rstrip() + "\n\n" + section + "\n"


def trim_for_budget(text: str, max_lines: int = 200) -> str:
    lines = text.splitlines()
    while len(lines) > max_lines:
        new_lines: list[str] = []
        in_rat = False
        rat_data = 0
        removed = False
        for ln in lines:
            if ln.startswith("## Common Rationalizations"):
                in_rat = True
                new_lines.append(ln)
                continue
            if in_rat and ln.startswith("## "):
                in_rat = False
            if in_rat and ln.startswith("|") and "---" not in ln and "Excuse" not in ln:
                rat_data += 1
                if rat_data > 3:
                    removed = True
                    continue
            new_lines.append(ln)
        if removed:
            lines = new_lines
            continue
        # compress impact report
        text_joined = "\n".join(lines)
        text_joined = re.sub(
            r"(## Impact Report\n\n)(?:After completing[^\n]*\n)?```\n(.*?)```",
            lambda m: f"{m.group(1)}`{' '.join(m.group(2).split())[:180]}`",
            text_joined,
            flags=re.DOTALL,
        )
        lines = text_joined.splitlines()
        if len(lines) > max_lines:
            # drop red flags section if present (lowest priority)
            text_joined = re.sub(r"\n## Red Flags\n\n.*?(?=\n## |\n---\n|\Z)", "\n", text_joined, flags=re.DOTALL)
            lines = text_joined.splitlines()
        if len(lines) <= max_lines:
            break
        # remove one blank
        nl = []
        skipped = False
        for ln in lines:
            if not skipped and ln.strip() == "":
                skipped = True
                continue
            nl.append(ln)
        if nl == lines:
            break
        lines = nl
    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def main() -> int:
    anchors = ["Read `references/examples.md`", "## Impact Report", "---\n\nRead "]
    updated = 0
    for name, parts in sorted(RAT_VER.items()):
        skill_md = SKILLS / name / "SKILL.md"
        if not skill_md.exists():
            continue
        text = skill_md.read_text(encoding="utf-8")
        if "category: project-specific" not in text:
            continue
        orig = text
        if "rat" in parts and "## Common Rationalizations" not in text:
            text = insert_before_anchor(text, parts["rat"], anchors)
        if "ver" in parts and "## Verification" not in text:
            text = insert_before_anchor(text, parts["ver"], anchors)
        if "flags" in parts and "## Red Flags" not in text:
            text = insert_before_anchor(text, parts["flags"], anchors)
        if len(text.splitlines()) > 200:
            text = trim_for_budget(text, 200)
        if text != orig:
            skill_md.write_text(text, encoding="utf-8")
            print(f"updated: {name} ({len(text.splitlines())} lines)")
            updated += 1
    print(f"Total updated: {updated}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
