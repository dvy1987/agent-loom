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
