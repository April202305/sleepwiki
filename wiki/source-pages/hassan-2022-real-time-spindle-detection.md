---
type: source
aliases: ["Hassan 2022 RTSD"]
created: 2026-08-18
updated: 2026-08-18
sources: []
review_sections: ["2.2", "2.3", "4.2"]
status: active
review_due: 2027-08-18
---

# Hassan 等（2022）：脑状态依赖刺激的实时纺锤波检测

## 基本信息
- 类型：预印本；预录 EEG 实时回放验证
- 原始文件：`raw/inbox/hassan-2022-real-time-spindle-detection.pdf`
- source_id：`raw/inbox/hassan-2022-real-time-spindle-detection.pdf`
- 作者/机构：Umair Hassan、Gordon B. Feld、Til O. Bergmann
- 年份：2022
- 英文原题：Automated real-time EEG sleep spindle detection for brain state-dependent brain stimulation
- DOI：预印本 10.1101/2022.06.05.494865；出版社版 10.1111/jsr.13733
- 录入日期：2026-08-18
- review_sections：["2.2", "2.3", "4.2"]

## 核心摘要
[[model/RTSD]] 在专用 Simulink Real-Time 系统上流式回放预录睡眠 EEG，验证多通道纺锤波检测和相位触发。两个数据集分别含 20 名午睡与 10 名整夜记录受试者；相对三种离线算法总体约有 83% sensitivity、78% precision 和 0.81 F1。[[source-pages/hassan-2022-real-time-spindle-detection|本来源]]（PDF 第 1、6–10 页，Figure 4）

## 方法与发现
- 系统每 10 ms 分析最近 520 ms 数据；硬件与接口软件造成约 5–15 ms 延迟。相位模块使用 256 ms 窗口、65 ms 前向预测，并补偿固定软硬件偏移。[[source-pages/hassan-2022-real-time-spindle-detection|本来源]]（PDF 第 5–6 页）
- 验证是预录数据实时流送，不是睡眠中实际刺激；离线算法被当作参考，并非统一人工事件真值。[[source-pages/hassan-2022-real-time-spindle-detection|本来源]]（PDF 第 1、8–12 页）

## 关联词条
- 模型：[[model/RTSD]]
- 概念：[[concept/睡眠纺锤波]]、[[concept/闭环系统时延]]
- 综述：[[review/02-技术基础-2.3-文献需求单]]、[[review/02-技术基础-2.3-P1-证据包]]、[[review/证据矩阵]]

## 局限与待核实
- ⚠️5–15 ms 仅为硬件/接口延迟，不是含刺激执行的总时延。
- ⚠️预印本页码与出版社版不同；正文引用必须注明版本。

## 新增综述需求入口

- [[review/04-全周期-4.2-文献需求单]]

## 来源
- `raw/inbox/hassan-2022-real-time-spindle-detection.pdf`
