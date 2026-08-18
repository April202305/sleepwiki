---
type: model
aliases: []
created: 2026-08-18
updated: 2026-08-18
sources: ["source-pages/kulkarni-2019-real-time-spindle-detection"]
review_sections: ["2.2", "2.3", "4.2"]
status: active
review_due: 2027-08-18
---

# SpindleNet

## 基本信息
- 任务：实时 [[concept/睡眠纺锤波]] 事件检测
- 提出者/年份：Kulkarni 等，2019
- 模型类别：CNN + 单层 LSTM + 功率特征

## 架构与输入输出

模型从单通道 EEG 的 250 ms 移动窗口输出样本级纺锤波概率，在线步长为 1 个样本。[[source-pages/kulkarni-2019-real-time-spindle-detection]]（HTML 正文 §2.2–2.3）

## 训练与实验设置
- 数据集：[[dataset/MASS]]、[[dataset/DREAMS]]
- 指标：事件检测性能与相对专家起点的检测延迟；标注规则必须随数据集记录。

## 主要结果

指定工作站上的平均在线执行时间（含特征计算）约 6 ms，检测延迟约 150–350 ms；MASS 相对 OR/AND 起点约为 340/205 ms。[[source-pages/kulkarni-2019-real-time-spindle-detection]]（HTML Abstract、正文 §3.3）

## 优点与局限
- 可在线执行，并展示跨人群、颅内信号和动物信号的可运行性。
- ⚠️ 检测延迟与执行时间均不是闭环系统端到端时延。
- ⚠️ 无真值数据上的展示不能作为定量检测验证；不同数据集及既有算法不可直接比较。

## 关联概念与来源
- 概念：[[concept/睡眠纺锤波]]
- 数据集：[[dataset/MASS]]、[[dataset/DREAMS]]
- 来源：[[source-pages/kulkarni-2019-real-time-spindle-detection]]
- 综述：[[review/chapters/02-基础理论与核心概念]]、[[review/证据矩阵]]

## 来源
- [[source-pages/kulkarni-2019-real-time-spindle-detection]]
