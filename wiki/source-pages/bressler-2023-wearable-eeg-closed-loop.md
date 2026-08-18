---
type: source
aliases: ["Bressler 2023", "ENMod wearable EEG"]
created: 2026-08-18
updated: 2026-08-18
sources: ["raw/inbox/bressler-2023-wearable-eeg-closed-loop.pdf"]
review_sections: ["1.3", "2.1", "2.2", "2.3", "4.1", "5.1"]
status: active
review_due: 2027-08-18
---

# Bressler 等（2023）：可穿戴 EEG 的睡眠相关振荡闭环神经调控系统

## 基本信息

- 类型：可穿戴 EEG 闭环系统人体可行性研究
- 原始文件：`raw/inbox/bressler-2023-wearable-eeg-closed-loop.pdf`
- source_id：`raw/inbox/bressler-2023-wearable-eeg-closed-loop.pdf`
- 作者/年份：Scott Bressler、Ryan Neely、Ryan M. Yost、David Wang、Heather L. Read；2023
- 英文原题：A wearable EEG system for closed-loop neuromodulation of sleep-related oscillations
- DOI：10.1088/1741-2552/acfb3b
- review_sections：["1.3", "2.1", "2.2", "2.3", "4.1", "5.1"]

## 核心摘要

该研究在 [[device/Elemind Neuromodulation Device]] 上实现端侧 endpoint-corrected Hilbert transform（ecHT），以额区干电极 EEG 的 α 相位在入睡前触发骨传导粉噪。其直接支持“可穿戴感知—因果相位估计—刺激执行”可在居家运行；不支持全夜睡眠结构、长期安全性或临床疗效结论。[[device/Elemind Neuromodulation Device]]（PDF 第 4–5、13–15 页）

## 方法与发现

- ENMod 原型使用 Muse S Gen 2 头带的 Fp1、Fpz、Fp2 三个柔性干电极、耳上联接参考和骨传导驱动器；EEG 采样率为 250 Hz，设备以 5 秒 RMS 窗口选择当前质量最高通道用于相位估计。[[device/Elemind Neuromodulation Device]]（PDF 第 4–5 页）
- ecHT 以 128 点、逐样本滑动窗估计相位；研究用 21 名实验室参与者测得群体平均听觉 ERP P1 潜伏期为 62 ms，并用此值设定居家刺激起始相位。[[concept/实时相位估计]]（PDF 第 3–4 页）
- 居家可行性研究将声音限于熄灯后首个 30 分钟、瞄准约 10 Hz α 振荡峰或谷；对可评分数据的全体参与者（n=24），三种条件的 N2 入睡潜伏期差异不显著（ANOVA p=0.3756）。[[intervention/闭环听觉刺激]]（PDF 第 11–13 页）
- ⚠️作者报告约 30% 居家数据集没有可用 EEG，主要归因于电极—头皮接触差或电极材料退化；原型不能测量阻抗，且其 2.5 Hz 高通设置限制慢波检测。[[device/Elemind Neuromodulation Device]]（PDF 第 13–14 页）
- ⚠️客观入睡潜伏期较长的探索性子组仅 n=7；该子组的差异不能替代全体样本的阴性主要结果，也不能作为失眠治疗证据。[[intervention/闭环听觉刺激]]（PDF 第 12、15 页）

## 关联词条

- 设备：[[device/Elemind Neuromodulation Device]]
- 概念：[[concept/可穿戴 EEG]]、[[concept/实时相位估计]]、[[concept/闭环控制]]
- 干预：[[intervention/闭环听觉刺激]]
- 综述：[[review/chapters/01-引言]]、[[review/01-引言-1.3-文献需求单]]、[[review/01-引言-1.3-P1-证据包]]、[[review/02-技术基础-2.1-文献需求单]]、[[review/02-技术基础-2.1-P1-证据包]]、[[review/02-技术基础-2.2-文献需求单]]、[[review/02-技术基础-2.2-P1-证据包]]、[[review/02-技术基础-2.3-文献需求单]]、[[review/证据矩阵]]

## 局限与待核实

- ⚠️未报告可与其他系统统一比较的端到端总时延；62 ms 为实验室测得的 ERP 潜伏期，不是完整系统时延。
- ⚠️仅在入睡前 α 振荡及短时刺激窗口中验证；不能外推至 N3 慢波、REM 或整夜闭环干预。

## 来源

- `raw/inbox/bressler-2023-wearable-eeg-closed-loop.pdf`
