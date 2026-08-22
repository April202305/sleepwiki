---
type: source
aliases: ["Micro SleepNet 2023"]
created: 2026-08-19
updated: 2026-08-22
sources: []
review_sections: ["2.2", "2.3", "6.2"]
status: active
review_due: 2026-09-19
---

# Liu 等（2023）：Micro SleepNet移动端睡眠分期

## 基本信息
- 类型：论文
- 原始文件：`raw/inbox/liu-2023-micro-sleepnet.pdf`
- source_id：`raw/inbox/liu-2023-micro-sleepnet.pdf`
- 作者/机构：Guisong Liu 等
- 年份：2023
- 英文原题：Micro SleepNet: efficient deep learning model for mobile terminal real-time sleep staging
- 录入日期：2026-08-19
- review_sections：[`2.2`, `2.3`, `6.2`]

## 题录与引用字段
- 题录状态：已核验
- 核验来源：Crossref（DOI 10.3389/fnins.2023.1218072），核验日 2026-08-22
- 文献语种：英文
- 作者（原始顺序）：Guisong Liu; Guoliang Wei; Shuqing Sun; Dandan Mao; Jiansong Zhang; Dechun Zhao; Xuelong Tian; Xing Wang; Nanxi Chen
- 原始题名：Micro SleepNet: efficient deep learning model for mobile terminal real-time sleep staging
- 文献类型标识：[J/OL]
- 载体或容器题名：Frontiers in Neuroscience
- 出版年：2023
- 卷：17
- 期：
- 起止页码：
- 文章号：1218072
- 出版地：
- 出版者：
- 编辑：
- 会议名称：
- 会议地点：
- 会议日期：
- DOI：10.3389/fnins.2023.1218072
- URL：https://doi.org/10.3389/fnins.2023.1218072
- 发表或更新日期：2023-07-28
- 引用日期：2026-08-22
- 补充标识：
- 核验备注：
- Word 成稿引用：LIU G, WEI G, SUN S, 等. Micro SleepNet: efficient deep learning model for mobile terminal real-time sleep staging[J/OL]. Frontiers in Neuroscience, 2023, 17: 1218072. DOI:10.3389/fnins.2023.1218072.

## 核心摘要

Micro SleepNet以单个30 s EEG epoch为输入，采用组卷积、通道重排、注意力重校准和膨胀卷积，避免RNN长序列缓存。研究在Sleep-EDF-20、Sleep-EDF-78和SHHS上评估，并部署到Android手机。[[source-pages/liu-2023-micro-sleepnet]]（PDF 第 1、3–9 页）

## 方法与发现

- 论文报告模型约10万字节内存占用，Android手机单条输入推理约2.8 ms，并给出参数量/FLOPs比较。[[source-pages/liu-2023-micro-sleepnet]]（PDF 第 2、8–10 页，Tables 4–5）
- 使用Sleep-EDF的Fpz-Cz和SHHS单导EEG，报告accuracy、macro-F1、κ与逐类F1；N1仍是较弱类别。[[source-pages/liu-2023-micro-sleepnet]]（PDF 第 5–8 页，Figures 4–5）
- 2.8 ms仅为手机模型推理时间，不包含30 s窗口形成、采集、预处理、通信、决策和刺激执行。

## 关联词条
- 模型：[[model/Micro SleepNet]]
- 概念：[[concept/模型压缩与端侧部署]]、[[concept/类别不平衡]]、[[concept/闭环系统时延]]

## 局限与待核实
- ⚠️手机实测支持端侧推理，不等于闭环端到端时延或整夜在线人体运行。
- ⚠️功耗、峰值内存、时延抖动与整夜续航未完整报告；“adaptive recalibration”是特征注意力模块，不是概率校准。

## 来源
- `raw/inbox/liu-2023-micro-sleepnet.pdf`
