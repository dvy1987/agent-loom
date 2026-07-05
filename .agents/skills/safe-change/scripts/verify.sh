#!/usr/bin/env bash
# verify.sh — Detect and run type-check + tests; emit structured JSON result.
# Part of safe-change skill. Stdlib-only bash; no extra deps.
#
# Usage: verify.sh [ROOT]
#   ROOT defaults to . — use the package/fixture directory for subpath edits
#   (e.g. verify.sh examples/seed/calc), not always repo root.
set -euo pipefail

ROOT="${1:-.}"
cd "$ROOT"

TYPECHECK_OK=false
TESTS_OK=false
TYPECHECK_CMD=""
TEST_CMD=""
BEHAVIOR_VERIFIED=false

# --- Detect typecheck ---
if [[ -f package.json ]] && command -v npm >/dev/null 2>&1; then
  if node -e "const p=require('./package.json'); process.exit(p.scripts&&p.scripts.typecheck?0:1)" 2>/dev/null; then
    TYPECHECK_CMD="npm run typecheck"
  elif node -e "const p=require('./package.json'); process.exit(p.scripts&&p.scripts['type-check']?0:1)" 2>/dev/null; then
    TYPECHECK_CMD="npm run type-check"
  elif [[ -f tsconfig.json ]]; then
    TYPECHECK_CMD="npx tsc --noEmit"
  fi
elif [[ -f pyproject.toml ]] || [[ -f setup.py ]]; then
  if command -v mypy >/dev/null 2>&1; then
    TYPECHECK_CMD="mypy ."
  else
    TYPECHECK_CMD="python3 -m compileall -q ."
  fi
elif [[ -f go.mod ]]; then
  TYPECHECK_CMD="go build ./..."
elif [[ -f Cargo.toml ]]; then
  TYPECHECK_CMD="cargo check"
fi

# --- Detect tests ---
has_local_tests() {
  [[ -d tests ]] || compgen -G "test_*.py" >/dev/null 2>&1
}

has_collectible_tests() {
  command -v pytest >/dev/null 2>&1 || return 1
  pytest --collect-only -q 2>/dev/null | grep -q "::"
}

if [[ -f package.json ]] && command -v npm >/dev/null 2>&1; then
  if node -e "const p=require('./package.json'); process.exit(p.scripts&&p.scripts.test?0:1)" 2>/dev/null; then
    TEST_CMD="npm test"
  fi
elif has_local_tests || has_collectible_tests; then
  if command -v pytest >/dev/null 2>&1; then
    TEST_CMD="pytest -q"
  elif [[ -f manage.py ]]; then
    TEST_CMD="python3 manage.py test"
  fi
elif [[ -f go.mod ]]; then
  TEST_CMD="go test ./..."
elif [[ -f Cargo.toml ]]; then
  TEST_CMD="cargo test"
fi

# --- Run typecheck ---
if [[ -n "$TYPECHECK_CMD" ]]; then
  if eval "$TYPECHECK_CMD"; then TYPECHECK_OK=true; fi
else
  echo "[typecheck] skip: no command detected" >&2
  TYPECHECK_OK=true
fi

# --- Run tests ---
if [[ -n "$TEST_CMD" ]]; then
  if eval "$TEST_CMD"; then TESTS_OK=true; BEHAVIOR_VERIFIED=true; fi
else
  echo "[tests] skip: no command detected — behaviorVerified: false" >&2
  TESTS_OK=true
fi

PASS=false
if $TYPECHECK_OK && $TESTS_OK; then PASS=true; fi

export PASS="$PASS" TYPECHECK_OK="$TYPECHECK_OK" TESTS_OK="$TESTS_OK"
export BEHAVIOR_VERIFIED="$BEHAVIOR_VERIFIED" TYPECHECK_CMD="$TYPECHECK_CMD" TEST_CMD="$TEST_CMD"
python3 - <<'PY'
import json, os
def b(k): return os.environ.get(k, "false") == "true"
print(json.dumps({
  "pass": b("PASS"),
  "typecheck": b("TYPECHECK_OK"),
  "tests": b("TESTS_OK"),
  "behaviorVerified": b("BEHAVIOR_VERIFIED"),
  "typecheckCmd": os.environ.get("TYPECHECK_CMD", ""),
  "testCmd": os.environ.get("TEST_CMD", "")
}))
PY

$PASS || exit 1
