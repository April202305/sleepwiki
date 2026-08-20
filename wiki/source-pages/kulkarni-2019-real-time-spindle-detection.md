---
type: source
aliases: ["Kulkarni 2019 SpindleNet"]
created: 2026-08-18
updated: 2026-08-20
sources: []
review_sections: ["2.2", "2.3", "4.2"]
status: active
review_due: 2027-08-18
---

# Kulkarni 等（2019）：实时睡眠纺锤波检测

## 基本信息
- 类型：论文（PMC 作者稿 HTML 全文）
- 原始文件：`raw/inbox/kulkarni-2019-real-time-spindle-detection.html`
- source_id：`raw/inbox/kulkarni-2019-real-time-spindle-detection.html`
- 作者/机构：Prathamesh M. Kulkarni、Zhengdong Xiao、Eric J. Robinson、Apoorva Sagarwa Jami、Jianping Zhang、Haocheng Zhou、Simon E. Henin、Anli A. Liu、Ricardo S. Osorio、Jing Wang、Zhe Chen
- 年份：2019
- 英文原题：A deep learning approach for real-time detection of sleep spindles
- 期刊/DOI：Journal of Neural Engineering 16(3):036004；10.1088/1741-2552/ab0933
- 录入日期：2026-08-18
- review_sections：["2.2", "2.3", "4.2"]

## 核心摘要

研究提出 [[model/SpindleNet]]，将卷积网络、单层 LSTM 与功率特征结合，对单通道 EEG 进行在线 [[concept/睡眠纺锤波]] 事件检测。在线窗口长 250 ms、步长 1 个样本；作者报告包含特征计算的平均执行时间约 6 ms，检测延迟约 150–350 ms。[[source-pages/kulkarni-2019-real-time-spindle-detection|本来源]]（HTML Abstract、正文 §2.3、§3.3）

## 方法与发现

- [[dataset/MASS]] 实验使用 cohort subset #2 的 19 名健康受试者、C3-参考耳导联及专家标注；15 人有两位专家、4 人有一位专家，多个标注取并集作为真值，并进行五折交叉验证。[[source-pages/kulkarni-2019-real-time-spindle-detection|本来源]]（HTML 正文 §2.1）
- [[dataset/DREAMS]] 使用 8 名存在不同睡眠问题受试者的 30 分钟 PSG 片段，采样率和导联不一并统一重采样至 200 Hz；其中 6 例仅有一位专家标注。[[source-pages/kulkarni-2019-real-time-spindle-detection|本来源]]（HTML 正文 §2.1）
- MASS 上，相对较早的 OR 标注起点平均检测延迟约 340 ms，相对较保守的 AND 起点约 205 ms；无噪声合成信号约 150 ms。专家起点本身存在约 0.167 s 的平均差异。[[source-pages/kulkarni-2019-real-time-spindle-detection|本来源]]（HTML 正文 §3.3）
- 论文还在老年人、儿童、癫痫颅内 EEG 和大鼠 LFP 上展示泛化，但部分数据没有可用真值，只能支持可运行性或定性展示，不能并入有标注检测性能比较。[[source-pages/kulkarni-2019-real-time-spindle-detection|本来源]]（HTML 正文 §2.1、§3.4–3.5）

## 关联词条
- 模型：[[model/SpindleNet]]
- 数据集：[[dataset/MASS]]、[[dataset/DREAMS]]
- 概念：[[concept/睡眠纺锤波]]
- 综述：[[review/文献清单/02-技术基础-2.2-文献需求单]]、[[review/证据包/02-技术基础-2.2-P1-证据包]]、[[review/文献清单/02-技术基础-2.3-文献需求单]]、[[review/证据包/02-技术基础-2.3-P1-证据包]]、[[review/chapters/02-基础理论与核心概念]]、[[review/证据矩阵]]

## 局限与待核实
- ⚠️ 这是事件级检测，不是睡眠阶段分类、慢波相位估计或刺激疗效验证。
- ⚠️ 150–350 ms 是相对专家事件起点的检测延迟，约 6 ms 是指定硬件上的执行时间；二者均不是采集至刺激执行的完整系统总时延。
- ⚠️ MASS 与 DREAMS 的人群、导联、标注人数和规则不同；作者也指出既有算法因训练集、样本量、通道及在线/离线模式不同而难以公平比较。
- ⚠️ HTML 表格结构不稳定，本次不转录无法可靠定位的汇总性能值；阶段 3 若需定量比较，应回查 Table 2。

## 新增综述需求入口

- [[review/文献清单/04-全周期-4.2-文献需求单]]

## 来源
- 专项比较：[[review/2.3形式化指标与系统比较表]]
- `raw/inbox/kulkarni-2019-real-time-spindle-detection.html`
