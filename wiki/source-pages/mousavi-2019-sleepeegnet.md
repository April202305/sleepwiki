---
type: source
aliases: ["Mousavi 2019 SleepEEGNet"]
created: 2026-08-19
updated: 2026-08-22
sources: []
review_sections: ["2.2"]
status: active
review_due: 2027-08-19
---

# SleepEEGNet：序列到序列自动睡眠分期

## 基本信息
- 类型：论文
- 原始文件：`raw/inbox/mousavi-2019-sleepeegnet.pdf`
- source_id：`raw/inbox/mousavi-2019-sleepeegnet.pdf`
- 作者/机构：Sajad Mousavi、Fatemeh Afghah、U. Rajendra Acharya
- 年份：2019
- 英文原题：SleepEEGNet: Automated sleep stage scoring with sequence to sequence deep learning approach
- 录入日期：2026-08-19
- review_sections：["2.2"]

## 题录与引用字段
- 题录状态：已核验
- 核验来源：Crossref（DOI 10.1371/journal.pone.0216456），核验日 2026-08-22
- 文献语种：英文
- 作者（原始顺序）：Sajad Mousavi; Fatemeh Afghah; U. Rajendra Acharya
- 原始题名：SleepEEGNet: Automated sleep stage scoring with sequence to sequence deep learning approach
- 文献类型标识：[J/OL]
- 载体或容器题名：PLOS ONE
- 出版年：2019
- 卷：14
- 期：5
- 起止页码：
- 文章号：e0216456
- 出版地：
- 出版者：
- 编辑：
- 会议名称：
- 会议地点：
- 会议日期：
- DOI：10.1371/journal.pone.0216456
- URL：https://doi.org/10.1371/journal.pone.0216456
- 发表或更新日期：2019-05-07
- 引用日期：2026-08-22
- 补充标识：
- 核验备注：
- Word 成稿引用：MOUSAVI S, AFGHAH F, ACHARYA U R. SleepEEGNet: Automated sleep stage scoring with sequence to sequence deep learning approach[J/OL]. PLOS ONE, 2019, 14(5): e0216456. DOI:10.1371/journal.pone.0216456.

## 核心摘要

SleepEEGNet 以单通道 EEG 为输入，用 CNN 学习 epoch 内表征，再以双向 RNN 和注意力建模 epoch 间关系；报告总体准确率 84.26%、macro-F1 79.66%、κ=0.79。[[source-pages/mousavi-2019-sleepeegnet]]（PDF 第 1、9–11 页）

## 方法与发现

- 模型明确使用双向循环单元，同时访问先前与未来输入，因此适合离线序列评分，不能直接作为严格因果在线闭环证据。（PDF 第 4–5 页）
- 研究采用 20 折/10 折交叉验证，并区分 intra-patient 与 inter-patient 设置；跨设备及真实可穿戴端侧时延未验证。（PDF 第 8–11 页）

## 关联词条
- 模型：[[model/SleepEEGNet]]
- 概念：[[concept/时序上下文]]、[[concept/睡眠分期]]

## 局限与待核实
- ⚠️ 未报告闭环端侧推理、功耗或刺激触发验证；双向上下文含未来信息。

## 来源
- `raw/inbox/mousavi-2019-sleepeegnet.pdf`
