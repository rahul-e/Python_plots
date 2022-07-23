#!/usr/bin/python
import pandas as pd
import matplotlib.pyplot as plt
from subprocess import call
from matplotlib.patches import Circle


Normfac=0.008909

df = pd.read_csv('./Plot_within_a_plot/S1envy.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)
df.columns = ['Frequency','Envelope']
df.head()

s1x=df['Frequency'].values/845	#optstep#1
s1y=df['Envelope'].values/Normfac

df = pd.read_csv('./Plot_within_a_plot/S20envy.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)
df.columns = ['Frequency','Envelope']
df.head()

s4x=df['Frequency'].values/845	#optstep#4
s4y=df['Envelope'].values/Normfac


df = pd.read_csv('./Plot_within_a_plot/S40envy.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)
df.columns = ['Frequency','Envelope']
df.head()

s7x=df['Frequency'].values/845	#optstep#7
s7y=df['Envelope'].values/Normfac


df = pd.read_csv('./Plot_within_a_plot/S60envy.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)
df.columns = ['Frequency','Envelope']
df.head()

s10x=df['Frequency'].values/845	#optstep#10
s10y=df['Envelope'].values/Normfac

df = pd.read_csv('./Plot_within_a_plot/S80envy.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)
df.columns = ['Frequency','Envelope']
df.head()

s15x=df['Frequency'].values/845	#optstep#15
s15y=df['Envelope'].values/Normfac

df = pd.read_csv('./Plot_within_a_plot/S110envy.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)
df.columns = ['Frequency','Envelope']
df.head()

s20x=df['Frequency'].values/845	#optstep#20
s20y=df['Envelope'].values/Normfac



do = pd.read_csv('./Plot_within_a_plot/optimize.txt',
                 header=None,
                 sep='\s+', error_bad_lines=False)

do.columns = ['maxampFreq', 'maxBL', 'maxamp', 'normmaxamp' ]
do.head()

v=do['normmaxamp'].values
x = [i+1 for i in range(0, len(v))]


plt.plot(x,v,'o',markersize=4)
plt.ylim([1.59,2.07])
plt.xlabel('Optimisation step',fontsize=16)
plt.ylabel('Amplification factor',fontsize=16)

inset=plt.axes([0.15,0.72,0.14,0.14])
plt.plot(s1x,s1y)
plt.ylim([0,2.1])
plt.text(3.84,1.6,'#1')
plt.tick_params(axis='both', which='major', labelsize=8)


inset=plt.axes([0.3,0.52,0.14,0.14])
plt.plot(s4x,s4y)
plt.ylim([0,2.1])
plt.text(3.84,1.6,'#20')
plt.tick_params(axis='both', which='major', labelsize=8)

inset=plt.axes([0.42,0.31,0.14,0.14])
plt.plot(s7x,s7y)
plt.ylim([0,2.1])
plt.text(3.84,1.6,'#40')
plt.tick_params(axis='both', which='major', labelsize=8)


inset=plt.axes([0.6,0.18,0.14,0.14])
plt.plot(s10x,s10y)
plt.ylim([0,2.1])
plt.text(3.84,1.6,'#60')
plt.tick_params(axis='both', which='major', labelsize=8)


inset=plt.axes([0.73,0.7,0.14,0.14])
plt.plot(s15x,s15y)
plt.ylim([0,2.1])
plt.text(3.84,1.6,'#80')
plt.tick_params(axis='both', which='major', labelsize=8)


inset=plt.axes([0.81,0.5,0.14,0.14])
plt.plot(s20x,s20y)
plt.ylim([0,2.1])
plt.text(3.84,1.6,'#110')
plt.tick_params(axis='both', which='major', labelsize=8)

plt.tight_layout()
plt.savefig('optimize.png', dpi=300)
plt.show()



