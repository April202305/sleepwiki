---
type: source
aliases: ["SwSleepNet"]
created: 2026-08-19
updated: 2026-08-22
sources: []
review_sections: ["2.2"]
status: active
review_due: 2026-09-19
---
# Zhu 等（2024）：SwSleepNet实时预测与在线校准
## 基本信息
- 类型：论文
- 原始文件：`raw/inbox/en-09-zhu-2024-online-calibration.pdf`
- source_id：`raw/inbox/en-09-zhu-2024-online-calibration.pdf`
- 作者/机构：Hangyu Zhu、Yonglin Wu、Yao Guo 等
- 年份：2024
- 英文原题：Towards Real-Time Sleep Stage Prediction and Online Calibration Based on Architecturally Switchable Deep Learning Models
- 录入日期：2026-08-19
- review_sections：[`2.2`]
## 题录与引用字段
- 题录状态：已核验
- 核验来源：Crossref（DOI 10.1109/jbhi.2023.3327470），核验日 2026-08-22
- 文献语种：英文
- 作者（原始顺序）：Hangyu Zhu; Yonglin Wu; Yao Guo; Cong Fu; Feng Shu; Huan Yu; Wei Chen; Chen Chen
- 原始题名：Towards Real-Time Sleep Stage Prediction and Online Calibration Based on Architecturally Switchable Deep Learning Models
- 文献类型标识：[J/OL]
- 载体或容器题名：IEEE Journal of Biomedical and Health Informatics
- 出版年：2024
- 卷：28
- 期：1
- 起止页码：470-481
- 文章号：
- 出版地：
- 出版者：
- 编辑：
- 会议名称：
- 会议地点：
- 会议日期：
- DOI：10.1109/jbhi.2023.3327470
- URL：https://doi.org/10.1109/jbhi.2023.3327470
- 发表或更新日期：2024-01
- 引用日期：2026-08-22
- 补充标识：
- 核验备注：
- Word 成稿引用：ZHU H, WU Y, GUO Y, 等. Towards Real-Time Sleep Stage Prediction and Online Calibration Based on Architecturally Switchable Deep Learning Models[J/OL]. IEEE Journal of Biomedical and Health Informatics, 2024, 28(1): 470-481. DOI:10.1109/jbhi.2023.3327470.

## 核心摘要
SwSleepNet离线模式使用序列模块，在线模式以2、3或5 s短片段预测；连续两段预测不一致时触发上下文校正。三数据集离线accuracy为84.5%、86.7%和81.8%，在线短片段结果均超过80%。[[source-pages/zhu-2024-swsleepnet-online-calibration]]（PDF第1、3–9页）
## 关联词条
- 模型：[[model/SwSleepNet]]
- 概念：[[concept/不确定性与拒绝输出]]、[[concept/睡眠分期]]
## 局限与待核实
- ⚠️论文“calibration”指预测不一致后的上下文重判，不等同于ECE/Brier概率校准；在线准确率不能直接与30 s五分类排行。
## 来源
- `raw/inbox/en-09-zhu-2024-online-calibration.pdf`
