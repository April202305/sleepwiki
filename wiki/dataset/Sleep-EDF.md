---
type: dataset
aliases: ["Sleep-EDF Expanded", "Sleep-EDF-20", "Sleep-EDF-78", "Sleep-EDF-v1"]
created: 2026-08-11
updated: 2026-08-11
sources: ["source-pages/eldele-2021-attention-based-single-channel-eeg", "source-pages/zhou-2022-singlechannelnet"]
status: active
review_due: 2027-08-11
---

# Sleep-EDF

## 基本信息
- 发布机构/年份：PhysioBank；本文献涉及 Sleep Cassette 与扩展版本。
- 数据规模：[[source-pages/eldele-2021-attention-based-single-channel-eeg|Eldele 等（2021）]]使用 20 人与 78 人版本；[[source-pages/zhou-2022-singlechannelnet|Zhou 等（2022）]]另报告 20 人子集。（PDF 第 4 页；Zhou PDF 第 2–3 页）
- 受试者：Sleep Cassette 研究的参与者；精确纳入标准需核对原始数据集文档。⚠️
- 信号与采样率：两篇论文均采用 Fpz-Cz；Eldele 等报告采样率 100 Hz。（Eldele PDF 第 4 页；Zhou PDF 第 2–3 页）
- 标签标准：Zhou 等说明其实验 hypnogram 按 R&K 标注，并将 N3/N4 合并为 N3；与 AASM 的映射必须分开记录。[[source-pages/zhou-2022-singlechannelnet|Zhou 等（2022）]]（PDF 第 2 页）
- 获取方式/许可：待核实。

## 适用任务与常见划分

用于 [[concept/睡眠分期]]；该页所收录实验以 Fpz-Cz [[concept/单通道 EEG]] 为输入，并出现 subject-wise 与 epoch-wise 划分，二者结果不可直接对比。[[source-pages/zhou-2022-singlechannelnet|Zhou 等（2022）]]（PDF 第 4–6 页）

## 已关联模型
- [[model/AttnSleep|AttnSleep]]
- [[model/SingleChannelNet|SingleChannelNet]]

## 数据质量、偏差与局限

- ⚠️ 同名版本、受试者数量、清醒期截取与标签映射不同都会改变结果，应在实验页显式记录。
- 与 [[concept/时序上下文]]、[[concept/类别不平衡]] 和 [[concept/跨数据集泛化]] 相关的结果需注明具体版本与划分。

## 来源
- [[source-pages/eldele-2021-attention-based-single-channel-eeg|Eldele 等（2021）]]
- [[source-pages/zhou-2022-singlechannelnet|Zhou 等（2022）]]
- [[source-pages/liu-2023-micro-sleepnet]]

## 综述关联
- [[review/证据矩阵|证据矩阵]]
- [[concept/PSG 参考标准]]、[[concept/临床验证]]、[[concept/可穿戴 EEG]]、[[concept/领域自适应]]、[[concept/模型压缩与端侧部署]]
- [[model/DeepSleepNet]]、[[model/SeqSleepNet]]、[[model/SleepEEGNet]]、[[model/SleepTransformer]]
- [[source-pages/phan-mikkelsen-2022-automatic-sleep-staging]]
- [[review/完整综述大纲]]
