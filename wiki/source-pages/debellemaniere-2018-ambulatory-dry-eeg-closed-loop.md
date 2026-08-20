---
type: source
aliases: ["Debellemaniere 2018", "WDD closed-loop study"]
created: 2026-08-17
updated: 2026-08-20
sources: ["raw/inbox/debellemaniere-2018-ambulatory-dry-eeg-closed-loop.pdf"]
review_sections: ["1.2", "2.3", "3.1"]
status: active
review_due: 2027-08-17
---

# Debellemaniere 等（2018）：居家干电极 EEG 的听觉闭环慢振荡刺激

## 基本信息
- 类型：人体设备验证与居家观察性试点
- 原始文件：`raw/inbox/debellemaniere-2018-ambulatory-dry-eeg-closed-loop.pdf`
- source_id：`raw/inbox/debellemaniere-2018-ambulatory-dry-eeg-closed-loop.pdf`
- DOI：10.3389/fnhum.2018.00088
- 英文原题：Performance of an Ambulatory Dry-EEG Device for Auditory Closed-Loop Stimulation of Sleep Slow Oscillations in the Home Environment
- review_sections：["1.2", "2.3", "3.1"]

## 核心摘要
该研究验证无线干电极 [[device/Wireless Dreem Device]] 的居家链路：实时 N3 检测→慢振荡上升相声音触发。20 名健康青年在迷你 PSG 配对、随机双盲交叉条件下进行验证；实时 N3 检测灵敏度/特异度为 0.70/0.90，上升相靶向准确性为 45±52°。另有 90 名中年人的居家观察性试点。[[intervention/闭环听觉刺激]]（PDF 第 1 页）

## 方法与发现
- 系统以睡眠状态变化、觉醒或唤醒作为停止刺激的情形；研究明确了居家无人监测下的失败保护需求。[[device/Wireless Dreem Device]]（PDF 第 2 页）
- 在线链路每0.5 s估计一次信号质量，以30 s窗口判断N3，慢波相位拟合约保留5 s等效记忆；稳定N3 15 min后才开始刺激，大运动后3 min内不刺激，首个N3检测4 h后停止。声音以两次50 ms骨传导刺激为一组，不连续刺激超过两个慢振荡，两组之间至少间隔9 s；刺激后6 s内检测到运动或alpha活动则暂停30 s。[[source-pages/debellemaniere-2018-ambulatory-dry-eeg-closed-loop|本来源]]（PDF 第4–7页，Figure 3）
- N3门控在42,302个epoch中得到TP 8,610、FP 3,017、FN 3,666和TN 27,009，对应敏感度0.70、特异度0.90、precision 0.74及accuracy 0.84。研究记录17,786次真实刺激和17,579次sham；合并后86.1%位于N3、11.0%位于N2、0.4%位于N1、1.4%位于REM、1.1%位于清醒。[[source-pages/debellemaniere-2018-ambulatory-dry-eeg-closed-loop|本来源]]（PDF 第8–9页，Tables 2–3）
- WDD与PSG使用独立且未同步的时钟；温度等因素可造成整夜采样漂移，8 h末时间差可达秒级。研究采用每10 min分块的事后重同步，因此该结果不能证明在线共同时间基准或声音到耳端到端时延。[[source-pages/debellemaniere-2018-ambulatory-dry-eeg-closed-loop|本来源]]（PDF 第7页）
- ⚠️该结果是设备/即时生理响应与可行性证据，不能替代长期临床疗效。[[intervention/闭环听觉刺激]]（PDF 第 1 页）

## 关联词条
- 设备：[[device/Wireless Dreem Device]]
- 干预：[[intervention/闭环听觉刺激]]
- 综述：[[review/chapters/01-引言]]、[[review/文献清单/01-引言-1.2-文献需求单]]、[[review/证据包/01-引言-1.2-P1-证据包]]、[[review/文献清单/01-引言-1.3-文献需求单]]、[[review/证据包/01-引言-1.3-P1-证据包]]、[[review/文献清单/02-技术基础-2.1-文献需求单]]、[[review/证据包/02-技术基础-2.1-P1-证据包]]、[[review/文献清单/02-技术基础-2.3-文献需求单]]、[[review/证据包/02-技术基础-2.3-P1-证据包]]、[[review/文献清单/03-慢波干预-3.1-文献需求单]]、[[review/证据包/03-慢波干预-3.1-P1-证据包]]、[[review/证据矩阵]]

## ⚠️局限与待核实
- ⚠️总时延、误/漏触发和刺激剂量的完整拆分仍须在阶段 3 从全文逐项提取。

## 新增综述需求入口

- [[review/文献清单/04-全周期-4.5-文献需求单]]
- [[review/文献清单/05-系统形态-5.1-文献需求单]]
- [[review/文献清单/05-系统形态-5.4-文献需求单]]
- [[review/文献清单/06-挑战展望-6.4-文献需求单]]
- [[review/文献清单/06-挑战展望-6.5-文献需求单]]

## 来源
- 专项比较：[[review/2.3形式化指标与系统比较表]]
- `raw/inbox/debellemaniere-2018-ambulatory-dry-eeg-closed-loop.pdf`
