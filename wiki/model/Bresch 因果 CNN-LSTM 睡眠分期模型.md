---
type: model
aliases: ["Bresch causal CNN-LSTM"]
created: 2026-08-19
updated: 2026-08-19
sources: ["[[source-pages/bresch-2018-real-time-rnn-staging]]"]
review_sections: ["2.2"]
status: active
review_due: 2026-09-19
---

# Bresch 因果 CNN-LSTM 睡眠分期模型

## 基本信息
- 任务：单通道 EEG 五分类
- 提出者/年份：Bresch 等，2018
- 模型类别：CNN + 单向 LSTM

## 架构与输入输出
当前30 s EEG epoch经卷积表征后进入两层单向LSTM，逐epoch输出W、N1、N2、N3或REM。[[source-pages/bresch-2018-real-time-rnn-staging]]

## 训练与实验设置
- 数据集：内部29人147夜；[[dataset/SIESTA]]
- 指标：κ、逐类precision/recall/F1

## 主要结果
按受试者三折验证κ约0.73；跨数据库测试显示明显方向性域偏移。[[source-pages/bresch-2018-real-time-rnn-staging]]

## 优点与局限
架构因果且约9万参数；但缺真实人体端到端在线时延和功耗。

## 关联概念与来源
- 概念：[[concept/睡眠分期]]、[[concept/跨数据集泛化]]
- 来源：[[source-pages/bresch-2018-real-time-rnn-staging]]

## ⚠️待核实
- 预处理滤波的严格因果实现与目标硬件运行。

## 来源
- [[source-pages/bresch-2018-real-time-rnn-staging]]
