import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

df=pd.read_csv("Job-20210729C.txt",sep='\t',header=None)
df.columns=['X','Y']
x18=df['X'].values
y18=df['Y'].values

df=pd.read_csv("MaxPrinc_Job-20210803.txt",sep='\t',header=None)
df.columns=['X','Y']
x19=df['X'].values
y19=df['Y'].values

df=pd.read_csv("MaxPrinc_Job-20210804.txt",sep='\t',header=None)
df.columns=['X','Y']
x20=df['X'].values
y20=df['Y'].values
Flexuralstrength = 27.61

fig, ax1 = plt.subplots()

ax1.plot(x20,y20,'-b',marker='v',linewidth=1,markersize=8,markeredgecolor='b',markevery=2,markerfacecolor='none',label='crack at 26fpy')
ax1.plot(x19,y19,'-r',marker='s',linewidth=1,markersize=6,markeredgecolor='r',markevery=2,markerfacecolor='none',label='crack at 28fpy')
ax1.plot(x18,y18,'-k',marker='o',linewidth=1,markersize=8,markeredgecolor='k',markevery=2,markerfacecolor='none',label='crack at 30fpy')

ax1.tick_params(axis='both', which='both',direction='out',labelsize=16)
ax1.minorticks_on()

            
ax1.xaxis.grid(True, linestyle='-',which ='major',alpha=0.5)
ax1.xaxis.grid(True, linestyle=':',which ='minor')
ax1.yaxis.grid(True, linestyle='-',which ='major',alpha=0.5)
ax1.yaxis.grid(True, linestyle=':',which ='minor')
ax1.set_ylabel('Stress (MPa)',fontsize=16)
ax1.legend(loc='upper left',frameon=False)
ax1.set_xlabel('FPY',fontsize=16)
ax1.axvspan(25,34.5,color='r',alpha=0.1)


ax1.set_xlim(-0.5,34.5)


axins = ax1.inset_axes([0.2,0.28,0.5,0.5])
axins.plot(x20,y20,'-b',linewidth=1,marker='v',markevery=2,markerfacecolor='none')
axins.plot(x19,y19,'-r',linewidth=1,marker='s',markevery=2,markerfacecolor='none')
axins.plot(x18,y18,'-k',linewidth=1,marker='o',markevery=2,markerfacecolor='none')
axins.minorticks_on()

axins.set_xlim(25,34.5)
axins.grid(True, linestyle='-',which ='major',alpha=0.5)
axins.grid(True, linestyle=':',which ='minor')
axins.grid(True, linestyle='-',which ='major',alpha=0.5)
axins.grid(True, linestyle=':',which ='minor')
axins.axvspan(25,34.5,color='r',alpha=0.1)

#axins.annotate('crack opening',color='b',rotation=90,xy=(26,10),xycoords='data',xytext=(26,90),arrowprops=dict(color='b', shrink=0.05,headlength=4.5,width=0.1,),
#            horizontalalignment='right', verticalalignment='top',)

#axins.annotate('crack opening',color='r',rotation=90,xy=(28,30),xycoords='data',xytext=(28,105),arrowprops=dict(color='r', shrink=0.05,headlength=4.5,width=0.1,),
#            horizontalalignment='right', verticalalignment='top',)

#axins.annotate('crack opening',color='k',rotation=90,xy=(30,50),xycoords='data',xytext=(30,120),arrowprops=dict(color='k', shrink=0.05,headlength=4.5,width=0.1,),
#            horizontalalignment='right', verticalalignment='top',)

#plt.ylim([0,2.1])
#plt.text(3.84,1.6,'#1')
#plt.tick_params(axis='both', which='major', labelsize=8)

#ax1.indicate_inset_zoom(axins, edgecolor="black")
mark_inset(ax1, axins, loc1=3, loc2=4, fc="none", lw=1, ec='r',alpha=0.5)
fig.tight_layout()
plt.savefig('MPS_SRGW_KWRCinit.png',dpi=250)
plt.show()
