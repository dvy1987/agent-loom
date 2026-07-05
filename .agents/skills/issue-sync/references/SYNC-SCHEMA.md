# Issue Sync Map Schema

Path: `.agent-loom/issue-sync-map.json`

```json
{
  "source": "github:owner/repo",
  "target": "linear:team-key",
  "last_synced_at": "2026-07-05T12:00:00Z",
  "mirrors": [
    {
      "source_id": "github:42",
      "target_id": "linear:ENG-123",
      "status": "open",
      "last_synced_at": "2026-07-05T11:30:00Z"
    }
  ]
}
```

## ID format

- `github:<number>` or `github:<owner>/<repo>#<number>`
- `linear:<issue-id>`

## Env vars (examples)

| Tracker | Env |
|---------|-----|
| GitHub | `GITHUB_TOKEN` |
| Linear | `LINEAR_API_KEY` |

Names only in docs — never commit values.
