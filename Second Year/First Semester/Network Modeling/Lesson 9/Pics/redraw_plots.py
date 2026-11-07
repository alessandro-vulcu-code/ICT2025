"""Exact fluid-model plots derived in Lesson 9; no empirical samples."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
out=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
x=np.linspace(0,1,1001)
g=np.where(x<=.5,2*x,2*(1-x))
b=np.where(x<=.5,x/2-x*x,0)
q=np.where(x<=.5,0,-x*x+1.5*x-.5)
fig,ax=plt.subplots(3,1,figsize=(9,8),sharex=True,layout='constrained')
ax[0].plot(x,g,label='$G(t)/G_p$',color='black')
ax[0].plot(x[x<.5],g[x<.5],color='#c026a4',lw=2,label='$\\lambda_{out}(t)/G_p$')
ax[0].plot([.5,.5,1],[1,.5,.5],color='#c026a4',lw=2)
ax[0].axhline(.5,color='gray',ls='--',label='$\\rho/G_p=1/2$');ax[0].set_ylabel('Normalized rate');ax[0].legend(loc='upper right')
ax[1].plot(x,b,color='#c026a4');ax[1].set_ylabel('$b(t)/(G_p T)$');ax[1].set_yticks([0,1/16],['0','1/16'])
ax[2].plot(x,q,color='#e76f00');ax[2].set_ylabel('$b_i(t)/(G_p T)$');ax[2].set_yticks([0,1/16],['0','1/16'])
for a in ax:
 a.grid(alpha=.25);a.set_xlim(0,1)
ax[2].set_xticks([0,.25,.5,.75,1],['0','1/4','1/2','3/4','1']);ax[2].set_xlabel('$t/T$ (one period, initially empty bucket and input buffer)')
fig.savefig(out/'14-triangle-exact.png',dpi=180);plt.close(fig)
