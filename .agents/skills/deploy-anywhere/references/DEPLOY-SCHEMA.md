# Deploy Schema — `.agent-loom/deploy.yml`

Declarative deploy intent. Secrets referenced by **name only** — never store values in repo.

---

## Example

```yaml
build_cmd: npm run build
test_cmd: npm test
env_map:
  NODE_ENV: production
targets:
  - provider: vercel
    project_id: my-app
    org_id: team_abc
    prod: false
  - provider: github-actions
    workflow: deploy.yml
    prod: true
```

---

## Fields

| Field | Required | Description |
|-------|----------|-------------|
| `build_cmd` | yes | Build command before deploy |
| `test_cmd` | no | Run before build when set |
| `env_map` | no | Non-secret env defaults |
| `targets` | yes | ≥1 provider block |

### Target block

| Field | Description |
|-------|-------------|
| `provider` | `vercel` \| `github-actions` \| (future adapters) |
| `project_id` | Provider project slug/id |
| `org_id` | Org/team id when required |
| `prod` | `true` = production target |

---

## Preflight

```bash
python3 .agents/skills/deploy-anywhere/scripts/preflight.py .agent-loom/deploy.yml
```

Fails loudly on missing config or env secrets.

---

## Provider detection order

1. Explicit `targets` in deploy.yml
2. Repo signals: `vercel.json` → vercel; `.github/workflows/*deploy*` → github-actions
3. Ask user — never guess credentials
