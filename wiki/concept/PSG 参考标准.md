---
type: concept
aliases: ["polysomnography reference standard", "PSG ground truth"]
created: 2026-08-12
updated: 2026-08-18
sources: ["[[source-pages/phan-mikkelsen-2022-automatic-sleep-staging]]", "[[source-pages/de-gans-2024-eeg-wearables-systematic-review]]", "[[source-pages/mikkelsen-2019-ear-eeg-whole-night-sleep]]", "[[source-pages/pazuelo-2024-in-ear-signal-quality]]", "[[source-pages/mohamed-2023-wearable-eeg-review]]"]
review_sections: ["2", "3", "6"]
status: active
review_due: 2027-08-12
---

# PSG 参考标准

## 定义

多导睡眠图（PSG）是睡眠阶段评估的参考标准；可穿戴 EEG 的验证通常将其与 PSG 的人工评分进行比较。[[source-pages/de-gans-2024-eeg-wearables-systematic-review|de Gans 等（2024）]]（PDF 第 1、9–10 页）

## 在睡眠分期中的作用

PSG 为 [[concept/可穿戴 EEG]] 和自动 [[concept/睡眠分期]] 提供标签/对照来源，但评分者经验与训练会导致人工评分变异。[[source-pages/de-gans-2024-eeg-wearables-systematic-review|de Gans 等（2024）]]（PDF 第 9–10 页）

## 方法、参数或判定标准

比较时应记录同步方式、人工或自动评分、标签体系、评分者、通道与导联；κ 在类别不平衡条件下可用于一致性评估，但仍需与其他条件一起解读。[[source-pages/de-gans-2024-eeg-wearables-systematic-review|de Gans 等（2024）]]（PDF 第 10 页）

耳内设备验证还应说明 PSG 是完整还是部分配置、同步方式及两者共同记录的时长；Mikkelsen 等用部分 PSG 与耳内 EEG 同步记录，Pazuelo 等在 8 名受试者、超过 70 小时 PSG 睡眠中比较耳内和头皮信号。[[source-pages/mikkelsen-2019-ear-eeg-whole-night-sleep]]（PDF 第 3、8–9 页）；[[source-pages/pazuelo-2024-in-ear-signal-quality]]（PDF 第 9–12 页）

## 相关模型与数据集
- [[model/AttnSleep]]、[[model/SingleChannelNet]]
- [[dataset/Sleep-EDF]]、[[dataset/SHHS]]、[[dataset/CCSHS]]

## ⚠️争议与待核实

- ⚠️ 相对 PSG 的分期一致性不是闭环触发正确性、生理效应或临床获益的替代指标。

## 来源
- [[source-pages/danker-hopfe-2009-rk-aasm-reliability]]
- [[source-pages/danker-hopfe-2004-eight-labs-reliability]]
- [[source-pages/berry-2015-aasm-v2-2-updates]]
- [[source-pages/van-gorp-2022-uncertainty-framework]]
- [[source-pages/phan-mikkelsen-2022-automatic-sleep-staging|Phan 和 Mikkelsen（2022）]]
- [[source-pages/de-gans-2024-eeg-wearables-systematic-review|de Gans 等（2024）]]
- [[source-pages/mikkelsen-2019-ear-eeg-whole-night-sleep|Mikkelsen 等（2019）]]
- [[source-pages/pazuelo-2024-in-ear-signal-quality|Pazuelo 等（2024）]]
- [[source-pages/mohamed-2023-wearable-eeg-review|Mohamed 等（2023）]]

## 综述关联
- [[review/chapters/02-基础理论与核心概念]]、[[review/chapters/03-可穿戴睡眠信号采集硬件体系]]、[[review/chapters/06-现有研究对比]]
- [[concept/临床验证]]
- [[review/文献搜索策略_新版]]
- [[review/文献清单/02-技术基础-2.1-文献需求单]]
- [[concept/耳内 EEG]]
