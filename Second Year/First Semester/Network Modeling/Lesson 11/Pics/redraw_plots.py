"""Reproducible schematic redraws. No measured traffic or inferred coordinates."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
P=Path(__file__).parent
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
def save(fig,name):
    fig.tight_layout(); fig.savefig(P/name,dpi=170); plt.close(fig)
fig,ax=plt.subplots(figsize=(9,2.8)); ax.set(xlim=(0,10),ylim=(0,3)); ax.axis('off')
for x,w,t in [(0.2,2,'Users'),(3.5,2.4,'Buffer B\nlevel $q_i$'),(7.3,2,'Link C')]:
    ax.add_patch(Rectangle((x,1),w,1,fill=False,lw=2));ax.text(x+w/2,1.5,t,ha='center',va='center')
ax.annotate('',(3.5,1.5),(2.2,1.5),arrowprops={'arrowstyle':'->'}); ax.annotate('',(7.3,1.5),(5.9,1.5),arrowprops={'arrowstyle':'->'})
ax.text(2.8,2.3,'$x_i$ bytes / slot',ha='center');ax.text(8.3,.45,r'$\Delta=C\tau$ bytes / slot',ha='center')
ax.text(.2,.1,r'Slotted aggregate model (schematic); overflow: $q_i+x_i>B+\Delta$')
save(fig,'01-system.png')
fig,ax=plt.subplots(figsize=(8,2));ax.set(xlim=(0,5),ylim=(-.7,1));ax.axis('off');ax.annotate('',(4.8,0),(0,0),arrowprops={'arrowstyle':'->'})
for i in range(4):
    ax.plot([i,i],[-.07,.07],color='k');ax.annotate(f'$x_{{{i+1}}}$',(i+.5,0),(i+.5,.7),ha='center',arrowprops={'arrowstyle':'->'})
ax.text(1,-.4,r'Each slot: duration $\tau$; arrivals $x_i$; service allowance $\Delta$')
save(fig,'02-slots.png')
# Density shapes are illustrative only; no assumed distribution in the exercise.
z=np.linspace(-3,5,900); f=np.exp(-.5*((z+.5)/.8)**2)+.32*np.exp(-.5*((z-2)/1.1)**2)
f/=np.trapezoid(f,z); mean=np.trapezoid(z*f,z); z=z-mean; a=.9
fig,axs=plt.subplots(3,1,figsize=(8,8))
for ax,title in zip(axs,['Original nonnegative variable (schematic)','Centering: right tail only','Absolute deviation: both tails']):
    ax.set_title(title,loc='left');ax.set_yticks([])
axs[0].plot(z+4,f,color='forestgreen');axs[0].axvline(4,ls='--',color='gray');axs[0].set(xlabel='$x$',xticks=[4],xticklabels=['$m_x$'],ylabel='$f_x(x)$')
for j,ax in enumerate(axs[1:]):
    ax.plot(z,f,color='forestgreen');ax.axvline(0,ls='--',color='gray');mask=z>a if j==0 else abs(z)>a
    ax.fill_between(z,0,f,where=mask,color='mediumseagreen',alpha=.4);ax.set(xlabel='$z=x-m_x$',ylabel='$f_{x-m_x}(z)$',xticks=[-a,0,a],xticklabels=['$-a$','0',r'$a=\Delta-m_x$'])
save(fig,'03-centering-tails.png')
fig,ax=plt.subplots(figsize=(7,3)); z=np.linspace(-3,3,500);f=np.maximum(0,1-(z/3)**2)**2
ax.plot(z+4,f,color='forestgreen');ax.axvline(4,color='gray',ls='--');ax.fill_between(z+4,0,f,where=abs(z)>1,color='mediumseagreen',alpha=.4);ax.set(yticks=[],xticks=[3,4,5],xticklabels=['$m_x-a$','$m_x$','$m_x+a$'],xlabel='$x$',title='Symmetry assumption: equal tail areas (schematic)');save(fig,'04-symmetry.png')
fig,ax=plt.subplots(figsize=(8,3));x=np.linspace(0,14,900);y=np.exp(-((x-1.4)/.65)**2)+.3*np.exp(-((x-11)/.7)**2)
ax.plot(x,y,color='forestgreen');ax.set(xlabel='$x$',ylabel='density (schematic)',yticks=[],xticks=[],title='Small values frequent; rare large values increase dispersion');save(fig,'05-irregular.png')
fig,ax=plt.subplots(figsize=(7,4));d=np.linspace(0,1.3,400);ax.plot(d,np.maximum(0,1-d),color='forestgreen',label=r'$B+\Delta=m_x/\varepsilon$');ax.fill_between(d,np.maximum(0,1-d),1.3,where=d>.01,color='turquoise',alpha=.25,label=r'Feasible for $q_i=0$ and $\Delta>m_x$');ax.axvline(.01,color='k',ls='--',label=r'$\Delta=m_x$');ax.plot([.55,.55,0],[0,.45,.45],color='royalblue',ls=':');ax.set(xlim=(0,1.3),ylim=(0,1.3),xlabel=r'$\Delta=C\tau$ / $(m_x/\varepsilon)$',ylabel=r'$B$ / $(m_x/\varepsilon)$',title=r'Empty-buffer bound; $\varepsilon=10^{-2}$');ax.legend(fontsize=9);save(fig,'06-empty-region.png')
fig,ax=plt.subplots(figsize=(7,4));d=np.linspace(0,1.2,400)
for alpha,c in [(0,'forestgreen'),(.5,'crimson'),(.8,'magenta')]:ax.plot(d,np.maximum(0,(1-d)/(1-alpha)),color=c,label=fr'$\alpha={alpha}$')
ax.axvline(1,color='gray',ls=':');ax.set(xlim=(0,1.2),ylim=(0,3),xlabel=r'$\Delta$ / $(m_x/\varepsilon)$',ylabel=r'$B$ / $(m_x/\varepsilon)$',title='Corrected family: common intercept on service axis');ax.legend();save(fig,'07-alpha.png')
# Schematic step paths manually drawn, with no numerical labels or empirical claim.
fig,axs=plt.subplots(2,1,figsize=(8,6));q=[0,0,1,3,2,1,0,0,0,0,1,3,4];t=[0,0,1,3,2,1,0,-1,-2,-1,0,2,3];qr=np.array(t)-np.minimum.accumulate(np.minimum(t,0))
axs[0].step(range(len(q)),q,where='post',color='royalblue');axs[0].annotate('Initial transient (schematic)',(2,1),(0,3.8),arrowprops={'arrowstyle':'->'});axs[0].set(ylabel='$q_i$',title='Stationarity concerns distribution, not a flat sample path')
axs[1].step(range(len(t)),t,where='post',label=r'$\widetilde q_i$: unreflected',color='royalblue');axs[1].step(range(len(t)),qr,where='post',label='$q_i$: reflected at zero',color='magenta');axs[1].axhline(0,color='gray',lw=.8);axs[1].legend(fontsize=9);axs[1].set(ylabel='backlog (schematic)',title='Same increments; unused service cannot become credit')
for ax in axs:ax.set(xlabel='slot $i$',xticks=[],yticks=[])
save(fig,'08-queue-paths.png')
fig,ax=plt.subplots(figsize=(7,3.5));d=np.linspace(0,1,200);ax.plot(d,1-d,color='darkorange');ax.plot([.2,.4,.6,.8],[.8,.6,.4,.2],'o',mfc='none',color='darkorange');ax.axvline(.12,color='gray');ax.set(xticks=[],yticks=[],xlabel=r'$C\tau$',ylabel='$B$',title='Lecture heuristic: replace $q_i$ by a typical level (schematic)');save(fig,'09-heuristic.png')
