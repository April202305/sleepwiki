---
type: model
aliases: []
created: 2026-08-12
updated: 2026-08-19
sources: ["source-pages/phan-mikkelsen-2022-automatic-sleep-staging", "source-pages/phan-2019-seqsleepnet"]
review_sections: ["2.2", "4"]
status: active
review_due: 2027-08-12
---

# SeqSleepNet

## 基本信息
- 任务：[[concept/睡眠分期]]
- 提出者/年份：Phan 等，2019
- 模型类别：RNN epoch 编码 + RNN 序列编码

## 架构与输入输出

综述将其列为输入时频表示、以 RNN 同时完成 epoch 与序列编码的长时序系统。[[source-pages/phan-mikkelsen-2022-automatic-sleep-staging|Phan 和 Mikkelsen（2022）]]（PDF 第 6–7 页，Table 1）

原始研究使用 epoch 级与序列级双向 RNN；MASS 20 折中每折按受试者划分 180/10/10 名训练、验证和测试对象。[[source-pages/phan-2019-seqsleepnet]]（PDF 第 3–6 页）

## 训练与实验设置
- 数据集：[[dataset/Sleep-EDF]]、[[dataset/SHHS]]、[[dataset/MESA]]
- 指标：Cohen's κ、macro-F1 或准确率；须按原始协议核验。

## 主要结果

本文暂不转录综述表中的数值，以避免在不同数据集与配置间形成无条件比较。[[source-pages/phan-mikkelsen-2022-automatic-sleep-staging|Phan 和 Mikkelsen（2022）]]（PDF 第 6–7 页）

## 优点与局限
- 代表以递归网络建模 [[concept/时序上下文]] 的序列到序列路线。
- ⚠️ 可穿戴设备实时部署、推理时延与目标设备泛化均待原始研究证据。
- ⚠️ 双向上下文访问未来 epoch，原实现不属于严格因果流式模型。

## 来源
- [[source-pages/phan-mikkelsen-2022-automatic-sleep-staging|Phan 和 Mikkelsen（2022）]]
- [[source-pages/phan-2019-seqsleepnet]]

## 综述关联
- [[review/chapters/04-多模态睡眠检测算法]]
- [[concept/领域自适应]]、[[concept/模型压缩与端侧部署]]
- [[review/完整综述大纲]]
