# Chrome DevTools MCP Setup

Load when Step 1 reports MCP unavailable.

## Install (project `.mcp.json` or agent settings)

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

- `--isolated`: temporary profile wiped on close — preferred for localhost testing.
- Default without connect flags: dedicated profile under cache dir, separate from daily Chrome.
- `--autoConnect` (Chrome 144+): attaches to running Chrome — only when logged-in state is required; warn user about open tabs and sessions.

## Tool capabilities

| Tool | Use |
|------|-----|
| Screenshot | Visual before/after |
| DOM inspection | Structure and rendering |
| Console | Errors and warnings |
| Network | Request/response debugging |
| Performance trace | LCP, long tasks, CLS |
| Accessibility tree | Names, roles, hierarchy |
| JS execution | Read-only state inspection (see SKILL.md security rules) |

If MCP cannot be installed in the environment, defer browser verification to manual DevTools or document the gap — do not pretend runtime was verified.
