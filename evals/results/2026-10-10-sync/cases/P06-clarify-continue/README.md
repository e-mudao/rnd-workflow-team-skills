# 报告列表
列表支持按 status 筛选和分页。标准库 Python，无外部服务。CSV 格式采用 UTF-8，字段顺序 id,status。

已确认导出当前筛选下全部记录，不受分页影响；无 Web 宿主，本次提供写本地文件的接口。

```python
from reports import export_reports
export_reports("reports.csv", status="open")
```

省略 status 导出全部记录；空结果仍写表头。目标父目录需已存在，已有同名文件将覆盖，文件系统错误向调用者传播。原 list_reports 分页行为保留。使用 `python3 -m unittest -v` 检查。样例 sample-open.csv 已实际生成。成员本地实现和验证完成，待 Mei 接收；没有部署。
