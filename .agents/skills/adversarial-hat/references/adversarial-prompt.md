# Adversarial Review Prompts (copy-paste library)

Use for DOUBT step in `adversarial-hat` Fresh-Context and In-Flight modes.

**Invariant:** Pass **ARTIFACT + CONTRACT only** — never pass the author's CLAIM or reasoning (biases toward agreement).

---

## Core adversarial prompt (documents & code)

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
<paste diff, function, plan section, or proposal — smallest reviewable unit>

CONTRACT:
<paste constraints the artifact must satisfy — FR ids, invariants, perf bounds>
```

---

## In-flight CLAIM template (author writes — do NOT pass to reviewer)

```markdown
## CLAIM
**Decision:** [What I'm about to do in one sentence]
**Why it matters:** [User impact / risk if wrong]
**Alternatives rejected:** [1–2 options and why not]
**Non-trivial because:** [see checklist below]
```

### Non-trivial decision checklist

Apply in-flight doubt when **any** apply:

- [ ] Changes branching logic or public API shape
- [ ] Crosses module boundaries or adds new dependency
- [ ] Relies on unverified invariant ("this is always sorted")
- [ ] Irreversible or hard to roll back (migration, data transform)
- [ ] Security, auth, or money path
- [ ] Performance-sensitive hot path
- [ ] Bug fix without reproduction test yet

**Skip** for: formatting, comments, renames, obvious one-liners, read-only exploration.

---

## EXTRACT template (what reviewer receives)

```markdown
## ARTIFACT
<minimal diff or function — no narrative>

## CONTRACT
- Must: [bullet invariants]
- Must not: [bullet prohibitions]
- Conventions: [link or one-line pattern from repo]
```

---

## Code-specific doubt prompt

```
You are reviewing a code change cold. The author believes this is correct.

Find:
1. Bugs and edge cases (null, empty, concurrent, error paths)
2. Contract violations vs CONTRACT section
3. Security issues (authz, injection, secrets in logs)
4. Test gaps — would a revert pass existing tests?
5. Architecture drift from stated conventions

Output format:
- [CRITICAL] file:line — issue — suggested fix direction
- [SIGNIFICANT] ...
- [MINOR] ...

If no issues after thorough review, say: "No actionable issues found" and list what you checked.
```

---

## Plan / PRD doubt prompt

```
Adversarial review of this plan section. Assume timeline and dependencies are optimistic.

Challenge:
- Hidden integration work (auth, migrations, third-party quotas)
- Tasks missing verification commands
- Horizontal slicing disguised as phases
- Requirements without traceability to FR/NFR
- Single points of failure with no mitigation

ARTIFACT:
<paste phase or task list>

CONTRACT:
<paste feature-spec acceptance criteria or constitution rules>
```

---

## Architecture decision doubt prompt

```
Stress-test this architecture decision before we build on it.

ARTIFACT:
<paste ADR snippet or design paragraph>

CONTRACT:
- Scale: [expected load]
- Team constraints: [skills, timeline]
- Must integrate with: [existing systems]

Find failure modes if we execute perfectly but the decision is wrong.
What cheaper option achieves 80%?
```

---

## TDD / behavioral doubt prompt

Use when CLAIM is a behavioral fix without repro test:

```
The author claims this code change fixes a bug. No failing test was shown.

ARTIFACT:
<diff>

CONTRACT:
- Bug report: [one sentence expected vs actual]
- Prove-It required: test must fail before fix on main

Find: cases where fix appears to work but contract still broken.
Recommend minimal repro test cases (names only).
```

---

## Cross-model offer script (interactive only)

After single-model DOUBT:

```
I've completed one adversarial pass (N findings: X critical, Y significant).
Want a second model to review the same ARTIFACT+CONTRACT cold? (y/n)
```

**Non-interactive / CI:** `Second opinion: skipped (non-interactive)`.

---

## Reconcile precedence (author classifies each finding)

1. **Contract misread** → fix CONTRACT wording, re-run DOUBT
2. **Valid + actionable** → change artifact, re-loop (max 3 cycles)
3. **Valid trade-off** → document explicitly for user decision
4. **Noise** → note; tighten CONTRACT if context would have prevented false flag

### Reconcile output template

```markdown
| Finding | Classification | Action |
|---------|----------------|--------|
| Missing null check | Valid + actionable | Fix in artifact, re-run cycle 2 |
| "Use Redis" | Valid trade-off | Escalate to user |
| Style nit | Noise | Dismiss |
```

---

## Stop conditions

- Trivial / duplicate findings only, **or**
- **3 cycles** completed → escalate to user with summary, **or**
- User says **"ship it"**

### Doubt theater detection

2+ cycles with substantive reviewer output but **zero** findings classified actionable → stop and escalate:

```
Doubt theater detected — reviewer may be validating. Escalate to user with
CLAIM + ARTIFACT + reviewer outputs. Do not loop again without human direction.
```

---

## stdin-safe CLI shapes (optional cross-model)

When spawning external reviewer CLI, pass artifact via file — not shell-escaped paste:

```bash
# Write artifact to temp file
cat > /tmp/artifact.md <<'EOF'
[paste ARTIFACT + CONTRACT only]
EOF

# Invoke reviewer with file input (project-specific CLI)
# Never interpolate user/artifact content into shell -c strings unsanitized
```

---

## Interaction with other skills

| Situation | Skill |
|-----------|-------|
| Behavioral bug fix | `test-driven-development` Prove-It satisfies DOUBT |
| Pre-merge PR | `code-review-crsp` five-axis review |
| Post-hoc document | Three-phase Diagnostic → Creative → Challenge in SKILL.md |
| Inversion | `inversion` — opposite framing; adversarial finds flaws in current |
