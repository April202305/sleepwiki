---
type: source
aliases: ["Hsieh 2021 eye-mask real-time staging"]
created: 2026-08-19
updated: 2026-08-22
sources: []
review_sections: ["2.1", "2.2", "2.3"]
status: active
review_due: 2026-09-19
---

# Hsieh 等（2021）：眼罩与移动端实时睡眠分期系统

## 基本信息
- 类型：论文
- 原始文件：`raw/inbox/hsieh-2021-eyemask-real-time-staging.pdf`
- source_id：`raw/inbox/hsieh-2021-eyemask-real-time-staging.pdf`
- 作者/机构：Tsung-Hao Hsieh 等；National Cheng Kung University
- 年份：2021
- 英文原题：Home-Use and Real-Time Sleep-Staging System Based on Eye Masks and Mobile Devices with a Deep Learning Model
- 录入日期：2026-08-19
- review_sections：[`2.1`, `2.2`, `2.3`]

## 题录与引用字段
- 题录状态：已核验
- 核验来源：Crossref（DOI 10.1007/s40846-021-00649-5），核验日 2026-08-22
- 文献语种：英文
- 作者（原始顺序）：Tsung-Hao Hsieh; Meng-Hsuan Liu; Chin-En Kuo; Yung-Hung Wang; Sheng-Fu Liang
- 原始题名：Home-Use and Real-Time Sleep-Staging System Based on Eye Masks and Mobile Devices with a Deep Learning Model
- 文献类型标识：[J/OL]
- 载体或容器题名：Journal of Medical and Biological Engineering
- 出版年：2021
- 卷：41
- 期：5
- 起止页码：659-668
- 文章号：
- 出版地：
- 出版者：
- 编辑：
- 会议名称：
- 会议地点：
- 会议日期：
- DOI：10.1007/s40846-021-00649-5
- URL：https://doi.org/10.1007/s40846-021-00649-5
- 发表或更新日期：2021-09-04
- 引用日期：2026-08-22
- 补充标识：
- 核验备注：
- Word 成稿引用：HSIEH T, LIU M, KUO C, 等. Home-Use and Real-Time Sleep-Staging System Based on Eye Masks and Mobile Devices with a Deep Learning Model[J/OL]. Journal of Medical and Biological Engineering, 2021, 41(5): 659-668. DOI:10.1007/s40846-021-00649-5.

## 核心摘要

研究构建额部 EEG/EOG 眼罩—BLE—移动端 MobileNetV2 分期系统，并以25名健康年轻成人同步 PSG 记录训练和验证。眼罩端执行预处理与特征提取，移动设备接收特征并实时分类。[[source-pages/hsieh-2021-eyemask-real-time-staging]]（PDF 第 2–5 页，Figures 1–4）

## 方法与发现

- 眼罩记录额部 EEG 与右侧 EOG；模块采用 nRF52840、ADS1299，支持250 Hz至16 kHz采样，在线边缘计算模式连续运行约9.5 h。[[source-pages/hsieh-2021-eyemask-real-time-staging]]（PDF 第 3页，Table 1）
- 25名受试者各完成一夜同步记录；PSG人工标签用作参考，研究采用leave-one-out验证并将睡眠分为四类。[[source-pages/hsieh-2021-eyemask-real-time-staging]]（PDF 第 4–7 页）
- 系统展示眼罩端特征提取、BLE传输和移动端推理的运行链，但未将采集、窗口等待、特征、通信和推理分别计时。[[source-pages/hsieh-2021-eyemask-real-time-staging]]（PDF 第 2–3、8–9 页）

## 关联词条
- 设备：[[device/Hsieh EEG-EOG 眼罩移动分期系统]]
- 模型：[[model/Hsieh MobileNetV2 睡眠分期模型]]
- 概念：[[concept/可穿戴 EEG]]、[[concept/模型压缩与端侧部署]]、[[concept/闭环系统时延]]

## 局限与待核实
- ⚠️样本为单中心健康年轻人且为四分类，不等同于AASM五分类临床泛化。
- ⚠️系统具备真实链路运行证据，但没有完整端到端时延拆分；MobileNetV2对当前输出是否使用未来epoch需按特征窗口解释，不能据“real-time”题名直接认定严格零前视。

## 来源
- `raw/inbox/hsieh-2021-eyemask-real-time-staging.pdf`
