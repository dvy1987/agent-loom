# Performance Optimization Patterns

Load when Step 2–3 need concrete fix patterns beyond the symptom table.

## Symptom Decision Tree

```
What is slow?
├── First page load → bundle size, TTFB, render-blocking CSS/JS, hero image
├── Interaction sluggish → long tasks, re-renders, controlled-input overhead
├── After navigation → API waterfalls, client render cost
└── Backend/API → N+1, indexes, connection pool, caching, external deps
```

## N+1 Queries

```typescript
// BAD: one query per row
const tasks = await db.tasks.findMany();
for (const t of tasks) {
  t.owner = await db.users.findUnique({ where: { id: t.ownerId } });
}

// GOOD: join/include
const tasks = await db.tasks.findMany({ include: { owner: true } });
```

## Pagination

Never `findMany()` without limits on list endpoints. Use `take`/`skip` or cursor pagination.

## Images (LCP)

- Explicit `width`/`height` to prevent CLS
- Modern formats (AVIF/WebP) with fallback
- `fetchpriority="high"` for LCP image only
- `loading="lazy"` below the fold

## Bundle Size

- Route-level `lazy()` + `Suspense` for heavy/rare features
- Profile before changing import style — splitting beats micro-import tweaks

## Caching

- Short TTL in-memory for hot read-mostly config
- HTTP `Cache-Control` for static assets (content-hashed filenames)
- Do not cache personalized or auth-sensitive responses without review

## Performance Budgets (example)

```
JS initial: < 200KB gzipped | CSS: < 50KB | API p95: < 200ms | LCP: ≤ 2.5s
```

Enforce via `bundlesize`, Lighthouse CI, or custom scripts in CI.
