# API and Interface Design — Full Worked Examples

Skill: `api-and-interface-design` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** Design tasks API for a new SaaS backend.

**Output:**
```
Contract-first Task + CreateTaskInput + PaginatedResult. REST: GET/POST /api/tasks, GET/PATCH/DELETE /api/tasks/:id. Single APIError body. Zod at route boundary only. Pagination query params on list.
```

## Example 2 — Step-by-step execution

**Input:** "Run `api-and-interface-design` on [concrete task]"

**Agent actions:**
1. Scope the interface
2. Write the contract
3. Apply core principles
4. Review for misuse
5. Document alongside code

## Example 3 — Anti-skip (rationalization defense)

**Input:** Agent tries to skip a gate

| Excuse | Reality |
|---|---|
| "We'll document the API later" | Types are the documentation — define them first. |
| "No pagination needed yet" | You need it at ~100 items; add it now. |
| "PATCH is too hard, use PUT" | Clients want partial updates. |
| "Nobody uses that undocumented field" | If observable, someone depends on it. |

## Example 4 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- Undocumented quirks become dependencies (Hyrum's Law).
- Validation in every internal function adds noise without safety.
- `PUT` for partial updates forces full-object payloads — prefer `PATCH`.
- Skipping pagination guarantees a breaking change at scale.

## Example 5 — Pattern reference (addyosmani/agent-skills)

**Source:** addyosmani snapshot 2026-05-29, security-scanned SAFE.

```
// Define the contract first
interface TaskAPI {
  // Creates a task and returns the created task with server-generated fields
  createTask(input: CreateTaskInput): Promise<Task>;

  // Returns paginated tasks matching filters
  listTasks(params: ListTasksParams): Promise<PaginatedResult<Task>>;

  // Returns a single task or throws NotFoundError
  getTask(id: string): Promise<Task>;

  // Partial update — only provided fields change
  updateTask(id: string, input: UpdateTaskInput): Promise<Task>;

  // Idempotent delete — succeeds even if already deleted
  deleteTask(id: string): Promise<void>;
}
```

---

See `SKILL.md` for hard rules and verification checklist.
