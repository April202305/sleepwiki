---
type: source
aliases: ["Gao 2023 TDSAN"]
created: 2026-08-19
updated: 2026-08-19
sources: []
review_sections: ["2.2", "6.2"]
status: active
review_due: 2026-09-19
---

# Gao 等（2023）：跨数据集域对抗单通道 EEG 分期

## 基本信息
- 类型：论文
- 原始文件：`raw/inbox/gao-2023-domain-adversarial-staging.pdf`
- source_id：`raw/inbox/gao-2023-domain-adversarial-staging.pdf`
- 作者/机构：Dong-Rui Gao 等
- 年份：2023
- 英文原题：Automatic sleep staging of single-channel EEG based on domain adversarial neural networks and domain self-attention
- 录入日期：2026-08-19
- review_sections：[`2.2`, `6.2`]

## 核心摘要

研究提出 TDSAN，在 Sleep-EDF-SC、Sleep-EDF-ST 和自采数据之间进行无监督域适应，以来源域标签和未标注目标域数据评估六种跨数据集方向。其价值是直接展示跨数据集域偏移和适应性能，而不是证明在线或可穿戴部署。[[source-pages/gao-2023-domain-adversarial-staging]]（PDF 第 1、3–9 页）

## 方法与发现

- 三个数据集均转为100 Hz、30 s单通道 EEG epoch，并按AASM五类处理；跨域实验明确将一个数据集作为来源域、另一个作为目标域。[[source-pages/gao-2023-domain-adversarial-staging]]（PDF 第 5–7 页）
- 报告 accuracy 与 macro-F1，并在六个跨域方向中与多种直接迁移和UDA基线比较。[[source-pages/gao-2023-domain-adversarial-staging]]（PDF 第 7–9 页，Tables 3–4）
- 该实验验证的是跨数据集适应；不能作为随机epoch与subject-wise同条件直接比较，也不提供严格在线或端侧时延证据。

## 关联词条
- 模型：[[model/TDSAN]]
- 概念：[[concept/领域自适应]]、[[concept/跨数据集泛化]]、[[concept/睡眠分期]]

## 局限与待核实
- ⚠️目标域训练使用未标注目标数据，不能等同于完全不接触目标域的外部验证。
- ⚠️不同数据库的人群、导联和采集条件不一致，性能不能与同库内部验证组成简单排名。

## 来源
- `raw/inbox/gao-2023-domain-adversarial-staging.pdf`
