---
type: concept
aliases: ["wearable EEG", "mobile EEG", "EEG-based wearable"]
created: 2026-08-12
updated: 2026-08-19
sources: ["[[source-pages/phan-mikkelsen-2022-automatic-sleep-staging]]", "[[source-pages/de-gans-2024-eeg-wearables-systematic-review]]", "[[source-pages/ferster-2022-real-time-phase-algorithms]]", "[[source-pages/bressler-2023-wearable-eeg-closed-loop]]", "[[source-pages/mikkelsen-2019-ear-eeg-whole-night-sleep]]", "[[source-pages/pazuelo-2024-in-ear-signal-quality]]", "[[source-pages/mohamed-2023-wearable-eeg-review]]", "[[source-pages/mascia-2023-parylene-tattoo-eeg]]", "[[source-pages/tabar-2021-ear-eeg-sleep-assessment]]", "[[source-pages/shustak-2019-temporary-tattoo-sleep-monitoring]]", "[[source-pages/melo-2024-single-channel-eeg-actigraphy]]"]
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

耳内与贴附式系统进一步表明，质量控制需进入设备层：Mikkelsen 等报告耳内电极的连接丢失与湿气相关失败，Pazuelo 等以运动/面部伪影条件检验耳内—头皮信号相关；超薄纹身 EEG 目前只完成清醒态验证。[[source-pages/mikkelsen-2019-ear-eeg-whole-night-sleep]]（PDF 第 3–4 页）；[[source-pages/pazuelo-2024-in-ear-signal-quality]]（PDF 第 6–8 页）；[[source-pages/mascia-2023-parylene-tattoo-eeg]]（PDF 第 1、7–8 页）

新增直接证据显示，ear-EEG 的参考配置可使五分类 κ 从 0.36 变化至 0.72；临时纹身阵列可在小样本中同步采集 EEG/EOG/EMG；单通道头带加入体动后对总体 F1 增益较小，但可降低 N1 错误率。三类结果对应导联配置、多模态可行性和任务特异边际增益，不能合并为统一设备排名。[[source-pages/tabar-2021-ear-eeg-sleep-assessment]]（PDF 第 1、6–8 页）；[[source-pages/shustak-2019-temporary-tattoo-sleep-monitoring]]（PDF 第 2–7 页）；[[source-pages/melo-2024-single-channel-eeg-actigraphy]]（PDF 第 1、5–6 页）

## 相关模型与数据集
- [[model/AttnSleep]]、[[model/SingleChannelNet]]
- [[dataset/Sleep-EDF]]、[[dataset/SHHS]]

## ⚠️争议与待核实

- ⚠️ 可穿戴 EEG 的分期表现不等于其可替代 PSG，也不等于可用于实时 [[concept/临床验证|闭环临床验证]]。
- ⚠️ 干/湿电极、单/双通道、具体导联与接触质量必须由原始设备研究单独记录；两篇综述不足以作统一结论。
- ⚠️Ferster 等的 Fpz–M2 单导联系统可支持特定实时相位算法基准，但不能由此推断所有可穿戴 EEG 均具备相同触发精度或闭环能力。[[source-pages/ferster-2022-real-time-phase-algorithms]]（PDF 第 2、7 页）
- ⚠️Bressler 等的三额区干电极原型在居家研究中约 30% 数据集没有可用 EEG，且未测量电极阻抗；这提示接触质量会直接限制闭环运行，不能由少数可评分记录概括所有可穿戴设备。[[source-pages/bressler-2023-wearable-eeg-closed-loop]]（PDF 第 5、13–14 页）
- ⚠️Mikkelsen 等的干接触耳内 EEG、Pazuelo 等的 Naox 设备和 Bressler 等的额区头带在人群、导联、参考标准、质量指标和任务上不同；不能以 κ、相关性、可用数据比例或主观舒适性构建统一性能排行。[[source-pages/mikkelsen-2019-ear-eeg-whole-night-sleep]]（PDF 第 1、3–7 页）；[[source-pages/pazuelo-2024-in-ear-signal-quality]]（PDF 第 1、9–12 页）

## 来源
- [[source-pages/phan-mikkelsen-2022-automatic-sleep-staging|Phan 和 Mikkelsen（2022）]]
- [[source-pages/de-gans-2024-eeg-wearables-systematic-review|de Gans 等（2024）]]
- [[source-pages/ferster-2022-real-time-phase-algorithms|Ferster 等（2022）]]
- [[source-pages/bressler-2023-wearable-eeg-closed-loop|Bressler 等（2023）]]
- [[source-pages/mikkelsen-2019-ear-eeg-whole-night-sleep|Mikkelsen 等（2019）]]
- [[source-pages/pazuelo-2024-in-ear-signal-quality|Pazuelo 等（2024）]]
- [[source-pages/mohamed-2023-wearable-eeg-review|Mohamed 等（2023）]]
- [[source-pages/mascia-2023-parylene-tattoo-eeg|Mascia 等（2023）]]
- [[source-pages/tabar-2021-ear-eeg-sleep-assessment|Tabar 等（2021）]]
- [[source-pages/shustak-2019-temporary-tattoo-sleep-monitoring|Shustak 等（2019）]]
- [[source-pages/melo-2024-single-channel-eeg-actigraphy|Melo 等（2024）]]

## 综述关联
- [[review/chapters/02-基础理论与核心概念]]、[[review/chapters/03-可穿戴睡眠信号采集硬件体系]]、[[review/chapters/06-现有研究对比]]
- [[review/文献搜索策略_新版]]
- [[concept/模型压缩与端侧部署]]
- [[concept/实时相位估计]]
- [[concept/闭环控制]]
- [[device/Elemind Neuromodulation Device]]
- [[device/干接触耳内 EEG 系统]]、[[device/Naox 耳内 EEG 设备]]、[[device/Parylene C 纹身 EEG 系统]]
- [[device/临时纹身多模态睡眠电极阵列]]、[[concept/多模态融合]]
- [[concept/耳内 EEG]]、[[concept/柔性贴附电极]]
- [[concept/可穿戴人工智能]]
