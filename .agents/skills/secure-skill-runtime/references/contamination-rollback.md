# Contamination Rollback Procedure

Load when a previously-approved skill or external pattern is found compromised after installation.

## Steps

1. **Identify** — Search provenance records for all content from the suspect source (repo URL or commit hash).
2. **Isolate** — Remove or quarantine every installed file traced to that source. Use provenance `installed_to` paths.
3. **Add to no-go list** — Add the source repo to `references/no-go-repos.md` with finding details.
4. **Re-scan neighbors** — Invoke ALL `secure-*` skills on every skill modified in the same session or `improve-skills` batch as the compromised content.
5. **Verify baseline** — Confirm `secure-*` skills themselves were not modified by the compromised source. Restore from last known-good commit if needed.
6. **Report** — Log rollback: what was removed, re-scanned, and verified clean.

Rollback is always available because provenance is append-only.
