# Golden Examples — Composition & Polish Moments

Layout and the one orchestrated motion moment are where "designed" vs "generic" is decided.
These show non-default compositions and the high-impact polish that beats scattered
micro-interactions.

---

## Hero — NOT the default centered-H1 + subhead + 2 CTAs

The default hero is the #1 marketing slop tell. Use an asymmetric, type-led layout instead.

```tsx
export function Hero() {
  return (
    <section className="mx-auto grid max-w-6xl gap-10 px-6 py-24 lg:grid-cols-[1.1fr_0.9fr] lg:items-center">
      <div className="space-y-6">
        {/* eyebrow + display type doing the work, left-aligned */}
        <p className="text-sm font-medium uppercase tracking-[0.12em] text-[--text-tertiary]">
          Research, organized
        </p>
        <h1 className="text-balance font-[--font-display] text-5xl/[1.05] font-semibold tracking-[-0.02em] text-[--text-primary] sm:text-6xl/[1.02]">
          Your sources, finally in one place.
        </h1>
        <p className="max-w-md text-lg text-[--text-secondary]">
          Capture, connect, and cite — without the tab graveyard.
        </p>
        <div className="flex gap-3">
          <Button size="lg">Start free</Button>
          <Button size="lg" variant="ghost">See how it works</Button>
        </div>
      </div>
      {/* product surface as the visual, not a stock illustration */}
      <div className="rounded-[--radius-lg] bg-[--surface-1] p-2 shadow-[--elevation-2]">
        <AppPreview />
      </div>
    </section>
  );
}
```
Moves: left-aligned asymmetric grid; `text-balance` + tight display tracking; product
preview carries the visual; ghost secondary so the primary CTA wins.

---

## App shell — dashboard with breathing chrome

```tsx
export function AppShell({ children }: { children: React.ReactNode }) {
  return (
    <div className="grid min-h-dvh grid-cols-[var(--sidebar,16rem)_1fr] bg-[--surface-0]">
      <aside className="flex flex-col gap-1 border-r border-[--border-subtle] p-3">
        <Nav />
      </aside>
      <div className="flex flex-col">
        <header className="flex h-14 items-center justify-between px-6">
          <Breadcrumbs />
          <CommandBarTrigger /> {/* a signature interaction, not just a search input */}
        </header>
        <main className="flex-1 px-6 py-4">{children}</main>
      </div>
    </div>
  );
}
```
Moves: `min-h-dvh` (mobile-safe); hairline divider, not boxes; a signature element
(command bar) over a generic search field.

---

## The ONE orchestrated entrance (beats scattered micro-interactions)

A single, well-staggered page-load reveal creates more delight than hover-scale on every
card. CSS-only, reduced-motion-safe.

```css
@media (prefers-reduced-motion: no-preference) {
  .reveal { opacity: 0; transform: translateY(8px); animation: reveal var(--dur-emphasized) var(--ease-decelerate) forwards; }
  .reveal:nth-child(1) { animation-delay: 0ms; }
  .reveal:nth-child(2) { animation-delay: 60ms; }
  .reveal:nth-child(3) { animation-delay: 120ms; }
  .reveal:nth-child(4) { animation-delay: 180ms; }
  @keyframes reveal { to { opacity: 1; transform: none; } }
}
```
```tsx
<ul>{items.map((it) => <li key={it.id} className="reveal">{/* ... */}</li>)}</ul>
```
Notes: staggered by `animation-delay`; disabled entirely under reduced-motion; one moment,
not everywhere.

---

## Composition rules that keep it from looking generic
- Asymmetry with editorial logic > centered everything.
- Hairlines + surface shifts > a border on every box.
- One signature element that recurs (command bar, marginalia, colored dot).
- Whitespace is a feature; let display type breathe (`text-balance`, generous line-height).
- Real, specific copy ("Ship a deploy in 47s"), never Lorem Ipsum, never "The future of X".
- Test 375px first; `min-h-dvh` not `min-h-screen`; touch targets ≥44px.
