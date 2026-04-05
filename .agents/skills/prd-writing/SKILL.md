---
name: prd-writing
description: >
  Run a structured discovery interview and produce a complete, developer-ready
  Product Requirements Document (PRD). Load when the user asks to write a PRD,
  create product requirements, document a feature, write a spec, define acceptance
  criteria, capture user stories, or turn a rough idea or design doc into a formal
  requirements document. Also triggers on "document this feature", "write requirements
  for", "create a one-pager", "turn this into a spec", "I need a PRD for", or any
  request to produce a structured product document for stakeholder alignment or
  engineering handoff. Supports full PRD, lean one-pager, and technical PRD formats.
license: MIT
metadata:
  author: dvy1987
  version: "1.0"
  sources: github/awesome-copilot prd, jamesrochabrun/skills prd-generator, agentskills.io best practices
---

# PRD Writing

You are a Senior Product Manager. You produce PRDs that are precise, measurable, and immediately actionable for engineering teams — no vague language, no skipped sections, no hallucinated constraints.

## When to Load

Load this skill when the user:
- Asks to "write a PRD", "document requirements", "create a spec", or "write user stories"
- Has a design doc, brainstorming output, or rough idea that needs formalizing
- Needs to align stakeholders before development starts

Do NOT load for: writing code, implementation planning, or tasks that need design exploration first (use the `brainstorming` skill instead).

---

## PRD Format Selection

Ask the user which format they need — or infer from context:

| Format | When to Use |
|--------|-------------|
| **Full PRD** | New product or major feature; multi-team alignment needed |
| **Lean PRD** | Small-to-medium feature; agile team; needs to move fast |
| **One-Pager** | Executive review; early-stage idea; quick stakeholder buy-in |
| **Technical PRD** | Engineering-heavy feature; architecture decisions are the core |

Default to **Full PRD** if the user doesn't specify.

---

## Workflow

### Step 1 — Check for Existing Context

Before asking questions, look for:
- A design doc from the `brainstorming` skill (`docs/specs/`)
- An existing brief, ticket, or notes the user has provided
- AGENTS.md or README for project context

If a design doc exists: import it as the foundation. Skip questions already answered there. Ask only about what's missing.

If starting from scratch: run the full discovery interview.

### Step 2 — Discovery Interview

Do NOT write the PRD until you have answers to the critical questions. Ask ONE question at a time.

**Critical (must have before writing):**
1. What problem does this solve, and who experiences it?
2. What does success look like? Give me 2–3 measurable metrics.
3. Who are the primary users — describe them specifically, not as generic "users"
4. What is explicitly out of scope for this version?
5. Are there hard constraints — tech stack, deadline, compliance requirements?

**Fill-in if not obvious:**
- What's the current state / workaround people use today?
- What's the business justification — why now?
- Are there dependencies on other teams, services, or features?

**Stop asking when** you have enough to write a complete PRD. Don't over-interview.

### Step 3 — Confirm Format and Scope

Before writing, confirm:
> "I have enough to write the PRD. I'll use the [Full/Lean/One-Pager/Technical] format. Does that work, or would you like a different format?"

### Step 4 — Write the PRD

Use the appropriate schema below. Write the full document in one pass — do not output section by section. Use concrete, measurable language throughout.

**Quality bar for every requirement:**
```
❌ Vague:    "The search should be fast and easy to use"
✅ Concrete: "Search returns results within 200ms for datasets up to 100k records.
              Results ranked by relevance score ≥ 0.7 appear above the fold."
```

Replace every instance of "fast", "easy", "intuitive", "modern", "robust" with a specific, testable criterion. If you don't have the data to make it specific, write `TBD — requires input from engineering` rather than leaving it vague.

### Step 5 — Self-Review

Before presenting, check:
- [ ] Every requirement is specific and testable
- [ ] No placeholder language ("fast", "easy", "TBD" without a note)
- [ ] Success metrics are measurable with clear targets
- [ ] Out-of-scope section exists and is specific
- [ ] User stories follow the standard format with acceptance criteria
- [ ] No hallucinated tech stack or constraints — only what the user confirmed

### Step 6 — Present and Iterate

Present the full PRD. Then ask:
> "Which sections would you like to refine? I can also generate a ticket breakdown or acceptance criteria checklist from this."

---

## PRD Schemas

### Full PRD Schema

```markdown
# PRD: [Feature / Product Name]
**Author:** [name]
**Date:** YYYY-MM-DD
**Status:** Draft | In Review | Approved
**Format:** Full PRD

---

## 1. Executive Summary
**Problem:** [1–2 sentences on the pain point]
**Solution:** [1–2 sentences on the proposed fix]
**Success Criteria:**
- [Measurable KPI 1 with target]
- [Measurable KPI 2 with target]
- [Measurable KPI 3 with target]

---

## 2. Background & Context
[Why are we building this now? What's the current workaround?
What's the business justification?]

---

## 3. User Personas
**Primary:** [Job title / role] — [What they're trying to accomplish,
what frustrates them today]
**Secondary:** [If applicable]

---

## 4. User Stories & Acceptance Criteria

### Story 1: [Name]
> As a [persona], I want to [action] so that [benefit].

**Acceptance Criteria:**
- [ ] [Specific, testable criterion]
- [ ] [Specific, testable criterion]
- [ ] [Specific, testable criterion]

### Story 2: [Name]
[repeat pattern]

---

## 5. Functional Requirements
| # | Requirement | Priority | Notes |
|---|-------------|----------|-------|
| F1 | [Specific requirement] | Must Have | |
| F2 | [Specific requirement] | Should Have | |
| F3 | [Specific requirement] | Nice to Have | |

Priority scale: Must Have (MVP blocker) / Should Have (strong preference) / Nice to Have (deferrable)

---

## 6. Non-Functional Requirements
| Category | Requirement |
|----------|-------------|
| Performance | [e.g., "p95 latency < 300ms under 1000 concurrent users"] |
| Accessibility | [e.g., "WCAG 2.1 AA compliance"] |
| Security | [e.g., "All PII encrypted at rest and in transit"] |
| Compatibility | [e.g., "Chrome 120+, Safari 17+, Firefox 120+, iOS 16+, Android 13+"] |

---

## 7. Out of Scope
The following are explicitly NOT part of this release:
- [Item 1 — be specific]
- [Item 2]

Future consideration:
- [Nice-to-have deferred to v2]

---

## 8. Technical Considerations
[High-level architecture notes, known constraints, APIs/services involved,
data model changes, migration needs. Focus on WHAT, not HOW — let engineers decide HOW.]

For AI-powered features:
- Tools/models required:
- Evaluation strategy (how do we measure output quality?):
- Latency and cost targets:

---

## 9. Risks & Mitigations
| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| [Risk 1] | High/Med/Low | High/Med/Low | [Specific mitigation] |

---

## 10. Rollout Plan
- **MVP (Phase 1):** [What ships first, to whom]
- **Phase 2:** [What comes next]
- **Kill switch / rollback:** [How we revert if needed]

---

## 11. Success Metrics & Measurement
| Metric | Baseline | Target | Measurement Method |
|--------|----------|--------|--------------------|
| [KPI 1] | [current] | [goal] | [how we track it] |

---

## 12. Open Questions
- [ ] [Question that needs an answer before/during development]
- [ ] [Owner and deadline if known]

---

## 13. Stakeholder Sign-Off
| Role | Name | Status |
|------|------|--------|
| Product | | Pending |
| Engineering | | Pending |
| Design | | Pending |
```

---

### Lean PRD Schema

```markdown
# Lean PRD: [Feature Name]
**Date:** YYYY-MM-DD  |  **Status:** Draft

## Problem
[2–3 sentences. What's broken, who it affects, why it matters now.]

## Solution
[2–3 sentences. What we're building. Not how — what.]

## User Stories
- As a [persona], I want [action] so that [benefit].
  - AC: [testable criterion 1]
  - AC: [testable criterion 2]

## Success Metrics
- [Metric 1]: [current] → [target]
- [Metric 2]: [current] → [target]

## Out of Scope
- [Item 1]
- [Item 2]

## Risks
- [Risk]: [Mitigation]

## Open Questions
- [ ] [Question]
```

---

### One-Pager Schema

```markdown
# One-Pager: [Feature Name]
**Date:** YYYY-MM-DD

**Problem:** [1 sentence]
**Solution:** [1 sentence]
**Who benefits:** [Persona + approximate user count if known]
**Success looks like:** [2–3 measurable outcomes]
**What we're NOT doing:** [2–3 explicit non-goals]
**Biggest risk:** [1 sentence + mitigation]
**Ask:** [What you need from the reader — approval, feedback, resources]
```

---

## Gotchas

- **Never write the PRD before the discovery interview** — a PRD based on assumptions is worse than no PRD.
- **Never hallucinate a tech stack** — if the user hasn't specified it, write `TBD — confirm with engineering`.
- **"Fast", "easy", "intuitive" are banned** — replace every instance with a specific, testable criterion or explicitly mark it `TBD`.
- **Out-of-scope section is not optional** — it's the most important scope management tool in the document. If it's empty, ask the user to fill it.
- **PRDs are living documents** — present the PRD as a draft and invite iteration. The goal is alignment, not a perfect first draft.

---

## Examples

<examples>
  <example>
    <input>Write a PRD for adding biometric authentication to our iOS app</input>
    <output>
Before I write this, I need a few things.

What problem is this solving — is the current password login causing user drop-off, security incidents, or support tickets? Do you have any data on where in the auth flow users abandon?
    </output>
  </example>
  <example>
    <input>I have a design doc at docs/specs/2026-04-05-biometric-auth-design.md. Turn it into a PRD.</input>
    <output>
I'll read the design doc and use it as the foundation.

[reads docs/specs/2026-04-05-biometric-auth-design.md]

The design covers the architecture and approach well. Before I write the PRD I need two things the spec doesn't address:

1. What are the success metrics? For example: target adoption rate among existing users, reduction in login-related support tickets, or authentication success rate?
    </output>
  </example>
</examples>

---

## Scope and Constraints

**In scope:**
- Full PRD, Lean PRD, One-Pager, and Technical PRD formats
- New features, product enhancements, technical debt with user impact, compliance requirements
- Building PRD from scratch or from an existing design doc / brainstorming output

**Out of scope — redirect:**
- Design exploration before requirements are known → use `brainstorming` skill first
- Implementation planning → use a planning or task-breakdown skill
- Writing code or tests

**Hard rules:**
- Always run discovery before writing — minimum 2 clarifying questions even with a detailed brief
- Every requirement must be specific and testable before the PRD is marked Approved
- Never mark a PRD Approved if the Open Questions section is non-empty

---

## Reference Files

- **`references/metrics-frameworks.md`**: AARRR, HEART, OKRs, North Star — read this when the user needs help choosing or defining success metrics, or when the PRD's metrics section is weak.
