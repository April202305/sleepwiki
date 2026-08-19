---
type: source
aliases: ["TinySleepNet 2020"]
created: 2026-08-19
updated: 2026-08-19
sources: []
review_sections: ["2.2"]
status: active
review_due: 2026-09-19
---
# Supratak和Guo（2020）：TinySleepNet
## 基本信息
- 类型：论文
- 原始文件：`raw/inbox/en-03-tinysleepnet-2020.pdf`
- source_id：`raw/inbox/en-03-tinysleepnet-2020.pdf`
- 作者/机构：Akara Supratak、Yike Guo
- 年份：2020
- 英文原题：TinySleepNet: An Efficient Deep Learning Model for Sleep Stage Scoring based on Raw Single-Channel EEG
- 录入日期：2026-08-19
- review_sections：[`2.2`]
## 核心摘要
TinySleepNet以原始单通道EEG为输入，通过轻量CNN与时序模块减少参数和训练需求，并采用序列训练与受试者级验证。[[source-pages/supratak-2020-tinysleepnet]]（PDF第1–4页）
## 方法与发现
- 模型用于五分类并报告跨数据集表现；其上下文方向、状态重置和在线实现须与论文代码/方法一致解释。
## 关联词条
- 模型：[[model/TinySleepNet]]
- 概念：[[concept/时序上下文]]、[[concept/模型压缩与端侧部署]]
## 局限与待核实
- ⚠️会议论文仅4页，预处理因果性、硬件时延和功耗字段有限；不单独证明真实在线人体系统。
## 来源
- `raw/inbox/en-03-tinysleepnet-2020.pdf`
