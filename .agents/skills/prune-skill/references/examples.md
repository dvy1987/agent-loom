# Prune Skill — Full Worked Examples

Skill: `prune-skill` | Load when producing output for this workflow.

## Example 1 — From skill workflow

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

## Example 2 — Typical invocation

**Input:** "Run `prune-skill` for [concrete task]"

**Output:**
```
Invoked `prune-skill`.
Step 1: Read the Skill
Step 2: Citation Audit
Step 3: Obsolescence Check
See SKILL.md Impact Report schema.
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
