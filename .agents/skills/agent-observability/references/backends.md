# Observability Backend Selection (free-tier-first)

Snapshot verified 2026-07. **Free tiers change — re-verify the numbers on the
vendor pricing page before committing.** The instrumentation (OTel GenAI /
OpenInference) is portable across all of these, so a wrong backend choice is a
config change, not a rewrite.

## Plain-language architecture

```
Your product (Cloud Run / Vercel / anywhere)
   └── instrumentation library (runs inside your app, adds ~ms)
         └── sends spans over HTTPS ──────────► Managed backend (their cloud)
                                                 └── you log in via browser to
                                                     view traces, costs, evals
```

- You never install a database. You never host anything. You add a library +
  2–3 environment variables (API key, endpoint).
- If the vendor disappears or the free tier shrinks: point the exporter at a
  different backend. Application code unchanged.

## Decision table

| Backend | Free tier (verify!) | Best when | Watch out |
|---|---|---|---|
| **Langfuse Cloud** | ~50k units/mo, 30-day retention, 2 users; Core ~$29/mo | Default general pick. Framework-agnostic, MIT OSS core (ClickHouse-backed since 2026), strong cost tracking per user/session | Self-assembly for eval orchestration; unit caps count every span |
| **Phoenix / Arize** | Phoenix self-host free (single container); Arize AX cloud ~25k spans/mo, 1 user | Agent-heavy products (deepest multi-step agent + tool-call views), ADK/OpenInference stacks, RAG retrieval debugging | Cloud free cap is small; Elastic license on OSS (fine unless reselling hosted) |
| **LangSmith** | ~5k traces/mo, 14-day retention; $39/seat after | Product is LangChain/LangGraph-first — zero-config capture, best LangGraph state views | Proprietary trace model = real migration cost; short free retention |
| **Braintrust** | ~1M spans + 10k eval runs/mo, unlimited users | Eval-in-CI culture; biggest free span budget by far | Closed source, no self-host, ~30-day retention |
| Self-host in cloud (Langfuse/Phoenix) | infra cost only | Hard data-residency requirement (traces may not leave your VPC) | LAST RESORT for this user: real ops burden (DB, Redis, storage, backups). Never on a laptop. |

Avoid: proxy-only tools in maintenance mode (e.g. Helicone post-acquisition,
2026) for new strategic setups.

## Quick picks by situation

- **"I just want to see why my agent is weird" (any stack):** Langfuse Cloud free.
- **Google ADK / multi-agent swarm (e.g. aegis-style):** Phoenix — OpenInference
  auto-instrumentation for ADK exists and its agent trace views are deepest.
  Arize AX free tier if cloud-managed is required and volume fits.
- **LangGraph product:** LangSmith (accept lock-in consciously) or Langfuse if
  you may leave LangChain later.
- **High volume, tiny budget, evals matter:** Braintrust free tier.
- **Regulated data:** self-host Langfuse in cloud (compute ~<$500/mo at millions
  of traces) — get help for this; it is the one option with real ops work.

## Redaction / PII checklist (do BEFORE production traffic)

1. List fields that must never leave: user names, emails, document bodies,
   health/finance details, API keys.
2. Enable the backend's masking hook (all four support masking/redaction
   callbacks or ingestion filters — default is usually OFF).
3. Send one test request containing a fake secret (e.g. `TEST-SECRET-123`);
   search for it in the backend UI. Found = redaction broken.
4. Re-run the check after any instrumentation upgrade.

## Volume math template

```
requests/month × spans/request (5–30 for agents) = spans/month
spans/month vs free cap → sampling % for successes (failures always 100%)
```

## Swap procedure (backend → backend)

1. Create account + API key on new backend.
2. Change exporter endpoint + key env vars (OTLP/HTTP or vendor `register()`).
3. Run one request; verify first trace on the new backend (Step 4 checklist).
4. Keep old backend read-only until its retention window drains.
