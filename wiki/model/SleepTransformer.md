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

# SleepTransformer

## 基本信息
- 任务：[[concept/睡眠分期]]
- 提出者/年份：Phan 等，2021（依综述表）
- 模型类别：Transformer epoch 编码 + Transformer 序列编码

## 架构与输入输出

Phan 和 Mikkelsen 将其列为时频输入，使用 Transformer 对 epoch 与跨 epoch 序列编码。[[source-pages/phan-mikkelsen-2022-automatic-sleep-staging|Phan 和 Mikkelsen（2022）]]（PDF 第 6–7 页，Table 1）

## 训练与实验设置
- 数据集：[[dataset/Sleep-EDF]]、[[dataset/SHHS]]、[[dataset/MESA]]
- 指标：κ、macro-F1 或准确率；须按具体原始实验核验。

## 主要结果

该模型可作为 Transformer 路线的例子，但不同通道与设置之间的综述表数值不得作为统一排名。[[source-pages/phan-mikkelsen-2022-automatic-sleep-staging|Phan 和 Mikkelsen（2022）]]（PDF 第 6–7 页）

## 优点与局限
- 代表非递归注意力式 [[concept/时序上下文]] 建模。
- ⚠️ 当前资料没有直接提供可穿戴端推理时延、能耗或闭环触发性能。

## 来源
- [[source-pages/phan-mikkelsen-2022-automatic-sleep-staging|Phan 和 Mikkelsen（2022）]]

## 综述关联
- [[review/chapters/04-多模态睡眠检测算法]]
- [[concept/领域自适应]]、[[concept/模型压缩与端侧部署]]
- [[review/完整综述大纲]]
