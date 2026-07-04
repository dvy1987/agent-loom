# Static SVG Craft

Read during svg-creation Step 3. For token-aligned icon **families** inside a design-system build, also read `design-system/references/svg-craft.md`.

## Canvas

- Default icon grid: `viewBox="0 0 24 24"` with 2px keyline padding (draw in 20×20).
- Dense UI: 16×16 viewBox; marketing icons: 32×32 or 48×48.
- Illustrations: pick viewBox to subject bounds — subject should fill ≥85% of viewBox.

## Paths and primitives

- Prefer `<circle>`, `<rect>`, `<line>` when sufficient — fewer points than equivalent `<path>`.
- Cubic beziers (`C`): control points set departure/arrival tangents; use smooth `S` to chain curves.
- Snap anchors to half-pixel grid for 1× crisp strokes.
- Target ≤2 paths per icon; one path is ideal.

## Stroke and fill

- Use `currentColor` so icons inherit text color.
- Pick one stroke weight per family: 1.5 default, 1.25 premium, 2 playful.
- `stroke-linecap` and `stroke-linejoin`: pick round OR butt/miter — never mix within a set.
- Filled shapes: ensure counters stay open at smallest display size.

## Structure

```svg
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
  stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"
  role="img" xmlns="http://www.w3.org/2000/svg">
  <title>Chevron right</title>
  <path d="M9 6l6 6-6 6"/>
</svg>
```

- Reusable gradients, masks, clipPaths, filters → `<defs>`.
- Prefix `id` values with asset slug when multiple SVGs share a page.

## AI output cleanup

When refining model-generated SVG:

1. Remove editor metadata, comments, empty groups.
2. Replace hardcoded hex with `currentColor` unless illustration needs fixed palette.
3. Collapse redundant transforms into path data.
4. Run through SVGO mentally: no `Path-1` names; semantic structure only.
5. Reject paths with hundreds of micro-segments — simplify or re-prompt.

## Bitmap → vector

If source is PNG/JPG:

- Use **vtracer** (`--preset photo|poster|bw`, `--mode spline`) or Potrace for binarized art.
- Hand-edit traced output: merge collinear segments, remove speckle, unify stroke width.
- Do not attempt pixel-perfect manual tracing in agent context.

## Static quality checklist

- [ ] `viewBox` set; subject fills frame
- [ ] `currentColor` or intentional fixed palette documented
- [ ] ≤800 bytes target for UI icons
- [ ] Readable at smallest intended size
- [ ] No scripts, external refs, or event handlers
