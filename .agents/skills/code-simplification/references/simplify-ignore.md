# Simplify-Ignore — Block Protection

Adapted from [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) `hooks/simplify-ignore.sh` (MIT). Full setup: **`hooks/SIMPLIFY-IGNORE.md`** at repo root.

## When to use

Mark performance-critical, generated, or vendored sections the model must not rewrite during **code-simplification**.

## Annotation syntax

```js
/* simplify-ignore-start: perf-critical */
// manually unrolled — do not collapse to a loop
result[0] = buf[0] ^ key[0];
result[1] = buf[1] ^ key[1];
/* simplify-ignore-end */
```

```python
# simplify-ignore-start: vendored hash table
# ... large third-party block ...
# simplify-ignore-end
```

- Optional reason after `start:` appears in the `BLOCK_<hash>` placeholder.
- Single-line blocks supported; multi-block per file supported.
- Comment styles: `/* */`, `//`, `#`, `<!-- -->`.

## Claude Code hooks (summary)

Register in `.claude/settings.json`:

- **PreToolUse Read** → filter file to placeholders
- **PostToolUse Edit|Write** → expand, apply edits, re-filter
- **Stop** → restore originals from `.claude/.simplify-ignore-cache/`

See `hooks/SIMPLIFY-IGNORE.md` for the JSON snippet and crash recovery (`echo '{}' | bash hooks/simplify-ignore.sh`).

## Example session

<input>Simplify `src/crypto.ts` but keep the unrolled XOR block</input>

<output>
1. Annotate XOR block with `simplify-ignore-start: perf-critical`.
2. Wire hooks per `hooks/SIMPLIFY-IGNORE.md`.
3. Run code-simplification on surrounding helpers only — model sees `/* BLOCK_a1b2c3d4: perf-critical */` instead of the loop body.
4. Session end restores real code with any approved edits outside protected blocks.
</output>
