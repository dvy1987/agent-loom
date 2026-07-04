# Ethical Patterns Gate

Hard gate for deceptive UI. Based on established dark-pattern taxonomy.
Any single hit = **Ethical patterns FAIL**. Fix before SHIP.

## Checklist (scan every interactive surface)

| Pattern | What to look for | FAIL example |
|---|---|---|
| **Confirm shaming** | Opt-out or decline uses guilt/shame language | "No thanks, I hate saving money" |
| **Mislabeled action** | Button/link label does not match the action it triggers | "Continue" that signs up for paid plan |
| **Hidden cost** | Price, subscription, or commitment revealed only after investment | Free trial → card required with no upfront mention |
| **Forced continuity** | Cancel/unsubscribe is buried, multi-step, or harder than sign-up | Account settings → 4 pages to cancel |
| **Fake urgency** | Countdown, "only X left", or pressure with no verifiable basis | Timer resets on refresh; stock never changes |
| **Privacy zuckering** | Default-opt-in to sharing/data collection; unclear consent | Pre-checked marketing + analytics boxes |
| **Roach motel** | Easy to enter, hard to exit (accounts, subscriptions, data export) | One-click signup, email-only cancellation |

## Agent scan method

1. Read every CTA, modal, banner, checkout step, settings screen, and empty/error state.
2. Trace each primary button to its actual outcome (not its label).
3. Compare sign-up vs cancel flows — exit must not be materially harder than entry.
4. Flag copy that manipulates emotion to override informed consent.

## Fix guidance (in findings)

Name the pattern, cite `file:line`, quote the offending copy, and give the honest replacement.
Example: `PricingModal.tsx:84` — mislabeled action: "Get started" submits payment → rename to "Start paid plan — $29/mo".
