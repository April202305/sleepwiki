---
type: dataset
aliases: ["ISRUC", "ISRUC-S3"]
created: 2026-08-20
updated: 2026-08-20
sources: ["source-pages/hu-2024-mtff-net"]
review_sections: ["2.2"]
status: needs_review
review_due: 2026-09-20
---

# ISRUC-Sleep

## 基本信息
- 发布机构/年份：待数据集原始来源核验。
- 数据规模：现有全文只直接支撑MTFF-Net使用ISRUC-S3；完整三队列、总受试者数和夜数待核验。
- 受试者：ISRUC-S3具体人群构成待数据集原始来源核验。
- 信号与采样率：应用研究使用EEG、ECG、EOG和EMG时频输入；原始通道配置与采样率待核验。[[source-pages/hu-2024-mtff-net]]（PDF第1、6–8页）
- 标签标准：五分类；标准版本和评分者数量待核验。
- 获取方式/许可：待核验。

## 适用任务与常见划分

当前可作为多模态离线五分类的应用数据集；不直接代表单导可穿戴EEG、在线因果分期或闭环刺激验证。[[source-pages/hu-2024-mtff-net]]（PDF第1、6–8页）

## 已关联模型
- MTFF-Net（见[[source-pages/hu-2024-mtff-net]]）

## 数据质量、偏差与局限
- ⚠️尚未Ingest数据集原始论文/正式说明，三队列118名、双专家评分等总库字段不得进入正文定量表。
- ⚠️应用研究为多模态、离线、双向模型条件，与单导因果可穿戴系统不可直接比较。

## 关联来源
- [[source-pages/hu-2024-mtff-net]]
- [[review/2.2公开数据集、标签体系与验证协议比较表]]

## 来源
- [[source-pages/hu-2024-mtff-net]]
