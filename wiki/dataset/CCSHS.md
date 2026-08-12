---
type: dataset
aliases: ["Cleveland Children's Sleep and Health Study"]
created: 2026-08-11
updated: 2026-08-11
sources: ["source-pages/zhou-2022-singlechannelnet"]
status: active
review_due: 2027-08-11
---

# CCSHS

## 基本信息
- 发布机构/年份：Cleveland Children's Sleep and Health Study；具体发布信息待核实。
- 数据规模：Zhou 等使用 515 名儿童队列的过夜 PSG 记录。（PDF 第 2 页）
- 受试者：儿科队列。[[source-pages/zhou-2022-singlechannelnet|Zhou 等（2022）]]（PDF 第 2 页）
- 信号与采样率：实验使用 C4/A1 单通道 EEG，128 Hz。[[source-pages/zhou-2022-singlechannelnet|Zhou 等（2022）]]（PDF 第 2–4 页）
- 标签标准：论文称 hypnogram 按 R&K 标注。[[source-pages/zhou-2022-singlechannelnet|Zhou 等（2022）]]（PDF 第 2 页）
- 获取方式/许可：待核实。

## 适用任务与常见划分

用于 [[concept/睡眠分期]] 五分类；论文以 C4/A1 [[concept/单通道 EEG]] 的 [[concept/时序上下文]] 输入进行实验，并报告 5 折交叉验证以及 subject-wise、epoch-wise 方案。[[source-pages/zhou-2022-singlechannelnet|Zhou 等（2022）]]（PDF 第 4–6 页）

## 已关联模型
- [[model/SingleChannelNet|SingleChannelNet]]

## 数据质量、偏差与局限

- ⚠️ 儿科队列与成人数据集的人群差异可能影响 [[concept/跨数据集泛化]]，且其阶段样本分布涉及 [[concept/类别不平衡]]；该点需更多直接证据验证。

## 来源
- [[source-pages/zhou-2022-singlechannelnet|Zhou 等（2022）]]

## 综述关联
- [[review/证据矩阵|证据矩阵]]
- [[concept/PSG 参考标准]]
