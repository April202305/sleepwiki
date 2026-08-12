---
type: model
aliases: []
created: 2026-08-12
updated: 2026-08-12
sources: ["source-pages/phan-mikkelsen-2022-automatic-sleep-staging"]
review_sections: ["4"]
status: active
review_due: 2027-08-12
---

# DeepSleepNet

## 基本信息
- 任务：[[concept/睡眠分期]]
- 提出者/年份：Supratak 等，2017；端到端变体在后续 SeqSleepNet 工作中作为基线呈现。
- 模型类别：CNN + RNN 时序模型

## 架构与输入输出

Phan 和 Mikkelsen 将其归为以 CNN 做 epoch 编码、RNN 做序列编码的系统。[[source-pages/phan-mikkelsen-2022-automatic-sleep-staging|Phan 和 Mikkelsen（2022）]]（PDF 第 6–7 页，Table 1）

## 训练与实验设置
- 数据集：[[dataset/Sleep-EDF]]
- 指标：Cohen's κ、macro-F1 或准确率；必须按原始实验协议复核。

## 主要结果

综述 Table 1 汇总其在多个数据集上的结果，但不同通道、划分和迁移设置使跨研究直接比较无效。[[source-pages/phan-mikkelsen-2022-automatic-sleep-staging|Phan 和 Mikkelsen（2022）]]（PDF 第 6–7 页）

## 优点与局限
- 代表 CNN + RNN 从局部 epoch 到跨 epoch [[concept/时序上下文]] 建模的路线。
- ⚠️ 该页仅由综述支撑；精确架构与结果需回到原始论文核验。

## 来源
- [[source-pages/phan-mikkelsen-2022-automatic-sleep-staging|Phan 和 Mikkelsen（2022）]]

## 综述关联
- [[review/chapters/04-多模态睡眠检测算法]]
- [[concept/模型压缩与端侧部署]]
- [[review/完整综述大纲]]
