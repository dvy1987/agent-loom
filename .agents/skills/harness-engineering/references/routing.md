# Harness Engineering — Routing

## Disambiguation matrix

| User says | Route | Not |
|-----------|-------|-----|
| "Set up project for agents" | `project-setup` → then `harness-generation` | harness-engineering alone |
| "Generate harness" | `harness-generation` | project-setup (unless no AGENTS.md) |
| "Improve harness" | `harness-engineering` → `harness-evolution` | agent-builder |
| "Design multi-agent" | `agent-builder` (+ harness v0 check) | harness-engineering |
| "What skill next" | `project-orchestrator` | harness-engineering |
| "Is self-improvement real?" | `reality-check` | harness-evolution |
| "Run evals on harness" | `eval-output` → `eval-pipeline` | harness-generation |

## Lifecycle map

```
GREENFIELD:     project-setup → harness-generation → eval-pipeline
LEGACY:         retroactive-project-setup → harness-generation
AGENT-CHAIN:    harness-generation? → agent-builder → setup-evaluation → agent-launcher
IMPROVE:        harness-evolution (eval required)
AUDIT:          reality-check
```

## PROGRAM.md pattern (auto-harness)

For long improvement campaigns, user may author `docs/harness/PROGRAM.md`:

```markdown
# Harness optimization program
Goal: pass@1 on [task set] ≥ [threshold]
Mutable surfaces: docs/harness/, AGENTS.md harness section only
Immutable: eval held-out split, secure-* skills, source code
Stop: 3 rounds without held-out gain
```

`harness-evolution` reads PROGRAM.md as constraints when present.

## Paradigm spectrum (papers)

| Level | Description |
|-------|-------------|
| Human harness engineering | Manual AGENTS.md + skills |
| External meta-agent | Meta-Harness coding-agent proposer |
| Self-harness | Same agent improves own scaffold (Self-Harness) |
| Harness + weights | SIA — **out of scope** for agent-loom |

## Pareto frontier output (Meta-Harness)

When evolution optimizes multiple objectives (pass@1 × token cost × latency):
- Return **non-dominated frontier** — not single scalar winner.
- Run held-out eval on frontier points only; proposer never sees held-out scores.
- Document frontier in `docs/harness/results.tsv` with objective columns.

## SIA / weight-update boundary

Document in limitations: harness-evolution does not train model weights.
If user needs weight updates, cite SIA externally — do not implement in skill library.
