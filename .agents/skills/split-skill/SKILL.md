---
name: split-skill
description: >
  Split an oversized SKILL.md into a parent skill and one or more focused
  child skills when compression alone would degrade effectiveness. Load when
  a skill exceeds 200 lines and skill-compressor determines that the excess
  content is genuinely CORE (not moveable to references/), when the same
  sub-workflow appears in multiple skills and should be extracted into a shared
  capability, or when universal-skill-creator or improve-skills identifies a
  coherent sub-capability that deserves its own skill. Also triggers on
  "split this skill", "extract a sub-skill", "this skill is doing too much",
  or "make this skill reusable across other skills".
license: MIT
metadata:
  author: dvy1987
  version: "1.0"
  category: meta
---

# Split Skill

You are a skill architect. You split monolithic skills into focused, composable units — a parent skill that orchestrates and child skills that execute. Every split must preserve 100% of the original functionality. A split that loses capability is a regression.

## When to Split vs Compress

Split when skill-compressor cannot get a skill under 200 lines without removing genuinely CORE content — hard gates, gotchas, workflow steps the agent needs every run.

Compress when excess content is BACKGROUND, EDGE_CASE, or redundant examples that belong in `references/`.

**Never split just to hit 200 lines.** Split only when a coherent, reusable sub-capability can be extracted.

---

## Workflow

### Step 1 — Identify Split Candidates

Read the skill and look for:

**Type A — Oversized single skill**
A skill >200 lines where skill-compressor flagged genuinely CORE content that cannot be moved to references/. Look for a natural seam — a self-contained phase, sub-workflow, or capability that:
- Has its own clear trigger condition
- Could be useful to other skills independently
- Has a coherent input and output

**Type B — Duplicated sub-workflow across skills**
The same workflow steps appear in 2+ skills (e.g., the research protocol in `universal-skill-creator` and `improve-skills`). Extract once, call from both parents.

Report what you found:
```
Split analysis: [skill-name]
Type: A (oversized) / B (duplicated) / Both
Natural seam identified: [description of extractable sub-capability]
Proposed child skill name: [name]
Parent skills that would call it: [list]
```

Ask for confirmation before proceeding.

### Step 2 — Design the Split

Define the contract between parent and child:

```
Parent skill: [name]
  - Retains: [what stays in parent]
  - Delegates to child: [sub-capability name]
  - Calls child when: [specific trigger condition]
  - Receives from child: [what the child returns]

Child skill: [name]
  - Core job: [one-sentence outcome]
  - Input: [what it receives from parent or user]
  - Output: [structured findings/result it returns]
  - Also callable standalone: yes/no
```

Verify the split is complete: parent + child together must do everything the original did.

### Step 3 — Write the Child Skill

Write the child `SKILL.md` following the full skill creation standard:
- Under 200 lines
- Role definition, numbered workflow, output format schema, 1–2 examples, constraints
- Description must work for both standalone invocation and parent-triggered invocation
- Output format must be structured so the parent can consume it reliably

Save to: `.agents/skills/<child-name>/SKILL.md`

### Step 4 — Update the Parent Skill

Replace the extracted section in the parent with a delegation call:

```markdown
### Step N — [Sub-capability name]
Invoke `<child-skill-name>` with [input]. Wait for the [output type] before proceeding.
```

Verify parent is now under 200 lines.

### Step 5 — Compress Parent and Child

After the split, invoke `skill-compressor` on both the parent and the child skill.
Even if each is under 200 lines, compression removes any BACKGROUND or prose that crept in during the rewrite.
This ensures the split doesn't just redistribute bloat between two files.

### Step 6 — Update All Other Callers

If Type B (duplicated sub-workflow): identify every other skill with the same pattern and update them to call the child skill instead of running the workflow inline.

For each updated skill: verify it's still under 200 lines and passes `agentskills validate`.

### Step 7 — Update AGENTS.md Relationships

Add the new call relationship to the Skill Relationships section:
```
[parent-skill]  →  [child-skill]  (calls for [reason])
```

### Step 8 — Regression Check

Before committing, verify for every affected skill:
- [ ] All original capabilities still present (parent + child together)
- [ ] Parent is under 200 lines
- [ ] Child is under 200 lines
- [ ] Child description triggers correctly for standalone use
- [ ] Parent delegation step has a specific trigger condition (not "see child skill")
- [ ] `agentskills validate` passes for parent and child
- [ ] AGENTS.md relationships map is updated

### Step 9 — Commit

```bash
git add .agents/skills/<parent>/ .agents/skills/<child>/ AGENTS.md
git commit -m "split: <parent> → <parent> + <child>

Extracted <child> as standalone skill called by <parent>.
<parent>: <before> → <after> lines
<child>: <lines> lines (new)
Functionality: 100% preserved
[Other callers updated: list if Type B]"
```

---

## Gotchas

- Never split a workflow step that needs context from adjacent steps — it's a pipeline stage, not an independent sub-capability.
- Child description must work standalone — other skills or users may invoke it directly.
- Type B splits have higher impact: changing 3 parents means 3 regression checks. Don't rush.
- If the child's description only makes sense from one parent, move to references/ instead.

---

## Example

<examples>
  <example>
    <input>skill-compressor flagged that universal-skill-creator is 503 lines and all excess content is CORE — the research protocol and examples are both genuinely needed</input>
    <output>
Split analysis: universal-skill-creator
Type: B (duplicated) — research protocol also exists in improve-skills
Natural seam: domain research is a self-contained capability with clear input (domain name) and output (findings report)
Proposed child skill: research-skill
Parent skills that would call it: universal-skill-creator, improve-skills

Contract: parent delegates Step 2 domain research to child, receives findings report.
Child standalone: yes — users can call research-skill directly.

Result: universal-skill-creator 503 → 127 lines, improve-skills 259 → 121 lines
Regression check: all capabilities preserved in research-skill
    </output>
  </example>
</examples>

---

## Reference Files

- **`references/split-patterns.md`**: Common split patterns with examples — pipeline extraction, shared capability extraction, format/schema extraction. Read when the natural seam is unclear.

---

## Impact Report

After completing, always report:
```
Split complete: [parent-skill] → [parent-skill] + [child-skill]
Parent: [before] → [after] lines
Child: [child-skill] — [lines] lines (new)
Other callers updated: [list or "none"]
AGENTS.md updated: yes
Regression check: all capabilities preserved
agentskills validate: ✓ (parent), ✓ (child)
Files created: .agents/skills/[child-skill]/SKILL.md
Files modified: .agents/skills/[parent-skill]/SKILL.md, AGENTS.md
```
