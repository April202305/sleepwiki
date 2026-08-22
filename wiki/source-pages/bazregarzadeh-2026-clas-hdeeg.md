---
type: source
aliases: ["CLAS-hdEEG"]
created: 2026-08-20
updated: 2026-08-22
sources: ["raw/inbox/bazregarzadeh-2026-clas-hdeeg.pdf"]
review_sections: ["2.3", "5.4", "6.3"]
status: active
review_due: 2026-09-20
---

# CLAS-hdEEG高密度脑电闭环听觉刺激平台

## 基本信息
- 类型：原始系统验证研究
- 原始文件：`raw/inbox/bazregarzadeh-2026-clas-hdeeg.pdf`
- source_id：`raw/inbox/bazregarzadeh-2026-clas-hdeeg.pdf`
- 作者/年份：Hanieh Bazregarzadeh 等，2026
- 英文原题：CLAS-hdEEG: high-density EEG software platform for real-time delta wave detection and closed-loop auditory stimulation
- DOI：10.1088/1741-2552/ae4e5b

## 题录与引用字段
- 题录状态：已核验
- 核验来源：Crossref（DOI 10.1088/1741-2552/ae4e5b），核验日 2026-08-22
- 文献语种：英文
- 作者（原始顺序）：Hanieh Bazregarzadeh; Clara Pic Roca; Antonio Martin; Karine Lacourse; Jean-Marc Lina; Julie Carrier; Catherine Duclos
- 原始题名：CLAS-hdEEG: high-density EEG software platform for real-time delta wave detection and closed-loop auditory stimulation
- 文献类型标识：[J/OL]
- 载体或容器题名：Journal of Neural Engineering
- 出版年：2026
- 卷：23
- 期：2
- 起止页码：
- 文章号：026010
- 出版地：
- 出版者：
- 编辑：
- 会议名称：
- 会议地点：
- 会议日期：
- DOI：10.1088/1741-2552/ae4e5b
- URL：https://doi.org/10.1088/1741-2552/ae4e5b
- 发表或更新日期：2026-03-17
- 引用日期：2026-08-22
- 补充标识：
- 核验备注：
- Word 成稿引用：BAZREGARZADEH H, PIC ROCA C, MARTIN A, 等. CLAS-hdEEG: high-density EEG software platform for real-time delta wave detection and closed-loop auditory stimulation[J/OL]. Journal of Neural Engineering, 2026, 23(2): 026010. DOI:10.1088/1741-2552/ae4e5b.

## 核心摘要
CLAS-hdEEG在EGI 128通道系统中实时使用Fz移动平均信号检测delta波极值，并在14名健康参与者N3睡眠中实施峰、谷及假刺激条件。[[source-pages/bazregarzadeh-2026-clas-hdeeg]]（摘要、Methods 2.1–2.4）

## 方法与发现
- 检测阈值包括峰峰值至少75 μV、波形时长160–1700 ms；刺激为短粉红噪声。[[source-pages/bazregarzadeh-2026-clas-hdeeg]]（摘要）
- 检测至刺激的平均时延为20.03±0.5 ms；以90°目标窗定义时，总相位命中率为0.913。[[source-pages/bazregarzadeh-2026-clas-hdeeg]]（摘要、Results 3）
- 同步通过EGI记录的数字输入硬件标记验证。⚠️ 原文同时明确指出该实现没有完整捕获神经检测至物理声音发出的端到端时延，因此20.03 ms不得写成“声音到耳”时延。[[source-pages/bazregarzadeh-2026-clas-hdeeg]]（摘要、Introduction 1.3.2、Discussion）

## 关联词条
- 比较表：[[review/2.3形式化指标与系统比较表]]
- 证据包：[[review/证据包/02-技术基础-2.3-P1-证据包]]

## 局限与待核实
- ⚠️ 未报告麦克风/人工耳物理输出、P95/P99或逐机会完整失败分类；固定EGI平台限制跨平台外推。

## 来源
- 系统比较：[[review/5.4典型闭环系统横向比较表]]
- `raw/inbox/bazregarzadeh-2026-clas-hdeeg.pdf`
