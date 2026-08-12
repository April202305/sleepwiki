---
type: model
aliases: ["Attention-Based Deep Learning Approach", "Eldele 2021 model"]
created: 2026-08-11
updated: 2026-08-11
sources: ["source-pages/eldele-2021-attention-based-single-channel-eeg"]
status: active
review_due: 2027-08-11
---

# AttnSleep

## 基本信息
- 任务：[[concept/睡眠分期]]五分类
- 提出者/年份：Eldele 等，2021
- 模型类别：注意力增强的 CNN 时序模型

## 架构与输入输出

以 [[concept/单通道 EEG]] 为输入，MRCNN 提取多频段特征，AFR 重校准特征依赖，TCE 用多头注意力和因果卷积编码 [[concept/时序上下文]]；另使用类别感知损失处理 [[concept/类别不平衡]]。[[source-pages/eldele-2021-attention-based-single-channel-eeg|Eldele 等（2021）]]（PDF 第 1–3 页）

## 训练与实验设置
- 数据集：[[dataset/Sleep-EDF|Sleep-EDF]]、[[dataset/SHHS|SHHS]]
- 指标：准确率、macro-F1、Cohen's κ、macro G-mean。[[source-pages/eldele-2021-attention-based-single-channel-eeg|Eldele 等（2021）]]（PDF 第 4 页，式 13–15）

## 主要结果

论文报告其模型在三项公开数据集上优于所比较方法；精确数值应直接复核论文 Table V。[[source-pages/eldele-2021-attention-based-single-channel-eeg|Eldele 等（2021）]]（PDF 第 5 页，Table V）

## 优点与局限

- 优点：并行注意力式时序建模，且显式考虑类别不平衡。[[source-pages/eldele-2021-attention-based-single-channel-eeg|Eldele 等（2021）]]（PDF 第 2–3 页）
- ⚠️ 不同数据集、通道和预处理下的结果不可直接横向比较。

## 来源
- [[source-pages/eldele-2021-attention-based-single-channel-eeg|Eldele 等（2021）]]

## 综述关联
- [[review/证据矩阵|证据矩阵]]
- [[review/chapters/04-多模态睡眠检测算法|多模态睡眠检测算法]]
- [[concept/PSG 参考标准]]、[[concept/临床验证]]、[[concept/可穿戴 EEG]]、[[concept/模型压缩与端侧部署]]
- [[review/完整综述大纲]]
