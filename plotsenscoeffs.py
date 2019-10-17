#!/usr/bin/python
import pandas as pd
import matplotlib.pyplot as plt
from subprocess import call
from matplotlib import rc
import numpy as np
from matplotlib import figure

Normfac=0.786707
plt.rcParams["figure.figsize"] = (10,3)

df = pd.read_csv('./Bl1ALsens.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)

df.columns = ['D1','D2','D3']
df.head()

axAL=df['D1'].values/Normfac
tanAL=df['D2'].values/Normfac
radAL=df['D3'].values/Normfac


df = pd.read_csv('./Bl1BEsens.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)

df.columns = ['D1','D2','D3']
df.head()

axBE=df['D1'].values/Normfac
tanBE=df['D2'].values/Normfac
radBE=df['D3'].values/Normfac

df = pd.read_csv('./Bl1ZEsens.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)

df.columns = ['D1','D2','D3']
df.head()

axZE=df['D1'].values/Normfac
tanZE=df['D2'].values/Normfac
radZE=df['D3'].values/Normfac

#********************** LINEAR *********************************

df = pd.read_csv('./LinBl1ALsens.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)

df.columns = ['D1','D2','D3']
df.head()

linaxAL=df['D1'].values/Normfac
lintanAL=df['D2'].values/Normfac
linradAL=df['D3'].values/Normfac


df = pd.read_csv('./LinBl1BEsens.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)

df.columns = ['D1','D2','D3']
df.head()

linaxBE=df['D1'].values/Normfac
lintanBE=df['D2'].values/Normfac
linradBE=df['D3'].values/Normfac

df = pd.read_csv('./LinBl1ZEsens.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)

df.columns = ['D1','D2','D3']
df.head()

linaxZE=df['D1'].values/Normfac
lintanZE=df['D2'].values/Normfac
linradZE=df['D3'].values/Normfac


blnum=[i+1 for i in range(75)]


p1=plt.bar(blnum,axAL,width=1.0,color="none",edgecolor='k')
p2=plt.bar(blnum,radAL,width=0.8,color="r")
p3=plt.bar(blnum,tanAL,width=0.6,color="b")
plt.xlim([1,76])
plt.xticks(np.arange(75),(' ','1',' ',' ',' ',' ',' ',' ',' ',' ','10',' ',' ',' ',' ',' ',' ',' ',' ',' ','20',' ',' ',' ',' ',' ',' ',' ',' ',' ','30',' ',' ',' ',' ',' ',' ',' ',' ',' ','40',' ',' ',' ',' ',' ',' ',' ',' ',' ','50',' ',' ',' ',' ',' ',' ',' ',' ',' ','60',' ',' ',' ',' ',' ',' ',' ',' ',' ','70',' ',' ',' ',' ','75'))
plt.xlabel('Blade number',fontsize=16)
plt.ylabel('Sensitivity',fontsize=16)
plt.legend((p1,p2,p3),('Axial','Tangential','Radial'))
plt.tick_params(axis='both', which='major', labelsize=12)

plt.tight_layout()
plt.savefig('SensitivityAL.png', dpi=300)
plt.show()

p1=plt.bar(blnum,axBE,width=1.0,color="none",edgecolor='k')
p2=plt.bar(blnum,radBE,width=0.8,color="r")
p3=plt.bar(blnum,tanBE,width=0.6,color="b")
plt.xlim([1,76])
plt.xticks(np.arange(75),(' ','1',' ',' ',' ',' ',' ',' ',' ',' ','10',' ',' ',' ',' ',' ',' ',' ',' ',' ','20',' ',' ',' ',' ',' ',' ',' ',' ',' ','30',' ',' ',' ',' ',' ',' ',' ',' ',' ','40',' ',' ',' ',' ',' ',' ',' ',' ',' ','50',' ',' ',' ',' ',' ',' ',' ',' ',' ','60',' ',' ',' ',' ',' ',' ',' ',' ',' ','70',' ',' ',' ',' ','75'))
plt.xlabel('Blade number',fontsize=16)
plt.ylabel('Sensitivity',fontsize=16)
plt.legend((p1,p2,p3),('Axial','Tangential','Radial'))
plt.tick_params(axis='both', which='major', labelsize=12)

plt.tight_layout()
plt.savefig('SensitivityBE.png', dpi=300)
plt.show()


p1=plt.bar(blnum,axZE,width=1.0,color="none",edgecolor='k')
p2=plt.bar(blnum,radZE,width=0.8,color="r")
p3=plt.bar(blnum,tanZE,width=0.6,color="b")
plt.xlim([1,76])
plt.xticks(np.arange(75),(' ','1',' ',' ',' ',' ',' ',' ',' ',' ','10',' ',' ',' ',' ',' ',' ',' ',' ',' ','20',' ',' ',' ',' ',' ',' ',' ',' ',' ','30',' ',' ',' ',' ',' ',' ',' ',' ',' ','40',' ',' ',' ',' ',' ',' ',' ',' ',' ','50',' ',' ',' ',' ',' ',' ',' ',' ',' ','60',' ',' ',' ',' ',' ',' ',' ',' ',' ','70',' ',' ',' ',' ','75'))
plt.xlabel('Blade number',fontsize=16)
plt.ylabel('Sensitivity',fontsize=16)
plt.legend((p1,p2,p3),('Axial','Tangential','Radial'))
plt.tick_params(axis='both', which='major', labelsize=12)

plt.tight_layout()
plt.savefig('SensitivityZE.png', dpi=300)
plt.show()



#****************************** Linear **********************************

p1=plt.bar(blnum,linaxAL,width=1.0,color="none",edgecolor='k')
p2=plt.bar(blnum,linradAL,width=0.8,color="r")
p3=plt.bar(blnum,lintanAL,width=0.6,color="b")
plt.xlim([1,76])
plt.xticks(np.arange(75),(' ','1',' ',' ',' ',' ',' ',' ',' ',' ','10',' ',' ',' ',' ',' ',' ',' ',' ',' ','20',' ',' ',' ',' ',' ',' ',' ',' ',' ','30',' ',' ',' ',' ',' ',' ',' ',' ',' ','40',' ',' ',' ',' ',' ',' ',' ',' ',' ','50',' ',' ',' ',' ',' ',' ',' ',' ',' ','60',' ',' ',' ',' ',' ',' ',' ',' ',' ','70',' ',' ',' ',' ','75'))
plt.xlabel('Blade number',fontsize=16)
plt.ylabel('Sensitivity',fontsize=16)
plt.legend((p1,p2,p3),('Axial','Tangential','Radial'))
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
plt.ylabel('Sensitivity',fontsize=16)
plt.legend((p1,p2,p3),('Axial','Tangential','Radial'))
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

plt.ylabel('Sensitivity',fontsize=16)
plt.legend((p1,p2,p3),('Axial','Tangential','Radial'))

plt.tick_params(axis='both', which='major', labelsize=12)



plt.tight_layout()

plt.savefig('LinSensitivityZE.png', dpi=300)

plt.show()


