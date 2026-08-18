---
type: source
aliases: ["Valenchon 2022", "Portiloop paper"]
created: 2026-08-17
updated: 2026-08-18
sources: ["raw/inbox/valenchon-2022-portiloop.pdf"]
review_sections: ["1.2", "2.2", "2.3"]
status: active
review_due: 2027-08-17
---

# Valenchon 等（2022）：Portiloop 开源实时闭环刺激工具

## 基本信息
- 类型：开源硬件/软件系统与实时事件检测验证
- 原始文件：`raw/inbox/valenchon-2022-portiloop.pdf`
- source_id：`raw/inbox/valenchon-2022-portiloop.pdf`
- DOI：10.1371/journal.pone.0270696
- 英文原题：The Portiloop: A deep learning-based open science tool for closed-loop brain stimulation
- review_sections：["1.2", "2.2", "2.3"]

## 核心摘要
[[device/Portiloop]] 将 EEG 获取、神经事件实时识别和精确定时刺激整合为可携带、低成本的闭环系统；其案例为实时睡眠纺锤波检测，并在 MODA 数据集上与离线专家表现比较。 （PDF 第 1–2 页）

## 方法与发现
- 系统描述了轻量循环神经网络、端侧硬件和检测阈值/延迟的设计约束。 （PDF 第 1–3 页）
- 纺锤波配置中，FIR、ANN 前向计算与声音控制器分别为 40、20 和 4 ms，构成 64 ms 常数延迟；Table 2 另列约 250±100 ms 的可变检测延迟，总计约 314 ms。阈值 0.84 时，按刺激是否落在专家标注事件内计算的 precision 与 recall 均为 0.71。[[source-pages/valenchon-2022-portiloop|本来源]]（PDF 第 13–15 页，Table 2、Figure 6）
- ⚠️其核心验证是检测技术案例，并非人体睡眠刺激疗效试验；不能替代居家闭环干预验证。 （PDF 第 1 页）

## 关联词条
- 设备：[[device/Portiloop]]
- 概念：[[concept/睡眠纺锤波]]
- 综述：[[review/chapters/01-引言]]、[[review/01-引言-1.2-文献需求单]]、[[review/01-引言-1.2-P1-证据包]]、[[review/01-引言-1.3-文献需求单]]、[[review/01-引言-1.3-P1-证据包]]、[[review/02-技术基础-2.2-文献需求单]]、[[review/02-技术基础-2.2-P1-证据包]]、[[review/02-技术基础-2.3-文献需求单]]、[[review/02-技术基础-2.3-P1-证据包]]、[[review/证据矩阵]]

## ⚠️局限与待核实
- ⚠️该总值包含估计的可变检测延迟，且案例基于标注数据的工程验证；不得写成人体在线刺激疗效或其他事件/设备的通用时延。

## 新增综述需求入口

- [[review/04-全周期-4.2-文献需求单]]

## 来源
- `raw/inbox/valenchon-2022-portiloop.pdf`
