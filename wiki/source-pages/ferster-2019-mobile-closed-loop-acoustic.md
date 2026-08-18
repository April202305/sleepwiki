---
type: source
aliases: ["Ferster 2019 MHSL-SB"]
created: 2026-08-18
updated: 2026-08-18
sources: []
review_sections: ["2.1", "2.3", "3.1"]
status: active
review_due: 2027-08-18
---

# Ferster 等（2019）：移动睡眠监测与闭环声刺激系统

## 基本信息
- 类型：移动 EEG 系统与居家实时触发研究
- 原始文件：`raw/inbox/ferster-2019-mobile-closed-loop-acoustic.pdf`
- source_id：`raw/inbox/ferster-2019-mobile-closed-loop-acoustic.pdf`
- 作者/机构：Maria Laura Ferster、Caroline Lustenberger、Walter Karlen；ETH Zurich
- 年份：2019
- 英文原题：Configurable Mobile System for Autonomous High-Quality Sleep Monitoring and Closed-Loop Acoustic Stimulation
- DOI：10.1109/LSENS.2019.2914425
- 录入日期：2026-08-18
- review_sections：["2.1", "2.3", "3.1"]

## 核心摘要
[[device/MHSL-SB]] 是 8 通道、24 位、250 Hz 的电池供电移动系统，以 Fpz-M2 实时执行 NREM、慢波活动、beta 功率和 PLL 相位联合门控。7 名健康老年人完成 98 个居家夜晚，其中 93 夜纳入触发分析、14 夜有专家评分。[[source-pages/ferster-2019-mobile-closed-loop-acoustic|本来源]]（PDF 第 1–3 页）

## 方法与发现
- 93 夜记录 360,571 次计算触发，75.7% 位于慢波 0°–90°上升相；平均相位 44.6°、SD 46.8°。14 个评分夜中 55,065 次触发的 97.5% 位于 NREM。[[source-pages/ferster-2019-mobile-closed-loop-acoustic|本来源]]（PDF 第 3–4 页，Figure 5）
- 居家阶段未播放声音，而是实时计算并保存触发；论文称 DAC 以最小延迟播放、系统需在数毫秒内触发，但未报告分段或实测总时延。[[source-pages/ferster-2019-mobile-closed-loop-acoustic|本来源]]（PDF 第 2–4 页）

## 关联词条
- 设备：[[device/MHSL-SB]]
- 概念：[[concept/闭环系统时延]]、[[concept/实时相位估计]]
- 干预：[[intervention/闭环听觉刺激]]
- 综述：[[review/文献清单/02-技术基础-2.3-文献需求单]]、[[review/证据包/02-技术基础-2.3-P1-证据包]]、[[review/文献清单/03-慢波干预-3.1-文献需求单]]、[[review/证据包/03-慢波干预-3.1-P1-证据包]]、[[review/chapters/02-基础理论与核心概念]]、[[review/证据矩阵]]

## 局限与待核实
- ⚠️触发精度基于离线零相位 Hilbert 参照；居家记录没有实际播放声音，不能验证刺激执行时延或疗效。
- ⚠️未报告采集至声音抵达的实测端到端时延与抖动。

## 新增综述需求入口

- [[review/文献清单/05-系统形态-5.4-文献需求单]]
- [[review/文献清单/06-挑战展望-6.3-文献需求单]]

## 来源
- `raw/inbox/ferster-2019-mobile-closed-loop-acoustic.pdf`
