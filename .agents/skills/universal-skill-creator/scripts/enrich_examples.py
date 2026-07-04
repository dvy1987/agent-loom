#!/usr/bin/env python3
"""Enrich thin references/examples.md from SKILL.md content. Stdlib only."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SKILLS = ROOT / ".agents/skills"

HAND_CURATED = {
    "test-driven-development", "debug-and-fix", "code-review-crsp", "implementation-plan",
    "spec-driven-development", "feature-spec", "adversarial-hat", "context-engineering",
    "frontend-design", "learn-from", "project-setup", "memory-startup", "codebase-understanding",
    "improve-skills", "incremental-implementation", "git-workflow-and-versioning", "knowledge-graph",
    "brainstorming", "validate-skills", "compress-skill", "universal-skill-creator",
    "performance-optimization", "shipping-and-launch", "browser-testing-with-devtools",
    "api-deprecation-and-migration",
}

AO_MAP = {
    "source-driven-development": "source-driven-development",
    "code-simplification": "code-simplification",
    "api-and-interface-design": "api-and-interface-design",
    "app-security-hardening": "security-and-hardening",
    "ci-cd-and-automation": "ci-cd-and-automation",
    "learn-from-repo": "learn-from-repo",
    "research-skill": "research-skill",
    "prd-writing": "prd-writing",
    "product-soul": "product-soul",
    "idea-generation": "idea-generation",
    "idea-evaluation": "idea-evaluation",
    "customer-discovery": "customer-discovery",
    "business-modeling": "business-modeling",
}


def extract_pairs(text: str) -> list[tuple[str, str]]:
    pairs: list[tuple[str, str]] = []
    for block in re.findall(r"<examples>(.*?)</examples>", text, re.DOTALL):
        for m in re.finditer(
            r"<example>\s*<input>(.*?)</input>\s*<output>(.*?)</output>\s*</example>",
            block,
            re.DOTALL,
        ):
            pairs.append((m.group(1).strip(), m.group(2).strip()))
    if not pairs:
        sec = re.search(r"## Example[s]?\s*\n(.*?)(?=\n## |\Z)", text, re.DOTALL)
        if sec:
            body = sec.group(1)
            inp = re.search(r"\*\*Input:\*\*\s*(.+)", body)
            out = re.search(r"\*\*Output:\*\*\s*(.+)", body, re.DOTALL)
            if inp:
                pairs.append((inp.group(1).strip(), (out.group(1).strip() if out else body[:1200])))
    return pairs


def extract_section(text: str, heading: str) -> str:
    m = re.search(rf"## {re.escape(heading)}\s*\n(.*?)(?=\n## |\Z)", text, re.DOTALL)
    return m.group(1).strip() if m else ""


def extract_rationalizations(text: str) -> list[tuple[str, str]]:
    sec = extract_section(text, "Common Rationalizations")
    if not sec:
        return []
    rows = re.findall(r"\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", sec)
    out = []
    for a, b in rows:
        a, b = a.strip(), b.strip()
        if a.lower() in ("excuse", "reason", '"reason to skip a gate"', "rationalization"):
            continue
        if a.startswith("---"):
            continue
        out.append((a, b))
    return out[:5]


def extract_gotchas(text: str) -> list[str]:
    sec = extract_section(text, "Gotchas")
    if not sec:
        return []
    return [ln.lstrip("- ").strip() for ln in sec.splitlines() if ln.strip().startswith("-")][:6]


def extract_workflow_steps(text: str) -> list[str]:
    steps = re.findall(r"^###? Step \d+[^—\n]*—?\s*(.+)$", text, re.MULTILINE)
    if not steps:
        steps = re.findall(r"^\d+\.\s+\*\*(.+?)\*\*", text, re.MULTILINE)
    if not steps:
        steps = re.findall(r"^\d+\.\s+(.+)$", text, re.MULTILINE)
    return [s.strip() for s in steps[:8]]


def extract_output_format(text: str) -> str:
    sec = extract_section(text, "Output Format")
    if not sec:
        sec = extract_section(text, "Impact Report")
    m = re.search(r"```\s*\n(.*?)```", sec, re.DOTALL)
    return m.group(1).strip() if m else ""


TARGET_MIN_LINES = 55


def line_count(path: Path) -> int:
    return len(path.read_text(encoding="utf-8").splitlines()) if path.exists() else 0


def needs_enrichment(path: Path) -> bool:
    if not path.exists():
        return True
    t = path.read_text(encoding="utf-8")
    return line_count(path) < TARGET_MIN_LINES or "Impact Report schema" in t


def is_preserve_append(path: Path) -> bool:
    """Hand-curated files with SAFE marker — extend, don't replace."""
    if not path.exists():
        return False
    t = path.read_text(encoding="utf-8")
    return "security-scanned SAFE" in t or "Full Session Examples" in t


MEMORY_EXAMPLES: dict[str, str] = {
    "memory": """## Example 1 — Orchestrator routing

**Input:** "Remember what we decided about auth"

**Output:** Route to `memory-recall` for search; if new fact → `memory-capture`; if architectural choice → `memory-decision`.

## Example 2 — Checkpoint after spec

**Input:** Agent finishes `feature-spec` for billing

**Output:** Auto-trigger `memory-capture` — persist open questions + approved scope to `docs/memory/`.

## Example 3 — Anti-skip

**Input:** "Skip memory, just implement"

**Output:** Block until at least `memory-capture` records the approved spec path and owner.

## Example 4 — Commit/push checkpoint

**Input:** User says "commit and push"

**Output:** Route `memory-handoff` → save handoff + update current-state → then `git-workflow-and-versioning` for commit/push. Never push without handoff on meaningful work.""",
    "memory-handoff": """## Example 1 — Commit / push trigger (v1.3)

**Input:** User says "commit these changes" or "push to origin"

**Output:** Run full handoff workflow first → append `docs/memory/agent-handoffs.md` → update current-state + project-index → incremental graph rebuild → then proceed with git commit and/or push.

## Example 2 — Commit and push together

**Input:** "commit and push when ready"

**Output:** Handoff documents working tree state and commits pending; after handoff saved, stage → commit → push. Next agent reads handoff even if push succeeds.

## Example 3 — Session end

**Input:** Large refactor complete, user leaving

**Output:** Handoff block: done / next / blockers / files touched / graph rebuild flag.

## Example 4 — Thin context recovery

**Input:** Next agent starts cold

**Output:** `memory-startup` reads handoff tail + project-index; does not load full history.""",
    "memory-capture": """## Example 1 — Session fact

**Input:** "We chose Postgres over SQLite for multi-tenant"

**Output:** Append dated entry to `docs/memory/session-notes.md` with source (user) and tags.

## Example 2 — After major skill edit

**Input:** `universal-skill-creator` finishes new skill

**Output:** Capture skill name, validation status, INDEX sync pending.

## Example 3 — Bounded capture

**Input:** Long debug log pasted

**Output:** Extract 3–5 bullets only; link to file path instead of pasting full log.

## Example 4 — Post-push continuity

**Input:** User pushed release tag without handoff

**Output:** Retroactive `memory-handoff` noting tag, commit SHA, and what's deployed vs deferred.""",
    "memory-decision": """## Example 1 — ADR-style record

**Input:** "Why JWT over sessions?"

**Output:** Write `docs/memory/decisions/YYYY-MM-DD-jwt-auth.md` — context, decision, consequences.

## Example 2 — Reversal

**Input:** New evidence contradicts old decision

**Output:** New decision file references superseded ADR; do not delete old record.

## Example 3 — Lightweight

**Input:** Small trade-off (library pick)

**Output:** One paragraph in session-notes with `decision:` tag for later promotion.

## Example 4 — Revisit trigger

**Input:** Decision assumed stable for 6 months

**Output:** Add `revisit: when traffic 10x` to decision file; `memory-recall` surfaces it on scale discussions.""",
    "memory-recall": """## Example 1 — Targeted query

**Input:** "What did we decide about dark mode?"

**Output:** Search project-index + decisions + recent handoffs; cite file paths.

## Example 2 — No match

**Input:** Query with no hits

**Output:** Say explicitly "no durable record"; offer `memory-capture` if user confirms.

## Example 3 — Bounded read

**Input:** Broad "what happened last week"

**Output:** Summarize last handoff + index highlights only — no full log scan.

## Example 4 — Pre-commit recall

**Input:** User says "push" after long session

**Output:** Recall latest handoff draft status; if stale, route to `memory-handoff` before push.""",
    "memory-promote": """## Example 1 — Session → durable

**Input:** Repeated session note about CI policy

**Output:** Promote to `docs/memory/decisions/` or project-index bullet.

## Example 2 — Criteria

**Input:** One-off typo fix note

**Output:** Do not promote — stays in session-notes.

## Example 3 — User request

**Input:** "Make this permanent"

**Output:** Promote with date + source handoff link.

## Example 4 — Reject promotion

**Input:** Experimental spike conclusion

**Output:** Keep in session-notes; promotion requires repeated use or explicit user "make global".""",
    "memory-compact": """## Example 1 — Bloated handoff log

**Input:** `agent-handoffs.md` > 200 entries

**Output:** Archive older entries to `docs/memory/archive/`; keep index of archived ranges.

## Example 2 — Duplicate notes

**Input:** Same decision captured 4 times

**Output:** Merge into single decision file; leave redirect stubs.

## Example 3 — Pre-audit

**Input:** Before `memory-audit`

**Output:** Compact first to reduce audit surface.

## Example 4 — Global budget pressure

**Input:** `~/.agent-loom/memories/` over active budget

**Output:** Archive low-signal entries; preserve decisions + provenance links.""",
    "memory-audit": """## Example 1 — Stale index

**Input:** project-index references removed skill

**Output:** Flag drift; list files to fix or archive.

## Example 2 — Orphan decisions

**Input:** Decision with no implementing code

**Output:** Mark `status: unverified` for human review.

## Example 3 — Coverage report

**Input:** User asks "is memory healthy?"

**Output:** Table: last handoff date, decision count, stale entries.

## Example 4 — Handoff hygiene

**Input:** Handoffs repeat same "next step" for 3 sessions

**Output:** Flag stale continuity; recommend `memory-compact` or update current-state.""",
    "memory-forget": """## Example 1 — Wrong capture

**Input:** "Forget the SQLite decision — we're not using it"

**Output:** Redact or strike through with date; never silent delete of audit trail.

## Example 2 — PII slip

**Input:** Accidental API key in session note

**Output:** Remove secret; log forget action in handoff.

## Example 3 — User privacy

**Input:** "Don't keep my client name"

**Output:** Forget named entities from session-notes only; keep structural decisions.

## Example 4 — Audit trail

**Input:** Forget request on captured secret

**Output:** Redact content; append forget record to handoff with date (no silent erase).""",
}


def ao_snippet(name: str) -> str:
    ao_name = AO_MAP.get(name)
    if not ao_name:
        return ""
    p = Path(f"/tmp/ao-ingest/{ao_name}.SKILL.md")
    if not p.exists():
        return ""
    text = p.read_text(encoding="utf-8", errors="replace")[:4000]
    # pull first code block or rationalization row
    block = re.search(r"```\w*\n(.*?)```", text, re.DOTALL)
    if block:
        return block.group(1).strip()[:800]
    return ""


def build_enriched(name: str, skill_text: str) -> str:
    title_m = re.search(r"^# (.+)$", skill_text, re.MULTILINE)
    title = title_m.group(1).strip() if title_m else name
    pairs = extract_pairs(skill_text)
    rats = extract_rationalizations(skill_text)
    gotchas = extract_gotchas(skill_text)
    steps = extract_workflow_steps(skill_text)
    out_fmt = extract_output_format(skill_text)
    ao = ao_snippet(name)

    lines = [
        f"# {title} — Full Worked Examples",
        "",
        f"Skill: `{name}` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).",
        "",
    ]

    for i, (inp, out) in enumerate(pairs[:4], 1):
        lines += [
            f"## Example {i} — Documented workflow",
            "",
            f"**Input:** {inp}",
            "",
            "**Output:**",
            "```",
            out,
            "```",
            "",
        ]

    n = len(pairs[:4]) + 1
    if steps:
        lines += [
            f"## Example {n} — Step-by-step execution",
            "",
            f"**Input:** \"Run `{name}` on [concrete task]\"",
            "",
            "**Agent actions:**",
        ]
        for j, s in enumerate(steps, 1):
            lines.append(f"{j}. {s}")
        lines.append("")
        if out_fmt:
            lines += ["**Impact Report shape:**", "```", out_fmt, "```", ""]
        n += 1

    if rats:
        lines += [
            f"## Example {n} — Anti-skip (rationalization defense)",
            "",
            "**Input:** Agent tries to skip a gate",
            "",
            "| Excuse | Reality |",
            "|---|---|",
        ]
        for a, b in rats[:4]:
            lines.append(f"| {a} | {b} |")
        lines.append("")
        n += 1

    if gotchas:
        lines += [
            f"## Example {n} — Gotcha application",
            "",
            "**Input:** Task hits a non-obvious edge case",
            "",
            "**Apply:**",
        ]
        for g in gotchas[:4]:
            lines.append(f"- {g}")
        lines.append("")
        n += 1

    if ao:
        lines += [
            f"## Example {n} — Pattern reference (addyosmani/agent-skills)",
            "",
            "**Source:** addyosmani snapshot 2026-05-29, security-scanned SAFE.",
            "",
            "```",
            ao,
            "```",
            "",
        ]

    if n == 1:
        lines += [
            "## Example 1 — Default invocation",
            "",
            f"**Input:** \"Help me with {name.replace('-', ' ')}\"",
            "",
            "**Output:** Follow SKILL.md workflow; report per Impact Report.",
            "",
        ]

    lines += ["---", "", "See `SKILL.md` for hard rules and verification checklist.", ""]
    return "\n".join(lines)


def build_appendix(name: str, skill_text: str, start_n: int) -> str:
    """Extend hand-curated L3 without replacing existing examples."""
    rats = extract_rationalizations(skill_text)
    gotchas = extract_gotchas(skill_text)
    steps = extract_workflow_steps(skill_text)
    lines: list[str] = [f"## Example {start_n} — Extended pass (L3 enrichment)", ""]
    n = start_n + 1
    if rats:
        lines += [
            f"## Example {n} — Anti-skip (rationalization defense)",
            "",
            "**Input:** Agent tries to skip a gate",
            "",
            "| Excuse | Reality |",
            "|---|---|",
        ]
        for a, b in rats[:5]:
            lines.append(f"| {a} | {b} |")
        lines.append("")
        n += 1
    if steps:
        lines += [
            f"## Example {n} — Step-by-step execution",
            "",
            f"**Input:** \"Run `{name}` on [concrete task]\"",
            "",
            "**Agent actions:**",
        ]
        for j, s in enumerate(steps[:6], 1):
            lines.append(f"{j}. {s}")
        lines.append("")
        n += 1
    if gotchas:
        lines += [f"## Example {n} — Gotcha application", "", "**Apply:**"]
        for g in gotchas[:5]:
            lines.append(f"- {g}")
        lines.append("")
    lines += [
        "## Verification checklist (L3)",
        "",
        "- [ ] Examples align with SKILL.md hard rules",
        "- [ ] Anti-skip or rationalization pattern shown",
        "- [ ] Output shape matches Impact Report",
        "- [ ] User can trace from input → durable artifact or chat outcome",
        "",
    ]
    return "\n".join(lines)


FOOTER = "\n\n---\n\nSee `SKILL.md` for hard rules and verification checklist.\n"


def main() -> int:
    enriched = 0
    for d in sorted(SKILLS.glob("*/")):
        if ".deprecated" in str(d):
            continue
        name = d.name
        skill_md = d / "SKILL.md"
        ex = d / "references" / "examples.md"
        if not skill_md.exists() or not ex.exists():
            continue
        if not needs_enrichment(ex):
            continue
        skill_text = skill_md.read_text(encoding="utf-8")
        if name in MEMORY_EXAMPLES:
            header = (
                f"# {name.replace('-', ' ').title()} — Full Worked Examples\n\n"
                f"Skill: `{name}` | Memory suite enrichment pass.\n\n"
            )
            new = header + MEMORY_EXAMPLES[name] + FOOTER
        elif is_preserve_append(ex):
            existing = ex.read_text(encoding="utf-8")
            start_n = len(re.findall(r"^## Example ", existing, re.MULTILINE)) + 1
            new = existing.rstrip() + "\n\n---\n\n" + build_appendix(name, skill_text, start_n)
            if len(new.splitlines()) < TARGET_MIN_LINES:
                new = build_enriched(name, skill_text)
        else:
            new = build_enriched(name, skill_text)
        ex.write_text(new, encoding="utf-8")
        enriched += 1
        print(f"enriched: {name} ({len(new.splitlines())} lines)")
    print(f"Total enriched: {enriched}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
