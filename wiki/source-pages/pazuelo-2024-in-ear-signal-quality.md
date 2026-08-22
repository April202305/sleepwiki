---
type: source
aliases: ["Pazuelo 2024", "Naox in-ear EEG signal quality"]
created: 2026-08-18
updated: 2026-08-22
sources: ["raw/inbox/pazuelo-2024-in-ear-signal-quality.pdf"]
review_sections: ["2.1", "5.4"]
status: active
review_due: 2027-08-18
---

# Pazuelo 等（2024）：耳内可穿戴设备的 EEG 信号质量评估

## 基本信息

- 类型：耳内 EEG 信号质量与头皮 EEG 比较研究
- 原始文件：`raw/inbox/pazuelo-2024-in-ear-signal-quality.pdf`
- source_id：`raw/inbox/pazuelo-2024-in-ear-signal-quality.pdf`
- 作者/年份：Jeremy Pazuelo 等；2024
- 英文原题：Evaluating the Electroencephalographic Signal Quality of an In-Ear Wearable Device
- DOI：10.3390/s24123973
- review_sections：["2.1"]

## 题录与引用字段
- 题录状态：已核验
- 核验来源：Crossref（DOI 10.3390/s24123973），核验日 2026-08-22
- 文献语种：英文
- 作者（原始顺序）：Jeremy Pazuelo; Jose Yesith Juez; Hanane Moumane; Jan Pyrzowski; Liliana Mayor; Fredy Enrique Segura-Quijano; Mario Valderrama; Michel Le Van Quyen
- 原始题名：Evaluating the Electroencephalographic Signal Quality of an In-Ear Wearable Device
- 文献类型标识：[J/OL]
- 载体或容器题名：Sensors
- 出版年：2024
- 卷：24
- 期：12
- 起止页码：
- 文章号：3973
- 出版地：
- 出版者：
- 编辑：
- 会议名称：
- 会议地点：
- 会议日期：
- DOI：10.3390/s24123973
- URL：https://doi.org/10.3390/s24123973
- 发表或更新日期：2024-06-19
- 引用日期：2026-08-22
- 补充标识：
- 核验备注：
- Word 成稿引用：PAZUELO J, JUEZ J Y, MOUMANE H, 等. Evaluating the Electroencephalographic Signal Quality of an In-Ear Wearable Device[J/OL]. Sensors, 2024, 24(12): 3973. DOI:10.3390/s24123973.

## 核心摘要

本文评估 Naox Technologies 的移动耳内 EEG，在硬件回放、清醒伪影范式和睡眠 PSG 记录中与头皮 EEG 比较。设备以 250 Hz、24 位分辨率采样并实时发送数据；结论是特定设备在所测指标上具可行性，而非证明所有耳内 EEG 与头皮 EEG 等价。[[device/Naox 耳内 EEG 设备]]（PDF 第 1–3 页）

## 方法与发现

- 设备包含左右耳内电极，报告电极—皮肤界面平均阻抗为 459±295 kΩ（n=7），采样率 250 Hz、分辨率 24 位。[[device/Naox 耳内 EEG 设备]]（PDF 第 2–3 页，Table 1）
- 清醒记录中，作者以眼、面、头部活动形成不同伪影等级，并同时比较耳内与头皮信号；伪影会改变相关性，不能省略伪影条件解释相关系数。[[concept/耳内 EEG]]（PDF 第 6–8 页）
- 睡眠部分对 8 名受试者完成超过 70 小时 PSG 记录，考察慢波、纺锤波和分期中的耳内—头皮相关性。[[concept/PSG 参考标准]]（PDF 第 9–12 页）
- ⚠️文章的相关性、信号特征和分期观察不等同于临床诊断准确性、实时触发精度或闭环疗效。[[concept/可穿戴 EEG]]（PDF 第 1、12–15 页）

## 关联词条

- 设备：[[device/Naox 耳内 EEG 设备]]
- 概念：[[concept/耳内 EEG]]、[[concept/可穿戴 EEG]]、[[concept/PSG 参考标准]]
- 综述：[[review/文献清单/02-技术基础-2.1-文献需求单]]、[[review/证据包/02-技术基础-2.1-P1-证据包]]、[[review/chapters/02-基础理论与核心概念]]、[[review/证据矩阵]]

## ⚠️局限与待核实

- ⚠️睡眠相关分析的样本和任务与清醒伪影范式不同；不同结果不能直接合并为单一准确率。
- ⚠️研究不报告闭环刺激或端到端触发时延。

## 来源

- 系统比较：[[review/5.4典型闭环系统横向比较表]]
- `raw/inbox/pazuelo-2024-in-ear-signal-quality.pdf`
