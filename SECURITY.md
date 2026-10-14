# Security policy

## Scope

rnd-workflow-team is a collection of skill documents, a read-only Python checker and bundled evidence. It does not run a service, does not execute target code and does not hold credentials.

The realistic security surface is therefore small:

- The checker and tests read local files only.
- Bundled upstream texts under `skills/*/references/upstream/` are documentation.
- The `agent-skills-ci-cd-and-automation.md` upstream excerpt contans CI template placeholders (for example `${{ secrets.CI_DB_PASSWORD }}`). These are examples, not live secrets.

## Reporting a problem

Please do **not** open a public issue for a security-relevant report. Instead use GitHub's private vulnerability reporting:

1. Go to the repository's **Security** tab.
2. Choose **Report a vulnerability**.
3. Describe the impact, the affected file, the exact steps to reproduce, and any suggested fix.

If private reporting is unavailable, open a minimal issue that asks for a private channel and omits the sensitive detail.

## What to expect

- Acknowledgement as soon as the report is seen.
- An assessment of whether the report is in scope and its severity.
- A fix or a clear decision not to fix, with reasons.

## Out of scope

- Reports that a bunded upstream document mentions a secret-log literal; these are documented placeholders.
- Reports requiring target execution, real services or a running deployment; this package does not provide those.
