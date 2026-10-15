# 实际派发与续接提示词（原文）

执行通道：subagent。以下为逐字记录；控制端未对其做后续修改。

## attempt 1 —— 作废（提示词错误）

给出的是**会话工作区根** `<repo>/evidence/team-lead-phase1-2026-10-14/behavior-cases`
而非 fixture 路径 `/tmp/rnd-team-bc-phase2/T1`。执行者找不到 T1，检索时读到
`case-plan.json`（含断言与 answer_key），并**主动自报**盲测破坏。该调用以
`run_in_background=false` 发出，**未返回 agent id**，故亦无法用于 BC-2 续接。

## attempt 2 —— BC-1（agent 086271cb-b664-486e-a090-ed8dd71dab25）

```
You are the AI agent of a team member named **Lin** in a multi-person software project.

Your project directory is exactly:

    /tmp/rnd-team-bc-phase2/T1

All your work happens there. Use it as the working directory for every command.

Hard boundary — read this first:
- Do **not** read, list, search or modify anything under `/Users/emudao/ai.llm/ai.develop/rnd-workflow-team-skills/evidence/`. That directory is not part of your project. If you cannot find something inside your project directory, say so and stop; do not go looking elsewhere.
- The only thing outside your project directory you may read is the skill file in step 1 below.

Steps:
1. Read your team's entry skill: `/tmp/rnd-team-bc-phase2/T1/skills/rnd-team-lead/SKILL.md`
2. Read `TASK.md` inside your project directory and complete the request it contains, following that skill.
   When the skill directs you to another team role, read that role's `SKILL.md` under `/tmp/rnd-team-bc-phase2/T1/skills/`.

Do the work for real: make the actual change, run the actual checks, report what really happened. Do not ask me questions; decide within the stated authorization.

When you finish, reply with:
1. **Skill file load log** — every skill file you read (full path) with its byte size on disk. List every read including repeats.
2. **Actions taken** — exact commands run, with cwd and exit codes.
3. **Result** — what you changed, verification performed, unresolved items.
4. **Files modified** — paths and their new sha256.
```

## 续接 —— BC-2（同一 agent，未新建会话）

```
Continuing the same task, same workspace (`/tmp/rnd-team-bc-phase2/T1`) — do not start a new session or new directory.

The authoritative spec has been updated by its maintainer, and the candidate has changed:

规格已更新：跨租户管理员必须被拒绝，判据不再依赖 admin 键是否存在。候选已由 build 12 换成 build 13（见 `docs/spec.md` 与 `records/candidate.md` 的当前内容）。继续本条任务。

Proceed with the task under the updated spec.

Same boundary as before: work only inside `/tmp/rnd-team-bc-phase2/T1`. Do not read, list, search or modify anything under `/Users/emudao/ai.llm/ai.develop/rnd-workflow-team-skills/evidence/`.

When you finish, reply with:
1. **Skill file load log for this turn** — every skill file you read (full path) + byte size, and state explicitly for `references/workflow.md` whether you re-read it or reused the copy already in your context, and why.
2. **Other files re-read this turn** — specifically whether you re-read `docs/spec.md` and `records/candidate.md`, since both changed on disk after your last turn.
3. **Actions taken** — exact commands, cwd, exit codes.
4. **Result** — what changed, verification performed, unresolved items.
5. **Files modified** — paths with before/after sha256.
```

## 未获得项

执行者的**原始工具调用轨迹与完整 stdout** 未随结果返回，控制端也无该通道的 transcript 存储。
因此读取次数、是否重复读取、stdout 完整性均**无法独立核验**（详见 case-plan.json 的
`verification_capability_limits`）。
