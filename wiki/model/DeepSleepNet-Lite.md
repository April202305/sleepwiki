---
type: model
aliases: []
created: 2026-08-19
updated: 2026-08-19
sources: ["[[source-pages/fiorillo-2021-deepsleepnet-lite]]"]
review_sections: ["2.2"]
status: active
review_due: 2026-09-19
---
# DeepSleepNet-Lite
## 基本信息
- 任务：单通道EEG分期与不确定实例检测
- 提出者/年份：Fiorillo等，2021
- 模型类别：轻量网络与Monte Carlo dropout
## 架构与输入输出
处理90 s Fpz-Cz序列并输出阶段及不确定性估计。[[source-pages/fiorillo-2021-deepsleepnet-lite]]
## 训练与实验设置
- 数据集：[[dataset/Sleep-EDF]]
## 主要结果
在轻量结构中加入MC dropout不确定性估计。
## 优点与局限
不等同概率校准；90 s上下文在线方向需核验。
## 关联概念与来源
- 概念：[[concept/不确定性与拒绝输出]]、[[concept/模型压缩与端侧部署]]
- 来源：[[source-pages/fiorillo-2021-deepsleepnet-lite]]
## ⚠️待核实
- 覆盖率、拒绝规则和端侧实测。
## 来源
- [[source-pages/fiorillo-2021-deepsleepnet-lite]]
