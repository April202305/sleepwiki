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

# SleepEEGNet

## 基本信息
- 任务：[[concept/睡眠分期]]
- 提出者/年份：综述表中列为 2019
- 模型类别：CNN + RNN 时序模型

## 架构与输入输出

Phan 和 Mikkelsen 的汇总表将其列为原始 EEG 输入、CNN epoch 编码与 RNN 序列编码。[[source-pages/phan-mikkelsen-2022-automatic-sleep-staging|Phan 和 Mikkelsen（2022）]]（PDF 第 6–7 页，Table 1）

## 训练与实验设置
- 数据集：[[dataset/Sleep-EDF]]
- 指标：综述报告 κ；精确设置待原始论文核验。

## 主要结果

本页不将综述汇总数值转化为跨模型排名。[[source-pages/phan-mikkelsen-2022-automatic-sleep-staging|Phan 和 Mikkelsen（2022）]]（PDF 第 6 页）

## 优点与局限
- 作为传统深度时序睡眠分期路线的代表模型。
- ⚠️ 干电极、跨设备与实时闭环应用未由当前来源直接验证。

## 来源
- [[source-pages/phan-mikkelsen-2022-automatic-sleep-staging|Phan 和 Mikkelsen（2022）]]

## 综述关联
- [[review/chapters/04-多模态睡眠检测算法]]
- [[concept/模型压缩与端侧部署]]
- [[review/完整综述大纲]]
