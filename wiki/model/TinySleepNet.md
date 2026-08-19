---
type: model
aliases: []
created: 2026-08-19
updated: 2026-08-19
sources: ["[[source-pages/supratak-2020-tinysleepnet]]", "[[source-pages/hong-2021-confidence-based-scoring]]"]
review_sections: ["2.2"]
status: active
review_due: 2026-09-19
---
# TinySleepNet
## 基本信息
- 任务：原始单导EEG五分类
- 提出者/年份：Supratak和Guo，2020
- 模型类别：轻量CNN与时序网络
## 架构与输入输出
30 s EEG表征与序列训练。[[source-pages/supratak-2020-tinysleepnet]]
## 训练与实验设置
- 数据集：多个公开睡眠数据库
- 指标：accuracy、macro-F1、κ等
## 主要结果
作为轻量基线并被Hong框架用作分类器。
## 优点与局限
会议全文信息有限；不自动视为真实在线端侧系统。
## 关联概念与来源
- 概念：[[concept/时序上下文]]、[[concept/模型压缩与端侧部署]]
- 来源：[[source-pages/supratak-2020-tinysleepnet]]、[[source-pages/hong-2021-confidence-based-scoring]]
## ⚠️待核实
- 预处理、状态方向和硬件运行。
## 来源
- [[source-pages/supratak-2020-tinysleepnet]]
- [[source-pages/hong-2021-confidence-based-scoring]]
