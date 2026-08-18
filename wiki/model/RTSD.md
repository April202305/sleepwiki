---
type: model
aliases: ["Real-Time Spindle Detector"]
created: 2026-08-18
updated: 2026-08-18
sources: ["source-pages/hassan-2022-real-time-spindle-detection"]
review_sections: ["2.2", "2.3", "4.2"]
status: active
review_due: 2027-08-18
---

# RTSD

## 基本信息
- 任务：多通道实时[[concept/睡眠纺锤波]]检测与相位触发
- 提出者/年份：Hassan、Feld、Bergmann，2022
- 模型类别：规则/信号处理与 phastimate 相位预测

## 架构与输入输出
每 10 ms 处理最近 520 ms 数据；相位模块以前向预测补偿固定软硬件偏移。[[source-pages/hassan-2022-real-time-spindle-detection]]（PDF 第 5–6 页）

## 优点与局限
- 预录午睡和整夜 EEG 实时回放中约 sensitivity 83%、precision 78%、F1 0.81。
- ⚠️不是实际睡眠中刺激验证；5–15 ms 不是系统总时延。

## 来源
- [[source-pages/hassan-2022-real-time-spindle-detection]]
