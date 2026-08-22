---
type: source
aliases: ["Sun 2023 FPGA sleep modulation"]
created: 2026-08-18
updated: 2026-08-22
sources: []
review_sections: ["2.2", "2.3"]
status: active
review_due: 2027-08-18
---

# Sun 等（2023）：FPGA 加速睡眠调控系统

## 基本信息
- 类型：PMC 作者稿 HTML；模型验证与台架系统展示
- 原始文件：`raw/inbox/sun-2023-fpga-sleep-modulation.html`
- source_id：`raw/inbox/sun-2023-fpga-sleep-modulation.html`
- 作者/机构：Mingzhe Sun、Aaron Zhou、Naize Yang、Yaqian Xu、Yuhan Hou、Andrew G. Richardson、Xilin Liu
- 年份：2023
- 英文原题：Design of a Sleep Modulation System with FPGA-Accelerated Deep Learning for Closed-loop Stage-Specific In-Phase Auditory Stimulation
- DOI：10.1109/ISCAS46773.2023.10181356
- 录入日期：2026-08-18
- review_sections：["2.2", "2.3"]

## 题录与引用字段
- 题录状态：已核验
- 核验来源：Crossref（DOI 10.1109/iscas46773.2023.10181356），核验日 2026-08-22
- 文献语种：英文
- 作者（原始顺序）：Mingzhe Sun; Aaron Zhou; Naize Yang; Yaqian Xu; Yuhan Hou; Andrew G. Richardson; Xilin Liu
- 原始题名：Design of a Sleep Modulation System with FPGA-Accelerated Deep Learning for Closed-loop Stage-Specific In-Phase Auditory Stimulation
- 文献类型标识：[C/OL]
- 载体或容器题名：2023 IEEE International Symposium on Circuits and Systems (ISCAS)
- 出版年：2023
- 卷：
- 期：
- 起止页码：1-5
- 文章号：
- 出版地：Monterey, CA, USA
- 出版者：IEEE
- 编辑：
- 会议名称：2023 IEEE International Symposium on Circuits and Systems (ISCAS)
- 会议地点：Monterey, CA, USA
- 会议日期：2023-5-21 至 2023-5-25
- DOI：10.1109/iscas46773.2023.10181356
- URL：https://doi.org/10.1109/iscas46773.2023.10181356
- 发表或更新日期：2023-05-21
- 引用日期：2026-08-22
- 补充标识：
- 核验备注：
- Word 成稿引用：SUN M, ZHOU A, YANG N, 等. Design of a Sleep Modulation System with FPGA-Accelerated Deep Learning for Closed-loop Stage-Specific In-Phase Auditory Stimulation[C/OL]//2023 IEEE International Symposium on Circuits and Systems (ISCAS). 2023: 1-5. DOI:10.1109/iscas46773.2023.10181356.

## 核心摘要
研究将单通道 [[model/Sun FPGA 睡眠分期模型]]、慢波零交叉检测、可编程延迟与粉噪输出集成到 FPGA 系统。模型在 [[dataset/MASS]] SS2/SS3 共 81 名受试者上平均准确率 85.8%、F1 79%；模拟引擎在 20 MHz 下处理 20 秒输入少于 1 秒。[[source-pages/sun-2023-fpga-sleep-modulation|本来源]]（HTML Abstract、§III–IV）

## 方法与发现
- 模型含双 CNN、双向 LSTM 和 8 位量化，使用当前及此前两个片段；模拟前端与声音模块仅在台架完成表征。[[source-pages/sun-2023-fpga-sleep-modulation|本来源]]（HTML §II–IV、Tables II–III、Figure 5）
- 论文未报告采集—判断—扬声器输出的实测总时延或抖动；“20 秒输入少于 1 秒”只是引擎吞吐量。[[source-pages/sun-2023-fpga-sleep-modulation|本来源]]（HTML §III.A、§IV）

## 关联词条
- 模型：[[model/Sun FPGA 睡眠分期模型]]
- 数据集：[[dataset/MASS]]
- 概念：[[concept/闭环系统时延]]
- 综述：[[review/文献清单/02-技术基础-2.3-文献需求单]]、[[review/证据矩阵]]

## 局限与待核实
- ⚠️闭环刺激仅为台架展示，没有在线人体睡眠验证。
- ⚠️双向 LSTM 与完整输入窗口的可用时点须和“实时”表述一并说明。

## 来源
- `raw/inbox/sun-2023-fpga-sleep-modulation.html`
