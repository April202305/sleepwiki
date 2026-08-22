---
type: source
aliases: ["Haggerty 2026 Thalamus"]
created: 2026-08-19
updated: 2026-08-22
sources: []
review_sections: ["2.3", "6.3"]
status: needs_review
review_due: 2027-02-19
---

# Thalamus：同步闭环多模态采集平台

## 基本信息
- 类型：代码/系统论文
- 原始文件：`raw/inbox/haggerty-2026-thalamus-closed-loop-system.pdf`
- source_id：`raw/inbox/haggerty-2026-thalamus-closed-loop-system.pdf`
- 作者/机构：Jarl Haggerty 等
- 年份：2026
- 英文原题：Thalamus: a real-time system for synchronized, closed-loop multimodal behavioral and electrophysiological data capture
- 录入日期：2026-08-19
- review_sections：["2.3", "6.3"]

## 题录与引用字段
- 题录状态：已核验
- 核验来源：Crossref（DOI 10.1038/s44172-026-00646-z），核验日 2026-08-22
- 文献语种：英文
- 作者（原始顺序）：Jarl Haggerty; Qasim Qureshi; Ellie D. Gabriel; Pedro GLB Borges; Pierce Davis; Katie Wingel; Jerry Cai; Krishna Sargur; Min Jae Kim; Agrita Dubey; Indie Garwood; Alex Vaz; Andrew G. Richardson; Han-Chiao Isaac Chen; Lauren H. Hammer; Joshua Gold; Brian Litt; Daniel Yoshor; Michael Beauchamp; Casey Halpern; Bijan Pesaran; Iahn Cajigas
- 原始题名：Thalamus: a real-time system for synchronized, closed-loop multimodal behavioral and electrophysiological data capture
- 文献类型标识：[J/OL]
- 载体或容器题名：Communications Engineering
- 出版年：2026
- 卷：5
- 期：1
- 起止页码：
- 文章号：93
- 出版地：
- 出版者：
- 编辑：
- 会议名称：
- 会议地点：
- 会议日期：
- DOI：10.1038/s44172-026-00646-z
- URL：https://doi.org/10.1038/s44172-026-00646-z
- 发表或更新日期：2026-03-26
- 引用日期：2026-08-22
- 补充标识：
- 核验备注：
- Word 成稿引用：HAGGERTY J, QURESHI Q, GABRIEL E D, 等. Thalamus: a real-time system for synchronized, closed-loop multimodal behavioral and electrophysiological data capture[J/OL]. Communications Engineering, 2026, 5(1): 93. DOI:10.1038/s44172-026-00646-z.

## 核心摘要

Thalamus 是面向神经外科和临床实验的开源多模态同步采集平台，采用可配置节点管线和 Python/C++ 分层架构，并通过回环与负载实验验证同步性能。[[source-pages/haggerty-2026-thalamus]]（PDF 第 1、8–13 页）

## 方法与发现

- 系统验证聚焦数据流同步、负载和失效保护，可支持闭环实验的实时计算。（PDF 第 8–13 页）
- 研究并非睡眠干预系统，没有测量 EEG 采集、睡眠算法、通信和声音抵达受试者构成的完整链路。（PDF 第 1、14–16 页）

## 关联词条
- 概念：[[concept/闭环系统时延]]、[[concept/闭环控制]]

## 局限与待核实
- ⚠️ 只能作为同步和失效保护的邻域工程参照；不解除 2.3/6.3 的睡眠刺激端到端时延缺口。

## 来源
- `raw/inbox/haggerty-2026-thalamus-closed-loop-system.pdf`
