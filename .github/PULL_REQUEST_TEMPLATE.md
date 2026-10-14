## What and why

Describe the change and the problem it solves.

## Evidence

- Checker: `python3 scripts/check_delivery.py`
- Tests: `python3 -B -m unittest discover -s scripts -p 'test_*.py' -v`

## Scopes and boundaries

- [ ] Skill bodies, sources or the shared `references/workflow.md` were changed (kept all 11 identical if so).
- [ ] Upstream texts and licenses under `references/upstream/` were preserved.
- [ ] Member completion and integrated completion are stated separately.

## Checklist

- [ ] Checker passes.
- [ ] Tests pass.
- [ ] No machine-specific absolute paths were introduced.
