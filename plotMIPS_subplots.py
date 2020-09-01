#python3
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.gridspec as gridspec

MeanFlexStrength=27.61 # Wood report on testing of failure of sealing ring inner groove Pg.42
df = pd.read_csv('Job-20200818_UpperInnerGrooveWallMaxMIPS.txt', sep='\t')
df.columns = ['X18', 'Y18']

X18U=df['X18'].values
Y18U=df['Y18'].values



df = pd.read_csv('Job-20200823_UpperInnerGrooveWallMaxMIPS.txt', sep='\t')
df.columns = ['X23', 'Y23']

X23U=df['X23'].values
Y23U=df['Y23'].values


Y18U_=[y/MeanFlexStrength for y in Y18U]
Y23U_=[y/MeanFlexStrength for y in Y23U]

df = pd.read_csv('Job-20200818_LowerInnerGrooveWallMaxMIPS.txt', sep='\t')
df.columns = ['X18', 'Y18']

X18L=df['X18'].values
Y18L=df['Y18'].values



df = pd.read_csv('Job-20200823_LowerInnerGrooveWallMaxMIPS.txt', sep='\t')
df.columns = ['X23', 'Y23']

X23L=df['X23'].values
Y23L=df['Y23'].values


Y18L_=[y/MeanFlexStrength for y in Y18L]
Y23L_=[y/MeanFlexStrength for y in Y23L]

#fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 20))
DF=[0, 0.000005, 0.000001]
fig, big_axes = plt.subplots( figsize=(10.0, 15.0) , nrows=2, ncols=1, sharey=False)


for i, big_ax in enumerate(big_axes, start=1):
    big_ax.set_title("Damping factor = %s" % DF[i], fontsize=16)
    
    # Turn off axis lines and ticks of the big subplot 
    # obs alpha is 0 in RGBA string!
    big_ax.tick_params(labelcolor=(1.,1.,1., 0.0), top='off', bottom='off', left='off', right='off')
    # removes the white frame
    big_ax._frameon = False


ax1 = fig.add_subplot(2,2,1)    
ax1.plot(X18U, Y18U, ':*', label='Detailed')
ax1.plot(X23U, Y23U, ':o', label='Simplified')

ax1.legend(fancybox=True, framealpha=0.5)
ax1.tick_params(axis='both', which='major', labelsize=16)

ax1.yaxis.get_label().set_fontsize(16)
ax1.xaxis.get_label().set_fontsize(16)

ax2 = fig.add_subplot(2,2,2)
ax2.plot(X18U, Y18U_, ':*', label='Detailed')
ax2.plot(X23U, Y23U_, ':o', label='Simplified')

ax2.legend(fancybox=True, framealpha=0.5)
ax2.tick_params(axis='both', which='major', labelsize=16)

ax2.yaxis.get_label().set_fontsize(16)
ax2.xaxis.get_label().set_fontsize(16)

ax3 = fig.add_subplot(2,2,3)
ax3.plot(X18L, Y18L, ':*', label='Detailed')
ax3.plot(X23L, Y23L, ':o', label='Simplified')

ax3.legend(fancybox=True, framealpha=0.5)
ax3.tick_params(axis='both', which='major', labelsize=16)

ax3.yaxis.get_label().set_fontsize(16)
ax3.xaxis.get_label().set_fontsize(16)

ax4 = fig.add_subplot(2,2,4)
ax4.plot(X18L, Y18L_, ':*', label='Detailed')
ax4.plot(X23L, Y23L_, ':o', label='Simplified')

ax4.legend(fancybox=True, framealpha=0.5)
ax4.tick_params(axis='both', which='major', labelsize=16)

ax4.yaxis.get_label().set_fontsize(16)
ax4.xaxis.get_label().set_fontsize(16)

plt.setp(ax1, xlabel='FPY')
plt.setp(ax2, xlabel='FPY')
plt.setp(ax3, xlabel='FPY')
plt.setp(ax4, xlabel='FPY')

plt.setp(ax1, ylabel='MIPS (MPa)')
plt.setp(ax2, ylabel='Stress/Strength')
plt.setp(ax3, ylabel='MIPS(MPa)')
plt.setp(ax4, ylabel='Stress/Strength')


fig.subplots_adjust(wspace=0.25, hspace=0.2)

plt.tight_layout
plt.savefig('MaxMIPS_LowerUpperGroove_20200827.png',bbox_inches='tight', pad_inches=0, DPI=300)

plt.show()

