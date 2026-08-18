---
type: source
aliases: ["Patanaik 2018 real-time sleep staging"]
created: 2026-08-18
updated: 2026-08-18
sources: []
review_sections: ["2.2", "2.3"]
status: active
review_due: 2027-08-18
---

# Patanaik 等（2018）：实时自动睡眠分期端到端框架

## 基本信息
- 类型：论文
- 原始文件：`raw/inbox/patanaik-2018-end-to-end-real-time-sleep-staging.pdf`
- source_id：`raw/inbox/patanaik-2018-end-to-end-real-time-sleep-staging.pdf`
- 作者/机构：Amiya Patanaik、Ju Lynn Ong、Joshua J. Gooley、Sonia Ancoli-Israel、Michael W. L. Chee
- 年份：2018
- 英文原题：An end-to-end framework for real-time automatic sleep stage classification
- 期刊/DOI：SLEEP；10.1093/sleep/zsy041
- 录入日期：2026-08-18
- review_sections：["2.2", "2.3"]

## 核心摘要

研究提出客户端—服务器式 [[model/Patanaik 实时睡眠分期框架]]，从 EEG/EOG 的 30 秒 epoch 频谱图输出 W、N1、N2、N3、REM 五分类，并在四组 PSG 数据、共 11,727 小时和 1,403,164 个 epoch 上训练或验证。[[source-pages/patanaik-2018-end-to-end-real-time-sleep-staging|本来源]]（PDF 第 1–5 页）

## 方法与发现

- DS1 与 DS2 合计 1,330 份 PSG，按 75%/25% 分为训练和测试；DS3 为 210 名临床睡眠障碍患者，DS4 为 77 名帕金森病患者，作为独立验证。输入使用 C3-A2/C4-A1 的平均 EEG（可用时）及双侧 EOG，预处理后降采样至 100 Hz。[[source-pages/patanaik-2018-end-to-end-real-time-sleep-staging|本来源]]（PDF 第 2–4 页）
- 第一模块为 16 层深度 CNN，第二模块以相邻 epoch 的类别概率做上下文修正；模型共 178,114 个可调参数。离线模式使用当前 epoch 前后各 5 个输出；在线缺少后续 epoch 时，以此前 5 个输出再次填充，因此在线运行与离线上下文并不相同。[[source-pages/patanaik-2018-end-to-end-real-time-sleep-staging|本来源]]（PDF 第 4 页）
- 训练、测试、DS3、DS4 的总体准确率分别为 90.0%、89.8%、81.4%、72.1%，Cohen's κ 分别为 0.865、0.862、0.740、0.597；临床队列尤其是帕金森病/REM 睡眠行为障碍情境下 REM 表现下降。[[source-pages/patanaik-2018-end-to-end-real-time-sleep-staging|本来源]]（PDF 第 5–7 页，Table 2、Figure 2）
- 单个 epoch 在 CPU 上计算少于 5 ms，约 8.5 小时记录包含格式转换、传输和服务器返回在内约 5 秒；GPU 单 epoch 少于 1 ms。上述是计算/整夜处理速度，不是采集—决策—刺激执行的端到端时延。[[source-pages/patanaik-2018-end-to-end-real-time-sleep-staging|本来源]]（PDF 第 7 页）
- 实时声音刺激示例用 30 秒滚动缓冲区、每秒评分一次；文中说明滤波在时间正反两个方向执行以避免相位延迟，故该示例不能直接作为严格零前视、严格因果处理的证明。[[source-pages/patanaik-2018-end-to-end-real-time-sleep-staging|本来源]]（PDF 第 5 页）

## 关联词条
- 模型：[[model/Patanaik 实时睡眠分期框架]]
- 概念：[[concept/睡眠分期]]、[[concept/PSG 参考标准]]、[[concept/时序上下文]]
- 综述：[[review/02-技术基础-2.2-文献需求单]]、[[review/02-技术基础-2.2-P1-证据包]]、[[review/02-技术基础-2.3-文献需求单]]、[[review/02-技术基础-2.3-P1-证据包]]、[[review/chapters/02-基础理论与核心概念]]、[[review/证据矩阵]]

## 局限与待核实
- ⚠️ 在线上下文替代策略与双向滤波使“严格因果、完全不使用未来样本”的范围需要分模块说明，不能仅凭题名中的 real-time 推定。
- ⚠️ DS3/DS4 的疾病构成导致域偏移；四组结果不可视为同一人群性能。
- ⚠️ 论文只展示自动刺激功能，刺激结果另行研究；本资料不能证明生理或临床疗效。
- ⚠️ 未完整报告采集、缓冲、预处理、通信、决策和刺激执行的分段及统一总时延。

## 来源
- `raw/inbox/patanaik-2018-end-to-end-real-time-sleep-staging.pdf`
