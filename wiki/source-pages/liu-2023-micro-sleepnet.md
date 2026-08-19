---
type: source
aliases: ["Micro SleepNet 2023"]
created: 2026-08-19
updated: 2026-08-19
sources: []
review_sections: ["2.2", "2.3", "6.2"]
status: active
review_due: 2026-09-19
---

# Liu 等（2023）：Micro SleepNet移动端睡眠分期

## 基本信息
- 类型：论文
- 原始文件：`raw/inbox/liu-2023-micro-sleepnet.pdf`
- source_id：`raw/inbox/liu-2023-micro-sleepnet.pdf`
- 作者/机构：Guisong Liu 等
- 年份：2023
- 英文原题：Micro SleepNet: efficient deep learning model for mobile terminal real-time sleep staging
- 录入日期：2026-08-19
- review_sections：[`2.2`, `2.3`, `6.2`]

## 核心摘要

Micro SleepNet以单个30 s EEG epoch为输入，采用组卷积、通道重排、注意力重校准和膨胀卷积，避免RNN长序列缓存。研究在Sleep-EDF-20、Sleep-EDF-78和SHHS上评估，并部署到Android手机。[[source-pages/liu-2023-micro-sleepnet]]（PDF 第 1、3–9 页）

## 方法与发现

- 论文报告模型约10万字节内存占用，Android手机单条输入推理约2.8 ms，并给出参数量/FLOPs比较。[[source-pages/liu-2023-micro-sleepnet]]（PDF 第 2、8–10 页，Tables 4–5）
- 使用Sleep-EDF的Fpz-Cz和SHHS单导EEG，报告accuracy、macro-F1、κ与逐类F1；N1仍是较弱类别。[[source-pages/liu-2023-micro-sleepnet]]（PDF 第 5–8 页，Figures 4–5）
- 2.8 ms仅为手机模型推理时间，不包含30 s窗口形成、采集、预处理、通信、决策和刺激执行。

## 关联词条
- 模型：[[model/Micro SleepNet]]
- 概念：[[concept/模型压缩与端侧部署]]、[[concept/类别不平衡]]、[[concept/闭环系统时延]]

## 局限与待核实
- ⚠️手机实测支持端侧推理，不等于闭环端到端时延或整夜在线人体运行。
- ⚠️功耗、峰值内存、时延抖动与整夜续航未完整报告；“adaptive recalibration”是特征注意力模块，不是概率校准。

## 来源
- `raw/inbox/liu-2023-micro-sleepnet.pdf`
