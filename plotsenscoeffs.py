#!/usr/bin/python
import pandas as pd
import matplotlib.pyplot as plt
from subprocess import call
from matplotlib import rc
import numpy as np
from matplotlib import figure

Normfac = 0.786707 # Radial displacement nominal aligned with stacking axis for tuned case
plt.rcParams["figure.figsize"] = (10,3)

#********************** LINEAR *********************************

df = pd.read_csv('./outputALnode3134.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)

df.columns = ['D1','D2','D3']
df.head()

linaxAL=df['D1'].values/Normfac
lintanAL=df['D2'].values/Normfac
linradAL=df['D3'].values/Normfac


df = pd.read_csv('./outputBEnode3134.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)

df.columns = ['D1','D2','D3']
df.head()

linaxBE=df['D1'].values/Normfac
lintanBE=df['D2'].values/Normfac
linradBE=df['D3'].values/Normfac

df = pd.read_csv('./outputZEnode3134.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)

df.columns = ['D1','D2','D3']
df.head()

linaxZE=df['D1'].values/Normfac
lintanZE=df['D2'].values/Normfac
linradZE=df['D3'].values/Normfac


blnum=[i+1 for i in range(75)]


p1=plt.bar(blnum,linaxAL,width=1.0,color="none",edgecolor='k')
p2=plt.bar(blnum,linradAL,width=0.8,color="r")
p3=plt.bar(blnum,lintanAL,width=0.6,color="b")
plt.xlim([1,76])
plt.xticks(np.arange(75),(' ','1',' ',' ',' ',' ',' ',' ',' ',' ','10',' ',' ',' ',' ',' ',' ',' ',' ',' ','20',' ',' ',' ',' ',' ',' ',' ',' ',' ','30',' ',' ',' ',' ',' ',' ',' ',' ',' ','40',' ',' ',' ',' ',' ',' ',' ',' ',' ','50',' ',' ',' ',' ',' ',' ',' ',' ',' ','60',' ',' ',' ',' ',' ',' ',' ',' ',' ','70',' ',' ',' ',' ','75'))
plt.xlabel('Blade number',fontsize=16)
plt.ylabel('Sensitivity (1/rad)',fontsize=16)
plt.legend((p1,p2,p3),('Axial','Radial','Tangential'))
plt.tick_params(axis='both', which='major', labelsize=12)

plt.tight_layout()
plt.savefig('LinSensitivityAL.png', dpi=300)
plt.show()

p1=plt.bar(blnum,linaxBE,width=1.0,color="none",edgecolor='k')
p2=plt.bar(blnum,linradBE,width=0.8,color="r")
p3=plt.bar(blnum,lintanBE,width=0.6,color="b")
plt.xlim([1,76])
plt.xticks(np.arange(75),(' ','1',' ',' ',' ',' ',' ',' ',' ',' ','10',' ',' ',' ',' ',' ',' ',' ',' ',' ','20',' ',' ',' ',' ',' ',' ',' ',' ',' ','30',' ',' ',' ',' ',' ',' ',' ',' ',' ','40',' ',' ',' ',' ',' ',' ',' ',' ',' ','50',' ',' ',' ',' ',' ',' ',' ',' ',' ','60',' ',' ',' ',' ',' ',' ',' ',' ',' ','70',' ',' ',' ',' ','75'))
plt.xlabel('Blade number',fontsize=16)
plt.ylabel('Sensitivity (1/rad)',fontsize=16)
plt.legend((p1,p2,p3),('Axial','Radial','Tangential'))
plt.tick_params(axis='both', which='major', labelsize=12)

plt.tight_layout()
plt.savefig('LinSensitivityBE.png', dpi=300)
plt.show()


p1=plt.bar(blnum,linaxZE,width=1.0,color="none",edgecolor='k')
p2=plt.bar(blnum,linradZE,width=0.8,color="r")
p3=plt.bar(blnum,lintanZE,width=0.6,color="b")
plt.xlim([1,76])
plt.xticks(np.arange(75),(' ','1',' ',' ',' ',' ',' ',' ',' ',' ','10',' ',' ',' ',' ',' ',' ',' ',' ',' ','20',' ',' ',' ',' ',' ',' ',' ',' ',' ','30',' ',' ',' ',' ',' ',' ',' ',' ',' ','40',' ',' ',' ',' ',' ',' ',' ',' ',' ','50',' ',' ',' ',' ',' ',' ',' ',' ',' ','60',' ',' ',' ',' ',' ',' ',' ',' ',' ','70',' ',' ',' ',' ','75'))
plt.xlabel('Blade number',fontsize=16)

plt.ylabel('Sensitivity (1/rad)',fontsize=16)
plt.legend((p1,p2,p3),('Axial','Radial','Tangential'))

plt.tick_params(axis='both', which='major', labelsize=12)



plt.tight_layout()

plt.savefig('LinSensitivityZE.png', dpi=300)

plt.show()


