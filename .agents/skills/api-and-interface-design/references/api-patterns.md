# API patterns (api-and-interface-design)

## REST resources

```
GET    /api/tasks              → List (paginated)
POST   /api/tasks              → Create
GET    /api/tasks/:id          → Get one
PATCH  /api/tasks/:id          → Partial update
DELETE /api/tasks/:id          → Delete (idempotent OK)

GET    /api/tasks/:id/comments → Sub-resource list
POST   /api/tasks/:id/comments → Create sub-resource
```

Avoid verbs in URLs: `/api/createTask` → `POST /api/tasks`.

## Pagination response

```json
{
  "data": [],
  "pagination": {
    "page": 1,
    "pageSize": 20,
    "totalItems": 142,
    "totalPages": 8
  }
}
```

Query: `?page=1&pageSize=20&sortBy=createdAt&sortOrder=desc`

## Error body (consistent everywhere)

```typescript
interface APIError {
  error: {
    code: string;      // VALIDATION_ERROR
    message: string;   // Human-readable
    details?: unknown;
  };
}
```

| Status | Use |
|--------|-----|
| 400 | Malformed request |
| 401 | Not authenticated |
| 403 | Not authorized |
| 404 | Not found |
| 409 | Conflict |
| 422 | Semantic validation failed |
| 500 | Server error (no internal leak) |

## TypeScript patterns

```typescript
interface CreateTaskInput {
  title: string;
  description?: string;
  priority?: 'low' | 'medium' | 'high'; // additive optional
}

interface Task {
  id: string;
  title: string;
  description: string | null;
  createdAt: Date;
  updatedAt: Date;
}

type TaskId = string & { readonly __brand: 'TaskId' };

type TaskStatus =
  | { type: 'pending' }
  | { type: 'in_progress'; assignee: string }
  | { type: 'completed'; completedAt: Date };
```

## Boundary validation example

```typescript
app.post('/api/tasks', async (req, res) => {
  const result = CreateTaskSchema.safeParse(req.body);
  if (!result.success) {
    return res.status(422).json({
      error: { code: 'VALIDATION_ERROR', message: 'Invalid task data', details: result.error.flatten() },
    });
  }
  const task = await taskService.create(result.data);
  return res.status(201).json(task);
});
```

Internal service code trusts `result.data` — no re-validation.
