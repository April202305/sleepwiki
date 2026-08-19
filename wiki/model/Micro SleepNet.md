---
type: model
aliases: ["MicroSleepNet"]
created: 2026-08-19
updated: 2026-08-19
sources: ["[[source-pages/liu-2023-micro-sleepnet]]"]
review_sections: ["2.2", "2.3", "6.2"]
status: active
review_due: 2026-09-19
---

# Micro SleepNet

## 基本信息
- 任务：单通道EEG五分类与手机端推理
- 提出者/年份：Liu 等，2023
- 模型类别：轻量CNN

## 架构与输入输出
单个30 s epoch经组卷积、通道重排、ECSA注意力重校准和膨胀卷积输出阶段。[[source-pages/liu-2023-micro-sleepnet]]

## 训练与实验设置
- 数据集：[[dataset/Sleep-EDF]]、[[dataset/SHHS]]
- 指标：accuracy、macro-F1、κ、逐类F1、参数量、FLOPs和手机推理时间

## 主要结果
Android手机约100 KB内存占用、单条输入推理约2.8 ms。[[source-pages/liu-2023-micro-sleepnet]]

## 优点与局限
无需双向时序结构且有手机实测；推理时间不等于端到端闭环时延，功耗和整夜在线运行未完整报告。

## 关联概念与来源
- 概念：[[concept/模型压缩与端侧部署]]、[[concept/闭环系统时延]]
- 来源：[[source-pages/liu-2023-micro-sleepnet]]

## ⚠️待核实
- 峰值内存、时延抖动、功耗与整夜续航。

## 来源
- [[source-pages/liu-2023-micro-sleepnet]]
