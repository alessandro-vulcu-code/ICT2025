"""Clarify Lesson 8's seven diagrams as SVG and PNG.

Original qualitative profiles and mechanisms are retained; labels and layout are redesigned.
Requires rsvg-convert; source crops remain available for comparison.
"""
from pathlib import Path
import html
import re
import subprocess

ROOT = Path(__file__).resolve().parent
PINK = '#ed39d5'
ORANGE = '#ff7829'
PURPLE = '#c548e8'
YELLOW = '#ffe9a0'
BLACK = '#171717'

class Drawing:
    def __init__(self, name, width, height):
        self.name, self.width, self.height = name, width, height
        self.parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<title>{html.escape(name)} — clarified schematic diagram</title>
<desc>Qualitative redraw of the student's original diagram. Positions are graphical coordinates, not measured numerical data.</desc>
<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M1 1 L9 5 L1 9" fill="none" stroke="context-stroke" stroke-width="1.3"/></marker>
<pattern id="orange" width="17" height="17" patternUnits="userSpaceOnUse" patternTransform="rotate(32)"><path d="M0 0 V17" stroke="{ORANGE}" stroke-width="3"/></pattern>
<pattern id="purple" width="19" height="19" patternUnits="userSpaceOnUse" patternTransform="rotate(28)"><path d="M0 0 V19" stroke="{PURPLE}" stroke-width="3"/></pattern>
<pattern id="grey" width="25" height="25" patternUnits="userSpaceOnUse" patternTransform="rotate(35)"><path d="M0 0 V25" stroke="#8a8a8a" stroke-width="2"/></pattern>
</defs><rect width="100%" height="100%" fill="white"/>
<g font-family="DejaVu Sans, sans-serif" font-size="24" fill="{BLACK}" stroke-linecap="round" stroke-linejoin="round">''']
    def path(self, d, color=BLACK, width=2.5, fill='none', dash=None, arrow=False):
        extra = (f' stroke-dasharray="{dash}"' if dash else '') + (' marker-end="url(#arrow)"' if arrow else '')
        self.parts.append(f'<path d="{d}" fill="{fill}" stroke="{color}" stroke-width="{width}"{extra}/>')
    def line(self,x1,y1,x2,y2,color=BLACK,width=2.5,**kw): self.path(f'M{x1} {y1} L{x2} {y2}',color,width,**kw)
    def text(self,x,y,s,size=24,color=BLACK,anchor='start'):
        # Inline subscripts use _{...}, avoiding reliance on Unicode subscript fonts.
        chunks=re.split(r'(_\{[^}]+\})',s)
        out=''.join(f'<tspan baseline-shift="sub" font-size="70%">{html.escape(c[2:-1])}</tspan>' if c.startswith('_{') else html.escape(c) for c in chunks)
        self.parts.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}">{out}</text>')
    def rect(self,x,y,w,h,fill='none',color=BLACK,width=2.5):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{color}" stroke-width="{width}"/>')
    def axes(self,x,y,right,top):
        self.line(x-25,y,right,y,arrow=True)
        self.line(x,y+22,x,top,arrow=True)
    def brace(self,x1,x2,y,label):
        mid=(x1+x2)/2
        self.path(f'M{x1} {y} Q{x1} {y+12} {x1+15} {y+12} L{mid-16} {y+12} Q{mid} {y+12} {mid} {y+22} Q{mid} {y+12} {mid+16} {y+12} L{x2-15} {y+12} Q{x2} {y+12} {x2} {y}')
        self.text(mid,y+49,label,anchor='middle')
    def save(self):
        svg=ROOT/f'{self.name}-redrawn.svg'
        svg.write_text('\n'.join(self.parts)+ '\n</g></svg>\n')
        subprocess.run(['rsvg-convert','-w',str(self.width*2),'-o',str(svg.with_suffix('.png')),str(svg)],check=True)

# Consistent visual grammar: pink input, dashed blue output, orange queue,
# green recovered credits. All profiles are schematic, with no numerical time scale.
BLUE = '#2463a7'
GREEN = '#228971'
LIGHT_ORANGE = '#ffead6'
LIGHT_GREEN = '#d9f0e7'
GREY = '#8693a3'

def legend(d, y=69, queue=True, recovery=False):
    d.line(100,y-6,142,y-6,PINK,4)
    d.text(154,y,'Input G(t)',19)
    d.line(330,y-6,372,y-6,BLUE,4,dash='9 6')
    d.text(384,y,'Shaper output',19)
    if queue:
        d.rect(615,y-20,28,19,LIGHT_ORANGE,color=ORANGE,width=1)
        d.text(655,y,'Buffered data',19)
    if recovery:
        d.rect(850,y-20,28,19,LIGHT_GREEN,color=GREEN,width=1)
        d.text(890,y,'Recovered tokens',19)

def guide(d,x,y1,y2,label,ylabel):
    d.line(x,y1,x,y2,GREY,1.3,dash='5 6')
    d.text(x,ylabel,label,18,anchor='middle')

def title(d,s): d.text(45,35,s,25)

def rate_axes(d,base=330,top=112,right=1050):
    d.axes(100,base,right,top)
    d.text(65,top+6,'Rate',17,anchor='end')
    d.text(right+9,base+8,'t',20)

def ref(d,y,label,right=1030):
    d.line(100,y,right,y,GREY,1.3,dash='7 7')
    d.text(85,y+6,label,20,anchor='end')

def sample_path(path):
    tokens=re.findall(r'[MCLHV]|-?\d+(?:\.\d+)?',path)
    i=0; pts=[]; x=y=0
    while i<len(tokens):
        cmd=tokens[i]; i+=1
        n={'M':2,'L':2,'C':6,'H':1,'V':1}[cmd]
        a=list(map(float,tokens[i:i+n])); i+=n
        if cmd=='C':
            for j in range(1,81):
                t=j/80; u=1-t
                pts.append((u**3*x+3*u*u*t*a[0]+3*u*t*t*a[2]+t**3*a[4],u**3*y+3*u*u*t*a[1]+3*u*t*t*a[3]+t**3*a[5]))
            x,y=a[4:]
        else:
            if cmd=='H': x=a[0]
            elif cmd=='V': y=a[0]
            else:x,y=a
            pts.append((x,y))
    return pts

def svgline(points):
    return 'M'+' L'.join(f'{x:.3f} {y:.3f}' for x,y in points)

def queue_regions(d,path,start,rho):
    pts=sample_path(path)
    # Use fine interpolation for all segments, including horizontal plateaus.
    dense=[]
    for (x0,y0),(x1,y1) in zip(pts,pts[1:]):
        for j in range(max(1,int((x1-x0)*4))):
            t=j/max(1,int((x1-x0)*4)); dense.append((x0+(x1-x0)*t,y0+(y1-y0)*t))
    dense.append(pts[-1])
    active=[(x,y) for x,y in dense if x>=start]
    area=0; region=[(start,active[0][1])]; cross=None; end=None
    for (x0,y0),(x1,y1) in zip(active,active[1:]):
        da=(rho-(y0+y1)/2)*(x1-x0)
        if cross is None and y1>=rho:
            cross=(x1,y1); growth=region+[(x1,rho)]
        if area+da<=0 and area>0 and cross:
            frac=area/(-da)
            end=(x0+frac*(x1-x0),y0+frac*(y1-y0)); region.append(end); break
        area+=da; region.append((x1,y1))
    assert cross and end
    grow=[p for p in region if p[0]<=cross[0]]
    drain=[p for p in region if p[0]>=cross[0]]
    d.path(svgline([(start,rho)]+grow+[(cross[0],rho)])+' Z',color='none',width=0,fill=LIGHT_ORANGE)
    d.path(svgline([(cross[0],rho)]+drain+[(end[0],rho)])+' Z',color='none',width=0,fill='#e2edf8')
    tail=[end]+[p for p in dense if p[0]>end[0]]
    return end,svgline(tail)


# 1. Same topology, named components; formulas stay next to their components.
d=Drawing('01-shaper-and-link',1120,370)
title(d,'Token bucket shaper and output link')
for x,w,name,detail,col in [(70,165,'Input buffer','B_{i}',ORANGE),(320,160,'Shaper','',BLUE),(570,170,'Output buffer','B_{o}',ORANGE),(835,170,'Link','capacity c',BLUE)]:
    d.rect(x,193,w,78,fill='#f5f8fc',color=col,width=2)
    d.text(x+w/2,224,name,21,anchor='middle')
    d.text(x+w/2,252,detail,19,anchor='middle')
for x1,x2 in [(235,310),(480,560),(740,825),(1005,1075)]:d.line(x1,232,x2,232,BLUE,2.5,arrow=True)
d.text(24,178,'G(t)',20)
d.line(24,232,60,232,PINK,3,arrow=True)
d.text(520,208,'λ_{out}',21,BLUE,anchor='middle')
d.text(1061,208,'λ_{f}',21,BLUE,anchor='middle')
d.path('M335 89 L345 137 H455 L465 89',BLUE,2.5)
for x in range(359,450,23):
    d.parts.append(f'<circle cx="{x}" cy="121" r="5" fill="{GREEN}"/>')
d.line(400,57,400,87,GREEN,2.5,arrow=True)
d.text(428,77,'ρ = λ',21,GREEN)
d.line(400,140,400,183,GREEN,2.5,arrow=True)
d.text(503,125,'b = (λ_{p} − ρ)T_{b}',22)
d.text(152,322,'B_{i} = (λ_{p} − ρ)T_{g}',20,anchor='middle')
d.text(710,322,'B_{o} = (λ_{p} − c)T_{b}',20,anchor='middle')
d.text(710,349,'for ρ < c < λ_{p}',17,GREY,anchor='middle')
d.save()

# 2. Input keeps the original overshoot, shoulder and low-rate tail.
# Isolate curve identities and signed areas instead of copying margin prose.
d=Drawing('02-above-declared-peak',1120,535)
title(d,'Input exceeds the declared peak')
legend(d)
rate_axes(d)
ref(d,160,'λ_{p}')
ref(d,245,'ρ = λ')
pre='M100 295 C145 302 190 303 220 277 C245 251 260 246 285 245 C340 245 355 246 375 207 C399 162 410 161 445 160 C464 160 481 142 495 137'
post='C510 130 520 145 521 155 C527 163 548 160 576 164 C603 166 610 170 614 192 C618 208 635 203 639 218 C644 235 641 239 650 245 C675 249 688 257 710 275 C738 300 767 315 800 317 H1040'
(t2,y2),tail=queue_regions(d,pre+post,495,245)
d.path(pre+post,PINK,3.5)
d.path(pre+f' L495 245 H{t2} L{t2} {y2}'+tail[tail.index(' L'):],BLUE,4,dash='10 7')
# area below the output is explicitly distinguished from queue growth.
d.rect(495,249,155,80,fill='url(#purple)',color='none',width=0)
guide(d,495,121,360,'t_{0}',390)
guide(d,650,205,360,'t_{1}',390)
guide(d,t2,245,360,'t_{2}',390)
d.text(527,198,'queue grows',18,ORANGE)
d.text(705,276,'queue drains',18,BLUE)
d.text(507,314,'forwarded',17,PURPLE)
d.text(100,441,'t_{0}: tokens exhausted',19)
d.text(426,441,'t_{1}: input drops below ρ',19)
d.text(774,441,'t_{2}: queue empty',19)
d.text(100,487,'Area added to the queue = area served later above the input (no loss).',19,GREY)
d.save()

# 3. Same lower hump, dip and rebound; output visibly separates at exhaustion.
d=Drawing('03-below-declared-peak',1120,535)
title(d,'Above the mean, below the declared peak')
legend(d)
rate_axes(d)
ref(d,142,'λ_{p}')
ref(d,245,'ρ = λ')
pre='M100 295 C147 301 181 280 200 253 C205 245 213 245 225 245 H280 C305 246 323 237 338 208 C357 175 390 176 430 172 C478 168 525 165 568 169'
post='C609 174 621 215 638 240 C665 278 687 298 714 297 C738 297 745 275 770 279 C793 282 802 297 830 299 C860 302 878 300 900 296 H1040'
(t2,y2),tail=queue_regions(d,pre+post,568,245)
d.path(pre+post,PINK,3.5)
d.path(pre+f' V245 H{t2} V{y2}'+tail[tail.index(' L'):],BLUE,4,dash='10 7')
for x in (280,510,568,t2):
    d.line(x,153 if x<t2 else 245,x,355,GREY,1.2,dash='5 6')
# Stagger nearby labels to avoid collisions.
d.text(280,385,'burst starts',17,anchor='middle')
d.text(510,418,'T_{b} reference',17,anchor='end')
d.text(580,385,'tokens exhausted',17)
d.text(t2+20,418,'queue empty',17,anchor='middle')
d.text(100,478,'b / (λ̃ − ρ)  >  T_{b} = b / (λ_{p} − ρ)',25)
d.text(100,511,'A lower burst rate consumes stored tokens more slowly.',18,GREY)
d.save()

# 4. Keep packet-level view; compressed time is explicit, no invented packet count.
d=Drawing('04-sensor-packets',1120,315)
title(d,'Sensor packets: same size, different spacing')
d.text(45,73,'W = 512 bytes per packet',19,GREY)
for x,w,label,col in [(90,250,'Normal',LIGHT_GREEN),(360,180,'Alarm',LIGHT_ORANGE),(560,250,'Normal',LIGHT_GREEN),(830,180,'Alarm',LIGHT_ORANGE)]:
    d.rect(x,95,w,132,fill=col,color='none',width=0)
    d.text(x+w/2,120,label,19,anchor='middle')
d.line(75,222,1055,222,arrow=True)
d.text(1067,228,'t',21)
for x in [110,205,300,375,395,415,435,455,475,495,515,580,675,770,845,865,885,905,925,945,965,985]:
    d.line(x,218,x,147,PINK,3)
d.text(215,261,'1 packet / minute',19,anchor='middle')
d.text(450,261,'1 packet / second',19,anchor='middle')
d.text(685,261,'1 packet / minute',19,anchor='middle')
d.text(920,261,'1 packet / second',19,anchor='middle')
d.text(450,292,'D = 30 s',18,anchor='middle')
d.text(920,292,'D = 30 s',18,anchor='middle')
d.save()

# 5. Two equal-width alarm rectangles, correctly identified baseline and full area.
d=Drawing('05-sensor-fluid-profile',1120,480)
title(d,'Fluid model of the sensor source')
d.text(45,73,'Rate in bytes/minute; time in minutes',18,GREY)
rate_axes(d,base=330,top=105)
ref(d,140,'λ_{p}')
d.text(86,277,'λ_{L}',21,anchor='end')
d.rect(340,140,85,190,LIGHT_ORANGE,color='none',width=0)
d.path('M100 270 H340 V140 H425 V270 H790 V140 H875 V270 H1030',PINK,3.5)
d.text(340,118,'30 720',20,anchor='middle')
d.text(175,261,'512',20)
d.text(455,195,'Alarm traffic: A = λ_{p}D',22,ORANGE)
d.path('M450 202 Q416 211 395 229',ORANGE,2,arrow=True)
d.brace(340,425,342,'D = 0.5')
d.brace(790,875,342,'D = 0.5')
d.brace(340,790,412,'δ: alarm start → next alarm start')
d.save()

# 6. Original sequence: one fully forwarded alarm immediately followed by
# another alarm. Stored tokens run out at the boundary, not before the first.
d=Drawing('06-empty-bucket-alarm',1120,550)
title(d,'Two consecutive alarms: tokens run out between them')
legend(d)
rate_axes(d,base=330,top=110)
ref(d,145,'λ_{p}')
ref(d,250,'ρ = λ')
d.text(85,306,'λ_{L}',20,anchor='end')
d.rect(260,145,260,185,'#f6e4fb',color='none',width=0)
d.rect(520,145,260,105,LIGHT_ORANGE,color='none',width=0)
d.rect(520,250,260,80,'#e2edf8',color='none',width=0)
d.path('M100 300 H260 V145 H780 V300 H1040',PINK,3.5)
d.path('M100 300 H260 V145 H520 V250 H1030',BLUE,4,dash='10 7')
d.text(390,215,'Forwarded',22,BLUE,anchor='middle')
d.text(390,249,'A = λ_{p}T_{b}',23,BLUE,anchor='middle')
d.text(650,186,'Buffered',21,ORANGE,anchor='middle')
d.text(650,221,'(λ_{p} − ρ)T_{b}',23,ORANGE,anchor='middle')
d.text(650,300,'Forwarded: ρT_{b}',20,BLUE,anchor='middle')
for x,label in [(260,'0'),(520,'D = T_{b}'),(780,'2T_{b}')]:
    guide(d,x,145,349,label,377)
d.text(885,235,'queue drains',18,BLUE)
d.brace(260,520,396,'first alarm')
d.brace(520,780,396,'second alarm')
d.text(260,487,'Full bucket',19,GREEN,anchor='middle')
d.text(520,487,'Empty bucket',19,ORANGE,anchor='middle')
d.text(100,532,'Second alarm: A = ρT_{b} + (λ_{p} − ρ)T_{b}; no recovery time between alarms (δ = 0).',20)
d.save()

# 7. Shared time axis across rates, credits and queue: same two-alarm mechanism.
# Equal-width alarms. Graphic ratios obey net token/queue balance; no numeric
# waiting time is claimed. t=0 is the END of the first alarm, as in the notes.
d=Drawing('07-board-two-alarms',1120,930)
title(d,'Two alarms: token recovery, exhaustion and buffering')
legend(d,recovery=True)
d.text(45,106,'1  Traffic rates',21)
rate_axes(d,base=325,top=117)
ref(d,140,'λ_{p}')
ref(d,245,'ρ = λ')
d.text(86,291,'λ_{L}',20,anchor='end')
# Peak excess is 105 px; token refill is 40 px per time unit. A 210 px
# normal interval buys 80 px at peak; both alarms last 160 px.
x0,x1,x2,x3,x4=290,500,580,660,870
# recovery area = (245..285)×210 = 8400; initial burst advantage = 105×80.
d.rect(x0,245,x1-x0,40,LIGHT_GREEN,color='none',width=0)
d.rect(x2,140,x3-x2,105,LIGHT_ORANGE,color='none',width=0)
d.path(f'M100 285 H130 V140 H{x0} V285 H{x1} V140 H{x3} V285 H1040',PINK,3.5)
d.path(f'M100 285 H130 V140 H{x0} V285 H{x1} V140 H{x2} V245 H{x4} V285 H1040',BLUE,4,dash='10 7')
d.text(370,271,'b(δ)',22,GREEN)
d.text(620,190,'β(δ)',22,ORANGE,anchor='middle')
for x in (x0,x1,x2,x3,x4):d.line(x,125,x,790,GREY,1,dash='4 7')
d.brace(130,x0,338,'first alarm')
d.brace(x0,x1,338,'δ')
d.brace(x1,x3,338,'T_{b}')
d.text(45,442,'2  Tokens in the bucket',21)
d.axes(100,560,1050,455)
d.text(84,474,'b',21,anchor='end')
d.text(68,566,'0',19,anchor='end')
# Full b at first alarm start, zero at t=0; partial refill before second alarm.
d.path(f'M130 470 L{x0} 560 L{x1} 515 L{x2} 560 H{x4} L1040 523',GREEN,3.5)
d.path(f'M{x0} 560 L{x1} 515 V560 Z',color='none',width=0,fill=LIGHT_GREEN)
d.text(410,493,'b(δ) < b',22,GREEN)
d.line(x1,601,x2,601,BLUE,2)
d.line(x1,595,x1,607,BLUE,2)
d.line(x2,595,x2,607,BLUE,2)
d.text((x1+x2)/2,632,'T′',22,BLUE,anchor='middle')
d.text(45,678,'3  Input backlog',21)
d.axes(100,790,1050,690)
d.text(68,795,'0',19,anchor='end')
d.path(f'M100 790 H{x2} L{x3} 730 L{x4} 790 H1040',ORANGE,3.5)
d.path(f'M{x2} 790 L{x3} 730 L{x4} 790 Z',color='none',width=0,fill=LIGHT_ORANGE)
d.text(686,717,'β(δ)',23,ORANGE)
for x,label in [(x0,'0'),(x1,'δ'),(x2,'δ + T′'),(x3,'δ + T_{b}'),(x4,'queue empty')]:
    d.text(x,827,label,18,anchor='middle')
d.text(100,873,'T′ = b(δ) / (λ_{p} − ρ)',24)
d.text(580,873,'β(δ) = (λ_{p} − ρ)(T_{b} − T′)',24)
d.text(100,911,'Schematic case: 0 < T′ < T_{b}; input queue initially empty.',18,GREY)
d.save()
