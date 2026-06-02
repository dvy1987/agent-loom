# Adversarial Review Prompt (fresh context)

Use for Step 3 (DOUBT) in `adversarial-hat` Fresh-Context or In-flight modes. Pass **ARTIFACT + CONTRACT only** — never pass the author's CLAIM or reasoning (biases toward agreement).

```
Adversarial review. Find what is wrong with this artifact.
Assume the author is overconfident. Look for:
- Unstated assumptions
- Edge cases not handled
- Hidden coupling or shared state
- Ways the contract could be violated
- Existing conventions this might break
- Failure modes under unexpected input

Do NOT validate. Do NOT summarize strengths. Find issues, or state
explicitly that you cannot find any after thorough examination.

ARTIFACT:
<paste diff, function, or proposal — smallest reviewable unit>

CONTRACT:
<paste constraints the artifact must satisfy>
```

## Reconcile precedence (author classifies each finding)

1. Contract misread → fix contract, re-run
2. Valid + actionable → change artifact, re-loop
3. Valid trade-off → document explicitly for user
4. Noise → note; improve contract if context would have prevented false flag

## Stop conditions

- Trivial / duplicate findings only, **or**
- 3 cycles completed → escalate to user, **or**
- User says "ship it"

**Doubt theater:** 2+ cycles with substantive reviewer output but zero findings classified actionable → stop and escalate.
