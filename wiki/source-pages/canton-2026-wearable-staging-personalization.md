---
type: source
aliases: ["Canton 2026 wearable personalization"]
created: 2026-08-18
updated: 2026-08-18
sources: ["raw/inbox/canton-2026-wearable-staging-personalization.pdf"]
review_sections: ["6.2", "6.5"]
status: active
review_due: 2027-08-18
---

# Canton 等（2026）：可穿戴睡眠分类中的数据集适配

## 基本信息
- 类型：腕部加速度—PSG 数据集与模型评测研究
- 原始文件/source_id：`raw/inbox/canton-2026-wearable-staging-personalization.pdf`
- 作者/年份：Canton 等；2026
- 英文原题：What matters beyond model choice for wearable sleep staging? How personalization, evaluation choices, and easy-to-classify wake impact performance
- DOI：10.1093/sleepadvances/zpag051
- review_sections：["6.2", "6.5"]

## 核心摘要
新增 SleepAccel-Clinical（28 名 OSA 参与者的 Apple Watch 加速度与同步 PSG），并与 SleepAccel（31 人）、DREAMT（100 人）等比较；训练集中纳入 OSA 人群可改善在疑似睡眠障碍数据上的表现，简单“易分类清醒”结构会显著影响指标。[[concept/域偏移]]（PDF 第 1–4 页）

## 局限与待核实
- ⚠️输入为腕部加速度而非 EEG，且重点为睡眠/清醒分类与数据集偏差；只能支持人群匹配和评测边界，不能替代个体化 EEG 分期或闭环干预证据。

## 关联词条
- 概念：[[concept/域偏移]]
- 综述：[[review/文献清单/06-挑战展望-6.2-文献需求单]]、[[review/证据包/06-挑战展望-6.2-P1-证据包]]、[[review/证据矩阵]]

## 来源
- `raw/inbox/canton-2026-wearable-staging-personalization.pdf`
