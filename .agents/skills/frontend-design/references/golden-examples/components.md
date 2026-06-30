# Golden Examples — Core Components

Reference implementations to emulate, not copy blindly. They show the *level of craft*
expected: every state defined, tokens (never hex), focus-visible rings, no slop tells.
Stack: React + Tailwind (v4, token-driven). Adapt class names to the project's tokens.

The point of these is positive taste — models escape the corpus mean by seeing good
examples, not just bans.

---

## Button — all states, four variants

```tsx
import { cva, type VariantProps } from "class-variance-authority";
import { cn } from "@/lib/utils";

const button = cva(
  // base: focus-visible ring, motion, disabled, never transition-all
  "inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-[--radius-md] " +
    "font-medium select-none transition-[background-color,transform,box-shadow] duration-[--dur-quick] " +
    "ease-[--ease-standard] outline-none focus-visible:ring-2 focus-visible:ring-[--focus-ring] " +
    "focus-visible:ring-offset-2 focus-visible:ring-offset-[--surface-0] active:translate-y-px " +
    "disabled:pointer-events-none disabled:opacity-60 motion-reduce:transition-none motion-reduce:active:translate-y-0",
  {
    variants: {
      variant: {
        primary: "bg-[--accent] text-[--text-on-accent] hover:bg-[--accent-hover] active:bg-[--accent-active]",
        secondary: "bg-[--surface-1] text-[--text-primary] border border-[--border-strong] hover:bg-[--surface-2]",
        ghost: "bg-transparent text-[--text-secondary] hover:bg-[--surface-2] hover:text-[--text-primary]",
        destructive: "bg-[--status-error] text-[--text-on-accent] hover:brightness-95 active:brightness-90",
      },
      size: { sm: "h-8 px-3 text-sm", md: "h-10 px-4 text-sm", lg: "h-12 px-6 text-base" },
    },
    defaultVariants: { variant: "primary", size: "md" },
  },
);

interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof button> {
  loading?: boolean;
}

export function Button({ className, variant, size, loading, children, disabled, ...props }: ButtonProps) {
  return (
    <button className={cn(button({ variant, size }), className)} disabled={disabled || loading} aria-busy={loading} {...props}>
      {loading && <Spinner className="size-4" aria-hidden />}
      {children}
    </button>
  );
}
```
Notes: hover shifts a real token (not opacity); `active:translate-y-px` gives a press; ring
is `:focus-visible` only; `motion-reduce` disables it; loading sets `aria-busy` and disables.

---

## Input — labelled, with rest/focus/error/disabled

```tsx
interface FieldProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label: string;
  error?: string;
}

export function Field({ id, label, error, className, ...props }: FieldProps) {
  const describedBy = error ? `${id}-error` : undefined;
  return (
    <div className="flex flex-col gap-1.5">
      <label htmlFor={id} className="text-sm font-medium text-[--text-secondary]">
        {label}
      </label>
      <input
        id={id}
        aria-invalid={!!error}
        aria-describedby={describedBy}
        className={cn(
          "h-10 rounded-[--radius-md] bg-[--surface-1] px-3 text-[--text-primary] " +
            "border border-[--border-subtle] placeholder:text-[--text-tertiary] " +
            "outline-none transition-colors duration-[--dur-quick] " +
            "focus-visible:border-[--accent] focus-visible:ring-2 focus-visible:ring-[--focus-ring] " +
            "disabled:opacity-60 disabled:cursor-not-allowed " +
            "aria-[invalid=true]:border-[--status-error] aria-[invalid=true]:ring-[--status-error]/30",
          className,
        )}
        {...props}
      />
      {error && (
        <p id={describedBy} className="text-sm text-[--status-error]">
          {error}
        </p>
      )}
    </div>
  );
}
```
Notes: real `<label htmlFor>`; `aria-invalid` + `aria-describedby` wire the error; error is a
token color, not red-500.

---

## Card — borderless by default (no grey 1px box)

```tsx
// Separation order: whitespace → 3-5% surface shift → soft elevation. Border only as last resort.
export function Card({ interactive, className, ...props }: React.HTMLAttributes<HTMLDivElement> & { interactive?: boolean }) {
  return (
    <div
      className={cn(
        "rounded-[--radius-lg] bg-[--surface-1] p-5",
        interactive &&
          "transition-[transform,background-color] duration-[--dur-base] ease-[--ease-standard] " +
            "hover:bg-[--surface-2] hover:-translate-y-0.5 motion-reduce:hover:translate-y-0 " +
            "focus-within:ring-2 focus-within:ring-[--focus-ring]",
        className,
      )}
      {...props}
    />
  );
}
```
Notes: NO default border. Elevation/contrast comes from the surface step. Interactive cards
lift slightly and respect reduced-motion.

---

## Badge — semantic status, not decoration

```tsx
const badge = cva("inline-flex items-center gap-1 rounded-full px-2 py-0.5 text-xs font-medium", {
  variants: {
    tone: {
      neutral: "bg-[--surface-2] text-[--text-secondary]",
      success: "bg-[--status-success]/12 text-[--status-success]",
      warning: "bg-[--status-warning]/12 text-[--status-warning]",
      error: "bg-[--status-error]/12 text-[--status-error]",
    },
  },
  defaultVariants: { tone: "neutral" },
});
export const Badge = ({ tone, className, ...p }: React.HTMLAttributes<HTMLSpanElement> & VariantProps<typeof badge>) => (
  <span className={cn(badge({ tone }), className)} {...p} />
);
```

---

## What makes these "golden" (apply to every component you build)
- Every interactive state present: rest, hover, active, `:focus-visible`, disabled, (loading where relevant).
- Tokens only — no hex, no `slate-*`, no `blue-600`.
- Hover changes a real token (L/chroma), never opacity-only.
- `focus-visible:ring` with offset; never `outline:none` alone.
- `motion-reduce:` variant on anything that transforms.
- Accessible wiring: labels, `aria-invalid`, `aria-busy`, `aria-describedby`.
