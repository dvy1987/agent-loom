# Prune Skill — Full Worked Examples

Skill: `prune-skill` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** Prune universal-skill-creator — check if its prompting technique recommendations are still valid

**Output:**
```
Citation audit for universal-skill-creator:
- arXiv:2602.12430 (Feb 2026): real | arXiv preprint, agent skills survey | recent | accurate
- arXiv:2603.29919 (Mar 2026): real | arXiv preprint, SkillReducer | recent | accurate
- arXiv:2509.00482 "Rule-Based Role Prompting": real | arXiv | Sep 2025 | PARTIALLY MISREPRESENTED

Issue found: arXiv:2509.00482 is cited as evidence that role prompting beats automated optimization. However, arXiv:2409.13979 (Feb 2025 update) shows role prompting does NOT expand factual accuracy on frontier models and may amplify bias. The skill's instruction "You are a [specific expert] specializing in [domain]" is role prompting.

Classification:
- Role prompting instruction: Accurate but outdated for frontier models → Replace with scoped version

Prune applied:
- Corrected: Role definition section — changed from universal instruction to scoped: "Add role definition for domain-specific tasks on non-frontier models. For GPT-5/Claude 4 class models, role definition adds minimal value — focus on workflow clarity instead." (arXiv:2409.13979)

Prune Log added to SKILL.md.
agentskills validate: ✓
```

## Example 2 — Step-by-step execution

**Input:** "Run `prune-skill` on [concrete task]"

**Agent actions:**
1. Read the Skill
2. Citation Audit
3. Obsolescence Check
4. Compile Prune List
5. Apply Prunes
6. Validate and Report

**Impact Report shape:**
```
Prune complete: [skill-name]
Citations audited: N
Items pruned: N
  - Removed: [item] ([source])
Items corrected: N
  - Corrected: [item] ([source])
Flagged for author review: N
Prune Log added to SKILL.md: yes
Files modified: .agents/skills/[skill-name]/SKILL.md
```

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- **Absence of evidence ≠ evidence of absence.** If you cannot find a paper disproving a technique, that does not mean the technique is valid. It means it is unverified — flag it, don't prune it.
- **Recency bias is its own failure mode.** Newer is not always better. Some 2022 findings remain valid. Require evidence of obsolescence, not just a newer paper that doesn't mention the technique.
- **Prune the instruction, not the concept.** If "use chain-of-thought" is obsolete for reasoning models, prune the instruction to use it universally — but you may keep a scoped version: "use CoT on non-reasoning models only."
- **Never prune gotchas without strong evidence.** Gotchas represent hard-won domain knowledge. The bar for pruning a gotcha is higher than for pruning a general technique instruction.

---

See `SKILL.md` for hard rules and verification checklist.
