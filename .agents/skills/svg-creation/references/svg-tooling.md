# SVG Tooling Taxonomy

Read when input is a **bitmap**, output needs **optimization**, or the user asks which tool/library to use. Distilled from awesome-svg categories — local guidance only, no external link farms.

## When to use what

| Job | Tool / approach | Use when |
|-----|-----------------|----------|
| Handcraft static icon | svg-creation `static-craft.md` | ≤48px UI, custom family, `currentColor` |
| Handcraft animation | svg-creation `animation-craft.md` | Self-contained SVG or inline DOM |
| Bitmap → vector | **vtracer** (`--preset photo\|poster\|bw`, `--mode spline`) | PNG/JPG logo, photo trace, pixel art |
| Bitmap → vector (B&W) | **Potrace** | High-contrast scans, single-color output |
| Optimize output | **SVGO** | Strip metadata, merge paths, shrink file size post-generation |
| Line-draw in web app | **vivus** / **lengthy-svg** | JS runtime; SVG must be inline in DOM — not `<img>` |
| Rich web animation | **Motion** (`motion-animation`) / **GSAP** (`gsap-animation`) | React app with inline SVG; sequencing, scroll — not README embeds |
| Programmatic Python SVG | **svg.py** | Build SVG from code/data pipelines — not agent markup authoring |
| Hand-drawn aesthetic | **rough.js** | Sketch/wireframe look; pairs with static craft rules |

## Decision tree

```
Input is raster?  → vtracer/Potrace → hand-cleanup → svg-creation
Need animated README/GitHub SVG?  → SMIL only (svg-creation) — no GSAP
Need animated inline React UI?  → CSS/Motion/GSAP on inline SVG
Icon inside DESIGN.md build?  → design-system svg-craft + svg-creation for motion
File too large?  → SVGO after quality gate passes
```

## Out of scope for this skill

- Wiring Gemini/OpenRouter APIs (SVG-ORA runtime) — use `ai-svg-prompts.md` as review gate only
- Installing or configuring tools — mention command, user runs locally
- Executing untrusted repo code during learning

## vtracer quick reference

```sh
vtracer --input input.png --output output.svg --preset photo --mode spline
```

Post-trace: merge collinear segments, remove speckle, unify stroke width, then svg-creation quality gate.
