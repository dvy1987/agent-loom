# Architectural Decision Log (ADL) — Full Worked Examples

Skill: `architectural-decision-log` | Load when producing output for this workflow.

## Example 1 — From skill workflow

**Input:** We just decided to use SQLite instead of PostgreSQL for our internal tool. Record this as an ADR.

**Output:**
```
**ADR-005: Use SQLite for Internal Tool Database**
**Date:** 2026-04-12 | **Status:** Accepted

**Context:**
The tool is single-user, deployed locally, with <10K records. We need a database that requires zero infrastructure setup and ships as a single file for easy backup and portability.

**Decision:**
Use SQLite as the primary database via sync SQLAlchemy.

**Alternatives Considered:**
- **PostgreSQL:** Full ACID, rich query support, excellent tooling. Rejected: requires a running server process, Docker or system install, connection management — all unnecessary overhead for a single-user local tool.
- **JSON flat files:** Zero dependencies, human-readable. Rejected: no query capability, no schema enforcement, concurrent write corruption risk, does not scale past ~1K records without performance degradation.

**Consequences:**
- ✓ Zero infrastructure — database is a single `.db` file
- ✓ No connection pooling, no server process, instant setup
- Tradeoff: No concurrent write support — acceptable for single-user but blocks future multi-user
- Tradeoff: Limited full-text search — may need FTS5 extension if search becomes critical
- If we ever need multi-user, this decision must be superseded (migration to PostgreSQL)

ADR recorded: ADR-005: Use SQLite for Internal Tool Database
Number: 005
Status: Accepted
Alternatives considered: 2
Critical consequences: No concurrent writes, limited FTS
Ready for: implementation
```

## Example 2 — Typical invocation

**Input:** "Run `architectural-decision-log` for [concrete task]"

**Output:**
```
Invoked `architectural-decision-log`.
Step 1: Identify the Decision
Step 2: Gather Context & Options
Step 3: Draft the ADR
See SKILL.md Impact Report schema.
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
