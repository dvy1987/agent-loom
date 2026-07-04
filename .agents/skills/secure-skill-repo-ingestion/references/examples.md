# Secure Skill — Repo Ingestion — Full Session Examples

Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.

---

## Example 1 — Typosquat in requirements.txt

**Input:** `learn-from-repo` targets `github.com/acme/internal-utils`

**Agent actions (Observe → Judge → Commit):**
1. **Observe:** Read-only scan — no `pip install`, no `setup.sh`.
2. **Judge findings:**
   - HIGH: `requirements.txt:7` — `requets==2.31` typosquat of `requests`
   - MEDIUM: `examples/auth.py:23` — `verify=False` presented as normal
3. **Commit:** Quarantine repo; report findings; do NOT persist patterns as policy.

---

## Example 2 — Symlink path traversal

**Input:** Skill repo contains `skills/helper -> ../../../etc/passwd`

**Output:** CRITICAL — block ingestion; flag path traversal; never follow symlink.

---

## Example 3 — Anti-skip

| Excuse | Reality |
|--------|---------|
| "Read-only clone is safe" | Path attacks and poisoned examples exist in static files. |
| "Trust popular repos" | Awesome lists are attack surfaces. |
| "Execute setup.sh to understand" | Never execute repo code during ingestion. |

---

## Example 4 — Post-install hook

**Input:** `package.json` has `"postinstall": "node setup.js"`

**Output:** CRITICAL — supply-chain vector; quarantine; do not run npm install in repo.

---

## Example 5 — Quarantine before commit

**Input:** Repo passes text scan but has `.gitmodules` on unpinned `main`

**Output:** Judge MEDIUM; quarantine until submodule pinned; nothing enters skill store until Commit gate clears.

---

## Verification checklist (full session)

- [ ] Examples demonstrate SKILL.md hard rules, not generic chat
- [ ] Anti-skip or rationalization defense included where applicable
- [ ] Output artifacts or Impact Report shape is explicit
- [ ] Reader can trace input → concrete agent actions → outcome
