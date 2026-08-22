---
type: source
aliases: ["Huang 2025 MultiSEss"]
created: 2026-08-19
updated: 2026-08-22
sources: []
review_sections: ["2.2"]
status: active
review_due: 2027-08-19
---

# MultiSEss：SE 注意力与状态空间睡眠分期

## 基本信息
- 类型：论文
- 原始文件：`raw/inbox/multisess-2025-ssm-staging.pdf`
- source_id：`raw/inbox/multisess-2025-ssm-staging.pdf`
- 作者/机构：Zhentao Huang、Yuyao Yang、Zhiyuan Wang 等
- 年份：2025
- 英文原题：MultiSEss: Automatic Sleep Staging Model Based on SE Attention Mechanism and State Space Model
- 录入日期：2026-08-19
- review_sections：["2.2"]

## 题录与引用字段
- 题录状态：已核验
- 核验来源：Crossref（DOI 10.3390/biomimetics10050288），核验日 2026-08-22
- 文献语种：英文
- 作者（原始顺序）：Zhentao Huang; Yuyao Yang; Zhiyuan Wang; Yuan Li; Zuowen Chen; Yahong Ma; Shanwen Zhang
- 原始题名：MultiSEss: Automatic Sleep Staging Model Based on SE Attention Mechanism and State Space Model
- 文献类型标识：[J/OL]
- 载体或容器题名：Biomimetics
- 出版年：2025
- 卷：10
- 期：5
- 起止页码：
- 文章号：288
- 出版地：
- 出版者：
- 编辑：
- 会议名称：
- 会议地点：
- 会议日期：
- DOI：10.3390/biomimetics10050288
- URL：https://doi.org/10.3390/biomimetics10050288
- 发表或更新日期：2025-05-03
- 引用日期：2026-08-22
- 补充标识：
- 核验备注：
- Word 成稿引用：HUANG Z, YANG Y, WANG Z, 等. MultiSEss: Automatic Sleep Staging Model Based on SE Attention Mechanism and State Space Model[J/OL]. Biomimetics, 2025, 10(5): 288. DOI:10.3390/biomimetics10050288.

## 核心摘要

MultiSEss 将多尺度卷积、SE 注意力与状态空间模块组合，用于公开 EEG 数据集上的五分类睡眠分期。论文提供离线数据集性能和消融实验，支持 SSM 用于 EEG 时序建模的可行性。[[source-pages/huang-2025-multisess]]（PDF 第 1、4–10 页）

## 方法与发现

- 模型在 Sleep-EDF-20、Sleep-EDF-78 和 SHHS 等公开数据上评估；验证重点为离线准确率、F1、κ 与模块消融。（PDF 第 5–10 页）
- 论文未提供可穿戴硬件实测、严格因果流式配置、单窗端到端时延、峰值内存或闭环刺激验证。（PDF 第 10–12 页）

## 关联词条
- 模型：[[model/MultiSEss]]
- 概念：[[concept/时序上下文]]、[[concept/模型压缩与端侧部署]]

## 局限与待核实
- ⚠️ 只能支撑“SSM 为候选路径”；不能证明其已优于 Transformer 的在线闭环适用性。

## 来源
- `raw/inbox/multisess-2025-ssm-staging.pdf`
