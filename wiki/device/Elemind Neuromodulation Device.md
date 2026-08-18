---
type: device
aliases: ["ENMod", "Elemind wearable EEG headband"]
created: 2026-08-18
updated: 2026-08-18
sources: ["[[source-pages/bressler-2023-wearable-eeg-closed-loop]]"]
review_sections: ["1.3", "2.1", "2.2", "4.1", "5.1"]
status: active
review_due: 2027-08-18
---

# Elemind Neuromodulation Device

## 基本信息

- 设备类型：头带式可穿戴 EEG 与骨传导声音刺激原型
- 生理模态：EEG
- EEG 形态：柔性干电极
- 通道与导联：Fp1、Fpz、Fp2；耳上联接参考、Fpz 邻近地电极
- 采样与佩戴信息：EEG 250 Hz；70 × 45 × 20 mm，43.9 g；基于 Muse S Gen 2 织物头带。[[source-pages/bressler-2023-wearable-eeg-closed-loop]]（PDF 第 4 页）

## 信号质量与噪声

- 以 5 秒 RMS 窗口选择最高质量通道；当前通道低于 2 µV RMS 时比较另两通道。[[source-pages/bressler-2023-wearable-eeg-closed-loop]]（PDF 第 4 页）
- 原型没有阻抗测量，用户用眨眼检测和 RMS 指示检查接触质量；约 30% 居家数据集因接触或电极材料问题没有可用 EEG。[[source-pages/bressler-2023-wearable-eeg-closed-loop]]（PDF 第 5、13–14 页）

## 可用于的睡眠任务

- 在熄灯后首 30 分钟，以 ecHT 跟踪 α 相位，并通过 22 kHz 骨传导驱动器输出锁相粉噪。[[source-pages/bressler-2023-wearable-eeg-closed-loop]]（PDF 第 4–6 页）

## 性能与比较条件

- 居家全体可评分样本的 N2 入睡潜伏期在无声音、α 峰和 α 谷条件间无显著差异（n=24，p=0.3756）。[[source-pages/bressler-2023-wearable-eeg-closed-loop]]（PDF 第 12 页）
- ⚠️不能与 [[device/Wireless Dreem Device]] 或 [[device/Portiloop]] 排名比较：目标阶段、导联、刺激、样本、终点与运行条件不同。

## 关联来源

- [[source-pages/bressler-2023-wearable-eeg-closed-loop]]
- [[concept/可穿戴 EEG]]、[[concept/实时相位估计]]、[[concept/闭环控制]]
- [[intervention/闭环听觉刺激]]

## ⚠️局限与待核实

- ⚠️2.5 Hz 高通抑制低频电子噪声，同时限制慢波活动检测；电池与存储限制使研究不能分析熄灯后两小时以外的睡眠结构。[[source-pages/bressler-2023-wearable-eeg-closed-loop]]（PDF 第 14 页）
- ⚠️P1 的 62 ms 是实验室 ERP 潜伏期，不能当作设备端到端时延。

## 来源

- [[source-pages/bressler-2023-wearable-eeg-closed-loop]]
