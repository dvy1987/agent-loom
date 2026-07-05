# Harness Readiness Gate

Plain-language guide for **when** harness skills fire — no dev jargon required.

## What a harness is (one sentence)

The **harness** is the project's agent setup: which instructions agents read, which skills they must follow, what they're allowed to touch, and how you check they're doing a good job.

## Auto-fire rules (agents MUST invoke harness skills)

| Situation | Skill | Plain explanation |
|-----------|-------|-------------------|
| Just finished `project-setup` or `retroactive-project-setup`, no `docs/harness/manifest.json` | `harness-generation` | First-time agent reliability setup |
| User complains agents are unreliable (any wording below) | `harness-engineering` | Diagnose bootstrap vs fix loop |
| `AGENTS.md` exists, no harness manifest | `harness-engineering` → bootstrap | Project has instructions but no reliability layer |
| Manifest exists, user wants better agents / same errors repeat | `harness-engineering` → evolution | Improve the setup from failure patterns |
| User asks if agents "learn" or "self-improve" | `reality-check` then maybe evolution | Verify claims before promising improvement |
| Building multi-agent workflow | `harness-generation` if missing, then `agent-builder` | Reliability layer before agent topology |

## Symptom phrases → route `harness-engineering`

Non-devs often say:

- "The agent keeps making the same mistake"
- "It doesn't follow my instructions"
- "Agents ignore the project rules"
- "AI keeps going off track / off rails"
- "Make my agents more reliable"
- "Why is Cursor/Codex/Claude so bad on this project?"
- "Agent forgot what we decided"
- "It skips tests / skips steps"
- "Agent quality got worse"
- "Fix how agents work here" (not fix application code)
- "Set up agents properly"
- "Agents don't use the skills"
- "Something's wrong with agent setup"

**Not harness** (route elsewhere):

- "Fix this bug in my app" → `debug-and-fix`
- "Design multiple agents" → `agent-builder` (after harness check)
- "Write AGENTS.md" only → `project-setup` (then auto-chain harness)

## Readiness checklist (silent scan)

```
[ ] AGENTS.md or agent instructions exist
[ ] docs/harness/manifest.json exists
[ ] docs/harness/eval-interface.md exists
[ ] User reported agent misbehavior → evolution path?
```

| Check | Missing → action |
|-------|------------------|
| Manifest | `harness-generation` |
| Eval interface | `harness-generation` or `eval-rubric-design` |
| User symptom + manifest | `harness-evolution` (after eval ready) |

## Non-technical owner script

When routing, tell the user in plain language:

> "Your project has agent instructions but not yet a **reliability setup** — the checklist that helps agents follow rules and improve when they fail. I'll run the harness bootstrap next (about 2 minutes of file setup). OK?"

Default: **proceed unless user opts out** when `owner_mode` is non-technical or hybrid.
