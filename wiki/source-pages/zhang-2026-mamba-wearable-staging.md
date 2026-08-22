---
type: source
aliases: ["Zhang 2026 wearable Mamba staging"]
created: 2026-08-19
updated: 2026-08-22
sources: []
review_sections: ["2.2", "6.2"]
status: active
review_due: 2027-08-19
---

# 无 EEG 可穿戴 Mamba 睡眠分期

## 基本信息
- 类型：论文
- 原始文件：`raw/inbox/zhang-2026-mamba-wearable-staging.pdf`
- source_id：`raw/inbox/zhang-2026-mamba-wearable-staging.pdf`
- 作者/机构：Andrew H. Zhang、Alex He-Mo、Richard Fei Yin 等
- 年份：2026
- 英文原题：Mamba-based deep learning approach for sleep staging on a wireless multimodal wearable system without electroencephalography
- 录入日期：2026-08-19
- review_sections：["2.2", "6.2"]

## 题录与引用字段
- 题录状态：已核验
- 核验来源：Crossref（DOI 10.1093/sleep/zsag022），核验日 2026-08-22
- 文献语种：英文
- 作者（原始顺序）：Andrew H Zhang; Alex He-Mo; Richard Fei Yin; Chunlin Li; Yuzhi Tang; Dharmendra Gurve; Veronique van der Horst; Aron S Buchman; Nasim Montazeri Ghahjaverestan; Maged Goubran; Bo Wang; Andrew S P Lim
- 原始题名：Mamba-based deep learning approach for sleep staging on a wireless multimodal wearable system without electroencephalography
- 文献类型标识：[J/OL]
- 载体或容器题名：SLEEP
- 出版年：2026
- 卷：49
- 期：4
- 起止页码：
- 文章号：zsag022
- 出版地：
- 出版者：
- 编辑：
- 会议名称：
- 会议地点：
- 会议日期：
- DOI：10.1093/sleep/zsag022
- URL：https://doi.org/10.1093/sleep/zsag022
- 发表或更新日期：2026-02-06
- 引用日期：2026-08-22
- 补充标识：
- 核验备注：
- Word 成稿引用：ZHANG A H, HE-MO A, YIN R F, 等. Mamba-based deep learning approach for sleep staging on a wireless multimodal wearable system without electroencephalography[J/OL]. SLEEP, 2026, 49(4): zsag022. DOI:10.1093/sleep/zsag022.

## 核心摘要

研究使用 ANNE One 的 ECG、PPG、三轴加速度和温度信号，在 357 名临床睡眠实验室成人的同步 PSG 标签上训练 Mamba 模型；五分类 balanced accuracy 65.11%、F1 66.15%、κ 53.23%。[[source-pages/zhang-2026-mamba-wearable-staging]]（PDF 第 1、7–9 页）

## 方法与发现

- 网络包含三层双向 Mamba block，明确利用双向窗口，不能视为严格因果在线实现。（PDF 第 5 页）
- 研究包含临床多样人群和实际无线可穿戴数据，但输入不含 EEG；模型结果不能直接证明 EEG Mamba 或相位触发性能。（PDF 第 3–6、11–13 页）
- 文中比较 LSTM、CRNN 与 Mamba，并报告约 1,271K 参数的 CRNN 基线；未形成统一设备端能耗与全链路时延基准。（PDF 第 6–9 页）

## 关联词条
- 模型：[[model/可穿戴多模态Mamba睡眠分期]]
- 概念：[[concept/闭环控制]]、[[concept/时序上下文]]

## 局限与待核实
- ⚠️ 无 EEG、双向上下文；只能补充可穿戴 Mamba 的临床分期证据，不能解除 EEG 因果部署缺口。

## 来源
- `raw/inbox/zhang-2026-mamba-wearable-staging.pdf`
