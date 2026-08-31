# v22图1：文件与编辑入口

- 可编辑主文件：`sleep-closed-loop.drawio`。文字、模块与连接箭头均为独立对象；用draw.io/diagrams.net打开，需安装SimHei（黑体）字体以保持布局。
- 论文引用文件：`sleep-closed-loop.pdf`（矢量、17 cm宽）。
- 预览：`sleep-closed-loop.png`（300 dpi）。
- 编辑后须重新导出PDF和PNG，再编译论文；仅保存drawio不会自动更新已编译论文。
- `build.py`是初始布局生成脚本。手工修改drawio后不要直接运行此脚本，以免覆盖手工调整。
- `export_xml.py`仅支持当前图的简化XML图形子集。复杂编辑后应优先用draw.io原生导出，并重新检查17 cm可读性。

2026-08-31：已插入`../../格式/闭环睡眠干预综述-v22.tex`作为图1，位于编译PDF第6页（正文页码4）。原TeX和PDF备份位于`../../格式/backups/v22-before-dual-panel-20260831/`。

排版检查：图宽170 mm；图中文字统一黑体，模块约7.94 pt、注释最小约7.37 pt，面板标题约11.9 pt。图题沿用论文宏：中文黑体9 pt、英文Times New Roman加粗9 pt，基线间距10.8 pt。源文件静态检查通过；原生draw.io渲染仍未复核，当前PDF与PNG采用同源XML导出。
