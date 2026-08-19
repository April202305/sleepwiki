---
type: model
aliases: ["SeqConfidNet-DCR"]
created: 2026-08-19
updated: 2026-08-19
sources: ["[[source-pages/hong-2021-confidence-based-scoring]]"]
review_sections: ["2.2", "6.2"]
status: active
review_due: 2026-09-19
---

# Hong 置信度选择性睡眠分期框架

## 基本信息
- 任务：EEG五分类、错误预测筛选与人工复核
- 提出者/年份：Hong 等，2021
- 模型类别：TinySleepNet分类器 + 置信度模型

## 架构与输入输出
分类器输出阶段，平行置信度模型输出0–1置信度；低于阈值的epoch拒绝并交由人工复核。[[source-pages/hong-2021-confidence-based-scoring]]

## 训练与实验设置
- 数据集：SNUBH、[[dataset/SHHS]]
- 指标：accuracy、错误检测、按复核比例的选择性性能

## 主要结果
复核最低置信度20%的epoch时，总体accuracy约由76%升至87%。[[source-pages/hong-2021-confidence-based-scoring]]

## 优点与局限
提供明确拒绝与复核流程；不是ECE/Brier意义上的概率校准，收益依赖人工纠正。

## 关联概念与来源
- 概念：[[concept/不确定性与拒绝输出]]
- 来源：[[source-pages/hong-2021-confidence-based-scoring]]

## ⚠️待核实
- 在线部署覆盖率—风险曲线与端到端时延。

## 来源
- [[source-pages/hong-2021-confidence-based-scoring]]
