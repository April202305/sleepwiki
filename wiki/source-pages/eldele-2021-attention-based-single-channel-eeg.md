---
type: source
aliases: ["Eldele 2021", "AttnSleep paper"]
created: 2026-08-11
updated: 2026-08-18
sources: ["raw/inbox/Eldele 等 - 2021 - An Attention-Based Deep Learning Approach for Sleep Stage Classification With Single-Channel EEG.pdf"]
status: active
review_due: 2027-08-11
---

# Eldele 等（2021）：AttnSleep 单通道 EEG 睡眠分期

## 基本信息
- 类型：论文
- 原始文件：`raw/inbox/Eldele 等 - 2021 - An Attention-Based Deep Learning Approach for Sleep Stage Classification With Single-Channel EEG.pdf`
- source_id：`raw/inbox/Eldele 等 - 2021 - An Attention-Based Deep Learning Approach for Sleep Stage Classification With Single-Channel EEG.pdf`
- 作者/机构：Emadeldeen Eldele 等
- 年份：2021
- 英文原题：An Attention-Based Deep Learning Approach for Sleep Stage Classification With Single-Channel EEG
- DOI：10.1109/TNSRE.2021.3076234
- 录入日期：2026-08-11

## 核心摘要

论文提出 [[model/AttnSleep|AttnSleep]]：以多分辨率 CNN、特征重校准和带因果卷积的多头注意力建模单通道 EEG 的时序依赖，并以类别感知损失应对类别不平衡。[[concept/单通道 EEG]]、[[concept/时序上下文]] 与 [[concept/类别不平衡]] 是其关键设计动机。（PDF 第 1–2 页）

## 方法与发现

- 模型由 MRCNN、AFR 与 TCE 组成；TCE 以多头注意力和因果卷积捕捉时间依赖。（PDF 第 1–3 页）
- 在 [[dataset/Sleep-EDF|Sleep-EDF-20]]、[[dataset/Sleep-EDF|Sleep-EDF-78]] 和 [[dataset/SHHS|SHHS]] 上使用单 EEG 通道评估；Sleep-EDF 使用 Fpz-Cz，SHHS 使用 C4-A1。（PDF 第 4 页，Table I）
- 预处理包括剔除 UNKNOWN、合并 N3/N4 为 N3、仅保留睡眠前后各 30 分钟清醒期。（PDF 第 4 页）
- 指标包括准确率、macro-F1、Cohen's κ 和 macro G-mean；论文将 macro-F1 与 macro G-mean 用于处理不平衡数据的评估。（PDF 第 4 页，式 13–15）

## 关联词条
- 模型：[[model/AttnSleep|AttnSleep]]
- 数据集：[[dataset/Sleep-EDF|Sleep-EDF]]、[[dataset/SHHS|SHHS]]
- 概念：[[concept/睡眠分期]]、[[concept/单通道 EEG]]、[[concept/时序上下文]]、[[concept/类别不平衡]]

## 局限与待核实
- ⚠️ PDF 文本抽取未保留 Table V 的完整数值；如需跨模型精确指标比较，应直接核对原始 PDF 表格。

## 来源
- `raw/inbox/Eldele 等 - 2021 - An Attention-Based Deep Learning Approach for Sleep Stage Classification With Single-Channel EEG.pdf`

## 综述关联
- [[review/证据矩阵|证据矩阵]]
- [[review/完整综述大纲]]
