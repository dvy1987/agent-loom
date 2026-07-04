#!/usr/bin/env python3
"""Seed INGEST-QUEUE.md with completed Phase 3 comparisons. Stdlib only."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
QUEUE = ROOT / "docs/comparisons/INGEST-QUEUE.md"

DONE_ROWS = [
    "| 2026-06-01 | addyosmani/agent-skills | spec-driven-development | spec-driven-development | Phase 3 pair 1 — MERGE | done |",
    "| 2026-06-01 | addyosmani/agent-skills | test-driven-development | test-driven-development | Phase 3 pair 2 — MERGE | done |",
    "| 2026-06-01 | addyosmani/agent-skills | debugging-and-error-recovery | debug-and-fix | Phase 3 pair 3 — MERGE | done |",
    "| 2026-06-01 | addyosmani/agent-skills | code-review-and-quality | code-review-crsp | Phase 3 pair 4 — MERGE | done |",
    "| 2026-06-01 | addyosmani/agent-skills | idea-refine | brainstorming | Phase 3 pair 5 — MERGE | done |",
    "| 2026-06-01 | addyosmani/agent-skills | planning-and-task-breakdown | implementation-plan | Phase 3 pair 6 — KEEP+MERGE | done |",
    "| 2026-06-01 | addyosmani/agent-skills | doubt-driven-development | adversarial-hat | Phase 3 pair 7 — MERGE | done |",
    "| 2026-06-01 | addyosmani/agent-skills | frontend-ui-engineering | frontend-design | Phase 3 pair 8 — KEEP+MERGE | done |",
    "| 2026-07-03 | kevindeasis/awesome-ui | ux-context + ethical patterns | design-direction, design-review | learn-from ingestion | done |",
    "| 2026-07-03 | safishamsi/graphify | graph trace + query | knowledge-graph | learn-from ingestion | done |",
]

HEADER = """# Ingest Pairwise Compare Queue

Skills or patterns flagged by `learn-from-repo` Step 4b for Phase-3-style comparison before APPLY.

| Date | Source repo | Their pattern / skill | Our skill | Overlap reason | Status |
|------|-------------|----------------------|-----------|----------------|--------|
"""

FOOTER = """
**Pending:** *(none — next `learn-from-repo` overlap appends here with `status: pending`)*

**Process:** Run read-only compare → user approves → `improve-skills TARGET=<skill>`.
Regenerate: `python3 .agents/skills/universal-skill-creator/scripts/backfill_ingest_queue.py --check-only`
"""


def main() -> int:
    import sys

    check_only = "--check-only" in sys.argv
    if check_only:
        if not QUEUE.exists():
            print("INGEST-QUEUE missing")
            return 1
        text = QUEUE.read_text(encoding="utf-8")
        pending = [ln for ln in text.splitlines() if "| pending |" in ln.lower()]
        done = text.count("| done |")
        print(f"INGEST-QUEUE: {done} done, {len(pending)} pending")
        return 0

    body = HEADER + "\n".join(DONE_ROWS) + "\n" + FOOTER
    QUEUE.write_text(body, encoding="utf-8")
    print(f"Wrote {QUEUE} ({len(DONE_ROWS)} done rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
