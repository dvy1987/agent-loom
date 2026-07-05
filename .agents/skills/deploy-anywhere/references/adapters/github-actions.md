# GitHub Actions Adapter

Deploy via workflow dispatch or push-triggered workflow. No extra secrets when running **inside** GHA (`GITHUB_TOKEN` default). Local deploy orchestrates `gh workflow run`.

---

## Scaffold workflow (consumer repo)

Path: `.github/workflows/deploy.yml`

```yaml
name: Deploy
on:
  workflow_dispatch:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: ${{ env.BUILD_CMD }}
      env:
        BUILD_CMD: npm run build
```

---

## Local trigger

```bash
gh workflow run deploy.yml --ref main
gh run watch
```

---

## Secrets

Reference in workflow via `${{ secrets.NAME }}` — document required names in deploy.yml comments, never values.

---

## Rollback

Re-run previous successful workflow on prior SHA:

```bash
gh workflow run deploy.yml --ref <previous-sha>
```

---

## Output summary

```markdown
Target: github-actions
Run: <url>
Rollback: gh workflow run deploy.yml --ref <sha>
```
