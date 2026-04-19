# eval-output

> Orchestrator for evaluating LLM and agent outputs — routes to rubric design, LLM-as-judge scoring, or automated eval pipeline design.

## Install

```bash
npx skills eval-output -a codex      # Codex
npx skills eval-output -a replit     # Replit
cp -r eval-output/ .agents/skills/   # Universal
```

## Usage

Trigger: "evaluate this output", "score this response", "run an eval", "LLM as judge"

Part of the eval-output skill suite:
- `eval-rubric-design` — design evaluation rubrics
- `eval-judge` — score outputs using LLM-as-judge
- `eval-pipeline` — design automated eval pipelines

## Platforms

Works with: Codex, Ampcode, Claude Code, Warp, Gemini CLI, GitHub Copilot, Cursor, VS Code, Replit, Factory.ai, Bolt.new

## License

MIT
