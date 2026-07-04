# Venture Exploration — Full Worked Examples

Skill: `venture-exploration` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** I have an idea for an app that helps freelance designers chase late invoices. Is it a good business?

**Output:**
```
Stage diagnosis: **Evaluate** — you have an idea but no model or validation evidence yet.

Two prereqs to check before I route to `idea-evaluation`:

1. Specific segment — "freelance designers" is broad. Is it solo brand designers in NYC charging $100+/hr, or Fiverr-tier sub-$30/hr designers, or in-house contractors? Pick one.
2. Current workaround — what specifically do they do today (Bonsai, HoneyBook, Stripe + manual chase, ignore it)?

Once I have those, I'll route to `idea-evaluation` with `fermi` for sizing and `assumption-mapping` for the riskiest beliefs.
```

## Example 2 — Step-by-step execution

**Input:** "Run `venture-exploration` on [concrete task]"

**Agent actions:**
1. Read project state
2. Classify the request
3. Apply the stage's prerequisites
4. Invoke exactly one child
5. Loop or hand off
6. Handoff gate to `product-soul`
7. Log the route

**Impact Report shape:**
```
Venture exploration route complete
Stage: generate / model / evaluate / validate / handoff
Child invoked: <skill>
Prerequisites status: pass / N missing
Handoff gate (if relevant): N/5 — <missing items>
Next recommended step: <child or product-soul>
Logged to: docs/skill-outputs/SKILL-OUTPUTS.md
```

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- **Don't loop forever.** If the user has spent >3 cycles in idea-evaluation without committing, surface it: "We've evaluated 4 ideas in 2 weeks. Pick one to put real currency behind, or commit to a kill list and stop."
- **Don't accept "trust me, the segment is real" without evidence.** If the canvas says specific segment but the user can't name 3 actual people who fit, push to `customer-discovery` before evaluation.
- **`product-soul` does not screen.** Once you hand off, the assumption is the strategic concept survives. The handoff gate is the screen.
- **Generation without context produces generic ideas.** Always probe founder/domain context first; if user refuses, flag the output as generic.

---

See `SKILL.md` for hard rules and verification checklist.
