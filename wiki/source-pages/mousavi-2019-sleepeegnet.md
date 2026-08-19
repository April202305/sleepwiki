---
type: source
aliases: ["Mousavi 2019 SleepEEGNet"]
created: 2026-08-19
updated: 2026-08-19
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
