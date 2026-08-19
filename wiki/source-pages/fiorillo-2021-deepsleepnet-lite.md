---
type: source
aliases: ["DeepSleepNet-Lite"]
created: 2026-08-19
updated: 2026-08-19
sources: []
review_sections: ["2.2"]
status: active
review_due: 2026-09-19
---
# Fiorillo 等（2021）：DeepSleepNet-Lite与不确定性估计
## 基本信息
- 类型：论文
- 原始文件：`raw/inbox/en-12-deepsleepnet-lite-2021.pdf`
- source_id：`raw/inbox/en-12-deepsleepnet-lite-2021.pdf`
- 作者/机构：Luigi Fiorillo、Paolo Favaro、Francesca Dalia Faraci
- 年份：2021
- 英文原题：DeepSleepNet-Lite: A Simplified Automatic Sleep Stage Scoring Model With Uncertainty Estimates
- 录入日期：2026-08-19
- review_sections：[`2.2`]
## 核心摘要
模型处理90 s单通道Fpz-Cz EEG，并以Monte Carlo dropout估计不确定实例，兼顾轻量结构和不确定性输出。[[source-pages/fiorillo-2021-deepsleepnet-lite]]（PDF第1–8页）
## 关联词条
- 模型：[[model/DeepSleepNet-Lite]]
- 概念：[[concept/不确定性与拒绝输出]]、[[concept/模型压缩与端侧部署]]
## 局限与待核实
- ⚠️不确定性估计不等于经过校准的概率；90 s输入涉及相邻epoch，在线方向须核验。
## 来源
- `raw/inbox/en-12-deepsleepnet-lite-2021.pdf`
