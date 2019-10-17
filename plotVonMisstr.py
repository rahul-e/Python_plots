#!/usr/bin/python
import math
import pandas as pd
import matplotlib.pyplot as plt
from subprocess import call
from matplotlib import rc
import numpy as np
from matplotlib import figure

Normfac = 116 # Maximum normal stress Szz on blade for sector model, nonlinear, with mean value of anisotropy angles. 
plotVonMis = "Yes"
plt.rcParams["figure.figsize"] = (10,3)

df = pd.read_csv('./outrootAL6050.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)

df.columns = ['Sxx','Syy','Szz', 'Sxy', 'Syz', 'Szx']
df.head()

SxxAL=df['Sxx'].values/Normfac
SyyAL=df['Syy'].values/Normfac
SzzAL=df['Szz'].values/Normfac
SxyAL=df['Sxy'].values/Normfac
SyzAL=df['Syz'].values/Normfac
SzxAL=df['Szx'].values/Normfac


df = pd.read_csv('./outrootBE6050.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)

df.columns = ['Sxx','Syy','Szz', 'Sxy', 'Syz', 'Szx']
df.head()

SxxBE=df['Sxx'].values/Normfac
SyyBE=df['Syy'].values/Normfac
SzzBE=df['Szz'].values/Normfac
SxyBE=df['Sxy'].values/Normfac
SyzBE=df['Syz'].values/Normfac
SzxBE=df['Szx'].values/Normfac

df = pd.read_csv('./outrootZE6050.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)

df.columns = ['Sxx','Syy','Szz', 'Sxy', 'Syz', 'Szx']
df.head()

SxxZE=df['Sxx'].values/Normfac
SyyZE=df['Syy'].values/Normfac
SzzZE=df['Szz'].values/Normfac
SxyZE=df['Sxy'].values/Normfac
SyzZE=df['Syz'].values/Normfac
SzxZE=df['Szx'].values/Normfac



blnum=[i+1 for i in range(75)]


p1=plt.bar(blnum,SxxAL,width=1.0,color="none",edgecolor='k')
p2=plt.bar(blnum,SyyAL,width=0.8,color="r")
p3=plt.bar(blnum,SzzAL,width=0.6,color="b")
plt.xlim([1,76])
plt.xticks(np.arange(75),(' ','1',' ',' ',' ',' ',' ',' ',' ',' ','10',' ',' ',' ',' ',' ',' ',' ',' ',' ','20',' ',' ',' ',' ',' ',' ',' ',' ',' ','30',' ',' ',' ',' ',' ',' ',' ',' ',' ','40',' ',' ',' ',' ',' ',' ',' ',' ',' ','50',' ',' ',' ',' ',' ',' ',' ',' ',' ','60',' ',' ',' ',' ',' ',' ',' ',' ',' ','70',' ',' ',' ',' ','75'))
plt.xlabel('Blade number',fontsize=16)
plt.ylabel('Sensitivity (1/rad)',fontsize=16)
plt.legend((p1,p2,p3),('$\sigma_{xx}$','$\sigma_{yy}$','$\sigma_{zz}$'))
plt.tick_params(axis='both', which='major', labelsize=12)

plt.tight_layout()
plt.savefig('StressAL.png', dpi=300)
plt.show()

p1=plt.bar(blnum,SxxBE,width=1.0,color="none",edgecolor='k')
p2=plt.bar(blnum,SyyBE,width=0.8,color="r")
p3=plt.bar(blnum,SzzBE,width=0.6,color="b")
plt.xlim([1,76])
plt.xticks(np.arange(75),(' ','1',' ',' ',' ',' ',' ',' ',' ',' ','10',' ',' ',' ',' ',' ',' ',' ',' ',' ','20',' ',' ',' ',' ',' ',' ',' ',' ',' ','30',' ',' ',' ',' ',' ',' ',' ',' ',' ','40',' ',' ',' ',' ',' ',' ',' ',' ',' ','50',' ',' ',' ',' ',' ',' ',' ',' ',' ','60',' ',' ',' ',' ',' ',' ',' ',' ',' ','70',' ',' ',' ',' ','75'))
plt.xlabel('Blade number',fontsize=16)
plt.ylabel('Sensitivity (1/rad)',fontsize=16)
plt.legend((p1,p2,p3),('$\sigma_{xx}$','$\sigma_{yy}$','$\sigma_{zz}$'))
plt.tick_params(axis='both', which='major', labelsize=12)

plt.tight_layout()
plt.savefig('StressBE.png', dpi=300)
plt.show()


p1=plt.bar(blnum,SxxZE,width=1.0,color="none",edgecolor='k')
p2=plt.bar(blnum,SyyZE,width=0.8,color="r")
p3=plt.bar(blnum,SzzZE,width=0.6,color="b")
plt.xlim([1,76])
plt.xticks(np.arange(75),(' ','1',' ',' ',' ',' ',' ',' ',' ',' ','10',' ',' ',' ',' ',' ',' ',' ',' ',' ','20',' ',' ',' ',' ',' ',' ',' ',' ',' ','30',' ',' ',' ',' ',' ',' ',' ',' ',' ','40',' ',' ',' ',' ',' ',' ',' ',' ',' ','50',' ',' ',' ',' ',' ',' ',' ',' ',' ','60',' ',' ',' ',' ',' ',' ',' ',' ',' ','70',' ',' ',' ',' ','75'))
plt.xlabel('Blade number',fontsize=16)
plt.ylabel('Sensitivity (1/rad)',fontsize=16)
plt.legend((p1,p2,p3),('$\sigma_{xx}$','$\sigma_{yy}$','$\sigma_{zz}$'))
plt.tick_params(axis='both', which='major', labelsize=12)

plt.tight_layout()
plt.savefig('StressZE.png', dpi=300)
plt.show()


p1=plt.bar(blnum,SxyAL,width=1.0,color="none",edgecolor='k')
p2=plt.bar(blnum,SyzAL,width=0.8,color="r")
p3=plt.bar(blnum,SzxAL,width=0.6,color="b")
plt.xlim([1,76])
plt.xticks(np.arange(75),(' ','1',' ',' ',' ',' ',' ',' ',' ',' ','10',' ',' ',' ',' ',' ',' ',' ',' ',' ','20',' ',' ',' ',' ',' ',' ',' ',' ',' ','30',' ',' ',' ',' ',' ',' ',' ',' ',' ','40',' ',' ',' ',' ',' ',' ',' ',' ',' ','50',' ',' ',' ',' ',' ',' ',' ',' ',' ','60',' ',' ',' ',' ',' ',' ',' ',' ',' ','70',' ',' ',' ',' ','75'))
plt.xlabel('Blade number',fontsize=16)
plt.ylabel('Sensitivity (1/rad)',fontsize=16)
plt.legend((p1,p2,p3),('$\sigma_{xy}$','$\sigma_{yz}$','$\sigma_{zx}$'))
plt.tick_params(axis='both', which='major', labelsize=12)

plt.tight_layout()
plt.savefig('ShearstressAL.png', dpi=300)
plt.show()

p1=plt.bar(blnum,SxyBE,width=1.0,color="none",edgecolor='k')
p2=plt.bar(blnum,SyzBE,width=0.8,color="r")
p3=plt.bar(blnum,SzxBE,width=0.6,color="b")
plt.xlim([1,76])
plt.xticks(np.arange(75),(' ','1',' ',' ',' ',' ',' ',' ',' ',' ','10',' ',' ',' ',' ',' ',' ',' ',' ',' ','20',' ',' ',' ',' ',' ',' ',' ',' ',' ','30',' ',' ',' ',' ',' ',' ',' ',' ',' ','40',' ',' ',' ',' ',' ',' ',' ',' ',' ','50',' ',' ',' ',' ',' ',' ',' ',' ',' ','60',' ',' ',' ',' ',' ',' ',' ',' ',' ','70',' ',' ',' ',' ','75'))

plt.xlabel('Blade number',fontsize=16)
plt.ylabel('Sensitivity (1/rad)',fontsize=16)
plt.legend((p1,p2,p3),('$\sigma_{xy}$','$\sigma_{yz}$','$\sigma_{zx}$'))
plt.tick_params(axis='both', which='major', labelsize=12)

plt.tight_layout()
plt.savefig('ShearstressBE.png', dpi=300)
plt.show()


p1=plt.bar(blnum,SxyZE,width=1.0,color="none",edgecolor='k')
p2=plt.bar(blnum,SyzZE,width=0.8,color="r")
p3=plt.bar(blnum,SzxZE,width=0.6,color="b")
plt.xlim([1,76])
plt.xticks(np.arange(75),(' ','1',' ',' ',' ',' ',' ',' ',' ',' ','10',' ',' ',' ',' ',' ',' ',' ',' ',' ','20',' ',' ',' ',' ',' ',' ',' ',' ',' ','30',' ',' ',' ',' ',' ',' ',' ',' ',' ','40',' ',' ',' ',' ',' ',' ',' ',' ',' ','50',' ',' ',' ',' ',' ',' ',' ',' ',' ','60',' ',' ',' ',' ',' ',' ',' ',' ',' ','70',' ',' ',' ',' ','75'))
plt.xlabel('Blade number',fontsize=16)
plt.ylabel('Sensitivity (1/rad)',fontsize=16)
plt.legend((p1,p2,p3),('$\sigma_{xy}$','$\sigma_{yz}$','$\sigma_{zx}$'))
plt.tick_params(axis='both', which='major', labelsize=12)

plt.tight_layout()
plt.savefig('ShearstressZE.png', dpi=300)
plt.show()
