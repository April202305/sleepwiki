---
type: source
aliases: ["Radke 2024 transfer learning"]
created: 2026-08-18
updated: 2026-08-22
sources: ["raw/inbox/radke-2024-transfer-learning-sleep-staging.pdf"]
review_sections: ["6.2", "6.5"]
status: active
review_due: 2027-08-18
---

# Radke 等（2024）：预凝胶电极网格睡眠分期迁移学习

## 基本信息
- 类型：新型 EEG/EOG/EMG 传感器的迁移学习研究
- 原始文件/source_id：`raw/inbox/radke-2024-transfer-learning-sleep-staging.pdf`
- 作者/年份：Fabian A. Radke 等；2024
- 英文原题：Transfer Learning for Automatic Sleep Staging Using a Pre-Gelled Electrode Grid
- review_sections：["6.2", "6.5"]

## 题录与引用字段
- 题录状态：已核验
- 核验来源：Crossref（DOI 10.3390/diagnostics14090909），核验日 2026-08-22
- 文献语种：英文
- 作者（原始顺序）：Fabian A. Radke; Carlos F. da Silva Souto; Wiebke Pätzold; Karen Insa Wolf
- 原始题名：Transfer Learning for Automatic Sleep Staging Using a Pre-Gelled Electrode Grid
- 文献类型标识：[J/OL]
- 载体或容器题名：Diagnostics
- 出版年：2024
- 卷：14
- 期：9
- 起止页码：
- 文章号：909
- 出版地：
- 出版者：
- 编辑：
- 会议名称：
- 会议地点：
- 会议日期：
- DOI：10.3390/diagnostics14090909
- URL：https://doi.org/10.3390/diagnostics14090909
- 发表或更新日期：2024-04-26
- 引用日期：2026-08-22
- 补充标识：
- 核验备注：
- Word 成稿引用：RADKE F A, DA SILVA SOUTO C F, PÄTZOLD W, 等. Transfer Learning for Automatic Sleep Staging Using a Pre-Gelled Electrode Grid[J/OL]. Diagnostics, 2024, 14(9): 909. DOI:10.3390/diagnostics14090909.

## 核心摘要
模型先在公开 PSG 数据预训练，再用预凝胶电极网格的 12 夜数据微调；仅用 EEG+EOG 时总体 F1=0.81（Wake 0.84、N1 0.62、N2 0.81、N3 0.87、REM 0.88）。[[concept/域偏移]]（PDF 第 1、5–11 页）

## 局限与待核实
- ⚠️仅 12 夜健康人数据，属于设备域适配而非逐人在线个体化；未验证闭环干预。

## 关联词条
- 概念：[[concept/域偏移]]
- 综述：[[review/文献清单/06-挑战展望-6.2-文献需求单]]、[[review/证据包/06-挑战展望-6.2-P1-证据包]]、[[review/证据矩阵]]

## 来源
- `raw/inbox/radke-2024-transfer-learning-sleep-staging.pdf`
