# Agent System Architecture — Full Worked Examples

Skill: `agent-system-architecture` | Load when producing output for this workflow.

## Example 1 — From skill workflow

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

## Example 2 — Typical invocation

**Input:** "Run `agent-system-architecture` for [concrete task]"

**Output:**
```
Invoked `agent-system-architecture`.
Step 1: Define the Objective
Step 2: Select Orchestration Pattern
Step 3: Define Wiring & Communication
See SKILL.md Impact Report schema.
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
