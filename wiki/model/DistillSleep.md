---
type: model
aliases: []
created: 2026-08-19
updated: 2026-08-19
sources: ["[[source-pages/park-2025-distillsleep]]"]
review_sections: ["2.2", "2.3"]
status: active
review_due: 2026-09-19
---
# DistillSleep
## 基本信息
- 任务：单通道EEG端侧分期
- 提出者/年份：Park等，2025
- 模型类别：知识蒸馏轻量模型
## 架构与输入输出
以教师—学生蒸馏压缩单导EEG分期模型。[[source-pages/park-2025-distillsleep]]
## 训练与实验设置
- 数据集与指标：见来源页
## 主要结果
报告端侧运行、分期和解释性字段。
## 优点与局限
面向部署；真实闭环端到端时延不能由推理时间替代。
## 关联概念与来源
- 概念：[[concept/模型压缩与端侧部署]]
- 来源：[[source-pages/park-2025-distillsleep]]
## ⚠️待核实
- 全处理链严格零前视。
## 来源
- [[source-pages/park-2025-distillsleep]]
