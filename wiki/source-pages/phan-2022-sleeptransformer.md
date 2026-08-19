---
type: source
aliases: ["Phan 2022 SleepTransformer"]
created: 2026-08-19
updated: 2026-08-19
sources: []
review_sections: ["2.2"]
status: active
review_due: 2027-08-19
---

# SleepTransformer：可解释性与不确定性睡眠分期

## 基本信息
- 类型：论文（arXiv 预印本，注明已发表于 IEEE TBME）
- 原始文件：`raw/inbox/phan-2022-sleeptransformer.pdf`
- source_id：`raw/inbox/phan-2022-sleeptransformer.pdf`
- 作者/机构：Huy Phan、Kaare Mikkelsen、Oliver Y. Chén、Philipp Koch、Alfred Mertins、Maarten De Vos
- 年份：2022
- 英文原题：SleepTransformer: Automatic Sleep Staging with Interpretability and Uncertainty Quantification
- 录入日期：2026-08-19
- review_sections：["2.2"]

## 核心摘要

SleepTransformer 使用 epoch 级与序列级自注意力进行序列到序列评分，并以注意力和预测不确定性辅助解释。SHHS 与 Sleep-EDF-78 上分别报告约 84.9% 与 87.7% 总体准确率。[[source-pages/phan-2022-sleeptransformer]]（PDF 第 1、6–8 页）

## 方法与发现

- SHHS 包含 5,791 名对象；Sleep-EDF-78 采用被试级交叉验证。（PDF 第 2、5 页）
- 模型一次处理由多个 epoch 组成的完整序列，自注意力可访问序列内两侧上下文；论文没有验证严格因果流式配置。（PDF 第 3–6 页）
- 表中报告模型参数量和训练时间，但未提供可穿戴设备单窗推理时延、功耗或刺激链路。（PDF 第 9 页）

## 关联词条
- 模型：[[model/SleepTransformer]]
- 概念：[[concept/时序上下文]]、[[concept/模型压缩与端侧部署]]

## 局限与待核实
- ⚠️ 不确定性用于识别低置信度 epoch，不等同于经过验证的在线拒绝触发机制。

## 来源
- `raw/inbox/phan-2022-sleeptransformer.pdf`
