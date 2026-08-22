---
type: source
aliases: ["Santostasi 2015", "sleep PLL"]
created: 2026-08-18
updated: 2026-08-22
sources: ["raw/inbox/santostasi-2015-pll-acoustic-stimulation.html"]
review_sections: ["3.1", "3.2", "6.3"]
status: active
review_due: 2027-08-18
---

# Santostasi 等（2015）：睡眠声刺激的实时锁相环

## 基本信息
- 类型：实时相位算法与小样本人体验证研究；PMC 作者稿 HTML
- 原始文件：`raw/inbox/santostasi-2015-pll-acoustic-stimulation.html`
- source_id：`raw/inbox/santostasi-2015-pll-acoustic-stimulation.html`
- 作者/年份：Giovanni Santostasi 等；2015
- 英文原题：Phase-Locked Loop for Precisely Timed Acoustic Stimulation during Sleep
- DOI：10.1016/j.jneumeth.2015.11.007
- review_sections：["3.1", "3.2", "6.3"]

## 题录与引用字段
- 题录状态：已核验
- 核验来源：Crossref（DOI 10.1016/j.jneumeth.2015.11.007），核验日 2026-08-22
- 文献语种：英文
- 作者（原始顺序）：Giovanni Santostasi; Roneil Malkani; Brady Riedner; Michele Bellesi; Giulio Tononi; Ken A. Paller; Phyllis C. Zee
- 原始题名：Phase-locked loop for precisely timed acoustic stimulation during sleep
- 文献类型标识：[J/OL]
- 载体或容器题名：Journal of Neuroscience Methods
- 出版年：2016
- 卷：259
- 期：
- 起止页码：101-114
- 文章号：
- 出版地：
- 出版者：
- 编辑：
- 会议名称：
- 会议地点：
- 会议日期：
- DOI：10.1016/j.jneumeth.2015.11.007
- URL：https://doi.org/10.1016/j.jneumeth.2015.11.007
- 发表或更新日期：2016-02
- 引用日期：2026-08-22
- 补充标识：
- 核验备注：
- Word 成稿引用：SANTOSTASI G, MALKANI R, RIEDNER B, 等. Phase-locked loop for precisely timed acoustic stimulation during sleep[J/OL]. Journal of Neuroscience Methods, 2016, 259: 101-114. DOI:10.1016/j.jneumeth.2015.11.007.

## 核心摘要

研究提出以 PLL 在线估计慢波相位并递送声音。目标相位 240°时，在慢波存在条件下的刺激相位均值为 243.15±3.06°；作者还在 5 名参与者的午睡实验中报告刺激相对 sham 的 delta 功率增加 15.3%。[[concept/实时相位估计]]（HTML Results 3.3–3.4，Figures 14–18、Table 1）

## 方法与发现
- PLL 以额区 EEG 为输入，可持续跟踪慢波并针对用户指定相位输出声音；幅度门控可提高目标相位的集中度。[[concept/实时相位估计]]（HTML Discussion）
- 作者将 PLL 与复现的 Ngo 固定参数算法进行同数据比较：PLL 相位分布更集中，但该比较不是独立、跨设备临床验证。[[concept/实时相位估计]]（HTML Results 3.3，Figure 14）
- 5 人结果显示刺激相对 sham 的 delta 功率增加 15.3%，前四个声音的同步反应显著；该小样本生理结果不能代表临床疗效。[[intervention/闭环听觉刺激]]（HTML Results 3.4，Figures 16–18、Table 1）

## 关联词条
- 概念：[[concept/实时相位估计]]、[[concept/闭环控制]]
- 干预：[[intervention/闭环听觉刺激]]
- 综述：[[review/文献清单/03-慢波干预-3.1-文献需求单]]、[[review/证据包/03-慢波干预-3.1-P1-证据包]]、[[review/证据矩阵]]

## 局限与待核实
- ⚠️算法相位结果与 5 人探索性生理结果验证层级不同；未给出可与其他系统统一比较的完整端到端时延分解。

## 来源
- `raw/inbox/santostasi-2015-pll-acoustic-stimulation.html`
