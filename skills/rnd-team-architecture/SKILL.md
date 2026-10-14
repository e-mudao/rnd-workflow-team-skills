---
name: rnd-team-architecture
description: Use when a multi-person project needs a consequential shared architecture, interface, dependency or data model decision beyond existing conventions.
---

# 必要架构决策

输入需求、现有结构、约束和风险。负责必要的架构、接口、依赖或数据模型决策；局部实现优先沿用项目约定。

## 多人任务边界

核对当前共享接口/模型的维护人和受影响任务。用现行合同、建议变更、兼容/迁移方案及依赖安排交接；架构决定经当前规格/计划维护人整合后，分别由各任务负责人实施，不直接修改其他成员范围。

[接手、分工与交接字段](references/workflow.md) 使用项目现有记录；只有本地草稿时不声称已通知或同步给其他成员。

## 本次范围与证据

新需求或运行条件改变时，先检查被推翻的假设，安排能否定方案的最小真实探针，再进入依赖实现、推广或大量重复稳定性测试。保留既定重复次数门槛，探针通过不替代它；新支持范围不倒推为原始遗漏。探针与决定由受托维护人完成或接收，不因架构角色接管他人实现。

## 方法

1. 明确问题和上下文，检查真实模块、数据流、边界、依赖及已有 ADR。
2. 比较少量能满足需求的方案，记录依据、成本、兼容性、迁移/恢复风险及负面后果，避免没有需求支撑的平台化。
3. 用 Context / Decision / Consequences 记录 ADR，保留被取代决定的引用和拒绝方案依据。
4. 把影响交 spec/plan 纳入当前规格及计划，再核对接口与数据约束确实反映决定。小决策可用现有文档中的一段说明。

## 核验与返回

架构或模型缺陷由本角色修复（RTN-6）；不代写规格或计划。图谱可帮助检索，空检索不能证明无影响，也不是必装依赖。

参照 [协作约定](references/workflow.md)；采用 agent-skills 的 ADR 方法，见 [固定来源](references/methods.md)。
