---
type: source
aliases: ["Phan & Mikkelsen 2022"]
created: 2026-08-12
updated: 2026-08-12
sources: ["raw/inbox/Phan和Mikkelsen - 2022 - Automatic sleep staging of EEG signals recent development, challenges, and future directions.pdf"]
review_sections: ["1", "2", "4", "6", "7", "8"]
status: active
review_due: 2027-08-12
---

# Phan 和 Mikkelsen（2022）：EEG 自动睡眠分期的进展、挑战与未来方向

## 基本信息
- 类型：综述论文
- 原始文件：`raw/inbox/Phan和Mikkelsen - 2022 - Automatic sleep staging of EEG signals recent development, challenges, and future directions.pdf`
- source_id：`raw/inbox/Phan和Mikkelsen - 2022 - Automatic sleep staging of EEG signals recent development, challenges, and future directions.pdf`
- 作者/机构：Huy Phan、Kaare Mikkelsen
- 年份：2022
- 录入日期：2026-08-12
- review_sections：["1", "2", "4", "6", "7", "8"]

## 核心摘要

本文综述五分类 EEG 自动睡眠分期，覆盖 PSG 与移动 EEG；讨论长时序模型、移动监测的低信噪比、分布偏移、端侧模型压缩和临床采纳。[[concept/睡眠分期]]、[[concept/可穿戴 EEG]]、[[concept/跨数据集泛化]] 是其与 EEG-BCI 综述相关的主要入口。（PDF 第 1–2、8–17 页）

## 方法与发现

- 长时序睡眠分期系统包含 CNN、RNN/CRNN、GCN、自注意力和 Transformer 等架构；表中列出 [[model/DeepSleepNet|DeepSleepNet]]、[[model/SeqSleepNet|SeqSleepNet]]、[[model/SleepEEGNet|SleepEEGNet]] 与 [[model/SleepTransformer|SleepTransformer]]。（PDF 第 6–7 页，Table 1）
- 作者明确警告：不同数据子集、通道数和训练/迁移设置会使跨论文的性能直接比较失去意义。（PDF 第 6 页）
- 文中称移动 EEG 的代表性 κ 约为 0.75，而 PSG 数据的代表性 κ 超过 0.8；作者将较低信噪比视为性能下降的重要原因。该结论为综述性陈述，需在原始设备研究中进一步复核。（PDF 第 10 页）
- 机构、人群、疾病、模态、设备和采集条件差异会导致分布偏移；文中讨论监督、半监督和无监督 [[concept/领域自适应]]。（PDF 第 15–17 页）
- 面向可穿戴/手机/IoT 端部署，模型需受能耗、存储和推理时延限制；文中讨论量化、剪枝、轻量结构与 NAS。（PDF 第 13 页）

## 关联词条
- 模型：[[model/DeepSleepNet]]、[[model/SeqSleepNet]]、[[model/SleepEEGNet]]、[[model/SleepTransformer]]
- 数据集：[[dataset/MESA]]、[[dataset/SHHS]]、[[dataset/Sleep-EDF]]
- 概念：[[concept/睡眠分期]]、[[concept/可穿戴 EEG]]、[[concept/跨数据集泛化]]、[[concept/领域自适应]]、[[concept/临床验证]]、[[concept/模型压缩与端侧部署]]
- 参考标准：[[concept/PSG 参考标准]]

## 局限与待核实
- ⚠️ 本文为综述；其汇总指标、设备性能和模型比较不能替代所引原始研究的条件化核验。
- ⚠️ 文中不提供可穿戴 EEG-BCI 闭环 N3 触发、刺激时延或剂量的直接证据。

## 来源
- `raw/inbox/Phan和Mikkelsen - 2022 - Automatic sleep staging of EEG signals recent development, challenges, and future directions.pdf`

## 综述关联
- [[review/证据矩阵]]
- [[review/chapters/02-基础理论与核心概念]]
- [[review/完整综述大纲]]
- [[review/文献搜索策略_新版]]
