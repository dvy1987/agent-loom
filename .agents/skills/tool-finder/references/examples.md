# Tool Finder — Full Worked Examples

Skill: `tool-finder` | Load when producing output for this workflow.

## Example 1 — From skill workflow

**Input:** Find a tool for: "search the web for recent research papers"

**Output:**
```
Tool: WebSearch
Category: Web search
Status: available (agent built-in)
No setup needed.
```

## Example 2 — From skill workflow

**Input:** Find a tool for: "query a PostgreSQL database"

**Output:**
```
Tool: PostgreSQL MCP server
Category: MCP server
Status: needs-setup
Setup: Configure `mcp__postgres` in your MCP settings with connection string. See: https://github.com/modelcontextprotocol/servers/tree/main/src/postgres
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
