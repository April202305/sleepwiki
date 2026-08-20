---
type: source
aliases: ["InsightSleepNet 2024"]
created: 2026-08-19
updated: 2026-08-20
sources: []
review_sections: ["2.2", "6.2"]
status: active
review_due: 2026-09-19
---

# Nam 等（2024）：PPG不确定性感知睡眠分期

## 基本信息
- 类型：论文
- 原始文件：`raw/inbox/nam-2024-insightsleepnet.pdf`
- source_id：`raw/inbox/nam-2024-insightsleepnet.pdf`
- 作者/机构：Borum Nam 等
- 年份：2024
- 英文原题：InsightSleepNet: the interpretable and uncertainty-aware deep learning network for sleep staging using continuous Photoplethysmography
- 录入日期：2026-08-19
- review_sections：[`2.2`, `6.2`]

## 核心摘要

InsightSleepNet使用连续PPG而非EEG，以因果TCN和局部注意力结合能量分数阈值进行四分类与拒绝输出，并在MESA、CFS和CAP三个数据集评估。它可补充选择性分类方法，但属于邻近技术证据。[[source-pages/nam-2024-insightsleepnet]]（PDF 第 1、3–8 页）

## 方法与发现

- 模型使用此前7个epoch的PPG历史上下文；MESA含2054名受试者并按受试者留出1850/204，CFS含320人，CAP含24名睡眠障碍患者。[[source-pages/nam-2024-insightsleepnet]]（PDF 第 4–6 页，Table 1）
- 推理时能量分数超过阈值即拒绝；阈值越严格，覆盖率下降而保留样本的accuracy、κ和weighted-F1上升。[[source-pages/nam-2024-insightsleepnet]]（PDF 第 5–10 页，Tables 2–4，Figure 4）
- 例如MESA无拒绝时accuracy 0.842、κ 0.742；不同阈值后保留样本accuracy为0.848–0.861、κ为0.752–0.777。[[source-pages/nam-2024-insightsleepnet]]（PDF 第 1、8 页，Table 2）

## 关联词条
- 模型：[[model/InsightSleepNet]]
- 数据集：[[dataset/MESA]]、[[dataset/CAP Sleep]]
- 数据集比较：[[review/2.2公开数据集、标签体系与验证协议比较表]]
- 概念：[[concept/不确定性与拒绝输出]]、[[concept/时序上下文]]

## 局限与待核实
- ⚠️输入为PPG，不能计入核心EEG校准/拒绝配额。
- ⚠️拒绝后性能只针对被保留样本，必须同时报告拒绝率；研究没有将其验证为闭环EEG触发安全机制。

## 来源
- `raw/inbox/nam-2024-insightsleepnet.pdf`
