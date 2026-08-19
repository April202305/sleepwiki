---
type: model
aliases: []
created: 2026-08-19
updated: 2026-08-19
sources: ["[[source-pages/nam-2024-insightsleepnet]]"]
review_sections: ["2.2", "6.2"]
status: active
review_due: 2026-09-19
---

# InsightSleepNet

## 基本信息
- 任务：PPG四分类、解释与拒绝输出
- 提出者/年份：Nam 等，2024
- 模型类别：因果TCN、局部注意力与能量分数选择性分类

## 架构与输入输出
连续PPG及此前7个epoch进入因果时序网络；能量分数超过阈值时拒绝输出。[[source-pages/nam-2024-insightsleepnet]]

## 训练与实验设置
- 数据集：[[dataset/MESA]]、CFS、CAP
- 指标：accuracy、weighted-F1、κ、拒绝率

## 主要结果
阈值拒绝降低覆盖率并提高保留样本性能。[[source-pages/nam-2024-insightsleepnet]]

## 优点与局限
明确实现选择性分类；输入为PPG，属于2.2邻近技术证据，不能替代EEG证据。

## 关联概念与来源
- 概念：[[concept/不确定性与拒绝输出]]、[[concept/时序上下文]]
- 来源：[[source-pages/nam-2024-insightsleepnet]]

## ⚠️待核实
- 概率校准指标未报告。

## 来源
- [[source-pages/nam-2024-insightsleepnet]]
