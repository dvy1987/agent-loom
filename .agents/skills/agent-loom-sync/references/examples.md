# Agent-Loom Sync — Examples

## Example 1 — First sync after copying .agents into a project

<input>sync skills from ../agent-loom — I copied .agents last month and want updates without losing my custom deploy skill</input>

<output>
**Sync plan** (dry-run)
Upstream: `/Users/me/Projects/agent-loom` @ `d148d27`
Add (12): knowledge-graph, agent-loom-sync, check_red_flags_quality, …
Update (8): validate-skills, improve-skills, memory-handoff, …
Unchanged (74): test-driven-development, …
Local-only protected (1): `my-deploy-pipeline`

**Protected automatically**
- `my-deploy-pipeline` — exists only in this repo (never deleted, never overwritten)

**Next:** Run with `--apply` after you confirm. Then `validate-skills` on changed skills.

Config will be written to `.agents/agent-loom-sync.json`.
</output>

## Example 2 — Protect a customized library skill (same name as upstream)

<input>I customized debug-and-fix for our stack — don't overwrite it on sync</input>

<output>
Add to `.agents/agent-loom-sync.json`:

```json
"forked_skills": {
  "debug-and-fix": "Custom triage for Stripe webhooks — 2026-07-04"
}
```

Re-run dry-run — `debug-and-fix` moves to Forked/skipped. Other library skills still update.

**Note:** Repo-only skills get `metadata.origin: project-local` from `universal-skill-creator` at create time; `agent-loom-sync --apply` backfills any missing.
</output>

## Example 3 — Apply sync

<input>apply the sync</input>

<output>
```bash
python3 .agents/skills/agent-loom-sync/scripts/sync_agent_loom.py --apply
```

Applied: 20 skills
Config updated: `.agents/agent-loom-sync.json` (`last_sync`, `upstream_commit`)

**Post-sync**
- [ ] `validate-skills` on updated skills
- [ ] Commit `.agents/` + config with message `chore: sync agent-loom library @ d148d27`
- [ ] `memory-handoff` if ending session

Logged to `docs/skill-outputs/SKILL-OUTPUTS.md`.
</output>
