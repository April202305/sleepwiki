---
type: source
aliases: ["Ferster 2022", "SleepLoop phase vocoder", "arXiv:2203.02354"]
created: 2026-08-17
updated: 2026-08-18
sources: ["raw/inbox/ferster-2022-benchmarking-real-time-algorithms.pdf"]
review_sections: ["1.2", "2.2", "2.3", "3.1", "6.3"]
status: active
review_due: 2027-08-17
---

# Ferster 等（2022）：可穿戴 EEG 低振幅慢波的实时相位刺激算法基准

## 基本信息

- 类型：实时算法基准研究；绿色开放获取预印本
- 原始文件：`raw/inbox/ferster-2022-benchmarking-real-time-algorithms.pdf`
- source_id：`raw/inbox/ferster-2022-benchmarking-real-time-algorithms.pdf`
- 作者/年份：Maria Laura Ferster 等；2022
- 英文原题：Benchmarking real-time algorithms for in-phase auditory stimulation of low amplitude slow waves with wearable EEG devices during sleep
- DOI：10.1109/TBME.2022.3157468
- 预印本：arXiv:2203.02354v1
- review_sections：["1.2", "2.2", "2.3", "3.1", "6.3"]

## 核心摘要

该研究在 324 段健康老年人与帕金森病患者记录上比较振幅阈值（AT）、相位锁定环（PLL）和相位声码器（PV）三种可穿戴 EEG 实时慢波相位算法；三者均有超过 70% 的触发落在目标慢波上升相，PV 对低振幅慢波与高于 1 Hz 的慢波具有更高靶向能力。[[concept/实时相位估计]]（PDF 第 1、7 页）

## 方法与发现

- 系统用单导联 Fpz–M2 EEG；决策逻辑同时要求 NREM、慢波活动、低 beta 功率及目标相位条件，以降低浅睡眠、觉醒和伪影情境下的非期望触发。[[concept/实时相位估计]]（PDF 第 2 页）
- 离线 Hilbert 变换需要事件前后数据，不能直接作为实时系统的因果相位估计；实时滤波也可能引入相位延迟。[[concept/实时相位估计]]（PDF 第 1 页）
- PV 对 20–60 μV 低振幅慢波的靶向能力为 74.2%，而 AT 为 32.3%；不同算法、指标与目标条件须保持原文比较范围。[[concept/实时相位估计]]（PDF 第 7 页，Table II）
- 硬件仿真中 PLL/PV 的相对计算资源消耗为 0.02/0.06，估计效率为 98%/94%；在一个帕金森病患者的前瞻性夜间记录中，ON 条件的已检测 NREM 慢波频段功率增加。[[concept/实时相位估计]]（PDF 第 7–8 页）
- ⚠️预印本的基准样本限于帕金森病与健康老年人；人体前瞻性验证仅为 1 名帕金森病患者，不能泛化为临床疗效或所有人群。[[concept/实时相位估计]]（PDF 第 8–9 页）

## 关联词条

- 概念：[[concept/实时相位估计]]、[[concept/可穿戴 EEG]]
- 干预：[[intervention/闭环听觉刺激]]
- 综述：[[review/chapters/01-引言]]、[[review/01-引言-1.2-文献需求单]]、[[review/01-引言-1.2-P1-证据包]]、[[review/01-引言-1.3-文献需求单]]、[[review/01-引言-1.3-P1-证据包]]、[[review/02-技术基础-2.2-文献需求单]]、[[review/02-技术基础-2.2-P1-证据包]]、[[review/02-技术基础-2.3-文献需求单]]、[[review/03-慢波干预-3.1-文献需求单]]、[[review/03-慢波干预-3.1-P1-证据包]]、[[review/证据矩阵]]

## ⚠️局限与待核实

- ⚠️原文报告计算资源与效率，但未提供可直接与其他系统统一比较的“采集至刺激”的总时延；证据矩阵仍保留总时延 `待核实`。
- ⚠️录入文件是预印本，正式同行评审版本的版面页码和个别表述可能不同；正文引用时应注明该版本状态。

## 新增综述需求入口

- [[review/06-挑战展望-6.2-文献需求单]]
- [[review/06-挑战展望-6.3-文献需求单]]

## 来源

- `raw/inbox/ferster-2022-benchmarking-real-time-algorithms.pdf`
