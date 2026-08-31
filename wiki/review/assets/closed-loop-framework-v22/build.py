"""Author editable diagram; export separately from the XML source of truth."""
from pathlib import Path
import xml.etree.ElementTree as E
P=Path(__file__).parent
root=E.Element('mxfile',host='app.diagrams.net',version='26.0.9')
d=E.SubElement(root,'diagram',id='sleep-framework',name='闭环系统与安全决策')
m=E.SubElement(d,'mxGraphModel',page='1',pageWidth='1700',pageHeight='1330',grid='1',gridSize='10')
r=E.SubElement(m,'root'); E.SubElement(r,'mxCell',id='0');E.SubElement(r,'mxCell',id='1',parent='0')
nodes={}
def box(id,x,y,w,h,text,fill='#EAF0F6',size=28,stroke='#63758A',bold=False):
    style=f'rounded=1;arcSize=8;whiteSpace=wrap;html=0;fontFamily=SimHei;fontSize={size};fontColor=#263238;fillColor={fill};strokeColor={stroke};strokeWidth=2.2;align=center;verticalAlign=middle;spacing=8;'
    if bold:style+='fontStyle=1;'
    c=E.SubElement(r,'mxCell',id=id,value=text,style=style,vertex='1',parent='1');E.SubElement(c,'mxGeometry',x=str(x),y=str(y),width=str(w),height=str(h),attrib={'as':'geometry'});nodes[id]=(x,y,w,h)
def txt(id,x,y,w,h,text,size=28,bold=False):box(id,x,y,w,h,text,'none',size,'none',bold)
def edge(id,s,t,points,label='',kind='main'):
    dash={'main':'','safe':'dashed=1;dashPattern=12 3;','adapt':'dashed=1;dashPattern=4 5;','log':'dashed=1;dashPattern=2 5;'}[kind]
    col='#263238' if kind=='main' else '#6B7280'
    sx,sy,sw,sh=nodes[s];tx,ty,tw,th=nodes[t];p,q=points[0],points[-1]
    st=f'html=0;rounded=0;noEdgeStyle=1;fontFamily=SimHei;fontSize=26;strokeColor={col};strokeWidth=2.2;endArrow={"none" if kind=="log" else "block"};endSize=9;endFill=1;labelBackgroundColor=#FFFFFF;'+dash
    st+=f'exitX={(p[0]-sx)/sw};exitY={(p[1]-sy)/sh};entryX={(q[0]-tx)/tw};entryY={(q[1]-ty)/th};exitPerimeter=0;entryPerimeter=0;'
    c=E.SubElement(r,'mxCell',id=id,source=s,target=t,value=label,style=st,edge='1',parent='1')
    g=E.SubElement(c,'mxGeometry',relative='1',attrib={'as':'geometry'})
    E.SubElement(g,'mxPoint',x=str(p[0]),y=str(p[1]),attrib={'as':'sourcePoint'});E.SubElement(g,'mxPoint',x=str(q[0]),y=str(q[1]),attrib={'as':'targetPoint'})
    ar=E.SubElement(g,'Array',attrib={'as':'points'})
    for x,y in points[1:-1]:E.SubElement(ar,'mxPoint',x=str(x),y=str(y))

txt('a_title',40,15,1620,60,'(a) 可穿戴睡眠闭环系统架构',42,True)
for i,(title,body) in enumerate([
('采集与质控','EEG主信号\n因果处理与质控'),('在线识别','阶段／事件／相位\n按任务选用'),('决策与安全门控','触发、拒绝或暂停\n条件详见(b)'),('刺激执行','物理输出作用于\n睡眠中的受试者'),('响应监测','持续采集信号\n脑电响应／觉醒')]):
    x=40+i*340;box('a'+str(i),x,210,260,145,title+'\n'+body,'#EAF0F6' if i<3 else '#E5F1E3',28)
for i,label in enumerate(['信号','估计','指令','响应']):edge('a_flow'+str(i),'a'+str(i),'a'+str(i+1),[(300+i*340,285),(380+i*340,285)],label)
edge('a_safety','a4','a2',[(1490,210),(1490,155),(920,155),(920,210)],'安全反馈：暂停／拒绝／恢复判断','safe')
edge('a_adapt','a4','a2',[(1600,210),(1600,95),(785,95),(785,210)],'可选自适应更新：需系统级验证','adapt')
txt('optional',40,110,620,80,'可选辅助信号\nEOG、EMG、PPG、加速度',26)
box('evaltitle',40,435,1620,55,'独立记录与验证层：本文组织的评价维度','#F1D7D4',30,'#B44948')
for i,lab in enumerate(['信号质量\n有效数据／伪影','在线识别\n任务性能／置信度','命中与时延\n物理到达／时延','运行与安全\n失败夜／拒绝／停机','生理与功能结局\n短窗／整夜／长期']):
    box('eval'+str(i),40+i*340,520,260,105,lab,'#F2F3F5',27,'#9AA1A8')
# All stage logs connect to the shared reporting layer; no control arrows.
for i in range(5):
    x=170+i*340
    edge('log_in'+str(i),'a'+str(i),'evaltitle',[(x,355),(x,435)],'日志' if i==0 else '', 'log')
    edge('log_out'+str(i),'evaltitle','eval'+str(i),[(x,490),(x,520)],'', 'log')
txt('evalnote',40,635,1620,48,'结合运行日志与独立结局测量；评价不等于实时反馈，各维度不代表均已验证。',27)

txt('b_title',40,705,1620,60,'(b) 闭环决策与安全反馈',42,True)
txt('b_input',40,770,1620,45,'输入：信号质量、睡眠阶段、事件或相位、置信度、既往刺激与剂量记录',27)
for i,lab in enumerate(['准入检查\n质量与状态\n是否满足条件？','目标条件检查\n按范式选用\n阶段／事件／相位','时机与剂量检查\n预设时机、间隔\n及剂量限制','生成刺激指令\n执行刺激\n持续监测响应','刺激后检查\n觉醒与信号状态\n决定暂停或重判']):box('b'+str(i),40+i*340,855,260,145,lab,'#EAF0F6' if i<3 else '#E5F1E3',28)
for i in range(4):edge('b_flow'+str(i),'b'+str(i),'b'+str(i+1),[(300+i*340,925),(380+i*340,925)],'通过' if i<3 else '响应')
edge('next_cycle','b4','b0',[(1530,855),(1530,835),(170,835),(170,855)],'未触发暂停：下一轮重新判断','safe')
box('reject',40,1085,940,80,'不满足条件：拒绝／等待 → 获取更新信息后重新判断','#F2F3F5',28,'#9AA1A8')
for i in range(3):edge('reject'+str(i),'b'+str(i),'reject',[(170+i*340,1000),(170+i*340,1085)],'否')
box('pause',1120,1085,540,80,'风险触发：暂停\n满足恢复条件后重新判断','#F2F3F5',28,'#9AA1A8')
edge('pause_e','b4','pause',[(1530,1000),(1530,1085)],'风险','safe')
edge('recheck','reject','b0',[(40,1125),(15,1125),(15,925),(40,925)],'','safe')
edge('resume','pause','b0',[(1390,1165),(1390,1205),(170,1205),(170,1165)],'满足恢复条件后重新判断','safe')
# Resume ends on reject node because it is the explicitly shared recheck route.
c=r.find("mxCell[@id='resume']");c.set('target','reject');c.set('style',c.get('style').split('entryX=')[0]+'entryX=0.1383;entryY=1;entryPerimeter=0;')
txt('bnote',40,1230,1620,45,'综合控制框架，非单一系统算法；响应驱动的参数更新见(a)虚线路径。',26)
txt('legend',40,1280,1620,40,'图例：实线＝主流程   长虚线＝安全反馈   短虚线＝可选更新   点线＝日志关联',26)
E.indent(root)
E.ElementTree(root).write(P/'sleep-closed-loop.drawio',encoding='utf-8',xml_declaration=True)
