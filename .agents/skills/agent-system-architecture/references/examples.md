# Agent System Architecture — Full Worked Examples

Skill: `agent-system-architecture` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** Design a multi-agent system for automated PR review that checks code quality, security vulnerabilities, and test coverage in parallel.

**Output:**
```
**System Overview:** Parallel review pipeline — three specialist agents analyze a PR independently, results merged by a lightweight aggregator.

**Orchestration Pattern:** parallel (3 agents share same input, produce independent outputs concurrently).

**Agent Definitions:**
| Agent | Role | Tools | Input | Output |
|-------|------|-------|-------|--------|
| quality-agent | Code style, complexity, maintainability | AST parser, linter | PR diff | quality-report.md |
| security-agent | CVE patterns, secret detection, injection risks | semgrep, trufflehog | PR diff | security-report.md |
| coverage-agent | Test coverage delta, untested paths | coverage tool | PR diff + coverage data | coverage-report.md |

**Wiring:** Message-passing. Each agent receives the PR diff as input. No inter-agent communication. Aggregator collects all three reports.

**State & Memory:** Stateless per run. No cross-PR memory. Each agent reads only its input file.

**Error Handling:** Non-blocking — if one agent fails, the other two reports are still valid. Aggregator notes the gap. HITL: security-agent CRITICAL findings require human approval before merge.

Architecture designed: pr-review-pipeline
Pattern chosen: parallel
Number of agents: 3 + aggregator
Coordination complexity: Low
Observability strategy: Token usage + latency per agent logged to manifest
Ready for: implementation-plan
```

## Example 2 — Step-by-step execution

**Input:** "Run `agent-system-architecture` on [concrete task]"

**Agent actions:**
1. Define the Objective
2. Select Orchestration Pattern
3. Define Wiring & Communication
4. Design for Observability
5. Present and Save

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- Shared-blackboard state creates hidden coupling — agents reading stale state produce cascading errors that look like logic bugs. Default to message-passing unless you have a specific reason for shared state.
- "Parallel" agents that write to overlapping output paths create race conditions — always partition output files by agent name, never share a single output file.
- Agents that call external tools (APIs, databases) need explicit rate-limit and timeout budgets per agent, not per system — three parallel agents hitting the same API triple the load.
- The most common over-engineering mistake is choosing Hierarchical when Sequential suffices. Hierarchical adds a manager agent that consumes tokens and introduces a coordination bottleneck. Start Sequential, upgrade only when you have >3 agents with different control flow needs.

---

See `SKILL.md` for hard rules and verification checklist.
