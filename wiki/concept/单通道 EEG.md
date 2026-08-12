---
type: concept
aliases: ["single-channel EEG", "single channel EEG"]
created: 2026-08-11
updated: 2026-08-11
sources: ["source-pages/eldele-2021-attention-based-single-channel-eeg", "source-pages/zhou-2022-singlechannelnet"]
status: active
review_due: 2027-08-11
---

# 单通道 EEG

## 定义

仅使用一个脑电导联作为 [[concept/睡眠分期]] 模型输入的设置；本文献涉及 Fpz-Cz、C4-A1 与 C4/A1 导联。[[source-pages/eldele-2021-attention-based-single-channel-eeg|Eldele 等（2021）]]（PDF 第 4 页）；[[source-pages/zhou-2022-singlechannelnet|Zhou 等（2022）]]（PDF 第 2、5 页）

## 在睡眠分期中的作用

可简化采集方案，是 [[model/AttnSleep|AttnSleep]] 与 [[model/SingleChannelNet|SingleChannelNet]] 的共同输入假设。

## 方法、参数或判定标准

不同数据集的通道和采样率不同：[[dataset/Sleep-EDF|Sleep-EDF]] 的 Fpz-Cz 为 100 Hz（Eldele 等），[[dataset/SHHS|SHHS]] 的 C4-A1 为 125 Hz，[[dataset/CCSHS|CCSHS]] 的 C4/A1 为 128 Hz。[[source-pages/eldele-2021-attention-based-single-channel-eeg|Eldele 等（2021）]]（PDF 第 4 页）；[[source-pages/zhou-2022-singlechannelnet|Zhou 等（2022）]]（PDF 第 2–4 页）

## 相关模型与数据集
- [[model/AttnSleep|AttnSleep]]、[[model/SingleChannelNet|SingleChannelNet]]
- [[dataset/Sleep-EDF|Sleep-EDF]]、[[dataset/SHHS|SHHS]]、[[dataset/CCSHS|CCSHS]]

## ⚠️争议与待核实

- ⚠️ 单通道选择与采样率差异是跨研究性能比较的混杂因素。

## 来源
- [[source-pages/eldele-2021-attention-based-single-channel-eeg|Eldele 等（2021）]]
- [[source-pages/zhou-2022-singlechannelnet|Zhou 等（2022）]]

## 综述关联
- [[review/证据矩阵|证据矩阵]]
- [[review/chapters/02-基础理论与核心概念|基础理论与核心概念]]
- [[source-pages/de-gans-2024-eeg-wearables-systematic-review]]
