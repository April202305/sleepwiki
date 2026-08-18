---
type: source
aliases: ["Zhou 2022", "SCNet paper"]
created: 2026-08-11
updated: 2026-08-18
sources: ["raw/inbox/Zhou 等 - 2022 - SingleChannelNet A model for automatic sleep stage classification with raw single-channel EEG.pdf"]
status: active
review_due: 2027-08-11
---

# Zhou 等（2022）：SingleChannelNet 单通道 EEG 睡眠分期

## 基本信息
- 类型：论文
- 原始文件：`raw/inbox/Zhou 等 - 2022 - SingleChannelNet A model for automatic sleep stage classification with raw single-channel EEG.pdf`
- source_id：`raw/inbox/Zhou 等 - 2022 - SingleChannelNet A model for automatic sleep stage classification with raw single-channel EEG.pdf`
- 作者/机构：Dongdong Zhou 等
- 年份：2022
- 英文原题：SingleChannelNet: A model for automatic sleep stage classification with raw single-channel EEG
- DOI：10.1016/j.bspc.2022.103592
- 录入日期：2026-08-11

## 核心摘要

论文提出 [[model/SingleChannelNet|SingleChannelNet（SCNet）]]，以原始 [[concept/单通道 EEG]] 的 90 秒上下文输入进行端到端五分类，在 [[dataset/CCSHS|CCSHS]]、[[dataset/Sleep-EDF|Sleep-EDF]] 及其 20 人子集上评估。（PDF 第 1 页摘要、第 2–3 页）

## 方法与发现

- SCNet 为深层 CNN；采用多尺度卷积块和 M-Apooling，输入尺寸为 `(90 × fs, 1)`，可适配不同采样率。（PDF 第 3–4 页，Table 2）
- 在 CCSHS 的 epoch-wise 5 折交叉验证中，准确率为 90.2%、κ 为 86.5%；N1 的召回率为 33.0%。（PDF 第 5 页，Table 3）
- 在 Sleep-EDF 的 epoch-wise 5 折交叉验证中，准确率为 86.1%、κ 为 80.5%；N1 的 F1 为 52.1%。（PDF 第 5 页，Table 4）
- 相较 30 秒输入，90 秒上下文输入的准确率在 CCSHS 与 Sleep-EDF 分别高 1.1 和 4.1 个百分点；κ 分别高 1.5 和 5.7 个百分点。（PDF 第 5–6 页，Tables 3–6）
- 跨数据集直接测试时，CCSHS 训练→Sleep-EDF 测试准确率为 65.9%；反向为 70.2%，表明跨数据集泛化仍有明显下降。（PDF 第 6 页）

## 关联词条
- 模型：[[model/SingleChannelNet|SingleChannelNet]]
- 数据集：[[dataset/CCSHS|CCSHS]]、[[dataset/Sleep-EDF|Sleep-EDF]]
- 概念：[[concept/睡眠分期]]、[[concept/单通道 EEG]]、[[concept/时序上下文]]、[[concept/类别不平衡]]、[[concept/跨数据集泛化]]

## 局限与待核实
- ⚠️ 两个数据集的通道、样本分布及划分方案不同；文内跨数据集结果不应与同数据集交叉验证结果直接等同。

## 来源
- `raw/inbox/Zhou 等 - 2022 - SingleChannelNet A model for automatic sleep stage classification with raw single-channel EEG.pdf`

## 综述关联
- [[review/证据矩阵|证据矩阵]]
- [[review/完整综述大纲]]
