---
type: source
aliases: ["DistillSleep 2025"]
created: 2026-08-19
updated: 2026-08-19
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
