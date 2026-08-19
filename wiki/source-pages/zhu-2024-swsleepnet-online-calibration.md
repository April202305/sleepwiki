---
type: source
aliases: ["SwSleepNet"]
created: 2026-08-19
updated: 2026-08-19
sources: []
review_sections: ["2.2"]
status: active
review_due: 2026-09-19
---
# Zhu 等（2024）：SwSleepNet实时预测与在线校准
## 基本信息
- 类型：论文
- 原始文件：`raw/inbox/en-09-zhu-2024-online-calibration.pdf`
- source_id：`raw/inbox/en-09-zhu-2024-online-calibration.pdf`
- 作者/机构：Hangyu Zhu、Yonglin Wu、Yao Guo 等
- 年份：2024
- 英文原题：Towards Real-Time Sleep Stage Prediction and Online Calibration Based on Architecturally Switchable Deep Learning Models
- 录入日期：2026-08-19
- review_sections：[`2.2`]
## 核心摘要
SwSleepNet离线模式使用序列模块，在线模式以2、3或5 s短片段预测；连续两段预测不一致时触发上下文校正。三数据集离线accuracy为84.5%、86.7%和81.8%，在线短片段结果均超过80%。[[source-pages/zhu-2024-swsleepnet-online-calibration]]（PDF第1、3–9页）
## 关联词条
- 模型：[[model/SwSleepNet]]
- 概念：[[concept/不确定性与拒绝输出]]、[[concept/睡眠分期]]
## 局限与待核实
- ⚠️论文“calibration”指预测不一致后的上下文重判，不等同于ECE/Brier概率校准；在线准确率不能直接与30 s五分类排行。
## 来源
- `raw/inbox/en-09-zhu-2024-online-calibration.pdf`
