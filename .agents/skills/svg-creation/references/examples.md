# SVG Creation — Worked Examples

Read when the deliverable type or output shape is unclear.

---

## Example 1 — Static icon (inline React)

**Input:** Draw a minimal "settings" gear icon for a 24px nav bar.

**Output:**

```svg
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
  stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"
  role="img" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <title>Settings</title>
  <circle cx="12" cy="12" r="3"/>
  <path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/>
</svg>
```

Delivery: inline — `currentColor`, 2 paths, round caps, fills 24×24 grid.

---

## Example 2 — Line-draw checkmark (inline CSS)

**Input:** Animated success checkmark for a form submit state.

**Output:**

```svg
<svg viewBox="0 0 52 52" role="img" xmlns="http://www.w3.org/2000/svg">
  <title>Success</title>
  <style>
    .ring { fill: none; stroke: #22c55e; stroke-width: 2;
      stroke-dasharray: 150; stroke-dashoffset: 150;
      animation: draw .6s ease forwards; }
    .tick { fill: none; stroke: #22c55e; stroke-width: 3;
      stroke-linecap: round; stroke-linejoin: round;
      stroke-dasharray: 50; stroke-dashoffset: 50;
      animation: draw .4s ease .5s forwards; }
    @media (prefers-reduced-motion: reduce) {
      .ring, .tick { animation: none; stroke-dashoffset: 0; }
    }
    @keyframes draw { to { stroke-dashoffset: 0; } }
  </style>
  <circle class="ring" cx="26" cy="26" r="24"/>
  <path class="tick" d="M14 27l7 7 16-16"/>
</svg>
```

Delivery: inline DOM — CSS keyframes with staggered delay.

---

## Example 3 — Morph menu (SMIL, self-contained)

**Input:** Hamburger icon that morphs to X on click — must work as standalone SVG file.

**Output:**

```svg
<svg viewBox="0 0 24 24" role="img" xmlns="http://www.w3.org/2000/svg" id="menu">
  <title>Menu</title>
  <path stroke="currentColor" stroke-width="2" stroke-linecap="round" fill="none"
    d="M 3,6 L 21,6">
    <animate attributeName="d" to="M 5,5 L 19,19" dur="0.3s"
      begin="menu.click" fill="freeze"/>
  </path>
  <path stroke="currentColor" stroke-width="2" stroke-linecap="round" fill="none"
    d="M 3,12 L 21,12">
    <animate attributeName="opacity" to="0" dur="0.1s"
      begin="menu.click" fill="freeze"/>
  </path>
  <path stroke="currentColor" stroke-width="2" stroke-linecap="round" fill="none"
    d="M 3,18 L 21,18">
    <animate attributeName="d" to="M 5,19 L 19,5" dur="0.3s"
      begin="menu.click" fill="freeze"/>
  </path>
</svg>
```

Delivery: `<img>` or file — SMIL `begin="menu.click"`, no CSS/JS.

---

## Example 4 — Breathing glow (SMIL loop)

**Input:** Subtle pulsing dot for a live-status indicator in a README.

**Output:**

```svg
<svg viewBox="0 0 200 200" role="img" xmlns="http://www.w3.org/2000/svg">
  <title>Live</title>
  <circle cx="100" cy="100" r="30" fill="#22c55e">
    <animate attributeName="r" values="30;35;30" dur="2s"
      calcMode="spline" keySplines="0.4 0 0.6 1;0.4 0 0.6 1"
      repeatCount="indefinite"/>
    <animate attributeName="opacity" values="1;0.6;1" dur="2s"
      calcMode="spline" keySplines="0.4 0 0.6 1;0.4 0 0.6 1"
      repeatCount="indefinite"/>
  </circle>
</svg>
```

Delivery: GitHub README — SMIL only, no dependencies.

---

## Example 5 — Gradient shift (SMIL, self-contained)

**Input:** Animated gradient banner for a marketing embed (no JS).

**Output:**

```svg
<svg viewBox="0 0 200 100" role="img" xmlns="http://www.w3.org/2000/svg">
  <title>Gradient banner</title>
  <defs>
    <linearGradient id="banner-shift" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%">
        <animate attributeName="stop-color"
          values="#e63946;#457b9d;#2a9d8f;#e63946" dur="4s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%">
        <animate attributeName="stop-color"
          values="#457b9d;#2a9d8f;#e63946;#457b9d" dur="4s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>
  </defs>
  <rect width="200" height="100" fill="url(#banner-shift)" rx="8"/>
</svg>
```

---

## Example 6 — Liquid wave (SMIL morph)

**Input:** Subtle animated wave footer for a landing page hero (inline or file).

**Output:**

```svg
<svg viewBox="0 0 200 100" role="img" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
  <title>Wave</title>
  <path fill="#457b9d" opacity="0.7">
    <animate attributeName="d" dur="5s" repeatCount="indefinite"
      values="M 0,40 C 30,35 70,45 100,40 L 100,100 L 0,100 Z;
              M 0,40 C 30,50 70,30 100,40 L 100,100 L 0,100 Z;
              M 0,40 C 30,35 70,45 100,40 L 100,100 L 0,100 Z"
      calcMode="spline" keySplines="0.4 0 0.6 1;0.4 0 0.6 1"/>
  </path>
</svg>
```

Use sparingly — `d` animation is repaint-heavy.
