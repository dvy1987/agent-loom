# Knowledge Graph — Full Worked Examples

Native agent-loom + graphify pattern examples.

---

## Example 1 — Query before rebuild

**Input:** "How does memory-handoff connect to knowledge-graph?"

```bash
python3 .agents/skills/knowledge-graph/scripts/query_graph.py path memory-handoff knowledge-graph
```
→ 1 hop `invokes` [EXTRACTED]. No full rebuild needed.

---

## Example 2 — Skill-library vs application mode

| Host | Mode | Nodes |
|---|---|---|
| agent-loom | skill-library | skills, invoke chains |
| Consumer app repo | application | modules, docs, memory |

---

## Example 3 — Handoff incremental sync

After `memory-handoff` Step 7 → `build_graph.py --incremental`. Handoff body skill mentions → semantic edges.

---

## Example 4 — Health audit

```bash
python3 .agents/skills/knowledge-graph/scripts/graph_health.py
```
P0: dangling invoke target. P1: stale vs latest handoff date.

---

## Example 5 — explain subcommand

```bash
python3 .agents/skills/knowledge-graph/scripts/query_graph.py explain validate-skills
```
Inbound/outbound with provenance tags.
