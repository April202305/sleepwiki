---
type: model
aliases: []
created: 2026-08-19
updated: 2026-08-19
sources: ["source-pages/huang-2025-multisess"]
review_sections: ["2.2"]
status: active
review_due: 2027-08-19
---

# MultiSEss

## 基本信息
- 任务：[[concept/睡眠分期]]
- 提出者/年份：Huang 等，2025
- 模型类别：多尺度卷积 + SE 注意力 + 状态空间模型

## 架构与输入输出

模型从 EEG 学习多尺度局部特征，并以 SE 注意力和状态空间模块建模时序，输出五类睡眠阶段。[[source-pages/huang-2025-multisess]]（PDF 第 3–6 页）

## 训练与实验设置
- 数据集：[[dataset/Sleep-EDF]]、[[dataset/SHHS]]
- 指标：accuracy、macro-F1、κ；以公开数据离线实验和消融为主。

## 优点与局限
- 直接补充 EEG 睡眠分期的 SSM 实例。
- ⚠️ 缺因果流式配置、端侧时延/内存实测、跨设备和闭环刺激验证。

## 来源
- [[source-pages/huang-2025-multisess]]
