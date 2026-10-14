# 独立文本审查

结论：未发现本轮同步引入的实质矛盾或要求遗漏。此结论仅针对所审文本和固定内容比较，不代表行为评测通过。

## 范围与方法

只读比较 baseline 与 work 的技能、README、guide；完整阅读共同 workflow 与新增原生桌面参考，逐角色检查 SKILL.md 差异及相关原有段落。未读取行为响应、案例操作、执行日志或行为评分；未修改任何技能。审查者仅写入本报告。

## 核对结果

- 状态原位修正、历史入口处理、回读、既有问题更新义务及共享未同步标记齐全。一次性小修无需新建索引，不免除受影响既有入口更新。见 [协作约定](../../../skills/rnd-team-lead/references/workflow.md) 的“当前状态与人工验收轮次”“分批与上下文”，以及 [guide](../../../guide.md) 第 3.5 节。
- 人工反馈绑定实际候选和轮次，源码、新构建、成员/集成候选与运行实例分列，短答不跨候选外推；待答候选覆盖前由有权维护者保存并核对可恢复产物。见协作约定相同章节及 [build](../../../skills/rnd-team-build/SKILL.md)、[verify](../../../skills/rnd-team-verify/SKILL.md)“本次范围与证据”。
- 关键反例先于依赖实施、推广和大量稳定性重复，既定次数门槛仍保留；新增支持范围不倒推为原始遗漏。见 [architecture](../../../skills/rnd-team-architecture/SKILL.md)、[plan](../../../skills/rnd-team-plan/SKILL.md) 和 [discover](../../../skills/rnd-team-discover/SKILL.md)。
- 拒绝、隐藏、禁用的进入、解除、合法恢复及同实例恢复齐全；建议、推断和确认分开，待决恢复不能自行成为验收。见 [spec](../../../skills/rnd-team-spec/SKILL.md)、[review](../../../skills/rnd-team-review/SKILL.md) 与 verify。
- 桌面参考区分普通、铺满、原生全屏、小窗口及适用多屏；先判断任务可完成性，区分几何推断与实际渲染/操作，并保留其他隐藏原因已证实、排除、未核分类。见 [原生桌面检查](../../../skills/rnd-team-design/references/native-desktop.md)。
- 编译 RED 与旧缺陷行为 RED/最小真实复现分开，修复前后同测及覆盖限制明确；完整行为参数仅在权威规格维护，计划和核验引用。低风险无正式规格时允许明确请求和现有事实为依据。见 build、plan、verify、spec 及共同协作约定。
- 明确低风险任务直接做、先读只问实质未知项、信息充分即继续、调查后由实际计划维护人缩减未执行安排均明确；已有适用计划、项目要求、指定文档、授权和证据规则保留。见协作约定“按目标选择工作”、[lead](../../../skills/rnd-team-lead/SKILL.md) 及 [README](../../../README.md) 末节。
- 11 个角色保留；现行维护权、按事项决定权、独立目录隔离、完整提交或未提交交接、误报撤销所需反证及历史保留、准确集成版本核验规则保留。共同 workflow 的 11 份副本逐字节相同。

## 固定内容验证

实际字节比较确认：28 个 `references/upstream` 文件、release/security 两份 `SKILL.md`、11 份角色根目录 LICENSE 均与 baseline 一致。11 份 sources.json 的全部既有顶层字段值保持一致，本轮只增加来源适配记录。

## 限制

没有独立执行行为场景，也未据行为输出反推文本结论；没有核验外部上游原文真实性或外部服务状态。固定字节比较以提供的 baseline 为准。文本能够表达这些边界，不等于实际使用时必然遵守。
