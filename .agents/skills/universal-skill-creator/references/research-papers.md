# Research Papers — State of the Art in Agent Skill Design

Read this when determining best practices for a new skill, evaluating whether a skill follows current research findings, or when the user asks what the latest research says about skill effectiveness.

---

## Tier 1 — Directly on Agent Skills (Read First)

### Agent Skills for Large Language Models (Feb 2026)
**arXiv:2602.12430** | Gao et al. | Comprehensive survey
> The definitive 2026 survey on the agent skills landscape. Covers: SKILL.md specification and progressive context loading; skill acquisition via RL and autonomous discovery (SEAgent); compositional skill synthesis; computer-use agent (CUA) stack; and a four-tier Security Governance Framework.

**Key findings for skill authors:**
- Progressive disclosure (metadata → body → references) is empirically validated as the correct architecture
- 26.1% of community-contributed skills contain security vulnerabilities — never put executable logic in SKILL.md that hasn't been reviewed
- Seven open challenges identified: cross-platform portability, capability-based permissions, skill versioning, compositional synthesis, autonomous discovery, benchmark standardization, trustworthy governance
- Skills and MCP are complementary layers — skills = procedural knowledge, MCP = external connectivity

**Apply when:** Designing the architecture of any new skill, especially cross-platform ones.

---

### SkillReducer: Optimizing LLM Agent Skills for Token Efficiency (Mar 2026)
**arXiv:2603.29919** | Gao, Li et al. | Empirical study on 55,315 skills
> Large-scale study of real-world skills. Finds systemic inefficiencies and proposes a two-stage compression framework (routing optimization + progressive disclosure restructuring).

**Key findings for skill authors:**
- 26.4% of skills lack routing descriptions entirely → always write a rich description
- Over 60% of skill body content is non-actionable (background, rationale, verbose prose) → cut ruthlessly
- 39% body compression achieves **2.8% quality improvement** — less-is-more is empirically proven
- Taxonomy of content types: Core Rules · Workflow Steps · Output Format · Examples · Background · Edge Cases
- Description compression of 48% with 100% routing preservation via adversarial delta debugging
- Benefits transfer across 5 models from 4 families (mean retention 0.965) — compressed skills are model-agnostic

**Apply when:** Writing or reviewing any skill body. Use the taxonomy to classify content. Move everything that isn't Core Rules, Workflow Steps, or Output Format to references/.

---

### Self-Generated In-Context Examples Improve LLM Agents (NeurIPS 2025)
**NeurIPS 2025 Poster** | Stanford/Berkeley
> Agents that accumulate successful trajectories as in-context examples outperform hand-crafted examples. Naive accumulation: ALFWorld 73%→89%. With curation: 93% — surpassing GPT-4o upgrades.

**Key findings for skill authors:**
- The examples section of a skill is one of its highest-leverage components
- Self-generated, task-specific examples outperform generic hand-crafted ones
- Implication: when a skill has been used successfully, extract real output examples and replace generic ones

**Apply when:** Writing the Examples section of a skill. Prefer real outputs from actual use over synthetic examples.

---

## Tier 2 — Prompt Engineering Foundations

### Rule-Based Role Prompting (Aug 2025)
**arXiv:2509.00482** | Ruangtanusak et al.
> Compares basic role prompting, improved role prompting, automatic prompt optimization (APO), and rule-based role prompting (RRP). RRP wins with character-card/scene-contract design + strict function-call enforcement.

**Key findings for skill authors:**
- Rule-based prompting (explicit MUST/NEVER statements) outperforms elaborate automated optimization
- "Character-card" pattern = role definition + domain + quality standard in the opening paragraph → maps directly to the skill role definition section
- Strict enforcement of tool/function calls outperforms loose descriptions

**Apply when:** Writing the role definition and Hard Rules sections of a skill.

---

### EvoFSM: Finite State Machine for Self-Evolving Agents (Jan 2026)
**arXiv:2601.09465** | Zhang et al.
> Decouples optimization into macroscopic Flow (state-transition logic) and microscopic Skill (state-specific behaviors). Self-evolving memory distills successful trajectories as reusable priors.

**Key findings for skill authors:**
- Workflow steps in a skill = microscopic Skill layer (state-specific behaviors)
- Skill relationships (brainstorming → prd-writing → implementation) = macroscopic Flow layer
- Skills should be scoped to one state/behavior — composability comes from chaining, not monoliths

**Apply when:** Deciding skill scope and how skills in a library chain together.

---

### A Survey on LLM-Based Agent Optimization (Mar 2025)
**arXiv:2503.12434** | Du et al.
> Comprehensive survey of agent optimization. Identifies that standard prompt design fails for long-term planning, dynamic interaction, and complex decision-making without specialized structures.

**Key findings for skill authors:**
- Skills need explicit workflow decomposition for tasks requiring planning (not just role + instructions)
- Dynamic environment interaction requires state-handling sections in the skill
- Complex decision-making benefits from explicit decision trees or branching conditions

**Apply when:** Designing skills for multi-step workflows or agentic tasks.

---

### Multi-Agent Design: Optimizing Prompts and Topologies (Feb 2025)
**arXiv:2502.02533** | Zhou et al.
> Three-stage optimization: block-level prompt optimization → workflow topology → global prompt optimization. MASS-optimized systems substantially outperform baselines.

**Key findings for skill authors:**
- Optimize descriptions (routing layer) first, then body, then cross-skill interactions
- Skill stacking order matters — put foundational skills (brainstorming) before dependent skills (prd-writing)
- Local (per-skill) optimization and global (cross-skill) optimization are both necessary

**Apply when:** Building a skill library with multiple interdependent skills.

---

## Tier 3 — Context Window and Token Budget

### Context Window Best Practices (2025–2026 consensus)
Synthesized from: Vercel AGENTS.md research, Maxim AI context engineering, Claude Code context window analysis

**Hard numbers for skill authors:**
| Layer | Always loaded | Token budget |
|-------|--------------|-------------|
| Skill description | Yes — every session | Target <100 tokens (~400 chars) |
| Skill body | Only when triggered | Target <1,500 tokens (~200 lines) |
| Reference files | Only when explicitly loaded | No practical limit |

**Vercel finding:** An 8KB compressed index in AGENTS.md achieved 100% accuracy vs 53% for a 40KB skill-based system. Information the agent doesn't have to decide to retrieve is more reliable than information it loads on demand.

**Practical implication:** For facts the agent must never miss (hard gates, gotchas), keep them in the body. For everything else, use references/ with specific load triggers.

---

## How to Use This File

When creating a new skill:
1. Check Tier 1 papers for architectural decisions
2. Apply SkillReducer taxonomy to classify every content block before writing
3. Use Rule-Based Role Prompting pattern for the role definition
4. Write examples from real use cases, not synthetic ones (NeurIPS 2025 finding)
5. Keep body under 200 lines — the less-is-more effect is empirically proven

When reviewing an existing skill for quality:
1. Does it follow progressive disclosure? (arXiv:2602.12430)
2. Is 60%+ of the body actionable? (arXiv:2603.29919)
3. Are hard gates and gotchas explicit and in the body? (arXiv:2509.00482)
4. Are examples from real outputs rather than generic placeholders? (NeurIPS 2025)
