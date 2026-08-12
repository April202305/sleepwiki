---
type: model
aliases: ["SCNet", "Single Channel Net"]
created: 2026-08-11
updated: 2026-08-11
sources: ["source-pages/zhou-2022-singlechannelnet"]
status: active
review_due: 2027-08-11
---

# SingleChannelNet

## 基本信息
- 任务：[[concept/睡眠分期]]五分类
- 提出者/年份：Zhou 等，2022
- 模型类别：原始单通道 EEG 深层 CNN

## 架构与输入输出

模型以 90 秒原始 [[concept/单通道 EEG]] 为输入，包含多尺度卷积块和 M-Apooling，不使用手工特征、滤波或重采样；其训练数据的阶段分布存在 [[concept/类别不平衡]]。[[source-pages/zhou-2022-singlechannelnet|Zhou 等（2022）]]（PDF 第 3–4、6 页）

## 训练与实验设置
- 数据集：[[dataset/CCSHS|CCSHS]]、[[dataset/Sleep-EDF|Sleep-EDF]]
- 指标：准确率、precision、recall、F1、Cohen's κ。[[source-pages/zhou-2022-singlechannelnet|Zhou 等（2022）]]（PDF 第 4 页，式 1–7）
- 划分：报告 epoch-wise 和 subject-wise 两种方案；解读时须区分两者。[[source-pages/zhou-2022-singlechannelnet|Zhou 等（2022）]]（PDF 第 5–6 页，Tables 7–8）

## 主要结果

epoch-wise 设置下：CCSHS ACC 90.2%、κ 86.5%；Sleep-EDF ACC 86.1%、κ 80.5%。[[source-pages/zhou-2022-singlechannelnet|Zhou 等（2022）]]（PDF 第 5 页，Tables 3–4）

## 优点与局限

- 90 秒 [[concept/时序上下文]] 相比 30 秒输入提高同数据集性能。[[source-pages/zhou-2022-singlechannelnet|Zhou 等（2022）]]（PDF 第 5–6 页，Tables 3–6）
- ⚠️ 跨 [[concept/跨数据集泛化]] 的直接测试仅达 65.9% 与 70.2% 准确率，说明未解决数据域差异。[[source-pages/zhou-2022-singlechannelnet|Zhou 等（2022）]]（PDF 第 6 页）

## 来源
- [[source-pages/zhou-2022-singlechannelnet|Zhou 等（2022）]]

## 综述关联
- [[review/证据矩阵|证据矩阵]]
- [[review/chapters/04-多模态睡眠检测算法|多模态睡眠检测算法]]
- [[concept/PSG 参考标准]]、[[concept/临床验证]]、[[concept/可穿戴 EEG]]、[[concept/模型压缩与端侧部署]]
- [[review/完整综述大纲]]
