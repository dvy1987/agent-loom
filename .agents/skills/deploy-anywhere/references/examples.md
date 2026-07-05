# Deploy Anywhere — Examples

## Ex.1 — Preflight fail

```markdown
PREFLIGHT FAIL — add before deploy:
  - env:VERCEL_TOKEN (required for vercel)

Stopped. No deploy attempted.
```

## Ex.2 — Vercel preview success

```markdown
## Deploy summary
Target: vercel (preview)
URL: https://my-app-abc123.vercel.app
Rollback: vercel rollback https://my-app-abc123.vercel.app
```
