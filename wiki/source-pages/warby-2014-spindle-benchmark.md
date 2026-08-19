---
type: source
aliases: ["Warby spindle benchmark"]
created: 2026-08-19
updated: 2026-08-19
sources: []
review_sections: ["2.2"]
status: active
review_due: 2026-09-19
---
# Warby 等（2014）：睡眠纺锤波统一benchmark
## 基本信息
- 类型：论文全文文本
- 原始文件：`raw/inbox/en-07-warby-2014-spindle-benchmark.fulltext.txt`
- source_id：`raw/inbox/en-07-warby-2014-spindle-benchmark.fulltext.txt`
- 作者/机构：Simon C. Warby 等
- 年份：2014
- 英文原题：Sleep-spindle detection: crowdsourcing and evaluating performance of experts, non-experts and automated methods
- 录入日期：2026-08-19
- review_sections：[`2.2`]
## 核心摘要
24名专家对110名健康受试者N2期C3-M2数据建立群体共识金标准，并比较专家、非专家和6种自动检测器。[[source-pages/warby-2014-spindle-benchmark]]（全文RESULTS与METHODS）
## 方法与发现
- 共识阈值0.25时得到1987个纺锤；个体专家event-wise F1为0.75±0.06，排除自身对共识贡献后为0.67±0.07。
- 研究明确区分by-event和by-sample评价，说明事件真值、重叠规则与标注者构成会改变结果。
## 关联词条
- 概念：[[concept/睡眠纺锤波]]
## 局限与待核实
- ⚠️当前为完整文本而非PDF，图表页码定位待补；离线benchmark不等于在线检测时延。
## 来源
- `raw/inbox/en-07-warby-2014-spindle-benchmark.fulltext.txt`
