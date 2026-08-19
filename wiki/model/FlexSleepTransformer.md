---
type: model
aliases: []
created: 2026-08-19
updated: 2026-08-19
sources: ["source-pages/guo-2024-flexsleeptransformer"]
review_sections: ["2.2", "6.2"]
status: active
review_due: 2027-08-19
---

# FlexSleepTransformer

## 基本信息
- 任务：[[concept/睡眠分期]]
- 提出者/年份：Guo 等，2024
- 模型类别：灵活通道 Transformer

## 架构与输入输出

通过多通道拼接或随机融合处理不同 PSG 通道组合，并在统一 Transformer 中输出五阶段序列。[[source-pages/guo-2024-flexsleeptransformer]]（PDF 第 3–6 页）

## 训练与实验设置
- 数据集：[[dataset/Sleep-EDF]]、SleepUHS
- 被试级十折验证；包含单数据集和混合数据训练。

## 主要结果

混合训练达到各数据集专用模型准确率的约 98%，跨数据集测试优于仅在另一单一数据集训练的模型。[[source-pages/guo-2024-flexsleeptransformer]]（PDF 第 1、6–8 页）

## 优点与局限
- 支持变通道和多数据集训练。
- ⚠️ 未验证严格因果推理、可穿戴端时延或刺激触发安全。

## 来源
- [[source-pages/guo-2024-flexsleeptransformer]]
