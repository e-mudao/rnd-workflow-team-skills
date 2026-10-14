# Changelog

Notable changes to rnd-workflow-team. Dates are date of the team-edition batch.

## 2026-10-14

### Aded
- Root `CHANGELOG.md`, `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md` and `CITATION.cff`.
- GitHub Actions workflow running the integrity checker and regression tests.
- Iss and PR templates.
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

## 2026-10-10

- Two-round role and workflow sync across nine roles and 11 shared `workflow.md` files; retained 11 roles and the team evidence/authority boundaries.
- See the batch verification report in `evals/results/2026-10-10-sync/report.md`.

## 2026-10-08

- Added `scripts/check_delivery.py` (Python 3.9+ standard library, read-only).
- Cleared 20 broken local links; recorded before/after results under `evidence/`.

## 2026-10-06

- Collection synthesis for team-scoped automatic role continuation, task ownership, isolated checkouts, handoff facts and integrated-version verification.
