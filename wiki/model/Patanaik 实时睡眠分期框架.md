---
type: model
aliases: ["real-time automatic sleep stage classification framework"]
created: 2026-08-18
updated: 2026-08-18
sources: ["source-pages/patanaik-2018-end-to-end-real-time-sleep-staging"]
review_sections: ["2.2", "2.3"]
status: active
review_due: 2027-08-18
---

# Patanaik 实时睡眠分期框架

## 基本信息
- 任务：[[concept/睡眠分期]]
- 提出者/年份：Patanaik 等，2018
- 模型类别：频谱图深度 CNN + MLP 上下文修正；客户端—服务器架构

## 架构与输入输出

EEG/EOG 的 30 秒 epoch 经滤波、100 Hz 重采样和频谱图转换后进入 16 层 CNN；第二模块根据相邻 epoch 的类别概率修正 W/N1/N2/N3/REM 输出。[[source-pages/patanaik-2018-end-to-end-real-time-sleep-staging]]（PDF 第 3–4 页）

## 训练与实验设置
- 数据集：四组研究内 PSG 队列，共 11,727 小时、1,403,164 epoch。
- 指标：总体准确率、Cohen's κ、各阶段性能。

## 主要结果

测试集准确率 89.8%、κ=0.862；独立睡眠障碍队列为 81.4%、κ=0.740，帕金森病队列为 72.1%、κ=0.597。CPU 单 epoch 计算少于 5 ms。[[source-pages/patanaik-2018-end-to-end-real-time-sleep-staging]]（PDF 第 5–7 页）

## 优点与局限
- 提供状态级在线输出及独立临床队列验证。
- ⚠️ 离线使用前后各 5 个 epoch，在线以既往输出替代未来输出；两种模式不能混写。
- ⚠️ 实时刺激示例采用双向滤波，不能据此声称全链路严格因果。
- ⚠️ 计算速度不是端到端触发时延，也不代表刺激疗效。

## 关联概念与来源
- 概念：[[concept/睡眠分期]]、[[concept/时序上下文]]、[[concept/PSG 参考标准]]
- 来源：[[source-pages/patanaik-2018-end-to-end-real-time-sleep-staging]]
- 综述：[[review/chapters/02-基础理论与核心概念]]、[[review/证据矩阵]]

## 来源
- [[source-pages/patanaik-2018-end-to-end-real-time-sleep-staging]]
