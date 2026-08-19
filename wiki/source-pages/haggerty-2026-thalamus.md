---
type: source
aliases: ["Haggerty 2026 Thalamus"]
created: 2026-08-19
updated: 2026-08-19
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
