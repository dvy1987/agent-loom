# Motion SVG and Scroll

Read before animating inline SVG or scroll-linked values.

## SVG pathLength (stroke draw)

Prerequisite: `fill="none"` + `stroke` + `strokeWidth` on the path.

```tsx
<motion.path
  d="M10,30 L50,30 L70,10 L90,50 L110,30 L190,30"
  fill="none"
  stroke="currentColor"
  strokeWidth={2}
  initial={{ pathLength: 0, opacity: 0 }}
  animate={{ pathLength: 1, opacity: 1 }}
  transition={{ duration: 1.2, ease: 'easeInOut' }}
/>
```

`pathLength` is normalized 0–1 — no manual `stroke-dasharray` math. For self-contained SVG files without React, use `svg-creation` SMIL/CSS.

Complex multi-segment morph → `gsap-animation` MorphSVG.

## motion.svg

Any SVG tag can be prefixed: `motion.svg`, `motion.circle`, `motion.g`. Animate `viewBox` for zoom effects sparingly.

## whileInView (scroll-triggered)

```tsx
<motion.section
  initial={{ opacity: 0, y: 32 }}
  whileInView={{ opacity: 1, y: 0 }}
  viewport={{ once: true, margin: '-100px' }}
  transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1] }}
/>
```

- `once: true` — animate in once (default good for marketing sections).
- `margin` — trigger before element fully enters viewport.

## useScroll + useTransform (scroll-linked)

```tsx
import { useScroll, useTransform, motion } from 'motion/react';

function ProgressBar() {
  const { scrollYProgress } = useScroll();
  const scaleX = useTransform(scrollYProgress, [0, 1], [0, 1]);

  return <motion.div className="progress" style={{ scaleX }} />;
}
```

## Reduced motion

Site-wide:

```tsx
import { MotionConfig } from 'motion/react';

<MotionConfig reducedMotion="user">{children}</MotionConfig>
```

Disables transform/layout animations globally; opacity/color still animate.

Bespoke (sidebar, parallax):

```tsx
const reduce = useReducedMotion();
const animate = reduce ? { opacity: 1 } : { x: 0 };
```

Parallax — zero out scroll-linked transform when reduced:

```tsx
const y = useTransform(scrollY, [0, 500], [0, -80]);
<motion.div style={{ y: reduce ? 0 : y }} />
```

## Performance

- Prefer `whileInView` over scroll listeners for simple reveals.
- Avoid `layout` on long lists — use enter stagger only.
- Scroll-linked parallax on heroes only; disable under reduced motion.
