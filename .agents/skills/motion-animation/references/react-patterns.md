# Motion React Patterns

Read when building variants, exit animations, gestures, or optimizing bundle size.

## Variants + stagger

```tsx
const container = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: { staggerChildren: 0.08, delayChildren: 0.05 },
  },
};

const item = {
  hidden: { opacity: 0, y: 16 },
  show: { opacity: 1, y: 0, transition: { duration: 0.35, ease: [0.16, 1, 0.3, 1] } },
};

<motion.ul variants={container} initial="hidden" animate="show">
  {items.map((t) => (
    <motion.li key={t} variants={item}>{t}</motion.li>
  ))}
</motion.ul>
```

Pass `variants` to children — do not repeat `initial`/`animate` on every child unless intentional.

## AnimatePresence (exit)

```tsx
<AnimatePresence mode="wait">
  {open && (
    <motion.div
      key="modal"
      initial={{ opacity: 0, scale: 0.96 }}
      animate={{ opacity: 1, scale: 1 }}
      exit={{ opacity: 0, scale: 0.96 }}
      transition={{ duration: 0.2 }}
    />
  )}
</AnimatePresence>
```

- `mode="wait"` — outgoing finishes before incoming (route/modal swaps).
- `mode="popLayout"` — for layout animations with exiting elements.
- Parent must stay mounted while children exit.

## Gestures (touch-safe)

```tsx
<motion.button
  whileHover={{ backgroundColor: 'var(--surface-hover)' }}
  whileTap={{ scale: 0.98 }}
  transition={{ type: 'tween', duration: 0.12 }}
/>
```

Prefer token-driven color shifts over opacity-only hover. Use `whileTap` for press feedback.

## Layout animations

```tsx
<motion.div layout transition={{ type: 'spring', stiffness: 500, damping: 40 }} />
```

Shared element:

```tsx
{tabs.map((t) => (
  <button key={t.id} onClick={() => setActive(t.id)}>
    {active === t.id && (
      <motion.span layoutId="tab-underline" className="underline" />
    )}
    {t.label}
  </button>
))}
```

Disable layout on reduced motion for large panels — swap to opacity fade.

## LazyMotion (bundle size)

```tsx
import { LazyMotion, domAnimation, m } from 'motion/react';

function App({ children }) {
  return (
    <LazyMotion features={domAnimation} strict>
      {children}
    </LazyMotion>
  );
}

// Use m.div instead of motion.div inside LazyMotion tree
<m.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} />
```

| Package | Adds |
|---------|------|
| `domAnimation` | animate, variants, exit, tap/hover/focus (~+15kb) |
| `domMax` | above + drag/pan + layout (~+25kb) |

Lazy-load features: `features={() => import('./features').then(r => r.default)}`.

## Next.js App Router

```tsx
'use client';
import { motion } from 'motion/react';
```

For route transitions, pair `AnimatePresence` with pathname `key` from `usePathname()`.

## Motion vs GSAP (quick route)

| Need | Pick |
|------|------|
| Declarative React props, list exit, layout | Motion |
| Scroll pin + scrub, DrawSVG morph, Vue | GSAP (`gsap-animation`) |
| README-embeddable SVG file | `svg-creation` SMIL |
