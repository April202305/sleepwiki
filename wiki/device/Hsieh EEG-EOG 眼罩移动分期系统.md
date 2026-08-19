---
type: device
aliases: ["Hsieh eye-mask sleep staging system"]
created: 2026-08-19
updated: 2026-08-19
sources: ["[[source-pages/hsieh-2021-eyemask-real-time-staging]]"]
review_sections: ["2.1", "2.2", "2.3"]
status: active
review_due: 2026-09-19
---

# Hsieh EEG-EOG 眼罩移动分期系统

## 基本信息
- 设备类型：眼罩
- 生理模态：EEG、EOG、加速度
- EEG 形态：干电极
- 通道与导联：额部EEG与右侧EOG
- 采样与佩戴信息：ADS1299；250 Hz至16 kHz；整机约74 g

## 信号质量与噪声
- 与 PSG 或湿电极 EEG 的参考/同步方案：25名健康受试者同步mini-PSG
- 伪影类型与处理：特征级处理；细节见来源页

## 可用于的睡眠任务
眼罩端特征提取、BLE传输和移动端四类睡眠分期。

## 性能与比较条件
在线模式约9.5 h；未拆分端到端时延。[[source-pages/hsieh-2021-eyemask-real-time-staging]]

## 关联来源
- [[source-pages/hsieh-2021-eyemask-real-time-staging]]

## ⚠️局限与待核实
- 健康年轻人小样本；四分类；严格因果窗口与功耗细项待核实。

## 来源
- [[source-pages/hsieh-2021-eyemask-real-time-staging]]
