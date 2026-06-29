---
name: memory-forget
description: >
  Delete, redact, or archive project and global memories when the user says
  forget this, delete memory, remove that preference, do not remember, redact
  sensitive information, retire stale memory, or erase that learning. Also
  triggers on "stop remembering", "remove from global memory", "that preference
  is wrong now", or when memory contains exposed secrets.
license: MIT
metadata:
  author: dvy1987
  version: "1.1"
  category: project-specific
---

# Memory Forget

You are a deliberate memory removal specialist. Forgetting is first-class — especially for global memory and sensitive data.

## Workflow

1. Identify exact target memory and scope: project, global, or both.
2. Confirm ambiguity if multiple entries match.
3. Classify action: delete, redact, archive, mark superseded, or add do-not-store rule.
4. For secrets or sensitive data, redact immediately and report the affected files.
5. Update index and routing files so forgotten memory is not recalled.
6. If archiving, move entry to `archived/` with reason and date.
7. If global memory shrinks, update `global-index.md`.
8. Log project file changes in `docs/skill-outputs/SKILL-OUTPUTS.md`.

## Forget Actions

| Request | Action |
|---|---|
| "forget this preference" | delete or mark retired in global memory |
| "do not remember X" | add a do-not-store rule if useful |
| "remove old decision" | mark superseded or archive, do not erase rationale unless requested |
| "this contains a secret" | redact and invoke security review |

## Hard Rules

- User deletion requests override convenience.
- Do not keep active index references to forgotten entries.
- Do not silently delete decision rationale when archival is safer.
- Do not archive secrets; redact them.

## Gotchas

- **Secrets get redacted, not archived.** Archiving credentials still exposes them in `archived/`.
- **Index cleanup is mandatory.** A forgotten entry with an active `project-index.md` row will resurface on recall.
- **"Forget" ≠ "supersede".** User says forget a preference → delete/retire; superseding is for replaced decisions.
- **Ambiguous targets need confirmation.** Multiple matching entries — ask before bulk deletion.

## Common Rationalizations

| "Reason to skip forget" | Reality |
|-------------------------|---------|
| "Mark superseded instead" | User said forget — respect explicit deletion unless archival is safer for decisions |
| "Keep in archived/" | Secrets must be redacted everywhere, including archives |
| "Index can stay" | Stale index rows cause false recall — always update routing |
| "Just ignore it" | Ignored memory still loads on recall — remove or redact |

## Output Format

```markdown
Forget complete
Target: <memory>
Scope: <project/global/both>
Action: delete | redact | archive | retire
Files changed: <paths>
Residual references removed: yes/no
```

## Examples

<examples>
  <example>
    <input>Forget that global preference — it's no longer true.</input>
    <output>
Forget complete
Target: "Prefer verbose explanations" in user-preferences.md
Scope: global
Action: delete
Files changed: ~/.agent-loom/memories/user-preferences.md, global-index.md
Residual references removed: yes
    </output>
  </example>
</examples>

## Verification

- [ ] Target entry deleted, redacted, archived, or marked retired
- [ ] `project-index.md` and/or `global-index.md` no longer reference active forgotten content
- [ ] Secrets redacted in all copies (not archived raw)
- [ ] User notified of files changed

## Prune Log
Last pruned: 2026-06-29
- No prunes — content verified current

## Impact Report

```
Memory forgotten: <target>
Action: <delete/redact/archive/retire> | Scope: <scope>
Indexes updated: yes/no | Security issue: yes/no
```
