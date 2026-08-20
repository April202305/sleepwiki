---
type: source
aliases: ["Navarrete CLAS outcome prediction"]
created: 2026-08-18
updated: 2026-08-20
sources: ["raw/inbox/navarrete-2022-ongoing-oscillations-outcome.pdf"]
review_sections: ["3.2", "4.5"]
status: superseded
review_due: 2027-08-18
---

# Navarrete 等：持续振荡预测 CLAS 刺激后结果

## 基本信息
- 类型：预印本；既有交叉实验数据的机器学习再分析
- 原始文件/source_id：`raw/inbox/navarrete-2022-ongoing-oscillations-outcome.pdf`
- 作者/年份：Miguel Navarrete 等；预印本版本 2021，正式题录年份待核实
- 英文原题：Ongoing neural oscillations predict the post-stimulus outcome of closed loop auditory stimulation during slow-wave sleep
- DOI：10.1101/2021.05.06.443016（预印本）
- review_sections：["3.2", "4.5"]

## 核心摘要
基于 21 名健康青年两夜平衡 STIM/SHAM 数据，随机森林利用当前慢振荡形态预测后续慢振荡幅度的准确率约 70%，预测刺激后纺锤活动约 60%。[[concept/实时相位估计]]（PDF 第 2、5 页）

## 方法与发现
- 50 ms 粉噪点击用于 N2/N3，试次后暂停 2.5 s；见觉醒或 REM 时人工停止。（PDF 第 5 页）
- STIM与SHAM的预测性能相近：刺激后SO trough ACC均0.71（95% CI分别0.67–0.74、0.69–0.74），峰峰值ACC为0.83与0.84，纺锤包络振幅ACC为0.59与0.60；这属于高/低响应分类，不是干预效应量。（PDF Results，分类结果段）
- 结果支持响应依赖的触发优化，但模型基于既有数据训练/验证，未证明在线自适应控制改善临床或行为终点。

## 关联词条
- 干预：[[intervention/闭环听觉刺激]]
- 综述：[[review/文献清单/03-慢波干预-3.2-文献需求单]]、[[review/证据包/03-慢波干预-3.2-P1-证据包]]、[[review/文献清单/04-全周期-4.5-文献需求单]]、[[review/证据包/04-全周期-4.5-P1-证据包]]、[[review/证据矩阵]]

## 局限与待核实
- ⚠️当前文件是未同行评审预印本；正式 NeuroImage 版本的页码与数值须取得后复核。
- 已由[[source-pages/navarrete-2022-ongoing-oscillations-outcome-formal]]替代用于正式引用；本页保留版本追溯，不再作为正文主引用。

## 来源
- `raw/inbox/navarrete-2022-ongoing-oscillations-outcome.pdf`
