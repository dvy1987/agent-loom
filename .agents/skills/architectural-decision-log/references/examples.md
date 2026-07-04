# Architectural Decision Log (ADL) — Full Worked Examples

Skill: `architectural-decision-log` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

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

## Example 2 — Step-by-step execution

**Input:** "Run `architectural-decision-log` on [concrete task]"

**Agent actions:**
1. Identify the Decision
2. Gather Context & Options
3. Draft the ADR
4. Link to Previous Decisions
5. Present and Save
6. Memory Checkpoint (Mandatory)

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- The highest-value ADR content is the rejected alternatives with rejection reasons — not the chosen option. Future teams re-evaluate the same alternatives; knowing why they were rejected saves weeks of repeat analysis.
- ADRs written retrospectively produce confabulated reasoning. Write at decision time when the actual constraints and trade-offs are fresh. A rough ADR today beats a polished one written from memory next month.
- "Accepted" is not permanent. Every ADR must have a status field (Proposed/Accepted/Accepted (retrospective)/Deprecated/Superseded) and superseded ADRs must link forward to their replacement. Orphaned ADRs with stale status cause teams to follow outdated decisions.
- `SYNTHESIS` mode is honest, not confident. Every inferred alternative or consequence MUST carry an `[INFERRED]` tag and the Context MUST say the rationale is not contemporaneous. Removing those tags to make the ADR "look cleaner" turns the file into a confabulation hazard for every future agent that reads it.

---

See `SKILL.md` for hard rules and verification checklist.
