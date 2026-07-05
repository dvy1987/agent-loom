# Vercel Adapter

Secrets (env names only): `VERCEL_TOKEN`, `VERCEL_ORG_ID`, `VERCEL_PROJECT_ID`

---

## Preview deploy sequence

```bash
# 1. Pull env + project settings
vercel pull --yes --environment=preview --token="$VERCEL_TOKEN"

# 2. Build locally (matches CI prebuilt pattern)
vercel build --token="$VERCEL_TOKEN"

# 3. Deploy prebuilt output
vercel deploy --prebuilt --token="$VERCEL_TOKEN"
```

---

## Production

Set `prod: true` in deploy.yml target → use `--environment=production` in `vercel pull`.

---

## Rollback

```bash
vercel rollback [deployment-url] --token="$VERCEL_TOKEN"
```

---

## Output summary

```markdown
Target: vercel (preview|prod)
URL: https://...
Rollback: vercel rollback <url>
```

Reference: Vercel GitHub Actions examples + KB (CI prebuilt flow).
