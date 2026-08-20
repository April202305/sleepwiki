---
type: dataset
aliases: ["DREAMS Sleep Spindles Database"]
created: 2026-08-18
updated: 2026-08-20
sources: ["source-pages/kulkarni-2019-real-time-spindle-detection"]
review_sections: ["2.2"]
status: needs_review
review_due: 2027-08-18
---

# DREAMS

## 基本信息
- 发布机构/年份：待核实
- 数据规模：Kulkarni 等使用 8 名受试者各 30 分钟 PSG 片段。
- 受试者：存在不同睡眠问题的患者。
- 信号与采样率：C3-A1 等导联；原采样率 50–200 Hz，研究中统一至 200 Hz。
- 标签标准：专家纺锤波标注；6 例只有一位专家标注，多标注时取并集。
- 获取方式/许可：待核实。

[[source-pages/kulkarni-2019-real-time-spindle-detection]]（HTML 正文 §2.1）

## 适用任务与常见划分

用于 [[concept/睡眠纺锤波]] 检测与 [[model/SpindleNet]] 外部数据测试。

## 已关联模型
- [[model/SpindleNet]]

## 数据质量、偏差与局限
- ⚠️ 受试者病理、导联、原采样率及专家标注数量不统一，不能与 [[dataset/MASS]] 直接合并比较。
- ⚠️ 本页仅依据一篇应用论文，数据库正式题录与许可待核实。

## 关联来源
- [[source-pages/kulkarni-2019-real-time-spindle-detection]]

## 来源
- [[source-pages/kulkarni-2019-real-time-spindle-detection]]
- [[review/2.2公开数据集、标签体系与验证协议比较表]]
