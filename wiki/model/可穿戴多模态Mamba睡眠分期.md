---
type: model
aliases: ["Wearable multimodal Mamba sleep staging"]
created: 2026-08-19
updated: 2026-08-19
sources: ["source-pages/zhang-2026-mamba-wearable-staging"]
review_sections: ["2.2", "6.2"]
status: active
review_due: 2027-08-19
---

# 可穿戴多模态 Mamba 睡眠分期

## 基本信息
- 任务：[[concept/睡眠分期]]
- 提出者/年份：Zhang 等，2026
- 模型类别：双向 Mamba 多模态序列模型

## 架构与输入输出

输入 ANNE One 的 ECG、PPG、加速度及温度，经三层双向 Mamba block 输出三、四或五类睡眠阶段。[[source-pages/zhang-2026-mamba-wearable-staging]]（PDF 第 1、5–6 页）

## 训练与实验设置
- 357 名睡眠实验室成人，同步 PSG 人工标签。
- 五分类 balanced accuracy 65.11%、F1 66.15%、κ 53.23%。

## 优点与局限
- 使用真实无线可穿戴与临床多样人群。
- ⚠️ 不含 EEG，且为双向模型；不能证明 EEG 因果闭环适用性。

## 来源
- [[source-pages/zhang-2026-mamba-wearable-staging]]
