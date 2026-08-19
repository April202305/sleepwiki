---
type: source
aliases: ["Bresch 2018 causal sleep staging"]
created: 2026-08-19
updated: 2026-08-19
sources: []
review_sections: ["2.2"]
status: active
review_due: 2026-09-19
---

# Bresch 等（2018）：单通道 EEG 因果循环网络睡眠分期

## 基本信息
- 类型：论文
- 原始文件：`raw/inbox/bresch-2018-real-time-rnn-staging.pdf`
- source_id：`raw/inbox/bresch-2018-real-time-rnn-staging.pdf`
- 作者/机构：Erik Bresch、Udo Großekathöfer、Gary Garcia-Molina
- 年份：2018
- 英文原题：Recurrent Deep Neural Networks for Real-Time Sleep Stage Classification From Single Channel EEG
- 录入日期：2026-08-19
- review_sections：[`2.2`]

## 核心摘要

研究以单通道 EEG 的 30 s epoch 为输入，使用卷积层和单向 LSTM 逐时步输出五分类，明确将其描述为 causal sleep staging。内部数据含 29 名健康受试者的 147 夜记录，三折验证按受试者拆分；另以 294 名受试者、588 夜的 SIESTA 数据进行训练、验证和跨数据库测试。[[source-pages/bresch-2018-real-time-rnn-staging]]（PDF 第 2–3、8–9 页）

## 方法与发现

- 基线网络约 9 万参数，采用 CNN 后接两层 LSTM；每个时步对应当前 30 s epoch，结构本身不需要未来 epoch。[[source-pages/bresch-2018-real-time-rnn-staging]]（PDF 第 3、10 页，Figure 2）
- 内部数据三折交叉验证按受试者划分，报告 κ 约 0.73；N1 仅占 2.5%，基线中未被检出，显示总体 κ 不能替代少数类别评价。[[source-pages/bresch-2018-real-time-rnn-staging]]（PDF 第 3–5 页，Figures 3–4）
- SIESTA 内部验证 κ 为 0.760±0.022；跨库时，SIESTA→内部数据库 κ 为 0.703，而内部数据库→SIESTA κ 为 0.454，提示训练规模和域偏移影响泛化。[[source-pages/bresch-2018-real-time-rnn-staging]]（PDF 第 8–9 页，Tables 4–5）

## 关联词条
- 模型：[[model/Bresch 因果 CNN-LSTM 睡眠分期模型]]
- 数据集：[[dataset/SIESTA]]
- 概念：[[concept/睡眠分期]]、[[concept/跨数据集泛化]]、[[concept/类别不平衡]]

## 局限与待核实
- ⚠️论文支持因果架构和低延迟可行性，但主要结果来自离线交叉验证/跨库实验；未报告采集—预处理—推理—通信的真实人体端到端在线时延，不能计为“真实在线实测”完整证据。
- ⚠️滤波实现的在线因果性和目标端硬件功耗未完整报告。

## 来源
- `raw/inbox/bresch-2018-real-time-rnn-staging.pdf`
