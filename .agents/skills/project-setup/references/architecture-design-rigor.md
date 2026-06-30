# Architecture & Design Rigor + Quality Bar

Loaded by `project-setup` when generating an AGENTS.md. Two jobs: (1) decide how
much architecture/design autonomy to hard-wire based on the owner's dev depth,
(2) score the draft AGENTS.md so only a genuinely repo-specific, high-signal file ships.

---

## 1. Owner Persona → Autonomy Policy

Set `owner_mode` from Axis 1 (role + "could you evaluate an architectural decision?"):

| Signal | `owner_mode` | Architecture autonomy | Design autonomy |
|---|---|---|---|
| Non-technical PM / founder, "I couldn't evaluate that" | `non-technical` | Agent-led + mandatory rigor | Agent-led + mandatory rigor |
| Some dev experience, can review | `hybrid` | Agent proposes, owner approves call | Agent-led, owner approves direction |
| Experienced engineer | `technical` | Owner-led, agent advises | Per preference |

For `non-technical` (and the architecture half of `hybrid`), the generated AGENTS.md
MUST include the `## Agent-Led Architecture & Design` block (see template). Never set
architecture/design autonomy to "ask the owner to decide" — they cannot. The agent
decides, applies rigor, and translates the choice into product terms for approval.

---

## 2. Architecture Rigor Mandate (what the block enforces)

Before ANY architectural decision — data model, API/module boundaries, framework or
library choice, state strategy, auth, persistence, deployment, scaling:

1. `brainstorming` — frame 2–4 candidate approaches; get direction approval.
2. `deep-thinking` — pressure-test with `first-principles`, `pre-mortem`,
   `assumption-mapping`, `second-order`. Surface failure modes before committing.
3. `api-and-interface-design` — for any module boundary or public interface.
4. `source-driven-development` — ground framework/library choices in official docs,
   not memory. Cite versions.
5. Translate to a **plain-language trade-off**: 2–4 options, and what each means for
   cost / speed / risk / future flexibility / the end user. Get the owner's approval on
   the PRODUCT implication — not the code.
6. `architectural-decision-log` — record the choice, alternatives, and "why".

Hard rule for the generated file: *never ship an architecture decision the owner
couldn't later have explained to them in one plain sentence.*

---

## 3. Design Rigor Mandate

Before ANY UI/UX work:

1. `frontend-design` orchestrator → `design-direction` (explore 2-3 distinct directions,
   commit to one "feels like X") → `design-system` (DESIGN.md + tokens + icons) →
   build → `design-review` (APCA + state-coverage gates).
2. Translate the chosen direction into product language for owner approval.
3. `design-review` must pass before the UI is considered done.

---

## 4. "Best AGENTS.md" Quality Rubric (self-check before saving)

Score the draft 0–2 on each (0 = absent, 1 = partial, 2 = strong). **Ship only at ≥ 12/14
AND no zero on a starred row.** If it fails, revise and re-score — do not save a draft
that fails the bar.

| # | Criterion | 2 = strong |
|---|---|---|
| 1★ | **Project-specific** | Every section reflects THIS repo/product — no generic filler an agent already knows |
| 2★ | **Command accuracy** | Key Commands are copied from real manifests/Makefile, not guessed |
| 3 | **Non-obvious patterns** | Captures the counterintuitive decisions an agent would otherwise break |
| 4★ | **Boundaries correct** | Allowed / Ask-first / Never match the owner's actual comfort + real protected paths |
| 5★ | **Skill Invocation block present** | Verbatim, non-negotiable block included |
| 6 | **Orchestration Map fits workflow** | Phases + skills match how this team actually ships |
| 7★ | **Persona rigor** | If `owner_mode` non-technical/hybrid, the Agent-Led Architecture & Design block is present and wired to real skills |

Line budget: total AGENTS.md < 150 lines. If over budget, cut generic prose first —
never cut the starred rows' content.

After scoring, show the user the rubric result (e.g. "13/14, no zeros") with the save.
