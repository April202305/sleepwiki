---
type: source
aliases: ["DistillSleep 2025"]
created: 2026-08-19
updated: 2026-08-22
sources: []
review_sections: ["2.2", "2.3"]
status: active
review_due: 2026-09-19
---
# Park 等（2025）：DistillSleep端侧实时单导EEG分期
## 基本信息
- 类型：论文
- 原始文件：`raw/inbox/en-01-distillsleep-2025.pdf`
- source_id：`raw/inbox/en-01-distillsleep-2025.pdf`
- 作者/机构：K. Park、J. Hong、W. Lee 等
- 年份：2025
- 英文原题：DistillSleep: real-time, on-device, interpretable sleep staging from single-channel electroencephalogram
- 录入日期：2026-08-19
- review_sections：[`2.2`, `2.3`]
## 题录与引用字段
- 题录状态：已核验
- 核验来源：Crossref（DOI 10.1093/sleep/zsaf240），核验日 2026-08-22
- 文献语种：英文
- 作者（原始顺序）：Keondo Park; Joopyo Hong; Wooseok Lee; Hyun-Woo Shin; Hyung-Sin Kim
- 原始题名：DistillSleep: real-time, on-device, interpretable sleep staging from single-channel electroencephalogram
- 文献类型标识：[J/OL]
- 载体或容器题名：SLEEP
- 出版年：2025
- 卷：48
- 期：12
- 起止页码：
- 文章号：zsaf240
- 出版地：
- 出版者：
- 编辑：
- 会议名称：
- 会议地点：
- 会议日期：
- DOI：10.1093/sleep/zsaf240
- URL：https://doi.org/10.1093/sleep/zsaf240
- 发表或更新日期：2025-08-22
- 引用日期：2026-08-22
- 补充标识：
- 核验备注：
- Word 成稿引用：PARK K, HONG J, LEE W, 等. DistillSleep: real-time, on-device, interpretable sleep staging from single-channel electroencephalogram[J/OL]. SLEEP, 2025, 48(12): zsaf240. DOI:10.1093/sleep/zsaf240.

## 核心摘要
研究提出面向单通道EEG端侧实时分期的DistillSleep，以知识蒸馏压缩模型并讨论可解释性和设备部署。[[source-pages/park-2025-distillsleep]]（PDF第1–12页）
## 方法与发现
- 以30 s单导EEG为基本输入，比较教师与学生模型，并报告分期、模型规模和端侧运行字段。[[source-pages/park-2025-distillsleep]]（PDF第3–12页）
- “实时”结论须分开登记网络是否访问未来、实际设备推理与窗口形成时间，不能只凭论文题名认定端到端严格因果。
## 关联词条
- 模型：[[model/DistillSleep]]
- 概念：[[concept/模型压缩与端侧部署]]、[[concept/睡眠分期]]
## 局限与待核实
- ⚠️设备推理时间不等于采集至触发总时延；全文未形成闭环刺激疗效证据。
## 来源
- `raw/inbox/en-01-distillsleep-2025.pdf`
