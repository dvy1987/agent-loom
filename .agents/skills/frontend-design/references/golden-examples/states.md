# Golden Examples — The States Agents Forget

Lack of polish = the "unfinished" feeling. It comes from shipping only the happy/full
state. Every data-bearing surface needs **empty, loading, and error** states designed with
the same care as the populated one. These three are mandatory gates in the build.

---

## Empty state — guidance, not a void

Bad: a blank panel, or a generic "No data". Good: a calm, on-brand state that explains and
offers the next action.

```tsx
export function EmptyState({ title, body, action }: { title: string; body: string; action?: React.ReactNode }) {
  return (
    <div className="flex flex-col items-center gap-3 py-16 text-center">
      {/* a single glyph or custom mark — NOT a stock illustration */}
      <div className="grid size-12 place-items-center rounded-full bg-[--surface-2] text-[--text-tertiary]">
        <PlusIcon className="size-6" aria-hidden />
      </div>
      <div className="max-w-sm space-y-1">
        <h3 className="text-base font-medium text-[--text-primary]">{title}</h3>
        <p className="text-sm text-[--text-secondary]">{body}</p>
      </div>
      {action}
    </div>
  );
}
// Usage: <EmptyState title="No projects yet" body="Create your first project to get going." action={<Button>New project</Button>} />
```

---

## Loading — skeletons that match the real layout (not a spinner)

Skeletons preserve layout and reduce perceived wait. Mirror the real content's shape.

```tsx
export function Skeleton({ className }: { className?: string }) {
  return (
    <div
      aria-hidden
      className={cn(
        "rounded-[--radius-md] bg-[--surface-2]",
        "animate-pulse motion-reduce:animate-none", // reduced-motion: no pulse
        className,
      )}
    />
  );
}

export function CardSkeleton() {
  return (
    <div className="space-y-3 rounded-[--radius-lg] bg-[--surface-1] p-5" aria-busy aria-live="polite">
      <Skeleton className="h-4 w-1/3" />
      <Skeleton className="h-3 w-full" />
      <Skeleton className="h-3 w-4/5" />
    </div>
  );
}
```
Notes: container gets `aria-busy` + `aria-live="polite"`; skeleton respects reduced-motion.
Prefer skeletons over spinners for content areas; reserve spinners for in-button actions.

---

## Error — recoverable, specific, calm

```tsx
export function ErrorState({ message, onRetry }: { message: string; onRetry?: () => void }) {
  return (
    <div role="alert" className="flex flex-col items-center gap-3 py-12 text-center">
      <WarningIcon className="size-6 text-[--status-error]" aria-hidden />
      <p className="max-w-sm text-sm text-[--text-secondary]">{message}</p>
      {onRetry && (
        <Button variant="secondary" size="sm" onClick={onRetry}>
          Try again
        </Button>
      )}
    </div>
  );
}
```
Notes: `role="alert"`; message is specific ("Couldn't load projects — check your connection"),
never "Something went wrong"; offers recovery.

---

## The container pattern that forces all states

```tsx
function Projects() {
  const { data, isLoading, error, refetch } = useProjects();
  if (isLoading) return <CardSkeleton />;
  if (error) return <ErrorState message="Couldn't load projects." onRetry={refetch} />;
  if (!data?.length) return <EmptyState title="No projects yet" body="Create one to begin." action={<Button>New project</Button>} />;
  return <ProjectGrid projects={data} />;
}
```
If a build renders data without all four branches (loading / error / empty / populated),
it is not done — `design-review` fails it on the state-coverage gate.
