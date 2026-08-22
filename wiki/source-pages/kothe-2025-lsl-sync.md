---
type: source
aliases: ["Lab Streaming Layer", "LSL同步"]
created: 2026-08-20
updated: 2026-08-22
sources: ["raw/inbox/kothe-2025-lsl-sync.pdf"]
review_sections: ["6.3"]
status: active
review_due: 2026-09-20
---

# Lab Streaming Layer多模态同步

## 基本信息
- 类型：通用同步工程与验证论文
- 原始文件：`raw/inbox/kothe-2025-lsl-sync.pdf`
- source_id：`raw/inbox/kothe-2025-lsl-sync.pdf`
- 作者/年份：Christian Kothe、Seyed Yahya Shirazi、Tobias Stenner 等，2025
- 英文原题：The lab streaming layer for synchronized multimodal recording
- DOI：10.1162/IMAG.a.136

## 题录与引用字段
- 题录状态：已核验
- 核验来源：Crossref（DOI 10.1162/imag.a.136），核验日 2026-08-22
- 文献语种：英文
- 作者（原始顺序）：Christian Kothe; Seyed Yahya Shirazi; Tristan Stenner; David Medine; Chadwick Boulay; Matthew I. Grivich; Fiorenzo Artoni; Tim Mullen; Arnaud Delorme; Scott Makeig
- 原始题名：The lab streaming layer for synchronized multimodal recording
- 文献类型标识：[J/OL]
- 载体或容器题名：Imaging Neuroscience
- 出版年：2025
- 卷：3
- 期：
- 起止页码：
- 文章号：IMAG.a.136
- 出版地：
- 出版者：
- 编辑：
- 会议名称：
- 会议地点：
- 会议日期：
- DOI：10.1162/imag.a.136
- URL：https://doi.org/10.1162/imag.a.136
- 发表或更新日期：2025
- 引用日期：2026-08-22
- 补充标识：
- 核验备注：
- Word 成稿引用：KOTHE C, SHIRAZI S Y, STENNER T, 等. The lab streaming layer for synchronized multimodal recording[J/OL]. Imaging Neuroscience, 2025, 3: IMAG.a.136. DOI:10.1162/imag.a.136.

## 核心摘要
LSL以逐样本时间戳、局域网时钟偏移和往返时间估计处理网络延迟与抖动，是多模态同步的邻近工程方法，不是睡眠闭环刺激效果研究。[[source-pages/kothe-2025-lsl-sync]]（摘要、§2.2）

## 方法与发现
- 网络时钟滤波后的残差在多数网络硬件上假定远低于1 ms；验证示例还显示设备“setup offset”必须单独标定。[[source-pages/kothe-2025-lsl-sync]]（§2.2、§3、Figures 3–4）
- LSL不能自行获知设备内部缓存、无线传输、驱动和访问造成的吞吐时延；应为每条采集流独立测量时延及其分布。[[source-pages/kothe-2025-lsl-sync]]（§1.2、§3）

## 关联词条
- 综述：[[review/2.3形式化指标与系统比较表]]

## 局限与待核实
- ⚠️ 非睡眠、非刺激链路证据，只能支撑同步方法和“设备时延需另测”的边界，不能进入2.3核心系统性能排行。

## 来源
- `raw/inbox/kothe-2025-lsl-sync.pdf`
