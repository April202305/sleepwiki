---
type: source
aliases: ["Phan 2019 SeqSleepNet"]
created: 2026-08-19
updated: 2026-08-22
sources: []
review_sections: ["2.2"]
status: active
review_due: 2027-08-19
---

# SeqSleepNet：分层循环序列到序列睡眠分期

## 基本信息
- 类型：论文（arXiv 预印本，注明已发表于 IEEE TNSRE）
- 原始文件：`raw/inbox/phan-2019-seqsleepnet.pdf`
- source_id：`raw/inbox/phan-2019-seqsleepnet.pdf`
- 作者/机构：Huy Phan、Fernando Andreotti、Navin Cooray、Oliver Y. Chén、Maarten De Vos
- 年份：2019
- 英文原题：SeqSleepNet: End-to-End Hierarchical Recurrent Neural Network for Sequence-to-Sequence Automatic Sleep Staging
- 录入日期：2026-08-19
- review_sections：["2.2"]

## 题录与引用字段
- 题录状态：已核验
- 核验来源：Crossref（DOI 10.1109/tnsre.2019.2896659），核验日 2026-08-22
- 文献语种：英文
- 作者（原始顺序）：Huy Phan; Fernando Andreotti; Navin Cooray; Oliver Y. Chen; Maarten De Vos
- 原始题名：SeqSleepNet: End-to-End Hierarchical Recurrent Neural Network for Sequence-to-Sequence Automatic Sleep Staging
- 文献类型标识：[J/OL]
- 载体或容器题名：IEEE Transactions on Neural Systems and Rehabilitation Engineering
- 出版年：2019
- 卷：27
- 期：3
- 起止页码：400-410
- 文章号：
- 出版地：
- 出版者：
- 编辑：
- 会议名称：
- 会议地点：
- 会议日期：
- DOI：10.1109/tnsre.2019.2896659
- URL：https://doi.org/10.1109/tnsre.2019.2896659
- 发表或更新日期：2019-03
- 引用日期：2026-08-22
- 补充标识：
- 核验备注：
- Word 成稿引用：PHAN H, ANDREOTTI F, COORAY N, 等. SeqSleepNet: End-to-End Hierarchical Recurrent Neural Network for Sequence-to-Sequence Automatic Sleep Staging[J/OL]. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 2019, 27(3): 400-410. DOI:10.1109/tnsre.2019.2896659.

## 核心摘要

SeqSleepNet 把逐 epoch 分类改写为序列到序列任务，以时频输入、epoch 级注意力双向 RNN 和序列级双向 RNN 同时建模短期与跨 epoch 上下文。MASS 200 名受试者的 20 折被试级划分中报告总体准确率约 87.1%。[[source-pages/phan-2019-seqsleepnet]]（PDF 第 1、5–8 页）

## 方法与发现

- 每折将 200 名受试者划分为 180/10/10 名训练、验证和测试对象，避免随机 epoch 泄漏。（PDF 第 5 页）
- 两级双向 RNN 都利用序列两侧信息；完整序列输出不满足严格流式因果条件。（PDF 第 3–5 页）

## 关联词条
- 模型：[[model/SeqSleepNet]]
- 概念：[[concept/时序上下文]]、[[concept/睡眠分期]]

## 局限与待核实
- ⚠️ MASS 主要为健康人群；作者明确提示疾病人群泛化仍需验证。未报告设备端时延或闭环刺激接口。

## 来源
- `raw/inbox/phan-2019-seqsleepnet.pdf`
