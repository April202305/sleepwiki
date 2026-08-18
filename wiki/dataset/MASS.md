---
type: dataset
aliases: ["Montreal Archive of Sleep Studies"]
created: 2026-08-18
updated: 2026-08-18
sources: ["source-pages/kulkarni-2019-real-time-spindle-detection", "source-pages/sun-2023-fpga-sleep-modulation"]
review_sections: ["2.2", "2.3"]
status: needs_review
review_due: 2027-08-18
---

# MASS

## 基本信息
- 发布机构/年份：待核实
- 数据规模：完整库约 200 份 PSG；Kulkarni 等仅使用 cohort subset #2 的 19 名健康受试者。
- 受试者：该子集为健康受试者。
- 信号与采样率：C3-参考耳 EEG；原 256 Hz，研究中重采样至 200 Hz。
- 标签标准：15 人由两位专家、4 人由一位专家标注纺锤波；研究以专家标注并集为真值。
- 获取方式/许可：待核实。

以上字段仅描述 Kulkarni 等所用子集。[[source-pages/kulkarni-2019-real-time-spindle-detection]]（HTML 正文 §2.1）

## 适用任务与常见划分

用于 [[concept/睡眠纺锤波]] 检测；[[model/SpindleNet]] 采用五折交叉验证。

## 已关联模型
- [[model/SpindleNet]]
- [[model/Sun FPGA 睡眠分期模型]]（SS2/SS3，共 81 人）

## 数据质量、偏差与局限
- ⚠️ 双专家/单专家标注混合，OR 与 AND 事件起点定义会改变检测延迟。
- ⚠️ 本页不能代表完整 MASS 的全部 cohort、通道或任务。

## 关联来源
- [[source-pages/kulkarni-2019-real-time-spindle-detection]]
- [[source-pages/sun-2023-fpga-sleep-modulation]]

## 来源
- [[source-pages/kulkarni-2019-real-time-spindle-detection]]
