---
type: source
aliases: ["Melo 等（2024）单通道 EEG 与体动睡眠分期"]
created: 2026-08-19
updated: 2026-08-19
sources: []
review_sections: ["2.1", "2.2", "6.5"]
status: active
review_due: 2027-08-19
---

# Melo 等（2024）：单通道 EEG 头带联合腕部体动的睡眠分期验证

## 基本信息
- 类型：论文
- 原始文件：`raw/inbox/melo-2024-single-channel-eeg-actigraphy.pdf`
- source_id：`raw/inbox/melo-2024-single-channel-eeg-actigraphy.pdf`
- 作者/机构：Mariana Cardoso Melo、Julia Ribeiro da Silva Vallim、Silvério Garbuio 等；Universidade Federal de São Paulo、SleepUp Tecnologia em Saúde Ltda 等
- 年份：2024
- 英文原题：Validation of a sleep staging classification model for healthy adults based on two combinations of a single-channel EEG headband and wrist actigraphy
- 期刊：Journal of Clinical Sleep Medicine，20(6)：983–990
- DOI：10.5664/jcsm.11082
- 录入日期：2026-08-19
- review_sections：["2.1", "2.2", "6.5"]

## 核心摘要

23 名健康参与者接受整夜 I 型 PSG，并分别佩戴柔性或刚性单通道额区 EEG 头带及腕部活动记录仪。加入体动后，两种组合的 N1 错误率分别由 15.7% 降至 9.8%、由 27.7% 降至 17.0%；整体 F1 仅小幅提高，作者认为体动不是模型的重要特征。[[source-pages/melo-2024-single-channel-eeg-actigraphy]]（PDF 第 1、5 页，Figure 1，Table 3）

## 方法与发现

- 组合 A 为柔性单通道 EEG 头带加活动记录（n=12），组合 B 为刚性头带加活动记录（n=11）；两种 EEG 头带采样率均为 512 Hz，并与 I 型 PSG 同步。[[source-pages/melo-2024-single-channel-eeg-actigraphy]]（PDF 第 1、3 页）
- 模型使用 18 个时域/频域特征和 bagged decision trees，采用 5 折交叉验证及随机 80/20 epoch 划分。[[source-pages/melo-2024-single-channel-eeg-actigraphy]]（PDF 第 1、4 页）
- 加入体动后组合 A/B 的 F1 分别为 98.4%/96.9%，移除体动后为 97.7%/95.3%；N1 错误率下降幅度较明显，但研究者仍将体动的整体贡献判断为较小。[[source-pages/melo-2024-single-channel-eeg-actigraphy]]（PDF 第 1、5–6 页，Table 3，Figure 1）

## 关联词条
- 模型：[[model/Melo 单通道 EEG-体动睡眠分期模型]]
- 概念：[[concept/可穿戴 EEG]]、[[concept/睡眠分期]]、[[concept/PSG 参考标准]]、[[concept/多模态融合]]
- 综述：[[review/证据包/02-技术基础-2.1-P1-证据包]]

## 局限与待核实
- ⚠️健康样本小，两个设备组合由不同参与者构成；随机 epoch 划分可能使个体信息跨训练/测试集合，不能直接代表跨受试者或临床泛化。
- ⚠️该研究为离线分期验证，未报告闭环触发、刺激执行或端到端时延。

## 来源
- `raw/inbox/melo-2024-single-channel-eeg-actigraphy.pdf`
