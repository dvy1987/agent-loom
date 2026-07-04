---
name: agent-loom-sync
description: >
  Sync library skills from an agent-loom upstream repo into this project's
  .agents/skills while preserving project-local and forked skills. Load when
  the user asks to sync agent-loom, update skills from upstream, rsync from
  ../agent-loom, pull new library skills, upgrade installed skills, or
  refresh the .agents folder without losing custom project skills. Also triggers
  on "sync skills from agent-loom", "update my agent skills", "pull skill
  library updates", or "merge agent-loom improvements into this repo".
license: MIT
metadata:
  author: dvy1987
  version: "1.0"
  category: project-specific
  sources: agent-loom consumer install pattern (copy .agents + local skills)
  resources:
    references:
      - examples.md
      - sync-policy.md
    scripts:
      - sync_agent_loom.py
    templates:
      - agent-loom-sync.json
---

# Agent-Loom Sync

You merge upstream agent-loom library improvements into a consumer project's `.agents/skills/` without deleting or overwriting skills that belong only to this project.

## Hard Rules

**Never delete local-only skills.** A skill directory present in the project but absent from upstream is project-local — keep it forever unless the user explicitly asks to remove it.

**Never overwrite protected or forked skills without explicit user approval.** Protection sources: `metadata.origin: project-local` in SKILL.md, `.agents/agent-loom-sync.json` → `protected_skills` / `forked_skills`, or skills that exist only locally.

**Always dry-run before apply.** Present the plan (add / update / unchanged / local-only / forked) and wait for confirmation before `--apply`.

**Never sync the project root `AGENTS.md` from upstream.** That file is project-specific (from `project-setup`). Only sync `.agents/skills/` and optionally `.agents/ROUTING.md` when the user opts in.

**Never run rsync on the whole `.agents/skills/` tree with `--delete`.** Sync per library skill directory only — bulk delete would remove project-local skills.

---

## Workflow

### Step 1 — Resolve upstream path

Default: `../agent-loom` relative to project root. Override via:
- User-provided path argument
- `.agents/agent-loom-sync.json` → `"upstream"`

Verify upstream exists and contains `.agents/skills/`. If missing, stop with the exact path checked.

Bootstrap config if absent: copy `templates/agent-loom-sync.json` → `.agents/agent-loom-sync.json`.

### Step 2 — Build sync plan

```bash
python3 .agents/skills/agent-loom-sync/scripts/sync_agent_loom.py --dry-run
```

Classify each skill — read `references/sync-policy.md` for protection rules. Summarize for the user:

| Bucket | Meaning |
|--------|---------|
| **Add** | New upstream skill not in project |
| **Update** | Upstream skill differs; safe to rsync |
| **Unchanged** | Already matches upstream hash |
| **Local-only** | Project skill with no upstream counterpart — protected |
| **Forked** | Modified library skill — skipped until user merges |

### Step 3 — Confirm with user

Show counts and name lists for Add and Update. Ask: "Apply sync?" One confirmation for apply; forked skills need per-skill decision if user wants upstream version.

### Step 4 — Apply

```bash
python3 .agents/skills/agent-loom-sync/scripts/sync_agent_loom.py --apply
```

Updates `.agents/agent-loom-sync.json` with `last_sync` and `upstream_commit`.

### Step 5 — Optional ROUTING.md

Only if user asks: `rsync` upstream `.agents/ROUTING.md` when project has not forked it (no local diff). Never auto-overwrite without asking.

### Step 6 — Post-sync validation

Invoke `validate-skills` (or run Step 4e craft gates) on updated skills. Report P0/P1 before user commits.

### Step 7 — Log and handoff

Append to `docs/skill-outputs/SKILL-OUTPUTS.md`. Recommend commit message: `chore: sync agent-loom library @ <commit>`. Offer `memory-handoff` if session ends.

---

## Marking project-local skills

When creating a skill only for this repo via `universal-skill-creator`, add under `metadata:`:

```yaml
  origin: project-local
```

Sync will never overwrite it. For one-off forks of a library skill, use `forked_skills` in config with a short reason.

---

## Gotchas

- **Copying all of `.agents/` once ≠ ongoing sync.** This skill is the ongoing path; re-copying blindly deletes project-local skills.
- **`../agent-loom` is relative to project root**, not the skill directory — run the script from repo root.
- **rsync `--delete` is per-skill**, removing stale files inside an updated library skill dir only.
- **Global install (`install.sh`) is different** — that symlinks to `~/.agents/skills`; this skill targets project-copied `.agents/`.
- **Upstream must be pulled first** — remind user to `git pull` in agent-loom before sync if they want latest.

---

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Just rsync the whole .agents folder" | Deletes project-local skills and project config |
| "Skip dry-run, I trust upstream" | Forked/custom skills get wiped without a plan |
| "Overwrite my fork — upstream is always right" | Require explicit per-skill opt-in to replace forked |
| "Sync AGENTS.md from agent-loom" | Project AGENTS.md is from project-setup — merge manually |
| "Delete skills removed upstream" | Local-only stays; upstream removals don't delete local skills |

---

## Verification

- [ ] Dry-run plan shown before apply
- [ ] All local-only skills listed under protected
- [ ] No protected/forked skill in Update list without user approval
- [ ] `agent-loom-sync.json` updated after apply
- [ ] SKILL-OUTPUTS.md appended when files changed

---

## Red Flags

- Whole-tree rsync with delete on `.agents/skills/`
- Local-only skill missing from protected list in plan
- Forked skill overwritten without user opt-in
- Upstream path points at wrong repo or missing `.agents/skills`

---

## Example

<examples>
  <example>
    <input>sync agent-loom from ../agent-loom without losing my custom skills</input>
    <output>Plan: 15 add, 22 update, 3 local-only protected. Awaiting confirm before --apply.</output>
  </example>
</examples>

Read `references/examples.md` for full session walkthroughs.

---

## Impact Report

`Agent-loom sync: upstream @ <commit> | add: N | update: N | protected: N | forked: N | applied: yes/no | Config: .agents/agent-loom-sync.json`
