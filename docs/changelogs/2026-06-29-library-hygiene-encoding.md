# Changelog — 2026-06-29 (library hygiene + encoding fix)

Significance: **PATCH** — internal quality and loader compliance; no new user-facing capabilities in this entry.

## Fixed

- **UTF-8 encoding on skill markdown** — agents installing the library on Windows can now run `agentskills validate` without decode failures on 43 previously affected skills. Re-run `pip install skills-ref` and validate locally if you maintain a fork.

## Changed

- **Library index sync** — README, SKILL-INDEX, skill-graph, and PRD counts reconciled to the post-improve-skills registry (98 skills at time of hygiene pass).
