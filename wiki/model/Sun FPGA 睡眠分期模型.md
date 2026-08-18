---
type: model
aliases: ["FPGA-accelerated sleep staging model"]
created: 2026-08-18
updated: 2026-08-18
sources: ["source-pages/sun-2023-fpga-sleep-modulation"]
review_sections: ["2.2", "2.3"]
status: active
review_due: 2027-08-18
---

# Sun FPGA 睡眠分期模型

## 基本信息
- 任务：单通道五类[[concept/睡眠分期]]
- 提出者/年份：Sun 等，2023
- 模型类别：双 CNN + 双向 LSTM；8 位量化 FPGA 实现

## 训练与实验设置
- 数据集：[[dataset/MASS]] SS2/SS3，共 81 名受试者
- 结果：平均准确率 85.8%、macro-F1 79%；20 MHz 下 20 秒输入处理少于 1 秒。[[source-pages/sun-2023-fpga-sleep-modulation]]（HTML §III–IV）

## 优点与局限
- ⚠️闭环仅台架展示；引擎吞吐量不是端到端时延，双向 LSTM 的在线可用边界需保留。

## 来源
- [[source-pages/sun-2023-fpga-sleep-modulation]]
