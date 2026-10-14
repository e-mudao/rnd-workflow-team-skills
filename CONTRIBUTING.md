# Contributing

Thanks for improving rnd-workflow-team-skills. This is a collection of `rnd-team-*` skills; the team-edition rules below keep it consistent.

## Ground rules

- Change the team edition only against **this workspace's** real problems, split of work, versions and evidence. Do not derive user confirmation from assistant suggestions.
- Keep upstream texts under `references/upstream/` and their licenses intact. If you adjust bundled sources, update the checker's expected inventory in `scripts/check_delivery.py` and the corresponding `references/sources.json`.
- Always distinguish member completion from integrated completion in any status claim.

## Before you open a PR

1. Run the integrity checker and the regression tests:

   ```sh
   python3 scripts/check_delivery.py
   python3 -B -m unittest discover -s scripts -p 'test_*.py' -v
   ```

2. Attach the resulting evidence (or a short summary) to the PR.
3. If you changed a skill body, source records or the shared `references/workflow.md`, say so explicitly in the PR description.

## Pull requests

- Keep each PR scoped to one concern; a large change that needs batched, reliable delivery should state its batches and checkpoints.
- Reference the exact files and the evidence you used.
- A PR that changes skill bodies must keep all 11 `references/workflow.md` identical.

## Reporting

- Bugs and feature requests: use the issue templates under `.gitthub/`.
- Security-relevant reports: follow `SECURITY.md` instead of a public issue.
