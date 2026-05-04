# Changelog: Spec-Driven Development Skill Suite

**Date:** 2026-05-04
**Type:** New skill family — 4 new skills, 1 reference file, 5 augmented existing skills
**Bar to beat:** GitHub Spec Kit (7 slash commands across 7 generated artifacts), AWS Kiro specs-first workflow

---

## What Changed

### 4 new skills added

| # | Skill | Lines | Role |
|---|-------|-------|------|
| 1 | `spec-driven-development` | 100 | Thin orchestrator. Routes the seven SDD slash commands (`/constitution`, `/specify`, `/clarify`, `/plan`, `/tasks`, `/analyze`, `/implement`) to the right leaf skill. Enforces phase order — never writes content directly. |
| 2 | `project-constitution` | 126 | Authors the project's irreducible engineering invariants — `C-N.M` rules across testing, security, performance, accessibility, dependencies, observability, migration, documentation. Versioned with an Amendments log. The third strategic artifact alongside AGENTS.md (agent behavior) and product-soul (strategy). |
| 3 | `feature-spec` | 140 | The missing core SDD artifact — executable WHAT+WHY. Owns both `/specify` and `/clarify` modes. Hard gate: cannot mark `Approved` while any `[NEEDS CLARIFICATION]` markers remain. Acceptance Criteria as Given/When/Then. Constitution waivers must be explicit. |
| 4 | `spec-crosscheck` | 140 | Hard readiness gate before implementation. Six checks: spec readiness, constitution coverage, spec→plan traceability, plan→spec traceability (no scope creep), task quality (DoD + target), out-of-scope adherence. Read-only — never modifies artifacts. Returns PASS/FAIL with `file:line` evidence. |

All four SKILL.md files are ≤200 lines (the project's hard rule). Total scope: 506 SKILL.md lines + 1 schema reference (96 lines).

### 1 reference file created

**`feature-spec/references/`**
- `feature-spec-schema.md` — full spec template (frontmatter + body), status lifecycle (Draft → Clarifying → Approved), cross-reference contract that other skills read, style guidelines

### 5 existing skills augmented (no regressions, all ≤200)

| Skill | Lines | Change |
|-------|-------|--------|
| `brainstorming` | 134 | Narrowed trigger phrasing (removed generic "spec" language). Step 10 now offers `feature-spec` handoff for SDD projects, in addition to `prd-writing` and `implementation-plan`. |
| `prd-writing` | 120 | Removed generic "write a spec" / "turn this into a spec" triggers. Added explicit boundary note: feature-specs are the executable contract; PRDs frame the product. |
| `problem-to-plan` | 137 | Repositioned as the tactical fast path (bugs, narrow refactors). Mini-spec renamed to "change-spec" in description. New gotchas: (a) feature-sized work routes to SDD; (b) if an Approved feature-spec exists, derive plan/TODO from it instead of writing a new change-spec. |
| `implementation-plan` | 135 | Reads `docs/specs/<slug>-feature-spec.md` first when present (refuses to proceed if status≠Approved). Reads `docs/constitution.md` for C-N rules. New **Step 4b — Requirement Traceability** section. Tasks-only mode for `/tasks`. Tells user to run `/analyze` next. |
| `project-setup` | 163 | New **Step 1d** detects SDD intent (existing constitution/specs/reviews) and asks if the project is specs-first. Offers `project-constitution` immediately after AGENTS.md saves when `sdd_mode: on`. SDD chain added to Orchestration Map. New rule for AGENTS.md: "When behavior changes, update the feature-spec first; the plan and tasks regenerate from it." |

---

## Phase Map (mirrors GitHub Spec Kit / Kiro slash-command shape)

| Slash command   | Intent                                | Routes to                                       |
|-----------------|---------------------------------------|-------------------------------------------------|
| `/constitution` | author or amend project rules         | `project-constitution`                          |
| `/specify`      | write a new feature spec              | `feature-spec` (mode=specify)                   |
| `/clarify`      | resolve [NEEDS CLARIFICATION] markers | `feature-spec` (mode=clarify)                   |
| `/plan`         | turn approved spec into a phased plan | `implementation-plan` (consumes feature-spec)   |
| `/tasks`        | derive agent-pickable tasks           | `implementation-plan` (tasks-only mode)         |
| `/analyze`      | hard readiness gate                   | `spec-crosscheck`                               |
| `/implement`    | execute the plan                      | `test-driven-development` (or direct execution) |

---

## Library hygiene updates

- **`AGENTS.md`** — added 6 new User Entry Points (spec-driven-development orchestrator, SDD/specs-first synonym, /specify, /clarify, /constitution, /analyze)
- **`docs/SKILL-INDEX.md`** — 4 new entries in Project-Specific section, Call Graph extended with full SDD subgraph (orchestrator routing + leaf skill cross-reads + brainstorming handoffs), Leaf Nodes list updated with `project-constitution` and `spec-crosscheck`, date bumped to 2026-05-02
- **`.agents/ROUTING.md`** — new **Spec-Driven Development Layer** section partitions four trigger groups (orchestrator, feature-spec, project-constitution, spec-crosscheck) with explicit "NOT this skill" callouts. Four new Hard Boundaries enforce: feature-spec ≠ brainstorming ≠ prd-writing; problem-to-plan stays tactical; orchestrator never writes directly; phase order is enforced

---

## Why this matters

agent-loom was previously **plan-first, not spec-first.** It had:
- `brainstorming` (design docs)
- `prd-writing` (product framing)
- `problem-to-plan` (tactical mini-specs)
- `implementation-plan` (phased roadmaps)

But it was **missing the three irreducible SDD primitives** that GitHub Spec Kit, AWS Kiro, and Amazon's specs-first workflow treat as non-negotiable in 2026:

1. **A constitution layer** — project-wide rules every spec must obey. AGENTS.md covers agent behavior; product-soul covers strategy; neither covers "every spec must be true to these engineering invariants."
2. **An executable feature spec artifact** — machine-parseable WHAT+WHY with no architecture, no library choices, no file paths. Acceptance criteria as Given/When/Then. Living source of truth that code is regenerated from, not the other way around.
3. **A hard readiness gate before implementation** — explicit consistency check across constitution + spec + plan + tasks, returning PASS/FAIL with evidence.

This release ships all three plus a thin orchestrator that mirrors the familiar slash-command shape without bloating the library into a 7-skill clone of Spec Kit.

---

## Boundary partition (the headline outcome)

```diagram
╭───────────────────╮  ╭──────────────────╮  ╭──────────────────╮
│ product-soul      │  │   AGENTS.md      │  │project-constitut.│
│  (strategy)       │  │ (agent behavior) │  │  (eng invariants)│
╰───────────────────╯  ╰──────────────────╯  ╰────────┬─────────╯
                                                      │
        ╭──────────────────╮       ╭──────────────────▼─────────╮
        │  brainstorming   │──┐    │ spec-driven-development    │
        │  (design/arch)   │  │    │  /constitution /specify    │
        ╰──────────────────╯  │    │  /clarify /plan /tasks     │
                              │    │  /analyze /implement       │
        ╭──────────────────╮  │    ╰────────┬───────────────────╯
        │  prd-writing     │──┤             │ delegates
        │  (product/PM)    │  │             ▼
        ╰──────────────────╯  │    ╭──────────────────╮
                              ├───▶│  feature-spec    │ ◀── /specify, /clarify
        ╭──────────────────╮  │    ╰────────┬─────────╯
        │ problem-to-plan  │  │             │ Approved
        │ (tactical only)  │  │             ▼
        ╰──────────────────╯  │    ╭──────────────────╮
                              └───▶│implementation-plan│ ◀── /plan, /tasks
                                   │ + traceability   │
                                   ╰────────┬─────────╯
                                            ▼
                                   ╭──────────────────╮
                                   │ spec-crosscheck  │ ◀── /analyze
                                   │ PASS|FAIL gate   │
                                   ╰────────┬─────────╯
                                            │ PASS
                                            ▼
                                   ╭──────────────────╮
                                   │test-driven-dev   │ ◀── /implement
                                   ╰──────────────────╯
```

---

## Skill count

**70 → 74** total skills.

## File counts

- 5 files created (4 SKILL.md + 1 reference schema)
- 8 files edited (5 SKILLs + AGENTS.md + SKILL-INDEX.md + ROUTING.md)
- 0 files deleted, 0 skills deprecated (`problem-to-plan` placed on watch — re-evaluate after one improvement cycle)

## Migration notes

- **Existing projects** continue to work unchanged. SDD is opt-in via `project-setup` Step 1d ("Is this a specs-first project?").
- **Existing `docs/specs/*.md` files** from `brainstorming` (suffix `-design.md`) and `problem-to-plan` (suffix `-spec.md`) are unaffected. New SDD artifacts use the `*-feature-spec.md` suffix.
- **No breaking trigger changes.** Generic phrases like "spec this out" no longer route to `problem-to-plan` first — they now route to `feature-spec` or `spec-driven-development`. If you genuinely want the tactical fast path, say "plan this change" or invoke `problem-to-plan` directly.
- **For SDD projects:** invoke `spec-driven-development` (or any slash command) at any phase. The orchestrator detects current state and refuses out-of-order phases with a clear message.

---

## Verification

- All 9 affected skills measured under the 200-line hard rule (range: 100–163 lines)
- All cross-references between skills (Calls / Called by / Cited by / Reads) consistent across SKILL files, SKILL-INDEX.md Call Graph, and ROUTING.md routing rules
- AGENTS.md User Entry Points and SKILL-INDEX.md User Entry Points lists synchronized
