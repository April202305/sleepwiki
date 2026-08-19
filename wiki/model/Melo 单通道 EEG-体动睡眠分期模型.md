---
type: model
aliases: ["Melo wearable sleep staging model"]
created: 2026-08-19
updated: 2026-08-19
sources: ["[[source-pages/melo-2024-single-channel-eeg-actigraphy]]"]
review_sections: ["2.1", "2.2"]
status: active
review_due: 2027-08-19
---

# Melo 单通道 EEG-体动睡眠分期模型

## 基本信息
- 任务：五分类睡眠分期
- 提出者/年份：Melo 等，2024
- 模型类别：18 个时域/频域特征 + bagged decision trees

## 架构与输入输出
- 输入为 30 秒单通道额区 EEG epoch，可选加入腕部活动记录 PIM 特征；输出五类睡眠阶段。[[source-pages/melo-2024-single-channel-eeg-actigraphy]]（PDF 第 3–4 页）

## 训练与实验设置
- 数据集：23 名健康参与者同步 I 型 PSG；两个不同头带组合。
- 指标：F1、逐期错误率等；5 折交叉验证及随机 80/20 epoch 划分。[[source-pages/melo-2024-single-channel-eeg-actigraphy]]（PDF 第 1、4 页）

## 主要结果
- 体动仅小幅提高总体 F1，但两种组合的 N1 错误率均下降。[[source-pages/melo-2024-single-channel-eeg-actigraphy]]（PDF 第 1、5–6 页，Table 3，Figure 1）

## 优点与局限
- 优点：同夜 PSG 参照，并比较两种单通道头带及有无体动特征。
- ⚠️小样本、健康人群和随机 epoch 划分限制跨受试者与临床泛化；不是在线闭环模型。

## 关联概念与来源
- 概念：[[concept/睡眠分期]]、[[concept/可穿戴 EEG]]、[[concept/多模态融合]]
- 来源：[[source-pages/melo-2024-single-channel-eeg-actigraphy]]

## ⚠️待核实
- 未报告采集至触发的端到端时延。

## 来源
- [[source-pages/melo-2024-single-channel-eeg-actigraphy]]
