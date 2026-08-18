---
type: source
aliases: ["Piorecky 2021 real-time slow oscillation"]
created: 2026-08-18
updated: 2026-08-18
sources: []
review_sections: ["2.3", "3.1", "6.3"]
status: active
review_due: 2027-08-18
---

# Piorecky 等（2021）：深睡眠慢振荡实时声刺激

## 基本信息
- 类型：人体实验数据与实时回放算法比较
- 原始文件：`raw/inbox/piorecky-2021-real-time-slow-oscillation.pdf`
- source_id：`raw/inbox/piorecky-2021-real-time-slow-oscillation.pdf`
- 作者/机构：Marek Piorecky、Vlastimil Koudelka、Vaclava Piorecka、Jan Strobl、Daniela Dudysova、Jana Koprivova
- 年份：2021
- 英文原题：Real-Time Excitation of Slow Oscillations during Deep Sleep Using Acoustic Stimulation
- DOI：10.3390/s21155169
- 录入日期：2026-08-18
- review_sections：["2.3", "3.1", "6.3"]

## 核心摘要
研究基于慢性失眠实验记录比较固定步长与 PLL 慢波声刺激。测试集为 9 名受试者的 18 份记录；算法比较主要通过离线 EEG 实时回放完成。固定步长在检测后预设 350 ms 发出第一次刺激，1.075 s 后第二次刺激，再暂停 2.5 s。[[source-pages/piorecky-2021-real-time-slow-oscillation|本来源]]（PDF 第 4–7 页）

## 方法与发现
- 固定步长与 PLL-XOR 的平均刺激相位约 257°与244°，后者离散度更大且更多落于下降相；作者认为固定步长在该数据与实现中更稳健。[[source-pages/piorecky-2021-real-time-slow-oscillation|本来源]]（PDF 第 12–19 页，Tables 3–4）
- 350 ms 是编程刺激间隔，不是实测系统延迟；PLL 对参数与个体高度敏感，无法据此建立通用最优参数。[[source-pages/piorecky-2021-real-time-slow-oscillation|本来源]]（PDF 第 6、17–20 页）

## 关联词条
- 概念：[[concept/实时相位估计]]、[[concept/闭环系统时延]]
- 干预：[[intervention/闭环听觉刺激]]
- 综述：[[review/02-技术基础-2.3-文献需求单]]、[[review/02-技术基础-2.3-P1-证据包]]、[[review/证据矩阵]]

## 局限与待核实
- ⚠️算法比较为预录数据回放；不能写成在线人体刺激系统的端到端时延比较。
- ⚠️人群和有效记录数量有限，不能推断临床疗效。

## 来源
- `raw/inbox/piorecky-2021-real-time-slow-oscillation.pdf`
