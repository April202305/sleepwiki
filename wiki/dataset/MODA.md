---
type: dataset
aliases: ["Massive Online Data Annotation", "MODA spindle dataset"]
created: 2026-08-20
updated: 2026-08-20
sources: ["source-pages/valenchon-2022-portiloop"]
review_sections: ["2.2", "2.3"]
status: needs_review
review_due: 2026-09-20
---

# MODA

## 基本信息
- 发布机构/年份：MODA项目；数据集原始论文题录待单独Ingest。
- 数据规模：MASS子集，phase 1为100名较年轻受试者、phase 2为80名较年长受试者，共约24 h标注信号。[[source-pages/valenchon-2022-portiloop]]（PDF第4、8–9页）
- 受试者：合计180人；具体纳入标准与夜数待数据集原始来源核验。
- 信号与采样率：MASS来源EEG；Portiloop应用中的确切导联和原始采样率待核验。
- 标签标准：平均约5名专家标注每段并给置信度，形成连续平均分数和经阈值/后处理得到的二值纺锤标签；专家相对最终标签的平均F1约0.72。[[source-pages/valenchon-2022-portiloop]]（PDF第4、8页）
- 获取方式/许可：Portiloop研究经数据库科学委员会审批；公开获取方式待核验。

## 适用任务与常见划分

用于纺锤波事件检测、阈值—precision/recall—检测延迟以及年轻/年长子集泛化评估。Portiloop按受试者划分验证集和测试集，各约10%。[[source-pages/valenchon-2022-portiloop]]（PDF第8、11–15页）

## 已关联模型
- [[device/Portiloop]]
- [[model/SpindleNet]]（Portiloop研究按同一MODA管线重训的基线）

## 数据质量、偏差与局限
- 只有约5%的信号被标为纺锤，类别高度不平衡。[[source-pages/valenchon-2022-portiloop]]（PDF第8–9页）
- ⚠️MODA仍是专家共识而非无误差真值；事件数“5,342”尚未由当前全文可靠定位，不能写入正式表。
- ⚠️现有验证基于标注数据回放，不是佩戴Portiloop获得的新人体在线刺激数据。

## 关联来源
- [[source-pages/valenchon-2022-portiloop]]
- [[review/2.2公开数据集、标签体系与验证协议比较表]]

## 来源
- [[source-pages/valenchon-2022-portiloop]]
