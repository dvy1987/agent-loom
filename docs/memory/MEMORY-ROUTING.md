# Memory Routing

Read this file first. Do not load every memory file by default.

| Intent | File | Read when |
|---|---|---|
| Resume work | `agent-handoffs.md` | Starting a new session; read latest entry only. |
| Current status | `current-state.md` | Need a snapshot of where the project is now. |
| Past decisions | `decision-log.md` | Need rationale for a choice; filter by tag/date. |
| Project learnings | `learnings.md` | Looking for known patterns or gotchas. |
| Parked ideas | `deferred.md` | Considering reopening a deferred option. |
| Open questions | `open-questions.md` | A blocking question needs resolution. |
| Session detail | `session-log.md` | Above sources are insufficient. |
| Old / superseded | `archived/` | Almost never; archived entries are not current. |

Routing rules:
- Always consult `project-index.md` before reading content files.
- Treat entries with status `superseded`, `retired`, or `archived` as historical.
- Prefer the smallest useful slice; do not load full logs by default.
