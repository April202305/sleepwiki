---
type: source
aliases: ["Mikkelsen 2019 around-the-ear EEG staging"]
created: 2026-08-19
updated: 2026-08-22
sources: []
review_sections: ["2.2", "6.5"]
status: active
review_due: 2027-08-19
---

# 耳周 EEG 随机森林睡眠—觉醒分期

## 基本信息
- 类型：论文
- 原始文件：`raw/inbox/mikkelsen-2019-ear-eeg-ml-staging.pdf`
- source_id：`raw/inbox/mikkelsen-2019-ear-eeg-ml-staging.pdf`
- 作者/机构：Kaare B. Mikkelsen 等
- 年份：2019
- 英文原题：Machine-learning-derived sleep–wake staging from around-the-ear electroencephalogram outperforms manual scoring and actigraphy
- 录入日期：2026-08-19
- review_sections：["2.2", "6.5"]

## 题录与引用字段
- 题录状态：已核验
- 核验来源：Crossref（DOI 10.1111/jsr.12786），核验日 2026-08-22
- 文献语种：英文
- 作者（原始顺序）：Kaare B. Mikkelsen; James K. Ebajemito; Maria A. Bonmati-Carrion; Nayantara Santhi; Victoria L. Revell; Giuseppe Atzori; Ciro della Monica; Stefan Debener; Derk-Jan Dijk; Annette Sterr; Maarten de Vos
- 原始题名：Machine-learning-derived sleep–wake staging from around-the-ear electroencephalogram outperforms manual scoring and actigraphy
- 文献类型标识：[J/OL]
- 载体或容器题名：Journal of Sleep Research
- 出版年：2018
- 卷：28
- 期：2
- 起止页码：
- 文章号：e12786
- 出版地：
- 出版者：
- 编辑：
- 会议名称：
- 会议地点：
- 会议日期：
- DOI：10.1111/jsr.12786
- URL：https://doi.org/10.1111/jsr.12786
- 发表或更新日期：2018-11-13
- 引用日期：2026-08-22
- 补充标识：
- 核验备注：
- Word 成稿引用：MIKKELSEN K B, EBAJEMITO J K, BONMATI-CARRION M A, 等. Machine-learning-derived sleep–wake staging from around-the-ear electroencephalogram outperforms manual scoring and actigraphy[J/OL]. Journal of Sleep Research, 2018, 28(2): e12786. DOI:10.1111/jsr.12786.

## 核心摘要

研究以 cEEGrid 耳周 EEG 的手工特征训练随机森林，并采用留一被试交叉验证；20 名参与者中最终分析 15 名健康良好睡眠者。[[source-pages/mikkelsen-2019-around-ear-rf-staging]]（PDF 第 1、3–6 页）

## 方法与发现

- 特征涵盖频谱、相关与信号形态，随机森林承担 30 秒 epoch 分类，并加入基于相邻 epoch 的后处理。（PDF 第 4–6 页）
- 研究支持传统模型在轻量耳周 EEG 上的可行性及可解释特征路径，但未报告特征提取/推理时延、模型大小、跨设备外部验证或闭环刺激。（PDF 第 9–12 页）

## 关联词条
- 设备：[[device/cEEGrid耳周EEG]]
- 概念：[[concept/睡眠分期]]、[[concept/领域自适应]]

## 局限与待核实
- ⚠️ 小样本健康人群；留一被试验证仍在同一采集体系内，不等同于跨设备泛化。

## 来源
- `raw/inbox/mikkelsen-2019-ear-eeg-ml-staging.pdf`
