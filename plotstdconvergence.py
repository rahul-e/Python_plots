#!/usr/bin/python
import pandas as pd
import matplotlib.pyplot as plt
from subprocess import call
from matplotlib import rc
import numpy as np
from matplotlib import figure

Normfacm1eo8=1.001190E-01
Normfacm2eo8=2.130604E-02
Normfacm1eo35=1.20270E-02

#plt.rcParams["figure.figsize"] = (10,3)

#**************************** M1EO8 ********************************
df = pd.read_csv('./Lineplot/M1EO8fixALPHA.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)

df.columns = ['Mean','STD']
df.head()

m1eo8ALmean=df['Mean'].values/Normfacm1eo8
m1eo8ALstd=df['STD'].values/Normfacm1eo8


df = pd.read_csv('./Lineplot/M1EO8fixBETA.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)

df.columns = ['Mean','STD']
df.head()

m1eo8BEmean=df['Mean'].values/Normfacm1eo8
m1eo8BEstd=df['STD'].values/Normfacm1eo8

df = pd.read_csv('./Lineplot/M1EO8fixZETA.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)

df.columns = ['Mean','STD']
df.head()

m1eo8ZEmean=df['Mean'].values/Normfacm1eo8
m1eo8ZEstd=df['STD'].values/Normfacm1eo8


#********************** M2EO8 *********************************

df = pd.read_csv('./Lineplot/M2EO8fixALPHA.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)

df.columns = ['Mean','STD']
df.head()

m2eo8ALmean=df['Mean'].values/Normfacm2eo8
m2eo8ALstd=df['STD'].values/Normfacm2eo8



df = pd.read_csv('./Lineplot/M2EO8fixBETA.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)

df.columns = ['Mean','STD']
df.head()

m2eo8BEmean=df['Mean'].values/Normfacm2eo8
m2eo8BEstd=df['STD'].values/Normfacm2eo8

df = pd.read_csv('./Lineplot/M2EO8fixZETA.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)

df.columns = ['Mean','STD']
df.head()

m2eo8ZEmean=df['Mean'].values/Normfacm2eo8
m2eo8ZEstd=df['STD'].values/Normfacm2eo8


#********************** M1EO35 *********************************

df = pd.read_csv('./Lineplot/M1EO35fixALPHA.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)

df.columns = ['Mean','STD']
df.head()

m1eo35ALmean=df['Mean'].values/Normfacm1eo35
m1eo35ALstd=df['STD'].values/Normfacm1eo35



df = pd.read_csv('./Lineplot/M1EO35fixBETA.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)

df.columns = ['Mean','STD']
df.head()

m1eo35BEmean=df['Mean'].values/Normfacm1eo35
m1eo35BEstd=df['STD'].values/Normfacm1eo35

df = pd.read_csv('./Lineplot/M1EO35fixZETA.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)

df.columns = ['Mean','STD']
df.head()

m1eo35ZEmean=df['Mean'].values/Normfacm1eo35
m1eo35ZEstd=df['STD'].values/Normfacm1eo35

alphasample=[i+1 for i in range(len(m1eo8ALstd))]
betasample=[i+1 for i in range(len(m1eo8BEstd))]
zetasample=[i+1 for i in range(len(m1eo8ZEstd))]

p1,=plt.plot(alphasample,m1eo8ALstd,'-o')
p2,=plt.plot(betasample,m1eo8BEstd,'-o')
p3,=plt.plot(zetasample,m1eo8ZEstd,'-o')
plt.xlim([0,165])

plt.xlabel('Number of Monte Carlo evaluations',fontsize=16)
plt.ylabel('Normalised standard deviation',fontsize=16)
plt.legend((p1,p2,p3),(r'$\beta=\beta_0, \zeta=\zeta_0$',r'$\alpha=\alpha_0, \zeta=\zeta_0$',r'$\alpha=\alpha_0, \beta=\beta_0$'))
plt.tick_params(axis='both', which='major', labelsize=12)
#plt.legend(loc=2, prop={'size': 6})
plt.tight_layout()
plt.savefig('STDm1eo8.png', dpi=300)
plt.show()

alphasample=[i+1 for i in range(len(m2eo8ALstd))]
betasample=[i+1 for i in range(len(m2eo8BEstd))]
zetasample=[i+1 for i in range(len(m2eo8ZEstd))]


p1,=plt.plot(alphasample,m2eo8ALstd,'-o')
p2,=plt.plot(betasample,m2eo8BEstd,'-o')
p3,=plt.plot(zetasample,m2eo8ZEstd,'-o')
plt.xlim([0,165])

plt.xlabel('Number of Monte Carlo evaluations',fontsize=16)
plt.ylabel('Normalised standard deviation',fontsize=16)
plt.legend((p1,p2,p3),(r'$\beta=\beta_0, \zeta=\zeta_0$',r'$\alpha=\alpha_0, \zeta=\zeta_0$',r'$\alpha=\alpha_0, \beta=\beta_0$'))
plt.tick_params(axis='both', which='major', labelsize=12)
#plt.legend(loc=2, prop={'size': 6})
plt.tight_layout()
plt.savefig('STDm2eo8.png', dpi=300)
plt.show()

alphasample=[i+1 for i in range(len(m1eo35ALstd))]
betasample=[i+1 for i in range(len(m1eo35BEstd))]
zetasample=[i+1 for i in range(len(m1eo35ZEstd))]

p1,=plt.plot(alphasample,m1eo35ALstd,'-o')
p2,=plt.plot(betasample,m1eo35BEstd,'-o')
p3,=plt.plot(zetasample,m1eo35ZEstd,'-o')
plt.xlim([0,165])

plt.xlabel('Number of Monte Carlo evaluations',fontsize=16)
plt.ylabel('Normalised standard deviation',fontsize=16)
plt.legend((p1,p2,p3),(r'$\beta=\beta_0, \zeta=\zeta_0$',r'$\alpha=\alpha_0, \zeta=\zeta_0$',r'$\alpha=\alpha_0, \beta=\beta_0$'))
plt.tick_params(axis='both', which='major', labelsize=12)
#plt.legend(loc=2, prop={'size': 6})
plt.tight_layout()
plt.savefig('STDm1eo35.png', dpi=300)
plt.show()


