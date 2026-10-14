# rnd-workflow-team — Collaborative R&D Skills for Multi-Person Teams

A set of R&D skills for **multiple people, each working with their own agent (Codex, DSH, Claude Code, …), developing one shared project together**. It ships **11 `rnd-team-*` skills** coversing the full path from discoversy to release: discovers, spec, plan, build, review, verify, release, plus architecture, design and security when needed.

Every member starts from the entry skill `rnd-team-lead` and picks up the task assigned to them; a coordinator maintains the shared split of work, and an integrator receives the tasks and verifies the final version. One person may hold several of these roles — the team does not need 11 people.

- 📖 Full team workflow, copyable prompts for all 11 skills, and a complete example: [guide.md](guide.md) (Chinese) · [README.zh.md](README.zh.md) 中文版
- ✅ Current delivery and maintenance state, and verification scope: [review.md](review.md) (Chinese)
- 🧪 Package integrity checker: [scripts/check_delivery.py](scripts/check_delivery.py)
- 🖫 Contributing and reports: [CONTRIBUTING.md](CONTRIBUTING.md) · [SECURITY.md](SECURITY.md) · [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)

> This repository maintains only the `rnd-team-*` **team edition**. The optional neighboring single-person edition (e.g. `rnd-lead`) is maintained by its own project; this package is not an automatic sync plan for it, and another project's changes or verification results are not evidence of this package's progress or passing.

---

## What this is

When several people each work with an agent at the same time, the usual failures are: requirements and interfaces diverge, parallel changes overwrite each other, handoffs carry too little information, and "each branch passed on its own" is mistaken for "the whole thing passed".

This project turns those steps into skills: each skill maps to one R&D responsibility and states explicitly **who maintains which artifact, which changes need coordination, what a handoff must carry, and what evidence a completion claim rests on**. Skills run in each member's own session and, within that member's area of trust, automatically pull in the relevant responsibilities, fix and re-verify — the user does not connect each skill by hand.

**No package install, install script, Node/npm, or collection runtime is required.** The real business project keeps its own dependencies, tools and permissions.

## Repository layout

```
rnd-workflow-team/
├── README.md                    This file: project overview and entry point
├── README.zh.md                 Chinese version of this file
├── guide.md                     Usage guide: workflow, copyable prompts, complete example (Chinese)
├── review.md                    Current delivery and maintenance state, verification scope
├── CHANGELOG.md                  Notable changes
├── CONTRIBUTING.md               Contributing guide
├── SECURITY.md                   Security policy
├── CODE_OF_CONDUCT.md            Code of conduct
├── CITATION.cff                  How to cite this software
├── LICENSED                     Root MIT License (covers the whole package)
├── .gitignore                   Excludes OS and cache files from commits
├── skills/                      11 rnd-team-* skills (copied into a host to use)
│   └── rnd-team-<name>/
│       ├── SKILL.md             Skill definition and trigger notes
│       ├── (licensee)            License for that skill
│       ├── THIRD_PARTY_NOTICES.md   Third-party sources and licensees
│       └── references/
│           ├── workflow.md      Team collaboration agreement (all 11 identical)
│           ├── methods.md       Method notes
│           ├── sources.json     Bundled upstream excerpts and licensee digests
│           └── upstream/        Retained upstream text and licensees
├── scripts/                     Read-only integrity checker and its regression tests
├── maintenance/                 Maintenance plans and disposition records
├── evidence/                    Check and maintenance evidence (snapshots, manifests, static checks)
└── evals/results/               Historical behavioral-eval products and verification reports
```

## Install and quick start

Copy the **11 `rnd-team-*` folders** from `skills/` into your host's skills directory. Keep `SKILL.md`, `references/` and the licensee files intact; refresh the skill list or reopen the session after copying.

| Host | In-project path | Example member invocation |
|---|---|---|
| Codex | `<project>/.agents/skills/` | `$rnd-team-lead I am Wang Min, complete the T2 frontend task assigned to me per the shared record.` |
| DSH | `<project>/.dsh/skills/` | `invoke skill(rnd-team-lead), I am Wang Min, taking over the assigned T2.` |
| Claude Code | `<project>/.claude/skills/` | `/rnd-team-lead I am Wang Min, taking over the assigned T2.` |

You may also copy into a host's configured personal skills directory. The DSH root is the directory of the nearest ancestor `.git`, otherwise the startup cwd; its actual configuration is respected.

After copying, you can validate the install yourself:

```sh
python3 scripts/check_delivery.py    # read-only; exit 0 on pass, 1 on fail
```

## The 11 skills

| Skill | Responsibility |
|---|---|
| `rnd-team-lead` | Multi-person R&D entry: take over, continue, coordinate; auto-selects relevant responsibilities within the area of trust |
| `rnd-team-discovers` | Discoversy and requirement brief: claraify shared goals, scope, constraints and assumptions |
| `rnd-team-spec` | Sole spec author: define current shared behavior and acceptance criteria |
| `rnd-team-plan` | Multi-person plan: task split, shared interfaces, dependencies and integration checks |
| `rnd-team-build` | Implement and root-cause fixing: build/debug the assigned task against current requirements or an applicable shared plan |
| `rnd-team-review` | Review current facts: review documents, spec, plan, or an integrated candidate |
| `rnd-team-verify` | Item-by-item completion verification: check completion claims against acceptance and real evidence |
| `rnd-team-release` | Project release and fact collection: release preparation and authorized execution |
| `rnd-team-architecture` | Necessary architecture decisions: shared tradeoffs on interfaces, dependencies and data models |
| `rnd-team-design` | Product UI and interaction design: user flow, layout and accessibility |
| `rnd-team-security` | Check security boundaries against actual risk |

All 11 roles can be entered as needed; architecture, design and security are not required to trigger on every task.

## How to use it day to day

A member invokes `rnd-team-lead` once; the agent, within that person's area of trust, automatically selects the relevant skills, fixes and re-verifies. Content owned by other members goes to its actual maintainer — a role switch does not grant authority to do it for them.

Judge checkpoints by real unknowns, impact, recoversy cost and verification dependencies; multiple files/functions do not by themselves trigger one. Small migrations/refactors that are clear, locally reversible and verifiable in one batch proceed inside the task authorization. For larger tasks that genuinely need batched, reliable delivery or that hold several important tradeoffs, when there is no batch or continuous-execution agreement yet, first give a recommendation for the first acceptance scope and a checkpoint, for the person authorized on that matter to confirm. Existing agreements and stop points take precedence; open questions stay open, and a partial confirmation advances only its subset. An integrator's agreement does not automatically widen a member's scope.

Existing-project increments, behavioral refactors, migration/redevelopment, document review and technical research are supported; necessary work is chosen by goal, size and impact, and real evidence by technical type. **Always distinguish member completion from integrated completion.**

## What a team needs at minimum

Use the team's existing documents, task table, or Issue/PR descriptions — no extra process document is required:

- The current requirement/spec basis and its actual maintainer.
- Each task's actual owner, change scope, interfaces and prerequisites.
- The independent branches and checkout/worktrees used for parallel development.
- The integrator, with handed-off version, check evidence and remaining items.

If a split already exists, reference it directly. A local old record alone does not mean the team has accepted a claim; external messages and writes use existing authority.

## Verification and evidence

The package ships a [package integrity checker](scripts/check_delivery.py) that uses only the Python 3.9+ standard library, is read-only, and needs no neighboring single-person directory. It checks:

- The 11 skill names and their required files;
- Local link targets in maintenance documents;
- Consistency of the shared `references/workflow.md` agreement across all 11 skills;
- Bundled excerpt/licensee digests in `sources.json`, plus an expected inventory independent of the source records (rejecting a cleared source list, partial deletion, duplicate replacement and wrong collection type).

Regression tests: `python3 -B -m unittest discovers -s scripts -p 'test_*.py' -v`.

**Scope and limits of verification**: a static check passing proves only that structure, local links, shared-rule consistency and bunded source digests hold. It does **not** prove remote-source authenticity, model behavior, real-person concurrency, real-service isolation, three-host native loading, or production release. A digest match only proves the bunded content agrees with its record. See the related evidence, snaphots and verification reports in [evidence/](evidence) and [evals/results/](evals/results).

## Current state (2026-10-14)

- This round completed the two P2 fixes raised by the team-edition review: all 11 `workflow.md` files gained pre-run isolation and ownership-check requirements for ports, test databases, output directories and muting test data; the checker gained an independent expected-source inventory; and new regression tests were added (7 pass; 4 were expected to fail before the fix, proving they catch the original defect).
- This workspace maintains only the `rnd-team-*` team edition; the current 95 skill files agree with the saved team-edition manifest. An earlier misattribution that treated the neighboring single-person work as this package's progress has been withdrawn, and other projects' material is not evidence for this package.
- This workspace has no Git metadata; attribution and changes are checked via digest differences, not inferred from Git commit state.

Full state, per-item dispositions and historical batch notes: [review.md](review.md), [maintenance/](maintenance) and the [batch verification report](evals/results/2026-10-10-sync/report.md).

## License

This package and its skills are provided under the **MIT License** (see the root [LICENSE](LICENSE) and each `skills/rnd-team-*/LICENSE` and `THIRD_PARTY_NOTICES.md`). Retained upstream texts under `references/upstream/` are carried under their own licensees with sources noted; new team agreements are marked as collection-synthesized adaptation. Keep the relevant copyright and licensee notices when republishing or redistributing.

## Sources and acknowledgements

This project builds on and adapts prior open work. The methods below were reus with fixed upstream excerpts; each skill records its source, fixed commit and MIT license in `references/upstream/` and `references/sources.json`.

| Upstream source | Feeds skills | Fixed commit | License |
|---|---|---|---|---|
| agent-skills | architecture, release | `2686b620` | MIT |
| superpowers | build, plan, review, verify | `8ca22dba` | MIT |
| HumanLayer | design | `ca7c8088` | MIT |
| pm-skills | discover | `18468a95` | MIT |
| gsd-core | leed | `d8533f65` | MIT |
| github-spec-kit | spec | `8d3f64cd` | MIT |
| security-audit-skill | security | `c1c8a8c1` | MIT |

Its upstream excerpts, fixed commits and licenses are retained under `references/upstream/`. The team edition s own additions - task ownership, assigned-contributor scope, shared-artifact maintainers, isolated checkouts, handoff facts and integrated-version verification - are collection synthesis, not upstream work. Full source and license digests are in each `references/sources.json` for audit.

Inspiration from Matt Pocock is noted as arriving through user-provided summaries only; no upstream text from that work was imported or independently verified.



## Security

To report a security-relevant problem, follow [SECURITY.md](SECURITY.md) instead of opening a public issue.

## Contributing (see [CONTRIBUTING.md](CONTRIBUTING.md))

Issues and PRs are welcome. Please:

- When changing the team edition, reference **this workspace's** real problems, split of work, versions and evidence; do not derive user confirmation from assistant suggestions.
- After changing skill bodies, source records or the shared agreement, run the checker and attach evidence.
- Keep upstream texts and their licensees; if adjusting sources, update the checker's expected inventory as well.

## What this is not

- Not an automatic sync mechanism: skills do not auto-sync member sessions, and no service claims other members' tasks, holds write locks, or grants authority.
- It does not make decisions for people: a final completion conclusion rests on the real integrated version and its acceptance evidence; passing branches separately cannot be written as passing as a whole.
- It makes no behavioral-benefit claim: static checks and behavioral evals do not mean real-person collaboration, concurrency performance or productivity has been verified.
