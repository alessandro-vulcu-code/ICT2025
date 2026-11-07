"""Reproduce Lesson 3 diagrams. Qualitative curves use drawing paths, not data/models.

Run with Python, Matplotlib and NumPy. PNG embeds and editable vector SVGs are
saved beside this script; source crops remain unchanged. Normalized drawing
coordinates are layout only. No random samples or fitted functions are used.
"""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/nm-lesson3-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, PathPatch, Ellipse
from matplotlib.path import Path as MPath

HERE = Path(__file__).resolve().parent
INK = '#243345'
RED = '#df3e43'
GREEN = '#80b940'
PURPLE = '#ae4fe0'
MAGENTA = '#ed36d2'
CYAN = '#79d3d5'
plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':13,
                     'text.color':INK, 'axes.labelcolor':INK,
                     'xtick.color':INK, 'ytick.color':INK,
                     'axes.spines.top':False, 'axes.spines.right':False,
                     'svg.fonttype':'none'})

def save(fig, name):
    for ext in ('png', 'svg'):
        fig.savefig(HERE / f'{name}-redrawn.{ext}', dpi=210,
                    facecolor='white', bbox_inches='tight', pad_inches=.22)
    plt.close(fig)

def canvas(w=8, h=4):
    fig, ax = plt.subplots(figsize=(w,h))
    return fig, ax

def schematic(ax, label='Schematic — not measured data'):
    ax.text(1,1.04,label,ha='right',va='bottom',transform=ax.transAxes,
            fontsize=10,color='#667589')

def arrow(ax, a, b, color=INK, style='-', lw=1.8, head='->'):
    ax.annotate('',xy=b,xytext=a,
                arrowprops=dict(arrowstyle=head,color=color,lw=lw,
                                linestyle=style,shrinkA=0,shrinkB=0))

def poly_arrow(ax, points, color=INK, style='-'):
    xs,ys=zip(*points[:-1])
    ax.plot(xs,ys,color=color,lw=1.8,linestyle=style)
    arrow(ax,points[-2],points[-1],color,style)

def box(ax, xy, width, height, label, color=INK):
    ax.add_patch(FancyBboxPatch(xy,width,height,
                 boxstyle='round,pad=0.015,rounding_size=0.045',
                 ec=color,fc='white',lw=1.8))
    ax.text(xy[0]+width/2,xy[1]+height/2,label,
            ha='center',va='center',color=color,fontsize=13)

def curve(ax, verts, color, lw=2.6, alpha=1):
    # A source-faithful illustrative Bezier path, not a numerical fit.
    codes=[MPath.MOVETO]+[MPath.CURVE4]*(len(verts)-1)
    ax.add_patch(PathPatch(MPath(verts,codes),fill=False,ec=color,
                           lw=lw,alpha=alpha,capstyle='round'))

def axes_clean(ax, xlim=(0,1), ylim=(0,1)):
    ax.set_xlim(*xlim);ax.set_ylim(*ylim)
    for s in ('left','bottom'):
        ax.spines[s].set_color(INK)
        ax.spines[s].set_linewidth(1.3)
    ax.tick_params(length=5)
    for a,b in [((.985,0),(1.025,0)),((0,.985),(0,1.025))]:
        ax.annotate('',xy=b,xytext=a,xycoords='axes fraction',
                    arrowprops=dict(arrowstyle='->',color=INK,lw=1.3),
                    annotation_clip=False)

# 01: topology and control/data paths. Layout mirrors the handwritten panel.
fig,ax=canvas(12,4.6)
ax.set(xlim=(0,12),ylim=(0,4.4));ax.axis('off')
box(ax,(.2,2.9),1.8,.9,'Data\ngenerator')
box(ax,(3.1,2.9),2,.9,'Admission\ncontrol (CAC)',RED)
box(ax,(6.3,2.9),2,.9,'Resource\nmanager',RED)
box(ax,(3.1,.55),2,.9,'Scheduler')
box(ax,(6.3,.55),2,.9,'Switching\nelements')
box(ax,(9.5,.55),2,.9,'End user')
arrow(ax,(2.02,3.35),(3.08,3.35),RED,':')
ax.plot([5.12,6.28],[3.35,3.35],color=RED,lw=1.8,linestyle=':')
poly_arrow(ax,[(1.1,2.88),(1.1,2),(2.55,2),(2.55,1),(3.08,1)])
poly_arrow(ax,[(7.3,2.88),(7.3,2.15),(4.1,2.15),(4.1,1.47)],RED,':')
arrow(ax,(5.12,1),(6.28,1));arrow(ax,(8.32,1),(9.48,1))
ax.text(.2,.02,'Solid: data path',fontsize=11,color=INK)
ax.text(3.2,.02,'Red dotted: admission / resource-allocation interactions',fontsize=11,color=RED)
save(fig,'01-network-modules')

# 02: source axes are unfinished. Do not invent a distribution or axis labels.
fig,ax=canvas(6,3.5)
ax.set(xlim=(-.1,1),ylim=(-.1,1));ax.axis('off')
arrow(ax,(-.06,0),(.96,0));arrow(ax,(0,-.06),(0,.95))
ax.text(.5,1.03,'Unfinished source sketch — axes only',ha='center',
        transform=ax.transAxes,fontsize=11,color='#667589')
save(fig,'02-demand-axes')

# 03: three qualitative utility profiles, no numeric scales or fitted functions.
fig,ax=canvas()
axes_clean(ax);ax.set(xticks=[],yticks=[])
ax.set_ylabel(r'$U_s(r_s(0),r_s(1)),\quad s\in D$')
ax.set_xlabel(r'$\min\{r_s(0),r_s(1)\}$')
ax.plot([0,.43],[0,.67],color=RED,lw=2.6)
curve(ax,[(0,0),(.12,.14),(.23,.4),(.34,.42),(.5,.44),(.76,.43),(.94,.43)],GREEN)
curve(ax,[(0,0),(.22,0),(.34,.01),(.43,.15),(.49,.28),(.49,.42),(.58,.47),(.72,.52),(.82,.54),(.93,.54)],PURPLE)
schematic(ax);save(fig,'03-downloader-utilities')

# 04: qualitative rise with the only source breakpoint labelled, 2 Mbps.
fig,ax=canvas()
axes_clean(ax);ax.set(xticks=[.6],xticklabels=['2 Mbps'],yticks=[])
ax.set_xlabel(r'$\min\{r_s(0),r_s(1)\}$');ax.set_ylabel('Watcher utility')
curve(ax,[(0,0),(.28,.005),(.46,.075),(.55,.38),(.57,.48),(.59,.62),(.6,.62),(.7,.62),(.8,.62),(.94,.62)],GREEN)
ax.plot([.6,.6],[0,.62],ls='--',lw=1.4,color=GREEN)
schematic(ax);save(fig,'04-watcher-utility')

# 05: ten employees, with an ellipsis instead of drawing extra source samples.
fig,ax=canvas(10,4.7)
ax.set(xlim=(0,10),ylim=(0,5));ax.axis('off')
for label,y in [(r'$s_1$',4.35),(r'$s_2$',3.25),(r'$s_3$',2.15)]:
    ax.plot(.65,y,'o',mfc='white',mec=INK,ms=13,mew=1.8)
    ax.text(.26,y+.21,label,fontsize=14)
    ax.plot([.82,3.25],[y,2.7],color=INK,lw=1.6)
ax.text(.63,1.2,r'$\vdots$',ha='center',fontsize=24)
ax.plot(.65,.5,'o',mfc='white',mec=INK,ms=13,mew=1.8)
ax.text(.23,.11,r'$s_{10}$',fontsize=14)
ax.plot([.82,3.25],[.5,2.7],color=INK,lw=1.6)
box(ax,(3.25,2.35),1.35,.7,'Gateway')
ax.plot([4.62,7.1],[2.7,2.7],color=INK,lw=2)
ax.text(5.85,3.15,r'$c=10$ Mbps',ha='center')
# Closed cloud-shaped outline, without introducing another network component.
verts=[(7.25,2.15),(6.83,2.1),(6.8,2.65),(7.12,2.81),
       (6.93,3.23),(7.38,3.53),(7.73,3.37),
       (8.05,3.84),(8.75,3.56),(8.75,3.21),
       (9.31,3.1),(9.29,2.51),(8.94,2.42),
       (9.14,1.96),(8.37,1.7),(8.06,1.99),
       (7.8,1.73),(7.31,1.82),(7.25,2.15)]
curve(ax,verts,INK,lw=1.8)
ax.text(8.08,2.73,'Internet',ha='center',va='center')
save(fig,'05-company-network')

# 06: exact piecewise-linear utility recoverable from the lecture and handwriting.
fig,ax=canvas()
axes_clean(ax,xlim=(0,2.1),ylim=(0,1.15))
ax.plot([0,.5,1.5,2],[0,0,1,1],lw=2.8,color=GREEN)
ax.plot([1.5,1.5],[0,1],ls='--',color=INK,lw=1.2)
ax.set(xticks=[.5,1.5],yticks=[.5,1],xlabel='Rate (Mbps)',ylabel='$U$')
ax.text(1,1.04,'Lecture’s piecewise-linear example',ha='right',
        va='bottom',transform=ax.transAxes,fontsize=10,color='#667589')
save(fig,'06-videocall-utility')

# 07: four candidate shapes. Normalized layout is explicitly not a capacity scale.
fig,ax=canvas(8.8,4.6)
axes_clean(ax)
ax.set(xticks=[.2,.78],xticklabels=['0.5','10'],yticks=[1],
       xlabel='$c$ (Mbps)',ylabel='Blockage probability')
black=[(0,1),(.42,1),(.79,.96),(.98,.36)]
magenta=[(0,1),(.015,.5),(.12,.16),(.4,.025)]
purple=[(0,1),(.025,.71),(.47,.23),(.93,.07)]
green=[(0,1),(.32,.96),(.86,.66),(.86,.025)]
curve(ax,green,CYAN,lw=14,alpha=.65)
for pts,col in [(black,INK),(magenta,MAGENTA),(purple,PURPLE),(green,GREEN)]:
    curve(ax,pts,col)
# Ellipse repeats the circled design-point label in the original sketch.
ax.add_patch(Ellipse((.78,-.064),.11,.105,fill=False,ec=INK,lw=1.2,
                     transform=ax.get_xaxis_transform(),clip_on=False))
schematic(ax,'Schematic candidates — horizontal spacing not to scale')
save(fig,'07-blockage-curves')

# 08: reproduce the source's stair steps and its zero-based arrival labels.
# Positions encode only the original ordering and unequal drawn gaps, not seconds.
fig,ax=canvas(10,4.8)
ax.set(xlim=(-.25,6.6),ylim=(-1.65,6.65));ax.axis('off')
arrow(ax,(-.15,0),(6.5,0));arrow(ax,(0,-.1),(0,6.45))
ax.text(-.2,6.5,'$N(t)$',ha='right',va='bottom')
ax.text(6.5,-.15,'Time',ha='right',va='top')
for k in range(1,6):
    ax.plot([-.07,.07],[k,k],color=INK,lw=1.2)
    ax.text(-.17,k,str(k),ha='right',va='center',fontsize=12)
positions=[.75,1.6,2.05,4.05,4.5,5.8]
xs=[0,positions[0],positions[0],positions[1],positions[1],positions[2],positions[2],positions[3],positions[3],positions[4],positions[4],6.1]
ys=[1,1,2,2,3,3,4,4,5,5,6,6]
ax.plot(xs,ys,color=GREEN,lw=2.6)
for i,x in enumerate(positions):
    ax.plot([x,x],[-.08,.08],color=INK,lw=1.2)
    ax.text(x,-.23,f'$T_{i}$',ha='center',va='top')
for i in range(4):
    a,b=positions[i],positions[i+1]
    arrow(ax,(a,-.85),(b,-.85),head='<->',lw=1.2)
    ax.text((a+b)/2,-1.12,f'$A({i+1})$',ha='center',va='top',fontsize=12)
ax.text(5.2,-.85,r'$\cdots$',ha='center',va='center',fontsize=20)
ax.text(6.5,6.65,'Schematic — source indexing and vertical offset retained',
        ha='right',fontsize=10,color='#667589')
save(fig,'08-counting-process')

print('Created eight PNG redraws and eight editable SVG files.')
