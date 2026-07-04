# Pre-mortem — Full Worked Examples

Skill: `pre-mortem` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** We're launching our community feature in 6 weeks. Run a pre-mortem.

**Output:**
```
It is 6 months from now. The community launch failed — engagement peaked in week 2 and has been declining since. The founding team is meeting to understand why.

Generate causes:
1. Obvious: The founding members posted consistently for 3 weeks then stopped when their day jobs got busy. There was no content pipeline.
2. Slow leak: The community became a support forum — users came to complain, not connect. Tone was set in week 1 and never recovered.
3. Wrong assumption: We assumed users wanted to connect with each other. Most just wanted better documentation.
4. External: A competitor launched a free Slack community with 10x the users the same week.
5. People cause: No one owned community full-time. It was everyone's secondary responsibility.

Ranked by impact × blindness:
1. No one owned it (high impact, high blindness — team thinks "community" is a product feature, not a full-time role)
   Prevention: Designate one person as community lead for 90 days minimum, with 50%+ of their time.

2. Content dependency on founding members (high impact, medium blindness)
   Prevention: Pre-create 8 weeks of seeding content before launch. Founding members commit to 2 posts/week for 90 days.

ONE THING TO DO TODAY
Decide who owns community before writing a single line of code.
```

## Example 2 — Step-by-step execution

**Input:** "Run `pre-mortem` on [concrete task]"

**Agent actions:**
1. Set the Scene
2. Generate Failure Causes (Diverge)
3. Prioritise by Impact × Blindness
4. Convert to Prevention Actions
5. Deliver

**Impact Report shape:**
```
Pre-mortem complete: [project/plan]
Time horizon: [N months/years]
Causes generated: N
High priority (impact × blindness): N
Prevention actions defined: N
```

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- The "obvious cause" is usually the most important one. Teams avoid stating it because it feels embarrassing. Name it first — it unlocks the rest.
- Pre-mortem is most powerful just before a major commitment, not after. If you're already mid-execution, `adversarial-hat` is more useful.
- Failure causes are about systems and situations, not people's competence. Keep it structural.
- 

---

See `SKILL.md` for hard rules and verification checklist.
