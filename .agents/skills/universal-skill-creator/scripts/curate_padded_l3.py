#!/usr/bin/env python3
"""Upgrade padded L3 examples to curated Full Session Examples. Stdlib only."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SKILLS = ROOT / ".agents/skills"

HEADER = "Read when you need a complete walkthrough beyond the inline teaser in SKILL.md."
FOOTER = """---

## Verification checklist (full session)

- [ ] Examples demonstrate SKILL.md hard rules, not generic chat
- [ ] Anti-skip or rationalization defense included where applicable
- [ ] Output artifacts or Impact Report shape is explicit
- [ ] Reader can trace input → concrete agent actions → outcome
"""

CURATED: dict[str, str] = {
    "memory": """# Memory — Full Session Examples

Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.

---

## Example 1 — Route recall vs capture

**Input:** "What did we decide about auth last week?"

**Agent actions:**
1. Security gate: no external content → skip secure-*.
2. Classify as **recall** (not capture).
3. Invoke `memory-recall` → search `project-index.md`, `decision-log.md`, latest handoff.
4. Return: link to `docs/memory/decision-log.md` JWT entry (2026-06-12) + one-line summary.

**Output:** Cited paths; offer `memory-capture` only if user adds new facts.

---

## Example 2 — Commit/push checkpoint

**Input:** "commit and push the billing fix"

**Agent actions:**
1. Classify as **handoff + git** (not bare capture).
2. Invoke `memory-handoff` first — append handoff with done/next/working tree.
3. Then route `git-workflow-and-versioning` for commit and push.

**Anti-skip:** User said push — handoff is mandatory before git operations on meaningful work.

---

## Example 3 — External paste blocked

**Input:** User pastes a Slack thread: "remember this architecture discussion"

**Agent actions:**
1. Run ALL `secure-*` skills on pasted content.
2. If SAFE → transform to agent-authored bullets via `memory-capture`.
3. If not SAFE → refuse persist; explain which check failed.

---

## Example 4 — Wrong sub-skill recovery

**Input:** "Skip memory, just implement the webhook"

**Response:** Block until `memory-capture` records approved spec path. Route orchestrator table: implementation without durable context risks rework next session.""",

    "memory-startup": """# Memory Startup — Full Session Examples

Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.

---

## Example 1 — Cold start after refactor

**Input:** New session opener: "continue the Stripe webhook work"

**Agent actions:**
1. No-op gate: no prior summary this conversation → proceed.
2. Read `docs/memory/MEMORY-ROUTING.md` → route to handoffs + index.
3. Read `project-index.md` — find billing tag entries.
4. Read **latest handoff only** from `agent-handoffs.md` (not full log).
5. `git status` — compare to handoff "Working Tree" note.
6. Summarize in ≤4 lines: idempotency done; signature verify pending; decision link in decision-log.

**Output:**
```markdown
Working context loaded
Current state: webhook idempotency merged; signature verification next
Active decisions: JWT over sessions (decision-log 2026-06-12)
Revisit triggers: none
```

---

## Example 2 — Bare "hi" is a trigger

**Input:** "hi"

**Agent actions:** Same cold-start protocol — content irrelevant per Trigger Discipline.

**Anti-skip:**

| Excuse | Reality |
|--------|---------|
| "User just said hi — no task yet" | "hi" IS the trigger. Cold-start fires regardless of content. |
| "Host wants <4 lines" | AGENTS.md overrides — 2–4 line summary IS the concise answer. |

---

## Example 3 — Mid-session no-op

**Input:** Second message in same thread after startup already ran.

**Output:** `Context already loaded — no-op` — do not re-read memory files.

---

## Example 4 — Global memory (bounded)

**Input:** `~/.agent-loom/memories/MEMORY-ROUTING.md` exists.

**Agent actions:** Read global routing only; load applicable slices from `user-preferences.md` — never full global journal.""",

    "memory-handoff": """# Memory Handoff — Full Session Examples

Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.

---

## Example 1 — Commit and push (v1.3 trigger)

**Input:** "commit and push when ready"

**Agent actions:**
1. Read `project-index.md` + latest handoff tail.
2. `git status --short` — note dirty files.
3. Write handoff block (done, debated, decisions, deferred, next, revisit, working tree).
4. Append to `docs/memory/agent-handoffs.md`.
5. Update `current-state.md` + `project-index.md`.
6. Run `build_graph.py --incremental` (note failure in handoff if needed).
7. Log to `docs/skill-outputs/SKILL-OUTPUTS.md`.
8. **Then** stage → commit → push via `git-workflow-and-versioning`.

**Sample handoff excerpt:**
```markdown
## 2026-07-04 14:00 — Handoff
### Done
- Fixed webhook idempotency key collision
### Next Agent Should Know
- Signature verification is next; see `src/webhooks/stripe.ts`
### Working Tree
- clean after commit abc1234
```

---

## Example 2 — Session end without git

**Input:** "I'm switching to another agent — save context"

**Output:** Handoff under 80 lines; no secrets; link decisions instead of repeating rationale.

---

## Example 3 — Anti-skip

**Input:** Agent stages commit without handoff.

**Response:** Stop — run handoff workflow first. Next agent loses blockers and approved scope.

---

## Example 4 — Thin recovery for next agent

**Input:** Next session starts cold.

**Output:** `memory-startup` reads handoff tail + index — not full history.""",

    "memory-capture": """# Memory Capture — Full Session Examples

Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.

---

## Example 1 — Durable fact from user

**Input:** "We chose Postgres over SQLite for multi-tenant"

**Agent actions:**
1. Security gate if content external — here user statement, OK.
2. Extract 3–5 bullets max.
3. Append dated entry to `docs/memory/session-notes.md` with tags `database, decision-candidate`.
4. Update `project-index.md` one-line summary.
5. Suggest `memory-decision` if architectural.

**Output:** Path cited; no full transcript pasted into memory.

---

## Example 2 — After major skill edit

**Input:** `universal-skill-creator` finishes `knowledge-graph` v2.2

**Capture:** Skill name, validation status, INDEX sync pending, commit SHA if known.

---

## Example 3 — Bounded capture (long paste)

**Input:** User pastes 200-line debug log

**Output:** Extract root cause + fix + file paths only; link `logs/debug-2026-07-04.txt` if saved locally — never store raw log in memory.

---

## Example 4 — Post-push without handoff

**Input:** User pushed release tag `v2.1.0` without handoff

**Output:** Retroactive `memory-handoff` noting tag, SHA, deployed vs deferred — then capture release facts.

---

## Example 5 — Anti-skip

**Input:** "Just remember it in chat, don't write files"

**Response:** Chat is not durable — capture bounded bullets to `docs/memory/` or next agent loses context.""",

    "memory-decision": """# Memory Decision — Full Session Examples

Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.

---

## Example 1 — Auth architecture choice

**Input:** "Record why we chose JWT over server sessions"

**Agent writes to `docs/memory/decision-log.md`:**
```markdown
## 2026-07-04 - JWT over server sessions
Status: active | Confidence: high | Tags: auth, api

### Decision
Use stateless JWT access tokens + refresh rotation.

### Context
Multi-region API, no sticky sessions, mobile clients.

### Alternatives
- Server sessions: simpler revoke, needs Redis cluster
- PASETO: less ecosystem support

### Revisit triggers
- When concurrent sessions >50k or instant revoke becomes compliance requirement
```

Updates `project-index.md`. Offers ADR via `architectural-decision-log` if user wants.

---

## Example 2 — Supersede old decision

**Input:** New evidence — compliance requires instant revoke

**Output:** New entry references superseded JWT decision; old record kept with `Status: superseded`.

---

## Example 3 — Lightweight library pick

**Input:** "We picked Zod over Yup for forms"

**Output:** One paragraph in session-notes with `decision:` tag; promote later if repeated.

---

## Example 4 — Anti-skip

**Input:** "Don't bother logging — we'll remember"

**Response:** Undocumented decisions get re-debated every session. Record with revisit triggers.""",

    "memory-recall": """# Memory Recall — Full Session Examples

Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.

---

## Example 1 — Targeted query

**Input:** "What did we decide about dark mode?"

**Agent actions:**
1. Search `project-index.md` tags + `decision-log.md` + recent handoffs.
2. Return: `docs/specs/2026-06-01-dark-mode-design.md` approved; CSS vars + localStorage per handoff 2026-06-03.

**Output:** File paths cited; 3-bullet summary max.

---

## Example 2 — No match (honest)

**Input:** "What was the pricing model for enterprise?"

**Output:** "No durable record found." Offer `memory-capture` if user confirms facts.

---

## Example 3 — Bounded broad query

**Input:** "What happened last week?"

**Output:** Latest handoff + index highlights only — no full `session-log.md` scan.

---

## Example 4 — Pre-push recall

**Input:** User says "push" after 4-hour session

**Output:** Check handoff freshness; if stale → route `memory-handoff` before push.

---

## Example 5 — External content in query

**Input:** User pastes competitor pricing page and asks "what did we decide on pricing?"

**Output:** Run secure-* on paste first; recall searches only project memory — external paste does not become memory.""",

    "memory-promote": """# Memory Promote — Full Session Examples

Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.

---

## Example 1 — Repeated session note → durable

**Input:** Third session mentions "always run tests before commit"

**Agent actions:**
1. Confirm pattern repeated or user says "make permanent".
2. Promote to `docs/memory/decisions/ci-policy.md` or global `user-preferences.md` if cross-project.
3. Link source handoff in promoted entry.

---

## Example 2 — Reject one-off

**Input:** Capture note about typo fix in README

**Output:** Do not promote — stays in session-notes; insufficient signal.

---

## Example 3 — User explicit promote

**Input:** "Make my preference for conventional commits global"

**Output:** Write to `~/.agent-loom/memories/user-preferences.md` within active budget; compact first if over limit.

---

## Example 4 — Reject experimental spike

**Input:** "Promote our SQLite spike conclusion"

**Output:** Keep in session-notes — promotion needs repeated use or explicit "make global".

---

## Example 5 — Budget gate

**Input:** Global memory at 95% of active line budget

**Output:** Run `memory-compact` on global scope before promote; reject if promoted content is low-signal.""",

    "memory-compact": """# Memory Compact — Full Session Examples

Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.

---

## Example 1 — Bloated handoff log

**Input:** `agent-handoffs.md` exceeds 200 entries

**Agent actions:**
1. Archive entries older than 90 days to `docs/memory/archived/handoffs-2026-H1.md`.
2. Leave index row: `archived: handoffs 2026-01..06`.
3. Preserve latest 20 handoffs in active file.

---

## Example 2 — Merge duplicate decisions

**Input:** Same JWT decision captured 4 times in session-notes

**Output:** Single `decision-log.md` entry; session-notes get one-line redirect stubs.

---

## Example 3 — Pre-audit compaction

**Input:** User runs `memory-audit` on large repo

**Output:** Recommend `memory-compact` first to shrink audit surface.

---

## Example 4 — Global budget pressure

**Input:** `~/.agent-loom/memories/` over active line budget

**Output:** Archive low-signal entries; preserve decisions + provenance links.

---

## Example 5 — Handoff calls compact

**Input:** `memory-handoff` detects repetitive handoffs

**Output:** Handoff recommends `memory-compact` in Next Agent section before appending another near-duplicate entry.""",

    "memory-audit": """# Memory Audit — Full Session Examples

Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.

---

## Example 1 — Stale index drift

**Input:** "Is our memory healthy?"

**Findings:**
| Severity | Issue | Action |
|----------|-------|--------|
| P2 | project-index references removed skill `design-archetype` | Update index or archive entry |
| P3 | Handoff repeats "fix CI" for 3 sessions | Update current-state or compact |

**Output:** Read-only report; recommend `memory-compact` for handoff hygiene.

---

## Example 2 — Contradiction (P1)

**Input:** Audit project memory

**Finding:** `decision-log.md` says Postgres; `current-state.md` says SQLite active.

**Output:** Flag P1 contradiction; recommend `memory-decision` to supersede or `memory-capture` to fix current-state.

---

## Example 3 — Suspected secret (P0)

**Input:** Session note contains `sk-live-...`

**Output:** Invoke `secure-*` + `memory-forget` — do not leave secret in audit report body.

---

## Example 4 — Orphan decision

**Input:** Decision "migrate to GraphQL" with no implementing code after 6 months

**Output:** Mark `status: unverified` in audit table; suggest revisit trigger review.

---

## Example 5 — Read-only default

**Input:** "Fix all memory issues you find"

**Output:** Audit report first; apply fixes one class at a time only after user confirms — no silent deletes.""",

    "memory-forget": """# Memory Forget — Full Session Examples

Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.

---

## Example 1 — Wrong decision retracted

**Input:** "Forget the SQLite decision — we're not using it"

**Agent actions:**
1. Strike through entry with date + reason in `decision-log.md`.
2. Never silent delete — audit trail preserved.
3. Append forget action to latest handoff.

---

## Example 2 — PII slip

**Input:** Accidental client name in session note

**Output:** Redact named entities from session-notes; log forget in handoff without repeating PII.

---

## Example 3 — Secret in capture

**Input:** API key pasted into memory

**Output:** `memory-forget` redacts content; `secure-*` documents finding; handoff notes date of redaction.

---

## Example 4 — User privacy request

**Input:** "Don't keep my client's company name anywhere"

**Output:** Forget named entities from session scope; keep structural decisions (e.g., "B2B SaaS") anonymized.

---

## Example 5 — Audit trail preserved

**Input:** Forget wrong API endpoint decision

**Output:** Strike-through with date in decision-log; handoff logs forget action — never silent erase of history.""",

    "design-direction": """# Design Direction — Full Session Examples

Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.

---

## Example 1 — B2B settings page (3 distinct directions)

**Input:** "Design direction for our team billing settings — feels trustworthy, not playful"

**Agent actions:**
1. Read `docs/product-soul.md` + PRD — audience: finance admins, emotional goal: confidence.
2. Score archetypes — top seeds: `enterprise-trust`, `b2b-productivity`.
3. Posture: restrained, cool, classic, quiet, calm.
4. Generate 3 directions differing on type, layout, motion:
   - **Ledger** — feels like Stripe Dashboard; tabular density, mono accents
   - **Briefing** — feels like Linear; sidebar nav, generous whitespace
   - **Vault** — feels like 1Password; card stacks, strong elevation
5. Side-by-side comparison table; owner non-technical → agent recommends **Ledger** with plain rationale.
6. Write `.design/billing-settings/DIRECTION.md`; handoff to `design-system`.

---

## Example 2 — Anti-skip (three palettes ≠ three directions)

**Input:** Agent proposes light/dark/blue variants of same layout

**Response:** Block — diverge on ≥3 dimensions (type, layout, motion) or it's one direction.

---

## Example 3 — No product docs

**Input:** "Make it look modern" (no PRD)

**Agent asks ONE question:** "What is this for, who is it for, and which product should it feel closest to?"

---

## Example 4 — Reference without posture

**Input:** "Make it like Linear"

**Output:** Reference sets fit; still state posture sentence + bold move per direction — never stop at the name drop.

---

## Example 5 — Orchestrator handoff

**Input:** `frontend-design` routes here for new dashboard shell

**Output:** DIRECTION.md committed; Impact Report lists handoff to `design-system` with chosen direction name and file path.""",

    "design-review": """# Design Review — Full Session Examples

Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.

---

## Example 1 — SHIP with minor fixes

**Input:** Review billing settings built against DIRECTION.md "Ledger"

**Agent actions:**
1. Capture screens at 1440px + 375px (Playwright or user paste).
2. Run `scripts/apca.mjs` — 2 pairs fail on secondary button dark mode.
3. Ethical patterns pass; UX heuristics: empty state missing for invoice list.
4. Findings (max 8 prioritized):
   - P0: Add empty state for zero invoices
   - P1: Secondary CTA Lc 42 → target 45 (token `--muted-foreground`)
5. Write `.design/billing-settings/REVIEW.md` — Verdict: **REVISE** (2 blockers).

---

## Example 2 — APCA hard gate

**Input:** "WCAG 4.5:1 passes, ship it"

**Response:** WCAG misreads dark/thin type. Re-run APCA — body text on `bg-muted` fails Lc 68 (<75).

---

## Example 3 — State coverage gate

**Input:** Happy path looks polished

**Output:** FAIL — no loading skeleton on invoice table; no error state on payment failure.

---

## Example 4 — Direction fidelity

**Input:** Hero uses Inter; DIRECTION.md specifies GT Sectra display

**Finding:** "Swap `--font-display` per DIRECTION.md §Typography — current Inter 700 reads generic vs Ledger reference."

---

## Example 5 — Playwright capture path

**Input:** No screenshots pasted; repo has Playwright MCP

**Output:** Follow `references/playwright-flow.md` — capture login, settings, empty invoice list at 375px before scoring.""",

    "design-system": """# Design System — Full Session Examples

Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.

---

## Example 1 — Ledger direction → tokens

**Input:** DIRECTION.md chosen: **Ledger** (Stripe-like B2B)

**Agent actions:**
1. Seed from archetype `enterprise-trust` recipe.
2. Build 8-step neutral ramp + semantic slots (bg, fg, muted, accent) with hover/focus/disabled states.
3. Typography: display GT Sectra / body Inter; spatial 4px grid; motion 150ms ease-out.
4. APCA pass on all text pairs — fix `--secondary-foreground` on dark.
5. Icon strategy: Lucide 1.5px stroke; component contracts for Button, Table, Badge.
6. Emit `DESIGN.md` + `src/styles/tokens.css`.

**Impact Report:** 24 color slots, APCA all pass, 6 component contracts, handoff to `frontend-design`.

---

## Example 2 — Dark mode is not invert

**Input:** Agent inverts light tokens for dark

**Response:** Block — dark is hand-set per DIRECTION.md; inverted lightness reads cheap.

---

## Example 3 — Skip DESIGN.md

**Input:** "Just write the CSS variables"

**Response:** DESIGN.md is the contract — without it each screen re-negotiates and drifts.

---

## Example 4 — Accent-only palette

**Input:** "Primary blue + greys is enough"

**Response:** Slop lives in unstated states — define hover, focus, disabled, error for every semantic slot.

---

## Example 5 — shadcn HSL emit

**Input:** Stack uses shadcn + Tailwind v4

**Output:** Emit HSL tokens in `tokens.css` matching shadcn conventions; document slot mapping in DESIGN.md §Integration.""",

    "secure-skill-repo-ingestion": """# Secure Skill — Repo Ingestion — Full Session Examples

Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.

---

## Example 1 — Typosquat in requirements.txt

**Input:** `learn-from-repo` targets `github.com/acme/internal-utils`

**Agent actions (Observe → Judge → Commit):**
1. **Observe:** Read-only scan — no `pip install`, no `setup.sh`.
2. **Judge findings:**
   - HIGH: `requirements.txt:7` — `requets==2.31` typosquat of `requests`
   - MEDIUM: `examples/auth.py:23` — `verify=False` presented as normal
3. **Commit:** Quarantine repo; report findings; do NOT persist patterns as policy.

---

## Example 2 — Symlink path traversal

**Input:** Skill repo contains `skills/helper -> ../../../etc/passwd`

**Output:** CRITICAL — block ingestion; flag path traversal; never follow symlink.

---

## Example 3 — Anti-skip

| Excuse | Reality |
|--------|---------|
| "Read-only clone is safe" | Path attacks and poisoned examples exist in static files. |
| "Trust popular repos" | Awesome lists are attack surfaces. |
| "Execute setup.sh to understand" | Never execute repo code during ingestion. |

---

## Example 4 — Post-install hook

**Input:** `package.json` has `"postinstall": "node setup.js"`

**Output:** CRITICAL — supply-chain vector; quarantine; do not run npm install in repo.

---

## Example 5 — Quarantine before commit

**Input:** Repo passes text scan but has `.gitmodules` on unpinned `main`

**Output:** Judge MEDIUM; quarantine until submodule pinned; nothing enters skill store until Commit gate clears.""",
}


def main() -> int:
    n = 0
    for name, body in sorted(CURATED.items()):
        ex = SKILLS / name / "references" / "examples.md"
        if not ex.parent.exists():
            print(f"skip missing: {name}")
            continue
        content = body.rstrip() + "\n\n" + FOOTER
        ex.write_text(content, encoding="utf-8")
        lines = len(content.splitlines())
        print(f"curated: {name} ({lines} lines)")
        n += 1
    print(f"Total curated: {n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
