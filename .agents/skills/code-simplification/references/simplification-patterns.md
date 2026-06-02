# Simplification patterns (code-simplification)

## Signal table

| Pattern | Signal | Simplification |
|---------|--------|----------------|
| Deep nesting (3+) | Hard to follow flow | Guard clauses, extract helpers |
| Long functions (50+ lines) | Multiple responsibilities | Split named functions |
| Nested ternaries | Mental stack | if/else, switch, lookup map |
| Boolean flag params | `fn(true, false)` | Options object or separate functions |
| Repeated conditionals | Same `if` in many places | Named predicate function |
| Generic names | `data`, `result`, `temp` | Domain-specific names |
| Abbreviations | `usr`, `cfg` | Full words unless universal (`id`, `url`) |
| "What" comments | `// increment` above `++` | Delete; keep "why" comments |
| Duplicated logic | Same 5+ lines twice | Shared function |
| Dead code | Unreachable, unused imports | Remove after confirming dead |
| Wrapper with no value | Pass-through only | Inline or delete |

## TypeScript / JavaScript (selected)

```typescript
// Before: unnecessary async
async function getUser(id: string) {
  return await userService.findById(id);
}
// After
function getUser(id: string) {
  return userService.findById(id);
}

// Before: manual filter loop
const active: User[] = [];
for (const u of users) if (u.isActive) active.push(u);
// After
const active = users.filter((u) => u.isActive);
```

## Python (selected)

```python
# Before: nested ifs
def process(data):
    if data is not None:
        if data.is_valid():
            return do_work(data)
# After: guard clauses
def process(data):
    if data is None:
        raise TypeError("Data is None")
    if not data.is_valid():
        raise ValueError("Invalid data")
    return do_work(data)
```

## React (judgment calls)

- Verbose conditional render → early return or small derived variables
- Prop drilling → flag for composition/context review; do not auto-refactor without user approval
