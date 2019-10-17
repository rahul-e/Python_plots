#!/usr/bin/python
import pandas as pd
import matplotlib.pyplot as plt
from subprocess import call
from matplotlib import rc
import numpy as np

#~~~~~~~~~~~~~~~~~~~~~~~~~~~ Normalization factors ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Normfac=1.0# data already normalized # 226.543 Maximum radial displacement for nominal geometry aligned with stacking axis 
Normfacsens=1.65708E-01 # Axial disp sensitivity w.r.t AL at considered node position
normfacalpha=20.0
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Variant 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

df = pd.read_csv('./MCSaverageAsymB.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)
df.columns = ['FEScodlavg','FEScodlstd','FEScodravg','FEScodrstd','RFScodlavg','RFScodlstd','RFScodravg','RFScodrstd']
df.head()

FavgpressFEmean=df['FEScodlavg'].values/Normfac	
FavgpressFEstd=df['FEScodlstd'].values/Normfac
FavgpressRFmean=df['RFScodlavg'].values/Normfac
FavgpressRFstd=df['RFScodlstd'].values/Normfac

avgpressFEmean=FavgpressFEmean[::3]
avgpressFEstd=FavgpressFEstd[::3]
avgpressRFmean=FavgpressRFmean[::3]
avgpressRFstd=FavgpressRFstd[::3]

df = pd.read_csv('./MCSmaxAsymB.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)
df.columns = ['FEScodlavg','FEScodlstd','FEScodravg','FEScodrstd','RFScodlavg','RFScodlstd','RFScodravg','RFScodrstd']
df.head()

FmaxpressFEmean=df['FEScodlavg'].values/Normfac	
FmaxpressFEstd=df['FEScodlstd'].values/Normfac
FmaxpressRFmean=df['RFScodlavg'].values/Normfac
FmaxpressRFstd=df['RFScodlstd'].values/Normfac

maxpressFEmean=FmaxpressFEmean[::3]
maxpressFEstd=FmaxpressFEstd[::3]
maxpressRFmean=FmaxpressRFmean[::3]
maxpressRFstd=FmaxpressRFstd[::3]



MCSsample=[i+1 for i in range(len(maxpressFEmean))]

fig, ax1  = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(MCSsample,maxpressFEmean,'k-o',MCSsample,maxpressRFmean,'r-^',ms=10,fillstyle='full',markeredgecolor='k')
ax2.plot(MCSsample,maxpressFEstd,'k-o',MCSsample,maxpressRFstd,'b-<',ms=10,fillstyle='none',markeredgecolor='k')
ax1.set_xlabel(r'Number of Monte Carlo evaluations',fontsize=16)
ax1.set_ylabel('Mean of normalised contact pressure',color='k', fontsize=16)
ax2.set_ylabel('STD of normalised contact pressure',color='k', fontsize=16)

ax1.legend(('MCS mean','RF mean'),loc='center')
ax2.legend(('MCS standard deviation','RF standard deviation'),loc='best')
plt.tight_layout()
plt.savefig('MCSmaxpress.png', dpi=300)
plt.show()

MCSsample=[i+1 for i in range(len(avgpressFEmean))]
fig, ax1  = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(MCSsample,avgpressFEmean,'k-o',MCSsample,avgpressRFmean,'k-^',ms=10,fillstyle='full',markeredgecolor='k')
ax2.plot(MCSsample,avgpressFEstd,'k-o',MCSsample,avgpressRFstd,'k-<',ms=10,fillstyle='none',markeredgecolor='k')
ax1.set_xlabel(r'Number of Monte Carlo evaluations',fontsize=16)
ax1.set_ylabel('Mean of normalised contact pressure',color='k', fontsize=16)
ax2.set_ylabel('STD of normalised contact pressure',color='k', fontsize=16)

ax1.legend(('MCS mean','RF mean'),loc='lower right')
ax2.legend(('MCS standard deviation','RF standard deviation'),loc='upper right')
plt.tight_layout()

plt.savefig('MCSavgpress.png', dpi=300)
plt.show()

