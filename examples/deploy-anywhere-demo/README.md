# Deploy Anywhere Demo

**Skill:** `deploy-anywhere`

## What it shows

Scaffold `.agent-loom/deploy.yml` and run preflight (no credentials required for dry scaffold).

## Try it

```text
Scaffold a deploy.yml for this repo with a github-actions target and run preflight
```

## Expected output

- `.agent-loom/deploy.yml` created from DEPLOY-SCHEMA
- `preflight.py` reports missing items **by name** (not values)
- No deploy attempted without secrets

## Note

Full deploy requires provider tokens — demo stops at preflight unless configured.
