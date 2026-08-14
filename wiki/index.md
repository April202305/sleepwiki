# Sleep-Wiki

睡眠研究知识库总目录。

## 内容分区

### 原始资料摘要

- [[source-pages/eldele-2021-attention-based-single-channel-eeg|Eldele 等（2021）]]：AttnSleep 的架构、数据集与实验摘要。`source`｜2026-08-11｜1 来源
- [[source-pages/zhou-2022-singlechannelnet|Zhou 等（2022）]]：SingleChannelNet 的上下文输入与跨数据集评估摘要。`source`｜2026-08-11｜1 来源
- [[source-pages/phan-mikkelsen-2022-automatic-sleep-staging|Phan 和 Mikkelsen（2022）]]：EEG 自动睡眠分期的进展、挑战与未来方向综述。`source`｜2026-08-12｜1 来源
- [[source-pages/de-gans-2024-eeg-wearables-systematic-review|de Gans 等（2024）]]：EEG 可穿戴设备睡眠评估系统综述（60 篇论文、34 种设备）。`source`｜2026-08-12｜1 来源

### 模型词条

- [[model/AttnSleep|AttnSleep]]：多分辨率 CNN、特征重校准与注意力时序编码。`model`｜2026-08-11｜1 来源
- [[model/SingleChannelNet|SingleChannelNet]]：基于 90 秒原始单通道 EEG 输入的深层 CNN。`model`｜2026-08-11｜1 来源
- [[model/DeepSleepNet|DeepSleepNet]]：CNN epoch 编码 + RNN 序列编码的代表路线。`model`｜2026-08-12｜1 来源
- [[model/SeqSleepNet|SeqSleepNet]]：RNN epoch 编码 + RNN 序列编码的序列到序列系统。`model`｜2026-08-12｜1 来源
- [[model/SleepEEGNet|SleepEEGNet]]：原始 EEG 输入的 CNN+RNN 传统深度时序路线。`model`｜2026-08-12｜1 来源
- [[model/SleepTransformer|SleepTransformer]]：Transformer epoch 编码 + Transformer 序列编码的非递归注意力路线。`model`｜2026-08-12｜1 来源

### 数据集词条

- [[dataset/Sleep-EDF|Sleep-EDF]]：文献中使用最广的 Sleep Cassette/扩展版本（Fpz-Cz, 100 Hz）。`dataset`｜2026-08-11｜3 来源
- [[dataset/SHHS|SHHS]]：多中心队列，Eldele 等按 AHI<5 筛选 329 人用于实验。`dataset`｜2026-08-11｜2 来源
- [[dataset/CCSHS|CCSHS]]：Zhou 等使用的 515 名儿童睡眠队列（C4/A1, 128 Hz）。`dataset`｜2026-08-11｜1 来源
- [[dataset/MESA|MESA]]：多民族动脉粥样硬化研究队列，Phan 和 Mikkelsen 模型比较表中列为多模型评估数据集。`dataset`｜2026-08-12｜1 来源

### 概念词条

- [[concept/睡眠分期]]：自动睡眠阶段分类任务（五分类：W/N1/N2/N3/REM）。`concept`｜2026-08-11｜3 来源
- [[concept/单通道 EEG]]：单导联 EEG 输入设置（Fpz-Cz、C4-A1 等）。`concept`｜2026-08-11｜3 来源
- [[concept/时序上下文]]：相邻 epoch/连续时段的信息建模机制。`concept`｜2026-08-11｜2 来源
- [[concept/类别不平衡]]：睡眠阶段样本数量不均及其评估影响（κ 推荐用于不平衡一致性评估）。`concept`｜2026-08-11｜3 来源
- [[concept/跨数据集泛化]]：跨人群、机构、设备与采集协议的直接测试能力。`concept`｜2026-08-11｜2 来源
- [[concept/可穿戴 EEG]]：头带、眼罩、贴片、耳内 EEG 等非传统 PSG 形态，涵盖 34 种设备。`concept`｜2026-08-12｜2 来源
- [[concept/PSG 参考标准]]：多导睡眠图作为睡眠评估对照来源与人工评分变异。`concept`｜2026-08-12｜2 来源
- [[concept/临床验证]]：分期一致性→生理效应→主观终点→安全性/依从性的分层验证体系。`concept`｜2026-08-12｜2 来源
- [[concept/领域自适应]]：监督/半监督/无监督适应以应对分布偏移。`concept`｜2026-08-12｜1 来源
- [[concept/模型压缩与端侧部署]]：量化、剪枝、轻量结构与 NAS 用于可穿戴/IoT 端部署。`concept`｜2026-08-12｜1 来源

### 专题综述

- [[review/可穿戴睡眠检测与闭环干预综述|可穿戴 EEG-BCI 睡眠分期与闭环干预综述]]：从状态估计、实时闭环控制到临床验证的九章入口。`review`｜2026-08-12｜用户定位
- [[review/证据矩阵|证据矩阵]]：EEG 形态、PSG 参考、运行模式、时延、剂量与验证层级的唯一登记表。`review`｜2026-08-12｜规则与结构来源
- [[review/完整综述大纲|完整综述大纲]]：EEG-BCI 睡眠分期与闭环干预的摘要和九章层级写作框架。`review`｜2026-08-12｜基于综述地图与证据矩阵
- [[review/文献搜索策略_新版|文献搜索策略_新版]]：数据库、四条检索线、纳排标准和证据登记流程。`review`｜2026-08-13｜待执行正式检索
- [[review/chapters/01-引言|第 1 章：从睡眠监测到闭环干预]]：EEG-BCI 问题、范围与贡献。`review`｜2026-08-12｜用户定位
- [[review/chapters/02-基础理论与核心概念|第 2 章：状态估计与闭环控制]]：睡眠分期、N3/慢波与操作性定义。`review`｜2026-08-12｜用户定位
- [[review/chapters/03-可穿戴睡眠信号采集硬件体系|第 3 章：干电极 EEG 与信号可用性]]：单/双通道、伪影、PSG 参考与系统约束。`review`｜2026-08-12｜用户定位
- [[review/chapters/04-多模态睡眠检测算法|第 4 章：睡眠状态估计算法]]：传统 ML 至时序深度模型、融合与泛化。`review`｜2026-08-12｜用户定位
- [[review/chapters/05-可穿戴睡眠闭环干预技术|第 5 章：闭环睡眠干预算法]]：实时检测、触发时延、刺激剂量与失败保护。`review`｜2026-08-12｜用户定位
- [[review/chapters/06-现有研究对比|第 6 章：验证与研究对比]]：PSG 一致性、在线触发、生理/临床终点与安全性。`review`｜2026-08-12｜用户定位
- [[review/chapters/07-当前领域共性挑战|第 7 章：共性瓶颈]]：信号、域偏移、实时控制与临床转化。`review`｜2026-08-12｜用户定位
- [[review/chapters/08-未来研究展望|第 8 章：未来研究展望]]：由可追溯缺口导出的研究方向。`review`｜2026-08-12｜用户定位
- [[review/chapters/09-总结|第 9 章：总结]]：以检测可信度为闭环可信度前提的证据化归纳。`review`｜2026-08-12｜用户定位

### 其他目录

- `wiki/device/`：可穿戴设备、传感器与信号采集词条（待填充）。
- `wiki/intervention/`：睡眠闭环干预范式与系统词条（待填充）。
- `wiki/experiment/`：实验设置、指标和结果解读。
- `wiki/queries/`：高频问答沉淀。

## 使用说明

原始素材请放入 `raw/` 对应子目录；AI 将把可验证的知识整理至本目录。无法确定归属或需人工确认的内容放入 `pending/`。
