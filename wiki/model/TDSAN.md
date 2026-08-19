---
type: model
aliases: ["Two-stage domain self-attention network"]
created: 2026-08-19
updated: 2026-08-19
sources: ["[[source-pages/gao-2023-domain-adversarial-staging]]"]
review_sections: ["2.2", "6.2"]
status: active
review_due: 2026-09-19
---

# TDSAN

## 基本信息
- 任务：跨数据集单通道EEG五分类
- 提出者/年份：Gao 等，2023
- 模型类别：域对抗网络与域自注意力

## 架构与输入输出
以来源域有标签epoch和目标域无标签epoch训练特征生成器、双分类器、域判别器与域注意力模块。[[source-pages/gao-2023-domain-adversarial-staging]]

## 训练与实验设置
- 数据集：Sleep-EDF-SC、Sleep-EDF-ST、自采数据
- 指标：accuracy、macro-F1

## 主要结果
在六个跨域方向与多种UDA基线比较，支持域适应可用于跨数据库分期。[[source-pages/gao-2023-domain-adversarial-staging]]

## 优点与局限
直接处理域偏移；目标域数据参与无监督训练，不等同于零接触外部验证，且为离线模型。

## 关联概念与来源
- 概念：[[concept/领域自适应]]、[[concept/跨数据集泛化]]
- 来源：[[source-pages/gao-2023-domain-adversarial-staging]]

## ⚠️待核实
- 跨设备而非跨数据库时的独立表现。

## 来源
- [[source-pages/gao-2023-domain-adversarial-staging]]
