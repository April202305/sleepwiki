---
type: model
aliases: []
created: 2026-08-19
updated: 2026-08-19
sources: ["[[source-pages/zhu-2024-swsleepnet-online-calibration]]"]
review_sections: ["2.2"]
status: active
review_due: 2026-09-19
---
# SwSleepNet
## 基本信息
- 任务：离线分期与短片段在线预测
- 提出者/年份：Zhu等，2024
- 模型类别：可切换序列CNN
## 架构与输入输出
离线使用序列扩展/整合；在线用SCNN与SE处理2–5 s片段，预测不一致时引入上下文重判。[[source-pages/zhu-2024-swsleepnet-online-calibration]]
## 训练与实验设置
- 数据集：Sleep-EDFx、MASS、HSFU
## 主要结果
三库离线accuracy 84.5%、86.7%、81.8%；在线短片段accuracy均超过80%。
## 优点与局限
“校准”为上下文重判，不是概率校准。
## 关联概念与来源
- 概念：[[concept/睡眠分期]]、[[concept/时序上下文]]
- 来源：[[source-pages/zhu-2024-swsleepnet-online-calibration]]
## ⚠️待核实
- 短片段标签与30 s标签的时间对齐。
## 来源
- [[source-pages/zhu-2024-swsleepnet-online-calibration]]
