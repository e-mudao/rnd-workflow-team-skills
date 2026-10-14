# rnd-workflow-team-skills — Collaborative R&D Skills for Multi-Person Teams

A set of R&D skills for **multiple people, each working with their own agent (Codex, DSH, Claude Code, …), developing one shared project together**. It ships **11 `rnd-team-*` skills** covering the full path from discovery to release: discover, spec, plan, build, review, verify, release, plus architecture, design and security when needed.

Every member starts from the entry skill `rnd-team-lead` and picks up the task assigned to them; a coordinator maintains the shared split of work, and an integrator receives the tasks and verifies the final version. One person may hold several of these roles — the team does not need 11 people.

- 📖 Full team workflow, copyable prompts for all 11 skills, and a complete example: [guide.md](guide.md) (Chinese) · [README.zh.md](README.zh.md) 中文版

---

## What this is

When several people each work with an agent at the same time, the usual failures are: requirements and interfaces diverge, parallel changes overwrite each other, handoffs carry too little information, and "each branch passed on its own" is mistaken for "the whole thing passed".

This project turns those steps into skills: each skill maps to one R&D responsibility and states explicitly **who maintains which artifact, which changes need coordination, what a handoff must carry, and what evidence a completion claim rests on**. Skills run in each member's own session and, within that member's area of trust, automatically pull in the relevant responsibilities, fix and re-verify — the user does not connect each skill by hand.

**No package install, install script, Node/npm, or collection runtime is required.** The real business project keeps its own dependencies, tools and permissions.

## Repository layout

```
rnd-workflow-team-skills/
├── README.md                    This file: project overview and entry point
├── README.zh.md                 Chinese version of this file
├── guide.md                     Usage guide: workflow, copyable prompts, complete example (Chinese)
├── CHANGELOG.md                  Notable changes
├── CONTRIBUTING.md               Contributing guide
├── CODE_OF_CONDUCT.md            Code of conduct
├── CITATION.cff                  How to cite this software
├── LICENSE                      Root MIT License (covers the whole package)
├── .gitignore                   Excludes OS and cache files from commits
├── skills/                      11 rnd-team-* skills (copied into a host to use)
│   └── rnd-team-<name>/
│       ├── SKILL.md             Skill definition and trigger notes
│       ├── LICENSE              License for that skill
│       ├── THIRD_PARTY_NOTICES.md   Third-party sources and licenses
│       └── references/
│           ├── workflow.md      Team collaboration agreement (all 11 identical)
│           ├── methods.md       Method notes
│           ├── sources.json     Bundled upstream excerpts and license digests
│           └── upstream/        Retained upstream text and licenses
└── maintenance/                 Maintenance plans and disposition records
```

## Install and quick start

Copy the **11 `rnd-team-*` folders** from `skills/` into your host's skills directory. Keep `SKILL.md`, `references/` and the license files intact; refresh the skill list or reopen the session after copying.

| Host | In-project path | Example member invocation |
|---|---|---|
| Codex | `<project>/.agents/skills/` | `$rnd-team-lead I am Wang Min, complete the T2 frontend task assigned to me per the shared record.` |
| DSH | `<project>/.dsh/skills/` | `invoke skill(rnd-team-lead), I am Wang Min, taking over the assigned T2.` |
| Claude Code | `<project>/.claude/skills/` | `/rnd-team-lead I am Wang Min, taking over the assigned T2.` |

You may also copy into a host's configured personal skills directory. The DSH root is the directory of the nearest ancestor `.git`, otherwise the startup cwd; its actual configuration is respected.

## The 11 skills

| Skill | Responsibility |
|---|---|
| `rnd-team-lead` | Multi-person R&D entry: take over, continue, coordinate; auto-selects relevant responsibilities within the area of trust |
| `rnd-team-discover` | Discovery and requirement brief: clarify shared goals, scope, constraints and assumptions |
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

Judge checkpoints by real unknowns, impact, recovery cost and verification dependencies; multiple files/functions do not by themselves trigger one. Small migrations/refactors that are clear, locally reversible and verifiable in one batch proceed inside the task authorization. For larger tasks that genuinely need batched, reliable delivery or that hold several important tradeoffs, when there is no batch or continuous-execution agreement yet, first give a recommendation for the first acceptance scope and a checkpoint, for the person authorized on that matter to confirm. Existing agreements and stop points take precedence; open questions stay open, and a partial confirmation advances only its subset. An integrator's agreement does not automatically widen a member's scope.

Existing-project increments, behavioral refactors, migration/redevelopment, document review and technical research are supported; necessary work is chosen by goal, size and impact, and real evidence by technical type. **Always distinguish member completion from integrated completion.**

## What a team needs at minimum

Use the team's existing documents, task table, or Issue/PR descriptions — no extra process document is required:

- The current requirement/spec basis and its actual maintainer.
- Each task's actual owner, change scope, interfaces and prerequisites.
- The independent branches and checkout/worktrees used for parallel development.
- The integrator, with handed-off version, check evidence and remaining items.

If a split already exists, reference it directly. A local old record alone does not mean the team has accepted a claim; external messages and writes use existing authority.

## License

This package and its skills are provided under the **MIT License** (see the root [LICENSE](LICENSE) and each `skills/rnd-team-*/LICENSE` and `THIRD_PARTY_NOTICES.md`). Retained upstream texts under `references/upstream/` are carried under their own licenses with sources noted; new team agreements are marked as collection-synthesized adaptation. Keep the relevant copyright and license notices when republishing or redistributing.

## Sources and acknowledgements

This project builds on and adapts prior open work. The methods below were reused with fixed upstream excerpts retained; each skill records its source, fixed commit and MIT license in `references/upstream/` and `references/sources.json`.

| Upstream source | Feeds skills | Fixed commit | License |
|---|---|---|---|
| agent-skills | architecture, release | `2686b620` | MIT |
| superpowers | build, plan, review, verify | `8ca22dba` | MIT |
| HumanLayer | design | `ca7c8088` | MIT |
| pm-skills | discover | `18468a95` | MIT |
| gsd-core | lead | `d8533f65` | MIT |
| github-spec-kit | spec | `8d3f64cd` | MIT |
| security-audit-skill | security | `c1c8a8c1` | MIT |

Its upstream excerpts, fixed commits and licenses are retained under `references/upstream/`. The team edition's own additions - task ownership, assigned-contributor scope, shared-artifact maintainers, isolated checkouts, handoff facts and integrated-version verification - are collection synthesis, not upstream work. Full source and license digests are in each `references/sources.json` for audit.

## Contributing (see [CONTRIBUTING.md](CONTRIBUTING.md))

Issues and PRs are welcome. Please:

- When changing the team edition, reference **this workspace's** real problems, split of work, versions and evidence; do not derive user confirmation from assistant suggestions.
- After changing skill bodies, source records or the shared agreement, run the repository's own checks and attach the evidence.
- Keep upstream texts and their licenses; if adjusting sources, update the expected inventory record as well.
