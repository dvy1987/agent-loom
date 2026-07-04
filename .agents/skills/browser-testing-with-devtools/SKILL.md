---
name: browser-testing-with-devtools
description: >
  Test and debug browser UIs using Chrome DevTools MCP — DOM inspection,
  console errors, network requests, performance traces, and visual verification.
  Load when building or debugging anything that renders in a browser, verifying
  a UI fix, profiling Core Web Vitals in a real page, or the user asks for
  browser testing with DevTools. Requires chrome-devtools MCP configured. Not
  for backend-only or CLI work. Pairs with frontend-design and performance-optimization.
license: MIT
metadata:
  author: dvy1987
  version: "1.0"
  category: project-specific
  sources: addyosmani/agent-skills browser-testing-with-devtools (11/12, 2026-05-29)
  resources:
    references:
      - examples.md
---

# Browser Testing with DevTools

Use Chrome DevTools MCP to verify runtime behavior — what the user sees, not what static analysis guesses.

## Hard Rules

- **Verify in browser** before claiming a UI fix works.
- Use **isolated profile** by default (`--isolated`); never use personal browser for untrusted pages.
- **Read-only JS** in page context unless user explicitly approves mutations.
- Capture **evidence**: screenshot, console excerpt, network failure, or trace — not vibes.
- Reproduce from a **clean navigation** when debugging flaky UI.

---

## Setup (chrome-devtools MCP)

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest", "--isolated"]
    }
  }
}
```

Use `--autoConnect` only when logged-in state is required — document the security trade-off.

---

## Workflow

### Step 1 — Define what to verify

State: URL, user action, expected DOM/console/network outcome.

### Step 2 — Navigate and observe

- Screenshot for visual state
- Console for errors/warnings
- Network for failed requests or wrong payloads
- DOM/a11y tree for structure and labels

### Step 3 — Diagnose

Map symptom → tool: layout → computed styles; slow paint → performance trace; API bug → network panel.

### Step 4 — Fix in code, re-verify

Same steps as Step 2 after change; keep before/after screenshots when useful.

### Step 5 — Report

Include evidence snippets and whether issue is fully resolved or partially mitigated.

---

## When NOT to use

- Pure server/API changes with no browser surface
- Environments where MCP cannot run (document manual repro instead)

---

## Gotchas

- Stale service worker caches mask fixes — hard refresh or disable SW when debugging.
- Flaky tests from animation timing — wait for stable selectors.
- `--autoConnect` exposes personal cookies and history.
- Executing arbitrary JS in page can mutate production-like data.

---

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "The code looks correct" | Runtime DOM, CSS cascade, and race conditions disagree. |
| "Unit tests cover it" | JSDOM does not run full layout, fonts, or real network. |
| "I'll check the browser later" | Later never comes; verify before marking done. |
| "MCP is too heavy" | One screenshot + console read often saves hours of guesswork. |
| "It's just a CSS tweak" | Tweaks cause CLS and overflow bugs visible only live. |

---

## Output Format

```markdown
## Browser verification — [feature]

URL: [path]
Steps: [actions]
Evidence: [screenshot/console/network]
Result: [pass/fail + notes]
```

---

## Examples

<examples>
  <example>
    <input>"Button click does nothing on /checkout."</input>
    <output>Console: `TypeError` on click handler; network shows no POST; fix null guard; re-verify POST 200 and success UI.</output>
  </example>
</examples>

---

## Verification

- [ ] Reproduced issue in browser with evidence captured
- [ ] Post-fix verification on same steps
- [ ] No new console errors on happy path
- [ ] Isolated profile used (or autoConnect risk documented)
- [ ] Network/DOM findings tied to specific code change

---

## Red Flags

- UI fix claimed done without browser verification
- Personal browser profile used on untrusted pages
- Page-context JS mutates state without explicit approval
- Stale service worker cache masks whether fix works
## Impact Report

```
URL: [path] | Issue: [one line]
Evidence: [screenshot/console/network]
Status: [fixed/partial/blocked]
```
