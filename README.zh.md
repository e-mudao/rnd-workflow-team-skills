# rnd-workflow-team — 多人协作版研发技能集合

一组供 **多个人各自使用 Agent（Codex、DSH、Claude Code 等）共同开发同一个项目** 的研发技能。共 **11 个 `rnd-team-*` 技能**，覆盖从需求发现到发布的全流程：发现、规格、计划、实现、审查、核验、发布，以及按需进入的架构、设计、安全。

每个成员从入口技能 `rnd-team-lead` 接手分配给自己的任务；协调负责人维护共享分工，集成负责人接收各任务并核验最终版本。这些职责可由同一人兼任，不要求团队真有 11 个成员。

- 📖 详细团队协作步骤、11 个技能的可复制 Prompt 和完整示例：[guide.md](guide.md)

---

## 这是什么

团队协作里，多个人各自带 Agent 同时开发，最常见的问题是：需求与接口不统一、并行改动互相覆盖、交接信息不足、各分支“分别通过”被误当成“整体通过”。

本项目把这些环节固化成技能：每个技能对应一个研发职责，明确规定**谁维护哪份制品、哪些变化需要协调、交接要带哪些信息、完成结论依据什么证据**。技能在成员自己的会话里运行，按成员受托范围自动选择相关职责、修复和复验，用户无需逐个手动连接技能。

**不需要安装包、安装脚本、Node/npm 或集合运行时。** 实际业务项目仍使用自己的依赖、工具与权限。

## 仓库结构

```
rnd-workflow-team/
├── README.zh.md                    本文件：项目说明与入口
├── README.md                    英文版 / English version
├── guide.md                     使用指南：协作流程、可复制 Prompt、完整示例
├── review.md                    当前交付与维护状态、验证范围
├── CHANGELOG.md                  变更日志
├── CONTRIBUTING.md               贡献指南
├── SECURITY.md                   安全政策
├── CODE_OF_CONDUCT.md            行为准则
├── CITATION.cff                  引用格式
├── LICENSED                     根 MIT 许可（覆盖整个包）
├── .gitignore                   提交时排除系统与缓存文件
├── skills/                      11 个 rnd-team-* 技能（复制到宿主使用）
│   └── rnd-team-<name>/
│       ├── SKILL.md             技能定义与触发说明
│       ├── LICENSE              该技能的许可
│       ├── THIRD_PARTY_NOTICES.md   第三方来源与许可
│       └── references/
│           ├── workflow.md      团队协作约定（11 份一致）
│           ├── methods.md       方法说明
│           ├── sources.json     随包上游摘录与许可摘要
│           └── upstream/        保留的上游原文与许可
├── scripts/                     只读完整性检查器及其回归测试
├── maintenance/                 维护计划与处置记录
├── evidence/                    检查与维护证据（快照、清单、静态检查）
└── evals/results/               历史行为评估产物与核验报告
```

## 安装与快速开始

将 `skills/` 中的 **11 个 `rnd-team-*` 文件夹**完整复制到宿主 skills 目录。保持 `SKILL.md`、`references/` 和许可文件完整；复制后刷新技能列表或重开会话。

| 宿主 | 项目内路径 | 成员调用示例 |
|---|---|---|
| Codex | `<项目>/.agents/skills/` | `$rnd-team-lead 我是王敏，按共享任务记录完成分配给我的 T2 前端功能。` |
| DSH | `<项目>/.dsh/skills/` | `调用 skill(rnd-team-lead)，我是王敏，接手已分配的 T2。` |
| Claude Code | `<项目>/.claude/skills/` | `/rnd-team-lead 我是王敏，接手已分配的 T2。` |

也可复制到宿主已配置的个人 skills 目录。DSH 根为最近祖先 `.git` 所在目录，否则为启动 cwd，沿用其实际配置。

复制后可自行校验安装完整性：

```sh
python3 scripts/check_delivery.py    # 只读；通过退出 0，失败退出 1
```

## 11 个技能

| 技能 | 职责 |
|---|---|
| `rnd-team-lead` | 多人研发入口：接手、续做、协调，按受托范围自动选择相关职责 |
| `rnd-team-discover` | 发现与需求简报：澄清共享目标、范围、约束与假设 |
| `rnd-team-spec` | 唯一规格作者：定义当前共享行为与验收标准 |
| `rnd-team-plan` | 多人实施计划：分工、共享接口、依赖与集成检查点 |
| `rnd-team-build` | 实现与根因修复：按当前需求或适用共享计划实现/调试受托任务 |
| `rnd-team-review` | 审查当前事实：审文档、规格、计划或集成候选 |
| `rnd-team-verify` | 逐项完成核验：对照验收与真实证据检查完成声明 |
| `rnd-team-release` | 项目发布与事实采集：发布准备与授权执行 |
| `rnd-team-architecture` | 必要架构决策：接口、依赖与数据模型的共享取舍 |
| `rnd-team-design` | 产品界面与交互设计：用户流程、布局与可访问性 |
| `rnd-team-security` | 按实际风险检查安全边界 |

11 个角色可按需进入；架构、设计和安全不要求每项任务都触发。

## 日常怎样使用

成员调用一次 `rnd-team-lead`，Agent 在本人受托范围自动选择相关技能、修复和复验。其他成员的内容交实际维护人，不能靠切换角色代做。

按实际未知项、影响、恢复成本和验证依赖判断检查点；多文件/多函数不单独触发。明确、局部可逆且可一批验证的小型迁移/重构直接在任务授权内接续。确需分批可靠交付或有多项重要取舍的较大任务，首次没有批次或连续执行约定时，先给首个可验收范围和检查点建议，由有权决定该事项的人确认。已有约定及停止点优先；待答保持待答，部分确认仅推进子集。集成者的同意不自动扩大成员范围。

支持现有项目增量、行为重构、迁移/重开发、文档审查和技术调研；按目标、规模及影响选择必要工作，按技术类型选择实际证据。**始终区分成员完成与集成完成。**

## 团队最少需要什么

使用团队现有的文档、任务表或 Issue/PR 说明即可，不要求再建一套流程文档：

- 当前需求/规格依据及实际维护人。
- 每项任务的实际负责人、修改范围、接口和前置依赖。
- 并行开发使用的独立分支与 checkout/工作树。
- 集成负责人，交接版本、检查证据和剩余项。

已有分工就直接引用。只有本地旧记录时不假定团队已经接受认领；外部消息和写入使用已有授权。


## 许可

本包及其技能按 **MIT 许可** 提供（见根目录 [LICENSE](LICENSE) 与各 `skills/rnd-team-*/LICENSE`、`THIRD_PARTY_NOTICES.md`）。`references/upstream/` 中保留的上游原文按其自身许可携带并注明来源；新增团队约定标记为集合综合适配。转载或再分发时请保留相应的版权与许可声明。

## 致谢与来源

本项目参考、借鉴并适配了多项既有开源工作。下列方法被重新使用，并保留固定的上游摘录；每个技能在 `references/upstream/` 与 `references/sources.json` 中记录其来源、固定提交与 MIT 许可。

| 上游来源 | 对应技能 | 固定提交 | 许可 |
|---|---|---|---|---|
| agent-skills | architecture、release | `2686b620` | MIT |
| superpowers | build、plan、review、verify | `8ca22dba` | MIT |
| HumanLayer | design | `ca7c8088` | MIT |
| pm-skills | discover | `18468a95` | MIT |
| gsd-core | lead | `d8533f65` | MIT |
| github-spec-kit | spec | `8d3f64cd` | MIT |
| security-audit-skill | security | `c1c8a8c1` | MIT |

上游摘录、固定提交与许可保留在 `references/upstream/` 下。本团队版新增的任务归属、成员受托范围、共享制品维护人、隔离工作树、交接事实与集成版本核验，均属集合综合适配，非上游工作。完整来源与许可摘要见各 `references/sources.json`，可审计。


## 贡献（详见 [CONTRIBUTING.md](CONTRIBUTING.md)）

欢迎提 Issue 或 PR。请：

- 改动团队版改进时引用**本工作区**的实际问题、分工、版本与证据；不从助手建议推导用户确认。
- 修改技能正文、来源记录或共同约定后，运行检查器并附带证据。
- 保留上游原文与其许可；如需调整来源，须一并审查检查器中的预期清单。

