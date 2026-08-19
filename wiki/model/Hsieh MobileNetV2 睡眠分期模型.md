---
type: model
aliases: ["Hsieh eye-mask MobileNetV2"]
created: 2026-08-19
updated: 2026-08-19
sources: ["[[source-pages/hsieh-2021-eyemask-real-time-staging]]"]
review_sections: ["2.2"]
status: active
review_due: 2026-09-19
---

# Hsieh MobileNetV2 睡眠分期模型

## 基本信息
- 任务：眼罩EEG/EOG四分类
- 提出者/年份：Hsieh 等，2021
- 模型类别：特征输入MobileNetV2

## 架构与输入输出
眼罩嵌入端提取时频特征，经BLE发送到移动端MobileNetV2完成实时阶段识别。[[source-pages/hsieh-2021-eyemask-real-time-staging]]

## 训练与实验设置
- 数据集：25名健康年轻成人同步PSG/眼罩记录
- 指标：一致性与睡眠参数

## 主要结果
支持眼罩—BLE—移动端实际运行链路。[[source-pages/hsieh-2021-eyemask-real-time-staging]]

## 优点与局限
具备移动端部署；四分类、小样本，未拆分完整端到端时延，严格零前视仍需保守解释。

## 关联概念与来源
- 概念：[[concept/模型压缩与端侧部署]]、[[concept/闭环系统时延]]
- 来源：[[source-pages/hsieh-2021-eyemask-real-time-staging]]

## ⚠️待核实
- 特征窗口是否包含未来样本。

## 来源
- [[source-pages/hsieh-2021-eyemask-real-time-staging]]
