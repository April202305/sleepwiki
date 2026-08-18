---
type: concept
aliases: ["wearable EEG", "mobile EEG", "EEG-based wearable"]
created: 2026-08-12
updated: 2026-08-17
sources: ["[[source-pages/phan-mikkelsen-2022-automatic-sleep-staging]]", "[[source-pages/de-gans-2024-eeg-wearables-systematic-review]]", "[[source-pages/ferster-2022-real-time-phase-algorithms]]"]
review_sections: ["1", "2", "3", "6", "7", "8"]
status: active
review_due: 2027-08-12
---

# 可穿戴 EEG

## 定义

用于非传统 PSG 场景、可自主佩戴或较少侵入地记录 EEG 的设备与系统；可包括头带、眼罩、单通道 EEG、贴片和耳内 EEG 等形态。de Gans 等系统综述纳入 60 篇论文、覆盖 34 种独特 EEG 可穿戴设备，以 Dreem 头带（多数测试伪影低于 20%）和耳内 EEG 等为常见形态，但该伪影率并非所有可穿戴 EEG 的普遍表现。[[source-pages/de-gans-2024-eeg-wearables-systematic-review|de Gans 等（2024）]]（PDF 第 1、8–9 页）

## 在睡眠分期中的作用

它支持长期与家庭环境 [[concept/睡眠分期]]，但与 PSG 相比常受较低信噪比、信息维度减少和每日佩戴差异影响。[[source-pages/phan-mikkelsen-2022-automatic-sleep-staging|Phan 和 Mikkelsen（2022）]]（PDF 第 9–10 页）

## 方法、参数或判定标准

相对 [[concept/PSG 参考标准]] 的验证需注明设备形态、电极类型、通道/导联、同步、自动或人工评分、人群与场景。指标异质时不可直接比较。[[source-pages/de-gans-2024-eeg-wearables-systematic-review|de Gans 等（2024）]]（PDF 第 9–10 页）

## 相关模型与数据集
- [[model/AttnSleep]]、[[model/SingleChannelNet]]
- [[dataset/Sleep-EDF]]、[[dataset/SHHS]]

## ⚠️争议与待核实

- ⚠️ 可穿戴 EEG 的分期表现不等于其可替代 PSG，也不等于可用于实时 [[concept/临床验证|闭环临床验证]]。
- ⚠️ 干/湿电极、单/双通道、具体导联与接触质量必须由原始设备研究单独记录；两篇综述不足以作统一结论。
- ⚠️Ferster 等的 Fpz–M2 单导联系统可支持特定实时相位算法基准，但不能由此推断所有可穿戴 EEG 均具备相同触发精度或闭环能力。[[source-pages/ferster-2022-real-time-phase-algorithms]]（PDF 第 2、7 页）

## 来源
- [[source-pages/phan-mikkelsen-2022-automatic-sleep-staging|Phan 和 Mikkelsen（2022）]]
- [[source-pages/de-gans-2024-eeg-wearables-systematic-review|de Gans 等（2024）]]
- [[source-pages/ferster-2022-real-time-phase-algorithms|Ferster 等（2022）]]

## 综述关联
- [[review/chapters/02-基础理论与核心概念]]、[[review/chapters/03-可穿戴睡眠信号采集硬件体系]]、[[review/chapters/06-现有研究对比]]
- [[review/文献搜索策略_新版]]
- [[concept/模型压缩与端侧部署]]
- [[concept/实时相位估计]]
