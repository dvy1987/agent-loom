# Why agent-loom?

**agent-loom** is a cross-platform skill library for AI coding agents — instructions that teach tools *how* to work, not just *what* to answer.

## What makes it different

1. **Self-maintaining** — skills are researched, validated, pruned, and deconflicted on a schedule; not a static prompt dump.
2. **Process-first** — plan, decompose, verify, and hand off context before one-shot execution.
3. **Safe change** — map blast radius, verify, auto-revert on failure (see `safe-change`).
4. **Provider-agnostic** — one install, every major agent host via agentskills.io standard.

## Not for you if…

- You want a single chat prompt, not a library of workflows.
- You never run agents on real codebases (no verify loop needed).
- You need hosted SaaS — this is files in your repo.

## Quick win

```text
Run the agent-loom quickstart
```

Produces a real verified edit on `examples/seed/calc/` in minutes.

## Learn more

- [README](../README.md) — install + full skill list
- [examples/](../examples/) — product tour demos
- [docs/SKILL-INDEX.md](SKILL-INDEX.md) — every skill
