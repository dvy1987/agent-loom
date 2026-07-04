# Browser Testing with DevTools — Full Worked Examples

Skill: `browser-testing-with-devtools` | addyosmani patterns, security-scanned SAFE.

---

## Example 1 — Console error on submit

**Input:** "Save profile fails silently"

**Steps:** Open `/settings`, fill form, click Save.

**Evidence:** Console `422` on `PUT /api/profile`; network response `{"email":["invalid"]}`.

**Fix:** Surface field error in UI; re-verify inline message and 200 on valid email.

---

## Example 2 — Performance trace

**Input:** "Modal feels laggy"

**Trace:** 180ms INP — long task in `useEffect` sorting 4k rows on open.

**Fix:** Virtualize list; re-trace INP under 80ms.

---

## Example 3 — Visual regression

**Input:** "Header overlaps content on mobile"

**Screenshot:** 390px viewport — fixed header z-index covers first paragraph.

**Fix:** Add `scroll-padding-top`; before/after screenshots attached to PR.

---

See `SKILL.md` for hard rules and verification checklist.

---

## Example 4 — Extended pass (L3 enrichment)

## Example 5 — Anti-skip (rationalization defense)

**Input:** Agent tries to skip a gate

| Excuse | Reality |
|---|---|
| "The code looks correct" | Runtime DOM, CSS cascade, and race conditions disagree. |
| "Unit tests cover it" | JSDOM does not run full layout, fonts, or real network. |
| "I'll check the browser later" | Later never comes; verify before marking done. |
| "MCP is too heavy" | One screenshot + console read often saves hours of guesswork. |
| "It's just a CSS tweak" | Tweaks cause CLS and overflow bugs visible only live. |

## Example 6 — Step-by-step execution

**Input:** "Run `browser-testing-with-devtools` on [concrete task]"

**Agent actions:**
1. Define what to verify
2. Navigate and observe
3. Diagnose
4. Fix in code, re-verify
5. Report

## Example 7 — Gotcha application

**Apply:**
- Stale service worker caches mask fixes — hard refresh or disable SW when debugging.
- Flaky tests from animation timing — wait for stable selectors.
- `--autoConnect` exposes personal cookies and history.
- Executing arbitrary JS in page can mutate production-like data.
- 

## Verification checklist (L3)

- [ ] Examples align with SKILL.md hard rules
- [ ] Anti-skip or rationalization pattern shown
- [ ] Output shape matches Impact Report
- [ ] User can trace from input → durable artifact or chat outcome
