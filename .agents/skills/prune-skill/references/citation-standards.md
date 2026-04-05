# Citation Standards

Read this before accepting any source as grounds for pruning a skill. Every prune requires a source that meets at least Medium trust. Low-trust sources require corroboration.

---

## Trust Tiers

### High Trust — Accept as grounds for pruning
- **Peer-reviewed conference proceedings**: NeurIPS, ICML, ICLR, ACL, EMNLP, CVPR
- **Peer-reviewed journals**: Nature, Science, JMLR, TACL, IEEE Transactions
- **Official lab technical reports**: Anthropic, OpenAI, Google DeepMind, Meta AI Research — with methodology section
- **Replicated findings**: Any arXiv paper whose findings have been independently replicated in a second paper

### Medium Trust — Accept with verification
- **arXiv preprints**: Must have 50+ citations OR be from a named lab (Anthropic, OpenAI, Stanford, MIT, CMU, Berkeley, Google, Microsoft Research, Meta) AND be less than 18 months old
- **Wharton Generative AI Lab (GAIL) reports**: Published methodology, named authors, specific benchmarks cited
- **Official model documentation**: Anthropic docs, OpenAI docs, Google AI docs — for capability and behavior claims about that specific model
- **Named practitioner engineering blogs**: Vercel, Stripe, Linear, Shopify Engineering, Cloudflare — for real-world production findings

### Low Trust — Require corroboration from Medium or High source
- **Anonymous or pseudonymous blog posts**: Acceptable only if they cite a Medium/High source directly
- **LinkedIn posts**: Never use as primary evidence; acceptable as pointers to primary sources
- **Reddit / Hacker News**: Acceptable as discovery mechanism only; always trace to primary source
- **Social media**: Not acceptable as evidence under any circumstances
- **Undated web pages**: Not acceptable
- **AI-generated content**: Not acceptable as a source about AI behavior

### Zero Trust — Never accept as grounds for pruning
- Sources that cannot be verified to exist (check the URL / DOI before citing)
- Sources older than 3 years on fast-moving topics (model behavior, prompting techniques, context windows)
- Sources whose conclusions are contradicted by a High Trust source without acknowledgment

---

## Verification Checklist

Before citing any source in a prune action:

- [ ] URL or DOI resolves and matches the described content
- [ ] Author names and institution are identifiable
- [ ] Publication date is within acceptable recency window for the topic
- [ ] The specific finding cited matches what the paper/post actually says (read it, don't trust the abstract alone)
- [ ] No High Trust source directly contradicts this finding

---

## Recency Windows by Topic

Different topics become stale at different rates:

| Topic | Recency window | Reason |
|-------|---------------|--------|
| Prompting technique effectiveness | 12 months | Model capabilities shift rapidly |
| Model context window limits | 6 months | Expanded frequently |
| Tool use / function calling capabilities | 6 months | New models add capabilities quickly |
| Skill directory paths / platform support | 12 months | Platform specs change with releases |
| agentskills.io specification | 18 months | Spec is more stable |
| General software engineering practices | 36 months | More stable domain |
| Academic findings on reasoning / CoT | 18 months | Active research area |

---

## Handling Conflicting Sources

When two Medium or High Trust sources contradict each other:

1. Prefer the more recent source if both are High Trust
2. Prefer the more specific source (e.g., findings on GPT-5 specifically beat findings on "frontier models generally")
3. If genuinely unresolved: do not prune — flag for human review instead
4. Always document the conflict in the Prune Log

---

## Misrepresentation Patterns to Watch For

These are common ways skills misrepresent research findings:

| Misrepresentation | Reality |
|------------------|---------|
| "CoT always improves performance" | CoT improves non-reasoning models inconsistently; adds cost with minimal gain for reasoning models (Wharton GAIL, Jun 2025) |
| "Role prompting expands model knowledge" | Role prompting does NOT expand factual accuracy on frontier models (arXiv:2409.13979) |
| "More examples = better" | Few-shot collapse confirmed above ~3 examples on modern models (arXiv:2509.13196) |
| "Complex constraints improve reliability" | Prompting Inversion: elaborate constraints harm GPT-5/Claude 4 class models (arXiv:2510.22251) |
| "Emotional phrases improve compliance" | Inconsistent / minimal effects on frontier models (Wharton GAIL Prompting Science Report 2, 2025) |
