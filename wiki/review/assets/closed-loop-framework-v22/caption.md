# 建议图题与使用说明

图X 可穿戴睡眠闭环系统架构、决策逻辑与评价维度。（a）从信号采集与质控到刺激后响应监测的系统链路及独立记录与验证层；（b）刺激准入、目标条件、时机与剂量检查及暂停和恢复逻辑。辅助模态与识别任务按具体系统和刺激范式选用；响应驱动的参数更新属于可选路径，需系统级验证。本图为本文综合的控制与评价框架，不代表单一系统已实现全部功能，也不表示各评价维度均已获得验证。

英文图题：Wearable sleep closed-loop system architecture, decision logic, and evaluation dimensions.

依据：当前 `../../格式/闭环睡眠干预综述-v22.tex` 第1.2—1.4节、第2章、第4.5节、第5.4节。详细依据见同目录brief.md；未新增性能数据或外部研究结论。

LaTeX使用：在通栏figure*环境中调用 `\includegraphics[width=\textwidth]{sleep-closed-loop.pdf}`，建议最终宽度约170 mm。若实际栏宽更小，应重新检查字号，不建议缩为单栏。

全部文字、节点与箭头在sleep-closed-loop.drawio中为可编辑对象。PDF为嵌入中文字体的矢量导出，PNG为300 dpi预览。导出工具为本目录export_xml.py，不是draw.io原生渲染器；在draw.io打开后，应复核字体、换行和箭头标签布局。未替换v22正文原图。
