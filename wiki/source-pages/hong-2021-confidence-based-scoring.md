---
type: source
aliases: ["Hong 2021 confidence-based sleep scoring"]
created: 2026-08-19
updated: 2026-08-22
sources: []
review_sections: ["2.2", "6.2"]
status: active
review_due: 2026-09-19
---

# Hong 等（2021）：置信度选择性睡眠分期

## 基本信息
- 类型：论文
- 原始文件：`raw/inbox/hong-2021-confidence-based-scoring.pdf`
- source_id：`raw/inbox/hong-2021-confidence-based-scoring.pdf`
- 作者/机构：Jung-Ki Hong 等；Seoul National University Bundang Hospital
- 年份：2021
- 英文原题：Confidence-Based Framework Using Deep Learning for Automated Sleep Stage Scoring
- 录入日期：2026-08-19
- review_sections：[`2.2`, `6.2`]

## 题录与引用字段
- 题录状态：已核验
- 核验来源：Crossref（DOI 10.2147/nss.s333566），核验日 2026-08-22
- 文献语种：英文
- 作者（原始顺序）：Jung Kyung Hong; Taeyoung Lee; Roben Deocampo Delos Reyes; Joonki Hong; Hai Hong Tran; Dongheon Lee; Jinhwan Jung; In-Young Yoon
- 原始题名：Confidence-Based Framework Using Deep Learning for Automated Sleep Stage Scoring
- 文献类型标识：[J/OL]
- 载体或容器题名：Nature and Science of Sleep
- 出版年：2021
- 卷：Volume 13
- 期：
- 起止页码：2239-2250
- 文章号：
- 出版地：
- 出版者：
- 编辑：
- 会议名称：
- 会议地点：
- 会议日期：
- DOI：10.2147/nss.s333566
- URL：https://doi.org/10.2147/nss.s333566
- 发表或更新日期：2021-12
- 引用日期：2026-08-22
- 补充标识：
- 核验备注：
- Word 成稿引用：HONG J K, LEE T, DELOS REYES R D, 等. Confidence-Based Framework Using Deep Learning for Automated Sleep Stage Scoring[J/OL]. Nature and Science of Sleep, 2021, Volume 13: 2239-2250. DOI:10.2147/nss.s333566.

## 核心摘要

研究在EEG五分类器旁加入置信度模型，以阈值接受或拒绝epoch预测，并将拒绝项交给人工复核。SNUBH实验使用702份PSG，另用SHHS验证；两者均在PSG层按70:15:15划分。[[source-pages/hong-2021-confidence-based-scoring]]（PDF 第 1、3–5 页）

## 方法与发现

- 输入为单导C3-A2 EEG，30 s epoch组成11-epoch序列；分类器基于TinySleepNet，置信度模型比较MCP、TCP、ConfidNet和dropout correct rate。[[source-pages/hong-2021-confidence-based-scoring]]（PDF 第 3–6 页，Figures 1–2）
- 总体置信度均值0.754与准确率0.758接近；仅复核最低置信度20%的epoch时，总体准确率从约76%提高至87%。[[source-pages/hong-2021-confidence-based-scoring]]（PDF 第 1、7–9 页）
- 这是选择性分类/人工复核证据；论文讨论校准与错误排序的区别，但未以ECE或Brier score证明概率校准。

## 关联词条
- 模型：[[model/Hong 置信度选择性睡眠分期框架]]
- 概念：[[concept/不确定性与拒绝输出]]、[[concept/睡眠分期]]

## 局限与待核实
- ⚠️性能提升以人工正确复核被拒绝epoch为前提，不是模型在全覆盖率下自身准确率提高。
- ⚠️11-epoch序列的严格实时方向需结合TinySleepNet实现核验；本研究不提供端到端在线部署时延。

## 来源
- `raw/inbox/hong-2021-confidence-based-scoring.pdf`
