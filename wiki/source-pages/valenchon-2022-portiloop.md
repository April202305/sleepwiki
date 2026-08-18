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
- ⚠️其核心验证是检测技术案例，并非人体睡眠刺激疗效试验；不能替代居家闭环干预验证。 （PDF 第 1 页）

## 关联词条
- 设备：[[device/Portiloop]]
- 概念：[[concept/睡眠纺锤波]]
- 综述：[[review/chapters/01-引言]]、[[review/01-引言-1.2-文献需求单]]、[[review/01-引言-1.2-P1-证据包]]、[[review/01-引言-1.3-文献需求单]]、[[review/证据矩阵]]

## ⚠️局限与待核实
- ⚠️需在阶段 3 核对其报告的具体检测阈值、端到端延迟和刺激执行条件。

## 来源
- `raw/inbox/valenchon-2022-portiloop.pdf`
