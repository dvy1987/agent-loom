# UI Implementation Patterns (reference)

AO `frontend-ui-engineering` craft merged into agent-loom build phase. Read during Step 4 (Build) alongside `golden-examples/*` and `build-conventions.md`.

**Stack assumption:** React/Next patterns shown; translate principles to Vue/Svelte per `build-conventions.md`.

---

## Container / presentation split (required for data surfaces)

```tsx
// containers/TeamListContainer.tsx — data + states
export function TeamListContainer() {
  const { data, error, isLoading } = useTeams();
  if (isLoading) return <TeamListSkeleton />;
  if (error) return <TeamListError error={error} onRetry={refetch} />;
  if (!data?.length) return <TeamListEmpty onCreate={openCreate} />;
  return <TeamListView teams={data} />;
}

// components/TeamListView.tsx — pure presentation
export function TeamListView({ teams }: { teams: Team[] }) {
  return (
    <ul className="divide-y divide-[var(--border-subtle)]">
      {teams.map((t) => (
        <li key={t.id} className="py-[var(--space-3)]">{t.name}</li>
      ))}
    </ul>
  );
}
```

**Rule:** Presentation components receive props only — no `fetch`, no router side effects.

---

## State management ladder (when to escalate)

| Level | Use when | Example |
|-------|----------|---------|
| `useState` | Single component UI | modal open, hover |
| Lifted state | 2–3 siblings share | filter + list + count |
| Context | Read-heavy global | theme, auth session, locale |
| URL search params | Shareable/bookmarkable | `?tab=`, `?page=`, filters |
| Server cache (TanStack Query, SWR) | Server data with staleness | lists, detail views |
| Global client store (Zustand, etc.) | Complex cross-route client state | cart, multi-step wizard |

**Anti-pattern:** Global store for data that belongs in URL or server cache.

---

## Optimistic updates (toggles, edits, deletes)

```tsx
const mutation = useMutation({
  mutationFn: updateTodo,
  onMutate: async (next) => {
    await queryClient.cancelQueries({ queryKey: ['todos'] });
    const previous = queryClient.getQueryData<Todo[]>(['todos']);
    queryClient.setQueryData(['todos'], (old) =>
      old?.map((t) => (t.id === next.id ? { ...t, ...next } : t))
    );
    return { previous };
  },
  onError: (_err, _next, context) => {
    queryClient.setQueryData(['todos'], context?.previous);
    toast.error('Could not save — reverted');
  },
  onSettled: () => queryClient.invalidateQueries({ queryKey: ['todos'] }),
});
```

**Requirements:** rollback on error, `aria-live` or toast for failure, disabled double-submit.

---

## Loading patterns

| Surface | Pattern | a11y |
|---------|---------|------|
| List / card grid | Skeleton matching layout | `aria-busy="true"` on region |
| Button action | Inline spinner + `disabled` | `aria-disabled` |
| Full page | Skeleton shell, not blank | focus management on load complete |
| Background refresh | Subtle opacity pulse on stale data | don't steal focus |

Avoid center-screen spinners for content areas — they read as unfinished (see `golden-examples/states.md`).

---

## Empty states (not an afterthought)

Every list/table needs:

1. **Illustration or icon** — token-colored, not stock clipart
2. **Headline** — what this area is for
3. **Primary action** — create, import, connect
4. **Secondary** — docs link if complex

```tsx
export function TeamListEmpty({ onCreate }: { onCreate: () => void }) {
  return (
    <div className="flex flex-col items-center py-[var(--space-12)] text-center">
      <TeamIcon className="size-12 text-[var(--text-muted)]" aria-hidden />
      <h2 className="mt-[var(--space-4)] text-[var(--text-primary)]">No teams yet</h2>
      <p className="mt-[var(--space-2)] max-w-sm text-[var(--text-secondary)]">
        Create a team to invite collaborators.
      </p>
      <Button className="mt-[var(--space-6)]" onClick={onCreate}>Create team</Button>
    </div>
  );
}
```

---

## Error states

- **Inline field errors** — `aria-describedby` linking input to error id
- **Section errors** — retry button + preserved user input
- **Fatal page errors** — error boundary with recovery path (reload, go home)

```tsx
export function TeamListError({ error, onRetry }: { error: Error; onRetry: () => void }) {
  return (
    <div role="alert" className="rounded-[var(--radius-md)] border border-[var(--status-error)] p-[var(--space-4)]">
      <p className="text-[var(--status-error-text)]">Could not load teams.</p>
      <Button variant="secondary" className="mt-[var(--space-3)]" onClick={onRetry}>Try again</Button>
    </div>
  );
}
```

Never expose raw stack traces in UI.

---

## Form patterns

```tsx
<label htmlFor="email" className="text-[var(--text-secondary)]">Email</label>
<input
  id="email"
  type="email"
  autoComplete="email"
  aria-invalid={!!errors.email}
  aria-describedby={errors.email ? 'email-error' : undefined}
  className="..."
/>
{errors.email && (
  <p id="email-error" role="alert" className="text-[var(--status-error-text)]">
    {errors.email.message}
  </p>
)}
```

- Submit: disable while pending; show progress on button
- Destructive actions: confirm dialog with focus trap
- Long forms: group with `<fieldset>` + `<legend>`

---

## Keyboard & focus (hard gates)

- All interactive elements reachable via Tab
- `focus-visible` ring using token `--focus-ring` (not `outline: none` without replacement)
- Modals: focus trap, Escape closes, return focus to trigger
- Skip link for main content on marketing pages
- Dropdowns: arrow keys, typeahead, `aria-expanded`

Test one critical flow with keyboard only before `design-review`.

---

## Responsive patterns

- Mobile-first: default styles = 375px
- Touch targets ≥ 44×44px
- Tables on mobile: card stack or horizontal scroll with sticky first column — never overflow hidden without affordance
- Navigation: bottom bar or collapsible drawer on small screens per archetype

---

## Data table patterns (dashboard archetype)

- Sticky header on scroll
- Sortable columns announce state (`aria-sort`)
- Row actions: kebab menu with keyboard support
- Pagination or virtual scroll — never render 10k DOM rows
- Empty + loading + error rows use same container contract

---

## Performance patterns

- Dynamic import heavy charts/editors: `next/dynamic` with skeleton
- Images: explicit `width`/`height`, `loading="lazy"` below fold
- Fonts: preload 1–2 weights from `tokens.css` — see `build-conventions.md`
- Avoid `transition-all` — animate specific properties only

---

## Error boundaries (React)

```tsx
'use client';
export class FeatureErrorBoundary extends Component<Props, { hasError: boolean }> {
  state = { hasError: false };
  static getDerivedStateFromError() { return { hasError: true }; }
  render() {
    if (this.state.hasError) return <FeatureCrashFallback onReset={() => this.setState({ hasError: false })} />;
    return this.props.children;
  }
}
```

Wrap route segments — not the entire app (preserve nav on partial failure).

---

## Anti-vibecoded component moves

Beyond `anti-vibecoded-checklist.md`:

- Restyle shadcn primitives with tokens — never ship default theme
- One signature interaction per feature (command palette, slide-over detail, inline edit)
- Data viz uses domain colors from tokens — not chart library defaults

---

## Cross-skill links

- **Tokens:** `design-system` — all values from `tokens.css`
- **States craft:** `golden-examples/states.md`, `polish-playbook.md`
- **Review:** `design-review` — APCA, 375px, dark mode
- **E2E:** `browser-testing-with-devtools` for layout/runtime bugs
