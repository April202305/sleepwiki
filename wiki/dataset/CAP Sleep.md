---
type: dataset
aliases: ["CAP", "CAP Sleep Database", "Cyclic Alternating Pattern Sleep Database"]
created: 2026-08-20
updated: 2026-08-20
sources: ["source-pages/nam-2024-insightsleepnet"]
review_sections: ["2.2"]
status: needs_review
review_due: 2026-09-20
---

# CAP Sleep

## 基本信息
- 发布机构/年份：PhysioNet；正式数据集题录与版本待核验。
- 数据规模：InsightSleepNet使用24名睡眠障碍患者的PPG子集；完整库记录数待数据集原始来源核验。[[source-pages/nam-2024-insightsleepnet]]（PDF第6页，Table 1）
- 受试者：该应用子集含失眠5人、夜间额叶癫痫8人、REM相关疾病等共24人。[[source-pages/nam-2024-insightsleepnet]]（PDF第6页）
- 信号与采样率：该应用只提取PPG，并重采样至约34.3 Hz；完整PSG导联和原始采样率待核验。[[source-pages/nam-2024-insightsleepnet]]（PDF第6–7页）
- 标签标准：应用研究映射为四分类；原始标签标准和评分者数量待核验。
- 获取方式/许可：公开数据库；具体许可待核验。

## 适用任务与常见划分

当前来源只支持病理人群PPG四分类与选择性预测，不足以支撑CAP微结构、K-complex或EEG在线因果评测。[[source-pages/nam-2024-insightsleepnet]]（PDF第3–8页）

## 已关联模型
- [[model/InsightSleepNet]]

## 数据质量、偏差与局限
- ⚠️24人是特定应用子集，不等于完整CAP Sleep数据库规模。
- ⚠️现有准入证据为PPG而非核心EEG；不能据此填写完整PSG导联、CAP微结构标签或事件时间戳。

## 关联来源
- [[source-pages/nam-2024-insightsleepnet]]
- [[review/2.2公开数据集、标签体系与验证协议比较表]]

## 来源
- [[source-pages/nam-2024-insightsleepnet]]
