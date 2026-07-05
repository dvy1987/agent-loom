# Motion Animation — Worked Examples

Read when the animation pattern or output shape is unclear.

---

## Example 1 — Page-load hero stagger

**Input:** Stagger hero headline, subcopy, and CTA on mount in React.

**Output:**

```tsx
'use client';
import { motion } from 'motion/react';

const container = {
  hidden: {},
  show: { transition: { staggerChildren: 0.1, delayChildren: 0.05 } },
};
const fadeUp = {
  hidden: { opacity: 0, y: 24 },
  show: { opacity: 1, y: 0, transition: { duration: 0.5, ease: [0.16, 1, 0.3, 1] } },
};

export function Hero() {
  return (
    <motion.div variants={container} initial="hidden" animate="show">
      <motion.h1 variants={fadeUp}>Ship faster</motion.h1>
      <motion.p variants={fadeUp}>Agents that remember.</motion.p>
      <motion.button variants={fadeUp}>Get started</motion.button>
    </motion.div>
  );
}
```

Wrap app in `<MotionConfig reducedMotion="user">` at layout level.

---

## Example 2 — Scroll-triggered feature cards

**Input:** Stagger feature cards into view on scroll in a Next.js landing page.

**Output:**

```tsx
'use client';
import { motion } from 'motion/react';

const list = {
  hidden: {},
  show: { transition: { staggerChildren: 0.08 } },
};
const card = {
  hidden: { opacity: 0, y: 40 },
  show: { opacity: 1, y: 0, transition: { duration: 0.45 } },
};

export function Features({ items }: { items: string[] }) {
  return (
    <motion.div className="grid" variants={list} initial="hidden" whileInView="show"
      viewport={{ once: true, margin: '-80px' }}>
      {items.map((t) => (
        <motion.article key={t} variants={card}>{t}</motion.article>
      ))}
    </motion.div>
  );
}
```

---

## Example 3 — AnimatePresence modal

**Input:** Fade/scale modal on open and close.

**Output:**

```tsx
'use client';
import { AnimatePresence, motion } from 'motion/react';

export function Modal({ open, onClose, children }: Props) {
  return (
    <AnimatePresence>
      {open && (
        <motion.div
          key="backdrop"
          className="backdrop"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          onClick={onClose}
        >
          <motion.div
            key="panel"
            className="panel"
            initial={{ opacity: 0, scale: 0.96, y: 8 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.96, y: 8 }}
            transition={{ duration: 0.2 }}
            onClick={(e) => e.stopPropagation()}
          >
            {children}
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
```

---

## Example 4 — Inline SVG logo draw

**Input:** Draw an inline SVG logo path on page load in React.

**Output:**

```tsx
'use client';
import { motion } from 'motion/react';

export function LogoDraw() {
  return (
    <motion.svg viewBox="0 0 200 60" aria-hidden="true">
      <motion.path
        d="M10,30 L50,30 L70,10 L90,50 L110,30 L190,30"
        fill="none"
        stroke="currentColor"
        strokeWidth={2}
        initial={{ pathLength: 0, opacity: 0 }}
        animate={{ pathLength: 1, opacity: 1 }}
        transition={{ duration: 1.2, ease: 'easeInOut' }}
      />
    </motion.svg>
  );
}
```

For README-embeddable file without React → `svg-creation` SMIL. For DrawSVG stagger on many paths → `gsap-animation`.

---

## Example 5 — Shared layoutId tab underline

**Input:** Animated underline follows active tab.

**Output:**

```tsx
'use client';
import { motion } from 'motion/react';

export function Tabs({ tabs, active, onChange }: Props) {
  return (
    <div className="tabs">
      {tabs.map((t) => (
        <button key={t.id} onClick={() => onChange(t.id)} className="tab">
          {active === t.id && (
            <motion.span layoutId="tab-underline" className="underline" />
          )}
          {t.label}
        </button>
      ))}
    </div>
  );
}
```

Use `domMax` feature package if inside `LazyMotion`.
