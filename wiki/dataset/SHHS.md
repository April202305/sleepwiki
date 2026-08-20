---
type: dataset
aliases: ["Sleep Heart Health Study"]
created: 2026-08-11
updated: 2026-08-20
sources: ["source-pages/eldele-2021-attention-based-single-channel-eeg"]
status: active
review_due: 2027-08-11
---

# SHHS

## 基本信息
- 发布机构/年份：Sleep Heart Health Study；具体发布信息待核实。
- 数据规模：Eldele 等从 6,441 名受试者中选择 329 名 AHI < 5 的受试者用于实验。（PDF 第 4 页）
- 受试者：多中心队列；论文描述其与睡眠呼吸障碍相关，并按 AHI < 5 筛选近似常规睡眠受试者。[[source-pages/eldele-2021-attention-based-single-channel-eeg|Eldele 等（2021）]]（PDF 第 4 页）
- 信号与采样率：实验使用 C4-A1 EEG，125 Hz。[[source-pages/eldele-2021-attention-based-single-channel-eeg|Eldele 等（2021）]]（PDF 第 4 页）
- 标签标准：论文中将 N3/N4 合并为 N3；原始标注标准待核实。
- 获取方式/许可：待核实。

## 适用任务与常见划分

用于 [[concept/睡眠分期]] 的 [[concept/单通道 EEG]] 评估。[[source-pages/eldele-2021-attention-based-single-channel-eeg|Eldele 等（2021）]]（PDF 第 4 页）

## 已关联模型
- [[model/AttnSleep|AttnSleep]]
- [[model/Hong 置信度选择性睡眠分期框架]]
- [[model/Micro SleepNet]]

## 数据质量、偏差与局限

- ⚠️ 上述 329 人是该论文的筛选样本，不等同于 SHHS 全量数据集规模。

## 来源
- [[source-pages/eldele-2021-attention-based-single-channel-eeg|Eldele 等（2021）]]
- [[source-pages/hong-2021-confidence-based-scoring]]
- [[source-pages/liu-2023-micro-sleepnet]]

## 综述关联
- [[review/证据矩阵|证据矩阵]]
- [[concept/PSG 参考标准]]、[[concept/临床验证]]、[[concept/可穿戴 EEG]]、[[concept/领域自适应]]、[[concept/模型压缩与端侧部署]]
- [[model/SeqSleepNet]]、[[model/SleepTransformer]]
- [[source-pages/phan-mikkelsen-2022-automatic-sleep-staging]]
- [[review/完整综述大纲]]
- [[review/2.2公开数据集、标签体系与验证协议比较表]]
