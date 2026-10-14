# Changelog

Notable changes to rnd-workflow-team-skills. Dates are date of the team-edition batch.

## 2026-10-14

### Added
- Root `CHANGELOG.md`, `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md` and `CITATION.cff`.
- GitHub Actions workflow running the integrity checker and regression tests.
- Issue and PR templates.
- English readme `README.md` (primary) and Chinese `README.zh.md`.
- Sources and acknowledgements section in both readmes.

### Changed
- Ignore file named `.gitignore` (git honors it correctly).
- Text files normalized to world-readable `0644`.
- One evidence log sanitized: machine-specific absolute paths replaced with `<repo-root>`.

### Removed
- macOS `.DS_Store` metadata and the `scripts/__pycache__/` bytecode cache from disk.

### Fixed
- All 11 `references/workflow.md` agree on pre-run isolation and ownership checks for ports, test databases, output directories and muting test data.
- The checker gained an independent expected-source inventory (rejecting a cleared source list, partial deletion, duplicate replacement and wrong collection type), plus `scripts/test_check_delivery.py` (7 tests).
- GitHub automation now sits on the paths GitHub actually reads: `.github/workflows/check.yml`, `.github/ISSUE_TEMPLATE/*.yml` and `.github/PULL_REQUEST_TEMPLATE.md`. All four files were previously under a misspelled `.gitthub/` directory, so the workflow never ran and the templates never appeared.
- `CITATION.cff` replaced its placeholder author and invalid `cont-act` key with the maintainer identity configured in this repository (`emudao`) and the CFF 1.2.0 `contact` field. `cffconvert --validate` accepts it under schema 1.2.0. The repository URL is declared but its reachability has not been confirmed.
- English readme proofread: a truncated word ("were reus"), a five-column separator on a four-column table, `gsd-core` feeding `leed` instead of `lead`, a missing apostrophe, and `license` written as `licensee`.
- Self-review of the release-prep commit: `.gitattributes` now uses Linguist's documented `-linguist-detectable` instead of the no-op `-linguist`; the workflow runs with `permissions: contents: read` and both actions pinned by commit; and CI covers the 3.9 floor the checker claims, not only 3.11.

### Notes
- Stated deviations, not silent ones. The release-prep commit deliberately carries four concerns in one commit (the pending readme edits, the four blocker fixes, same-class typo fixes and review evidence) although CONTRIBUTING asks for one concern per PR; and `evidence/final-review-2026-10-14/reprod.py` is committed byte-for-byte as the reviewer produced it, typos included, so the review record stays authentic rather than edited.
- The repository has no configured remote, so neither the workflow nor the citation URL has been exercised against a real GitHub remote.

## 2026-10-10

- Two-round role and workflow sync across nine roles and 11 shared `workflow.md` files; retained 11 roles and the team evidence/authority boundaries.
- See the batch verification report in `evals/results/2026-10-10-sync/report.md`.

## 2026-10-08

- Added `scripts/check_delivery.py` (Python 3.9+ standard library, read-only).
- Cleared 20 broken local links; recorded before/after results under `evidence/`.

## 2026-10-06

- Collection synthesis for team-scoped automatic role continuation, task ownership, isolated checkouts, handoff facts and integrated-version verification.
