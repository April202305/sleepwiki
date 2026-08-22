---
type: source
aliases: ["Guo 2024 FlexSleepTransformer"]
created: 2026-08-19
updated: 2026-08-22
sources: []
review_sections: ["2.2", "6.2"]
status: active
review_due: 2027-08-19
---

# FlexSleepTransformer：灵活输入通道睡眠分期

## 基本信息
- 类型：论文
- 原始文件：`raw/inbox/flexsleeptransformer-2024-sci-rep.pdf`
- source_id：`raw/inbox/flexsleeptransformer-2024-sci-rep.pdf`
- 作者/机构：Yanchen Guo、Maciej Nowakowski、Weiying Dai
- 年份：2024
- 英文原题：FlexSleepTransformer: a transformer-based sleep staging model with flexible input channel configurations
- 录入日期：2026-08-19
- review_sections：["2.2", "6.2"]

## 题录与引用字段
- 题录状态：已核验
- 核验来源：Crossref（DOI 10.1038/s41598-024-76197-0），核验日 2026-08-22
- 文献语种：英文
- 作者（原始顺序）：Yanchen Guo; Maciej Nowakowski; Weiying Dai
- 原始题名：FlexSleepTransformer: a transformer-based sleep staging model with flexible input channel configurations
- 文献类型标识：[J/OL]
- 载体或容器题名：Scientific Reports
- 出版年：2024
- 卷：14
- 期：1
- 起止页码：
- 文章号：26312
- 出版地：
- 出版者：
- 编辑：
- 会议名称：
- 会议地点：
- 会议日期：
- DOI：10.1038/s41598-024-76197-0
- URL：https://doi.org/10.1038/s41598-024-76197-0
- 发表或更新日期：2024-11-01
- 引用日期：2026-08-22
- 补充标识：
- 核验备注：
- Word 成稿引用：GUO Y, NOWAKOWSKI M, DAI W. FlexSleepTransformer: a transformer-based sleep staging model with flexible input channel configurations[J/OL]. Scientific Reports, 2024, 14(1): 26312. DOI:10.1038/s41598-024-76197-0.

## 核心摘要

模型允许不同数量和组合的 PSG 通道进入统一 Transformer，在 SleepEDF-78 与本地 SleepUHS 上进行被试级十折验证；混合数据训练达到各自专用模型准确率的约 98%，并改善跨数据集测试。[[source-pages/guo-2024-flexsleeptransformer]]（PDF 第 1、4–8 页）

## 方法与发现

- SleepEDF 与 SleepUHS 的单通道分别为 Fpz-Cz 与 F3-A2，通道和设备条件并不相同；研究使用 subject-wise cross-validation。（PDF 第 4–6 页）
- 灵活通道和混合训练支持跨中心输入适配，但仍属离线 PSG 分期；未报告因果流式推理、端侧时延或闭环触发安全。（PDF 第 8–12 页）

## 关联词条
- 模型：[[model/FlexSleepTransformer]]
- 概念：[[concept/领域自适应]]、[[concept/时序上下文]]

## 局限与待核实
- ⚠️ 跨数据集改善不能直接外推为消费级可穿戴设备 zero-shot 泛化。

## 来源
- `raw/inbox/flexsleeptransformer-2024-sci-rep.pdf`
