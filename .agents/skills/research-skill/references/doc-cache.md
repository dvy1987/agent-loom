# Doc Fetch Cache (ETag Revalidation)

Adapted from [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) `hooks/sdd-cache-{pre,post}.sh` (MIT).

## Mental model

- **URL-keyed** cache; **no TTL** — freshness is HTTP `304 Not Modified` only.
- Cached body is whatever the agent last stored (often WebFetch-shaped text, not raw HTML).
- **Prompt is metadata**, not part of the key — on cache hit, compare prompts before reusing.

## Cross-platform CLI (all agents)

From project root:

```bash
python3 .agents/skills/research-skill/scripts/doc_cache.py "https://example.com/docs" --prompt "extract API surface"
```

- Cache dir: `.agents/cache/doc-fetch/<sha>.json`
- Stdlib only; skips cache when origin sends no `ETag` / `Last-Modified`
- `--json` for machine-readable output

## Claude Code hooks (transparent WebFetch)

Copy `hooks/` to project root and register per **`hooks/SDD-CACHE.md`**:

| Event | Action |
|-------|--------|
| PreToolUse WebFetch | `304` → serve cache via stderr (exit 2) |
| PostToolUse WebFetch | Store body + validators |

## When skills must fetch

**Prefer in order:**

1. Claude Code with `sdd-cache` hooks wired (zero workflow change)
2. `doc_cache.py` before manual curl/WebFetch
3. Raw fetch only for one-off or validator-less URLs

## Example — research pass

<input>Research Stripe rate limiting — fetch their blog post twice in one week</input>

<output>
First fetch:
```bash
python3 .agents/skills/research-skill/scripts/doc_cache.py "https://stripe.com/blog/rate-limiters" --prompt "gotchas for API rate limits"
```
stderr: `[doc-cache] Fetched and cached …`

Second fetch (same URL): stderr: `[doc-cache] Cache hit (HTTP 304) …` — body unchanged unless origin updated.

If your angle differs from the stored prompt, delete `.agents/cache/doc-fetch/<sha>.json` and re-fetch.
</output>

## Testing

Smoke tests and freshness corruption steps: **`hooks/SDD-CACHE.md`** → Local testing.

## Limitations

See **`hooks/SDD-CACHE.md`** → Known limitations (prompt-shaped body, extra HEAD per write, no team cache).
