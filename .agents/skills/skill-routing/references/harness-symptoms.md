# Harness Symptom Routing

Load when the user complaint sounds like **agent behavior** not **application bugs**.

## Route to `harness-engineering` first

| User language | Why |
|---------------|-----|
| Agent keeps failing / same error again | Evolution or missing eval |
| Doesn't follow instructions / ignores rules | Context or governance layer |
| Going off rails / off track | Harness routing or skills not invoked |
| Not using skills / skips workflow | Skill Invocation or orchestration map gap |
| Unreliable / bad quality / worse than before | Harness or eval regression |
| Forgot context / lost thread | Lifecycle or memory — may be harness + memory |
| Set up agents / agent setup / agent config | Bootstrap path |
| Self-improving / get better over time | Evolution + reality-check |
| After project setup still broken | Missing harness bootstrap |

## Route to `harness-generation` directly

- `project-setup` or `retroactive-project-setup` **just completed** and manifest absent
- Explicit "first time agents in this repo"

## Do NOT route to harness

| User language | Route |
|---------------|-------|
| Fix bug in code | `debug-and-fix` |
| Review my PR | `code-review-crsp` |
| Write a feature spec | `feature-spec` |
| Which skill should I use (generic) | `skill-finder` or `project-orchestrator` |

## Ambiguity resolution

"Improve agents" at score ≥7:

> "Do you mean **fix the app's code** (debug) or **fix how AI assistants are set up** on this project (harness)?"

Default for non-technical owners: **harness** when `AGENTS.md` exists.
