---
type: dataset
aliases: ["SIESTA sleep database"]
created: 2026-08-19
updated: 2026-08-19
sources: ["[[source-pages/bresch-2018-real-time-rnn-staging]]"]
review_sections: ["2.2"]
status: active
review_due: 2026-09-19
---

# SIESTA

## 基本信息
- 发布机构/年份：待核实
- 数据规模：294名受试者、每人2夜，共588夜
- 受试者：临床睡眠实验室人群，具体构成待核实
- 信号与采样率：PSG；Bresch使用C3-M2并重采样至100 Hz
- 标签标准：R&K共识评分，S3/S4合并为N3
- 获取方式/许可：待核实

## 适用任务与常见划分
睡眠分期内部验证和跨数据库泛化测试。[[source-pages/bresch-2018-real-time-rnn-staging]]

## 已关联模型
- [[model/Bresch 因果 CNN-LSTM 睡眠分期模型]]

## 数据质量、偏差与局限
与居家额部EEG数据库在人群、导联和采集环境上存在域差异。

## 关联来源
- [[source-pages/bresch-2018-real-time-rnn-staging]]

## ⚠️待核实
- 原始数据库许可、疾病构成和评分者协议。

## 来源
- [[source-pages/bresch-2018-real-time-rnn-staging]]
