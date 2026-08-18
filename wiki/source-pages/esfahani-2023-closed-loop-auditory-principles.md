---
type: source
aliases: ["Esfahani 2023", "CLAS best practices"]
created: 2026-08-17
updated: 2026-08-18
sources: ["raw/inbox/esfahani-2023-closed-loop-auditory-principles.pdf"]
review_sections: ["1.2", "2.2", "2.3", "3.1", "6.3", "6.4"]
status: active
review_due: 2027-08-17
---

# Esfahani 等（2023）：闭环听觉刺激慢振荡的基本原理与最佳实践

## 基本信息

- 类型：闭环听觉刺激（CLAS）方法学综述
- 原始文件：`raw/inbox/esfahani-2023-closed-loop-auditory-principles.pdf`
- source_id：`raw/inbox/esfahani-2023-closed-loop-auditory-principles.pdf`
- 作者/年份：Mahdad Jafarzadeh Esfahani 等；2023
- 英文原题：Closed-loop auditory stimulation of sleep slow oscillations: Basic principles and best practices
- DOI：10.1016/j.neubiorev.2023.105379
- review_sections：["1.2", "2.2", "2.3", "3.1", "6.3", "6.4"]

## 核心摘要

该综述将 [[intervention/闭环听觉刺激]] 的实施拆为实时脑信号访问、目标振荡检测算法和刺激系统三部分，并强调参数取决于目标人群、设备与处理能力，不能设定为普适最佳值。[[intervention/闭环听觉刺激]]（PDF 第 3 页）

## 方法与发现

- 闭环状态依赖刺激以实时 EEG 评估内源脑活动，并按目标信号/振荡的状态精确安排刺激；这与只按预设时间参数或宏观睡眠阶段给刺激的方式不同。[[concept/实时相位估计]]（PDF 第 2–3 页）
- 从电极采集到耳端刺激须分别考虑脑—放大器、放大器—服务器、访问—处理、处理—触发和触发—扬声器/耳机等延迟；这些延迟可达数百毫秒，并会影响刺激精度和解释。[[concept/实时相位估计]]（PDF 第 3 页）
- 阈值检测计算量低，但振幅变异可使靶相位/时点不稳定；相位锁定环（PLL）等预测方法提供不同的相位追踪路径。现有直接比较不足以推荐一种通用算法。[[concept/实时相位估计]]（PDF 第 4 页）
- 声音音量需在不引起觉醒的条件下个体化；觉醒或阶段改变后迅速停止刺激是失败保护的一部分。[[intervention/闭环听觉刺激]]（PDF 第 5 页）
- ⚠️该文为方法学综述；它不能单独证明某一具体系统具有临床疗效或长期安全性。多数 CLAS 文献评估短期效果，长期睡眠、情绪和行为影响仍缺充分研究。[[intervention/闭环听觉刺激]]（PDF 第 12–13 页）

## 关联词条

- 概念：[[concept/实时相位估计]]、[[concept/可穿戴 EEG]]
- 干预：[[intervention/闭环听觉刺激]]
- 综述：[[review/chapters/01-引言]]、[[review/文献清单/01-引言-1.2-文献需求单]]、[[review/证据包/01-引言-1.2-P1-证据包]]、[[review/文献清单/01-引言-1.3-文献需求单]]、[[review/证据包/01-引言-1.3-P1-证据包]]、[[review/文献清单/02-技术基础-2.2-文献需求单]]、[[review/证据包/02-技术基础-2.2-P1-证据包]]、[[review/文献清单/02-技术基础-2.3-文献需求单]]、[[review/证据包/02-技术基础-2.3-P1-证据包]]、[[review/文献清单/03-慢波干预-3.1-文献需求单]]、[[review/证据包/03-慢波干预-3.1-P1-证据包]]、[[review/证据矩阵]]

## ⚠️局限与待核实

- ⚠️该综述列出时延组成，但没有为所有系统提供可横向比较的统一总时延；具体实现仍须回到原始系统研究。

## 新增综述需求入口

- [[review/文献清单/04-全周期-4.5-文献需求单]]
- [[review/文献清单/05-系统形态-5.1-文献需求单]]

## 来源

- `raw/inbox/esfahani-2023-closed-loop-auditory-principles.pdf`
