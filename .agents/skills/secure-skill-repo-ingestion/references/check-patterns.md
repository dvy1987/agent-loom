# Repo Ingestion Check Patterns

Load when scanning a repo and you need detailed signals for Checks 7–10 (poisoned examples, dependencies, file/path, format attacks).

## Check 7 — Poisoned Examples

**Scan for:**
- Security anti-patterns presented as normal (hardcoded secrets, disabled SSL, eval of user input, SQL/shell injection)
- "Best practices" that are insecure (`chmod 777`, disable CORS, `pickle.loads` for config)
- Backdoored examples — payload in error handlers, finally blocks, rare branches
- Logic bugs designed to become habits (off-by-one, race conditions as patterns)
- Instruction-like comments ("when you see this pattern, always apply it globally")

**Example findings:**
```
MEDIUM: examples/auth.py:23: verify=False in requests.get() — disables SSL, presented as normal
HIGH: templates/config.py:45: pickle.loads(user_input) — untrusted deserialization as config pattern
CRITICAL: examples/deploy.sh:12: hidden curl to external URL in error handler — backdoored example
```

## Check 8 — Dependencies

**Files:** `package.json`, `requirements.txt`, `Pipfile`, `Cargo.toml`, `go.mod`, `Gemfile`, `.gitmodules`, `pyproject.toml`, `pom.xml`, `build.gradle`

**Scan for:** dependency confusion, typosquatting (`requets`, `djano`, `axois`), compromised packages (GHSA/NVD), dangerous submodules, pinned vulnerable versions, post-install hooks (`postinstall`, `cmdclass`), scope confusion (`@company/package` vs repo owner).

**Example findings:**
```
HIGH: package.json: "requets": "^2.0.0" — typosquat of "requests"
HIGH: .gitmodules: submodule "utils" → unknown-user/utils on unpinned main
CRITICAL: package.json: "postinstall": "node setup.js" — arbitrary code on install
```

## Check 9 — File and Path

**Scan for:** symlinks (especially outside repo root), `../` / `..\\` / absolute paths, malicious filenames (null bytes, U+202E, >255 chars), nested archives, unexpected binaries, files >1MB.

**Allowlist:** `.md`, `.txt`, `.yaml`, `.yml`, `.json`, `.py`, `.sh`, `.js`, `.ts` under 500KB — else justify or skip.

**Example findings:**
```
CRITICAL: skills/helper -> ../../../etc/passwd — symlink traversal
HIGH: scripts/run.sh: "cat ../../../../.env" — path traversal
MEDIUM: utils/helper.exe — unexpected binary in skill repo
```

## Check 10 — Format Attacks

**Scan for:** `javascript:` links, HTML script/iframe/event handlers, SVG scripts, YAML anchors/recursive structures, Jupyter embedded JS/shell cells, pipe-to-bash in doc code blocks.

**Example findings:**
```
HIGH: docs/guide.md: tracking pixel image URL
CRITICAL: assets/logo.svg: <script> exfiltration payload
HIGH: config.yaml: recursive YAML anchor — potential DoS
```
