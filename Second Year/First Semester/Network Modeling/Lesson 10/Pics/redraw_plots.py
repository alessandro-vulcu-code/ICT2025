"""Reproduce exact distributions and bounds used in Lesson 10 (no invented data)."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
out=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
z=np.linspace(.02,8,1600)
fig,ax=plt.subplots(figsize=(8,4.6),layout='constrained')
ax.plot(z,np.exp(-z),label='Exact: $e^{-z}$',color='#a126bd')
ax.plot(z,np.minimum(1,1/z),label='Markov: $\\min(1,1/z)$',color='#ed7d12')
y=np.ones_like(z);use=z>1;y[use]=np.minimum(1,1/(z[use]-1)**2)
ax.plot(z,y,label='Chebyshev: $\\min(1,1/(z-1)^2)$ for $z>1$',color='#16899b')
ax.axvline(4,color='gray',ls=':',lw=1)
for yy,cc in [(np.exp(-4),'#a126bd'),(.25,'#ed7d12'),(1/9,'#16899b')]:ax.plot(4,yy,'o',color=cc)
ax.set(xlim=(0,8),ylim=(0,1.05),xlabel='$z=a/m_x=\\lambda a$',ylabel='Tail probability / upper bound')
ax.grid(alpha=.2);ax.legend();fig.savefig(out/'17-exponential-bounds-exact.png',dpi=170);plt.close(fig)
fig,axs=plt.subplots(1,2,figsize=(10,4.2),layout='constrained')
axs[0].stem([-1,0,1],[.25,.5,.25],basefmt=' ');axs[0].set(xlim=(-1.5,1.5),ylim=(0,.6),xlabel='$x$',ylabel='$P[X=x]$',title='Three-point distribution');axs[0].set_xticks([-1,0,1])
a=np.linspace(.001,2.2,800)
axs[1].plot(a,np.minimum(1,.5/a**2),color='#ed7d12',label='$\\min(1,\\sigma_x^2/a^2)$')
axs[1].plot([0,1],[.5,.5],color='#a126bd',label='$P[|X|\\geq a]$')
axs[1].plot([1,2.2],[0,0],color='#a126bd')
for xx,yy in [(0,1),(1,.5)]:axs[1].plot(xx,yy,'o',color='#a126bd')
for xx,yy in [(0,.5),(1,0)]:axs[1].plot(xx,yy,'o',mfc='white',mec='#a126bd')
axs[1].set(xlim=(-.08,2.2),ylim=(-.04,1.08),xlabel='$a$',ylabel='Tail probability / upper bound',title='Equality at $a=1$');axs[1].legend()
for ax in axs:ax.grid(alpha=.2)
fig.savefig(out/'18-chebyshev-tight-example.png',dpi=170);plt.close(fig)
