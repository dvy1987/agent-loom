# Venture Exploration — Full Worked Examples

Skill: `venture-exploration` | Load when producing output for this workflow.

## Example 1 — From skill workflow

**Input:** I have an idea for an app that helps freelance designers chase late invoices. Is it a good business?

**Output:**
```
Stage diagnosis: **Evaluate** — you have an idea but no model or validation evidence yet.

Two prereqs to check before I route to `idea-evaluation`:

1. Specific segment — "freelance designers" is broad. Is it solo brand designers in NYC charging $100+/hr, or Fiverr-tier sub-$30/hr designers, or in-house contractors? Pick one.
2. Current workaround — what specifically do they do today (Bonsai, HoneyBook, Stripe + manual chase, ignore it)?

Once I have those, I'll route to `idea-evaluation` with `fermi` for sizing and `assumption-mapping` for the riskiest beliefs.
```

## Example 2 — Typical invocation

**Input:** "Run `venture-exploration` for [concrete task]"

**Output:**
```
Invoked `venture-exploration`.
Step 1: Read project state
Step 2: Classify the request
Step 3: Apply the stage's prerequisites
See SKILL.md Impact Report schema.
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
