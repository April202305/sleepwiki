"""Deterministic exporter for this diagram's simple editable XML subset.
No browser / diagrams.net renderer is used. XML is the only semantic source.
"""
from pathlib import Path
import xml.etree.ElementTree as ET
import math, html
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
P=Path(__file__).parent
root=ET.parse(P/'sleep-closed-loop.drawio').getroot()
model=root.find('.//mxGraphModel');W=float(model.get('pageWidth'));H=float(model.get('pageHeight'))
pdfmetrics.registerFont(TTFont('SimHei','/Users/april/Library/Fonts/黑体.ttf'))
scale=170/25.4*72/W
c=canvas.Canvas(str(P/'sleep-closed-loop.pdf'),pagesize=(W*scale,H*scale))
c.setTitle('可穿戴睡眠闭环系统架构、决策逻辑与评价维度');c.scale(scale,scale)
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="170mm" height="{170*H/W}mm" viewBox="0 0 {W} {H}">','<rect width="100%" height="100%" fill="white"/>']
def props(cell):return dict(p.split('=',1) for p in cell.get('style','').split(';') if '=' in p)
def text(x,y,s,fs,align='middle',bold=False):
    c.setFillColor(HexColor('#263238'));c.setFont('SimHei',fs)
    # baseline conversion, text coordinates are center of text line
    if align=='middle':c.drawCentredString(x,H-y-fs*.35,s)
    else:c.drawString(x,H-y-fs*.35,s)
    svg.append(f'<text x="{x}" y="{y}" font-family="SimHei" font-size="{fs}" fill="#263238" text-anchor="{align}" dominant-baseline="central">{html.escape(s)}</text>')
def rect(x,y,w,h,fill,stroke,sw=2.2,rad=10):
    c.setLineWidth(sw)
    if fill!='none':c.setFillColor(HexColor(fill))
    if stroke!='none':c.setStrokeColor(HexColor(stroke))
    if fill!='none' or stroke!='none':c.roundRect(x,H-y-h,w,h,rad,stroke=int(stroke!='none'),fill=int(fill!='none'))
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rad}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
for cell in root.findall('.//mxCell[@vertex="1"]'):
    s=props(cell);g=cell.find('mxGeometry');x,y,w,h=[float(g.get(k)) for k in ['x','y','width','height']];fs=float(s.get('fontSize','28'))
    rect(x,y,w,h,s.get('fillColor','none'),s.get('strokeColor','none'))
    lines=cell.get('value','').split('\n');lh=fs*1.3
    for i,line in enumerate(lines):
        if pdfmetrics.stringWidth(line,'SimHei',fs)>w-10:print('TEXT_WIDTH',cell.get('id'),line)
        text(x+w/2,y+h/2+(i-(len(lines)-1)/2)*lh,line,fs)
for cell in root.findall('.//mxCell[@edge="1"]'):
    s=props(cell);g=cell.find('mxGeometry');sp=g.find("mxPoint[@as='sourcePoint']");tp=g.find("mxPoint[@as='targetPoint']")
    pts=[(float(p.get('x')),float(p.get('y'))) for p in [sp]+list(g.findall('./Array/mxPoint'))+[tp]]
    col=s.get('strokeColor','#263238');sw=float(s.get('strokeWidth','2.2'));dash=s.get('dashPattern','').split() if s.get('dashed')=='1' else []
    c.setStrokeColor(HexColor(col));c.setLineWidth(sw);c.setDash([float(x) for x in dash])
    path=c.beginPath();path.moveTo(pts[0][0],H-pts[0][1])
    for x,y in pts[1:]:path.lineTo(x,H-y)
    c.drawPath(path);c.setDash()
    svg.append(f'<polyline points="'+ ' '.join(f'{x},{y}' for x,y in pts)+f'" fill="none" stroke="{col}" stroke-width="{sw}" stroke-dasharray="'+','.join(dash)+'"/>')
    if s.get('endArrow')!='none':
        x,y=pts[-1];px,py=pts[-2];ang=math.atan2(y-py,x-px);a=12;b=5
        tri=[(x,y),(x-a*math.cos(ang)+b*math.sin(ang),y-a*math.sin(ang)-b*math.cos(ang)),(x-a*math.cos(ang)-b*math.sin(ang),y-a*math.sin(ang)+b*math.cos(ang))]
        path=c.beginPath();path.moveTo(tri[0][0],H-tri[0][1])
        for xx,yy in tri[1:]:path.lineTo(xx,H-yy)
        path.close();c.setFillColor(HexColor(col));c.drawPath(path,fill=1,stroke=0)
        svg.append('<polygon points="'+' '.join(f'{xx},{yy}' for xx,yy in tri)+f'" fill="{col}"/>')
    label=cell.get('value','')
    if label:
        lengths=[math.dist(a,b) for a,b in zip(pts,pts[1:])];half=sum(lengths)/2
        for (a,b),length in zip(zip(pts,pts[1:]),lengths):
            if half<=length:
                f=half/length;x=a[0]+f*(b[0]-a[0]);y=a[1]+f*(b[1]-a[1]);break
            half-=length
        fs=float(s.get('fontSize','26'));tw=pdfmetrics.stringWidth(label,'SimHei',fs)
        rect(x-tw/2-4,y-fs*.65,tw+8,fs*1.3,'#FFFFFF','none',rad=0);text(x,y,label,fs)
c.showPage();c.save()
svg.append('</svg>');(P/'sleep-closed-loop.svg').write_text('\n'.join(svg))
