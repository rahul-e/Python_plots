#!/usr/bin/python
import pandas as pd
import matplotlib.pyplot as plt
from subprocess import call
from matplotlib import rc
import numpy as np
from matplotlib import figure

plt.rcParams["figure.figsize"] = (10,3)

df = pd.read_csv('./axialfirst.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)

df.columns = ['AL','BE','ZE']
df.head()

FaxAL=df['AL'].values
FaxBE=df['BE'].values
FaxZE=df['ZE'].values


df = pd.read_csv('./Tangfirst.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)

df.columns = ['AL','BE','ZE']
df.head()

FtanAL=df['AL'].values
FtanBE=df['BE'].values
FtanZE=df['ZE'].values

df = pd.read_csv('./radialfirst.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)

df.columns = ['AL','BE','ZE']
df.head()

FradAL=df['AL'].values
FradBE=df['BE'].values
FradZE=df['ZE'].values

df = pd.read_csv('./axialtotal.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)

df.columns = ['AL','BE','ZE']
df.head()

TaxAL=df['AL'].values
TaxBE=df['BE'].values
TaxZE=df['ZE'].values


df = pd.read_csv('./Tangtotal.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)

df.columns = ['AL','BE','ZE']
df.head()

TtanAL=df['AL'].values
TtanBE=df['BE'].values
TtanZE=df['ZE'].values


df = pd.read_csv('./radialtotal.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)

df.columns = ['AL','BE','ZE']
df.head()

TradAL=df['AL'].values
TradBE=df['BE'].values
TradZE=df['ZE'].values

blnumCW=[i+1 for i in range(15)]
blnumCCW=[i+61 for i in range(15)]
blnum=[i+1 for i in range(30)]


p1=plt.bar(blnum,TradAL,width=0.8,color="none",edgecolor='k')
p2=plt.bar(blnum,FradAL,width=0.6,color="r")
plt.xlim([1,31])
plt.xticks(np.arange(31),(' ','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75'))
plt.xlabel('Blade number',fontsize=16)
plt.ylabel('Sobol indices',fontsize=16)
plt.legend((p1,p2),('Total order','First order'))
plt.tick_params(axis='both', which='major', labelsize=12)

plt.tight_layout()
plt.savefig('SobolradialAL.png', dpi=300)
plt.show()

p1=plt.bar(blnum,TaxAL,width=0.8,color="none",edgecolor='k')
p2=plt.bar(blnum,FaxAL,width=0.6,color="r")
plt.xlim([1,31])
plt.xticks(np.arange(31),(' ','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75'))
plt.xlabel('Blade number',fontsize=16)
plt.ylabel('Sobol indices',fontsize=16)
plt.legend((p1,p2),('Total order','First order'))
plt.tick_params(axis='both', which='major', labelsize=12)

plt.tight_layout()
plt.savefig('SobolaxialAL.png', dpi=300)
plt.show()


p1=plt.bar(blnum,TtanAL,width=0.8,color="none",edgecolor='k')
p2=plt.bar(blnum,FtanAL,width=0.6,color="r")
plt.xlim([1,31])
plt.xticks(np.arange(31),(' ','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75'))
plt.xlabel('Blade number',fontsize=16)
plt.ylabel('Sobol indices',fontsize=16)
plt.legend((p1,p2),('Total order','First order'))
plt.tick_params(axis='both', which='major', labelsize=12)

plt.tight_layout()
plt.savefig('SoboltangAL.png', dpi=300)
plt.show()


p1=plt.bar(blnum,TtanBE,width=0.8,color="none",edgecolor='k')
p2=plt.bar(blnum,FtanBE,width=0.6,color="r")
plt.xlim([1,31])
plt.xticks(np.arange(31),(' ','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75'))
plt.xlabel('Blade number',fontsize=16)
plt.ylabel('Sobol indices',fontsize=16)
plt.legend((p1,p2),('Total order','First order'))
plt.tick_params(axis='both', which='major', labelsize=12)

plt.tight_layout()
plt.savefig('SoboltangBE.png', dpi=300)
plt.show()


p1=plt.bar(blnum,TaxBE,width=0.8,color="none",edgecolor='k')
p2=plt.bar(blnum,FaxBE,width=0.6,color="r")
plt.xlim([1,31])
plt.xticks(np.arange(31),(' ','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75'))
plt.xlabel('Blade number',fontsize=16)
plt.ylabel('Sobol indices',fontsize=16)
plt.legend((p1,p2),('Total order','First order'))
plt.tick_params(axis='both', which='major', labelsize=12)

plt.tight_layout()
plt.savefig('SobolaxialBE.png', dpi=300)
plt.show()


p1=plt.bar(blnum,TradBE,width=0.8,color="none",edgecolor='k')
p2=plt.bar(blnum,FradBE,width=0.6,color="r")
plt.xlim([1,31])
plt.xticks(np.arange(31),(' ','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75'))
plt.xlabel('Blade number',fontsize=16)
plt.ylabel('Sobol indices',fontsize=16)
plt.legend((p1,p2),('Total order','First order'))
plt.tick_params(axis='both', which='major', labelsize=12)

plt.tight_layout()
plt.savefig('SobolradialBE.png', dpi=300)
plt.show()


p1=plt.bar(blnum,TtanZE,width=0.8,color="none",edgecolor='k')
p2=plt.bar(blnum,FtanZE,width=0.6,color="r")
plt.xlim([1,31])
plt.xticks(np.arange(31),(' ','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75'))
plt.xlabel('Blade number',fontsize=16)
plt.ylabel('Sobol indices',fontsize=16)
plt.legend((p1,p2),('Total order','First order'))
plt.tick_params(axis='both', which='major', labelsize=12)

plt.tight_layout()
plt.savefig('SoboltangZE.png', dpi=300)
plt.show()


p1=plt.bar(blnum,TradZE,width=0.8,color="none",edgecolor='k')
p2=plt.bar(blnum,FradZE,width=0.6,color="r")
plt.xlim([1,31])
plt.xticks(np.arange(31),(' ','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75'))
plt.xlabel('Blade number',fontsize=16)
plt.ylabel('Sobol indices',fontsize=16)
plt.legend((p1,p2),('Total order','First order'))
plt.tick_params(axis='both', which='major', labelsize=12)

plt.tight_layout()
plt.savefig('SobolradialZE.png', dpi=300)
plt.show()


p1=plt.bar(blnum,TaxZE,width=0.8,color="none",edgecolor='k')
p2=plt.bar(blnum,FaxZE,width=0.6,color="r")
plt.xlim([1,31])
plt.xticks(np.arange(31),(' ','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75'))
plt.xlabel('Blade number',fontsize=16)
plt.ylabel('Sobol indices',fontsize=16)
plt.legend((p1,p2),('Total order','First order'))
plt.tick_params(axis='both', which='major', labelsize=12)

plt.tight_layout()
plt.savefig('SobolaxialZE.png', dpi=300)
plt.show()

