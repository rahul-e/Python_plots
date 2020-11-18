#python
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

def sigmoid(x, L ,x0, k, b):
    y = L / (1 + np.exp(-k*(x-x0)))+b
    return (y)

xdata=[0,5,10,15,20,25]
ydata=[1,1,4,6,8,8]

x_sample=[0,   5,   11, 11.5, 12.0, 12.5, 13.0, 13.5, 15.0, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0]
y_sample=[0.2, 2.0, 3.5, 4.6, 4.3, 5.5, 6.1, 6.4, 6.8, 7.8, 8.0, 7.7, 8.2, 7.9, 8.1, 7.8]

x_pred=[0,   1.25, 2.5,  3.75, 5.0, 6.25, 7.5,  8.75, 10.0, 11.25, 12.5, 13.75, 15.0, 16.25, 17.5, 18.75, 20.0, 21.25, 22.5, 25.0]

y_pred=[0.2, 0.35, 0.45, 1.8,  2.0, 2.1,  2.05, 3.3,  3.6, 4.6,  5.5, 6.4,  6.8, 6.9,  6.7, 7.6,  7.8, 8.0,  8.1, 7.7]

print(len(x_sample),len(y_sample))

print(len(x_pred),len(y_pred))


p0 = [max(y_pred), np.median(x_pred),1,min(y_pred)] # this is an mandatory initial guess

popt, pcov = curve_fit(sigmoid, x_pred, y_pred,p0, method='dogbox')

x = np.linspace(0, 25, 1000)
y = sigmoid(x, *popt)


mu, sigma = 0.2, 1.0 # mean and standard deviation

#sigma1 = 2.5 # mean and standard deviation




mu1, sigma1 = 0.4, 1.5 # mean and standard deviation

mu2, sigma2 = 0.3, 2.5 # mean and standard deviation

mu3, sigma3 = 0.2, 0.8 # mean and standard deviation

#s = np.random.normal(mu, sigma, 1000)
#count, bins, ignored = plt.hist(s, 30, density=True, color='w')
#plt.plot(1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), bins, linewidth=1, color='k',linestyle='dashed')
#fig = plt.figure(frameon=False)
fig, ax1 = plt.subplots()
s = np.random.normal(mu, sigma, 1000)
count, bins, ignored = plt.hist(s, 30, density=True, color='w')


#ax1 = fig.add_axes([0, 0, 1, 1])

#ax2 = fig.add_axes([0.5, 0.5, 0.6, 0.6])
ax1.axis('on')
#plt.plot(xdata, ydata, 'o', label='Data')

#plt.ylim(0, 1.3)
plt.xlim(-1., 26.0)
#plt.ylim(0.,8.7)
plt.xlabel('Time (yrs)')
plt.ylabel('Graphite material property')
#plt.legend(loc='best')
#ax1 = fig.add_axes([0.5, 0.5, 0.6, 0.6])
ax1.plot(x_sample, y_sample, 'o', label='Data')
ax1.plot(x_pred,y_pred, 's', color='r',label='Supervised machine learning \nmodel',fillstyle='none')
ax1.plot(x,y, ':k', label='Mean of Gaussian process')
plt.legend(loc='best',frameon=False)
#axins = inset_axes(ax1, width=1.3, height=0.9)
axins1 = inset_axes(ax1, width="10%", height=.5, loc=1, bbox_to_anchor=(-0.22,-0.17,.3,.3), bbox_transform=ax1.transAxes) #posx, posy, width, height
axins1.plot(1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), bins, linewidth=1, color='k',linestyle='dashed')
axins1.patch.set_facecolor('red')
axins1.patch.set_alpha(0.1)
axins1.axis('off')


axins2 = inset_axes(ax1, width="10%", height=.5, loc=1, bbox_to_anchor=(-0.175,-0.14,.3,.3), bbox_transform=ax1.transAxes) #posx, posy, width, height
axins2.plot(1/(sigma2 * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu2)**2 / (2 * sigma2**2) ), bins, linewidth=1, color='k',linestyle='dashed', label='PDF')
axins2.patch.set_facecolor('red')
axins2.patch.set_alpha(0.1)
axins2.axis('off')



axins3 = inset_axes(ax1, width="10%", height=.5, loc=1, bbox_to_anchor=(-0.13,-0.14,.3,.3), bbox_transform=ax1.transAxes) #posx, posy, width, height
axins3.plot(1/(sigma2 * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu2)**2 / (2 * sigma2**2) ), bins, linewidth=1, color='k',linestyle='dashed', label='PDF')
axins3.patch.set_facecolor('red')
axins3.patch.set_alpha(0.1)
axins3.axis('off')



axins4 = inset_axes(ax1, width="10%", height=.5, loc=1, bbox_to_anchor=(-0.08,-0.05,.3,.3), bbox_transform=ax1.transAxes) #posx, posy, width, height
axins4.plot(1/(sigma2 * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu2)**2 / (2 * sigma2**2) ), bins, linewidth=1, color='k',linestyle='dashed', label='PDF')
axins4.patch.set_facecolor('red')
axins4.patch.set_alpha(0.1)
axins4.axis('off')


axins5 = inset_axes(ax1, width="10%", height=.5, loc=1, bbox_to_anchor=(-0.035,-0.018,.3,.3), bbox_transform=ax1.transAxes) #posx, posy, width, height
axins5.plot(1/(sigma3 * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu3)**2 / (2 * sigma3**2) ), bins, linewidth=1, color='k',linestyle='dashed', label='PDF')
axins5.patch.set_facecolor('red')
axins5.patch.set_alpha(0.1)
axins5.axis('off')


axins6 = inset_axes(ax1, width="10%", height=.5, loc=1, bbox_to_anchor=(0.01,0.02,.3,.3), bbox_transform=ax1.transAxes) #posx, posy, width, height
axins6.plot(1/(sigma2 * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu2)**2 / (2 * sigma2**2) ), bins, linewidth=1, color='k',linestyle='dashed', label='PDF')
axins6.patch.set_facecolor('red')
axins6.patch.set_alpha(0.1)
axins6.axis('off')


axins7 = inset_axes(ax1, width="10%", height=.5, loc=1, bbox_to_anchor=(0.05,0.07,.3,.3), bbox_transform=ax1.transAxes) #posx, posy, width, height
axins7.plot(1/(sigma2 * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu2)**2 / (2 * sigma2**2) ), bins, linewidth=1, color='k',linestyle='dashed', label='PDF')
axins7.patch.set_facecolor('red')
axins7.patch.set_alpha(0.1)
axins7.axis('off')


axins8 = inset_axes(ax1, width="10%", height=.5, loc=1, bbox_to_anchor=(0.099,0.14,.3,.3), bbox_transform=ax1.transAxes) #posx, posy, width, height
axins8.plot(1/(sigma2 * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu2)**2 / (2 * sigma2**2) ), bins, linewidth=1, color='k',linestyle='dashed', label='PDF')
axins8.patch.set_facecolor('red')
axins8.patch.set_alpha(0.1)
axins8.axis('off')


axins9 = inset_axes(ax1, width="10%", height=.5, loc=1, bbox_to_anchor=(0.15,0.21,.3,.3), bbox_transform=ax1.transAxes) #posx, posy, width, height
axins9.plot(1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), bins, linewidth=1, color='k',linestyle='dashed', label='PDF')
axins9.patch.set_facecolor('red')
axins9.patch.set_alpha(0.1)
axins9.axis('off')


axins10 = inset_axes(ax1, width="10%", height=.5, loc=1, bbox_to_anchor=(0.2,0.32,.3,.3), bbox_transform=ax1.transAxes) #posx, posy, width, height
axins10.plot(1/(sigma3 * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu3)**2 / (2 * sigma3**2) ), bins, linewidth=1, color='k',linestyle='dashed', label='PDF')
axins10.patch.set_facecolor('red')
axins10.patch.set_alpha(0.1)
axins10.axis('off')


axins11 = inset_axes(ax1, width="10%", height=.5, loc=1, bbox_to_anchor=(0.24,0.42,.3,.3), bbox_transform=ax1.transAxes) #posx, posy, width, height
axins11.plot(1/(sigma3 * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu3)**2 / (2 * sigma3**2) ), bins, linewidth=1, color='k',linestyle='dashed', label='PDF')
axins11.patch.set_facecolor('red')
axins11.patch.set_alpha(0.1)
axins11.axis('off')

axins12 = inset_axes(ax1, width="10%", height=.5, loc=1, bbox_to_anchor=(0.29,0.5,.3,.3), bbox_transform=ax1.transAxes) #posx, posy, width, height
axins12.plot(1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), bins, linewidth=1, color='k',linestyle='dashed', label='PDF')
axins12.patch.set_facecolor('red')
axins12.patch.set_alpha(0.1)
axins12.axis('off')


axins13 = inset_axes(ax1, width="10%", height=.5, loc=1, bbox_to_anchor=(0.34,0.55,.3,.3), bbox_transform=ax1.transAxes) #posx, posy, width, height
axins13.plot(1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), bins, linewidth=1, color='k',linestyle='dashed', label='PDF')
axins13.patch.set_facecolor('red')
axins13.patch.set_alpha(0.1)
axins13.axis('off')


axins14 = inset_axes(ax1, width="10%", height=.5, loc=1, bbox_to_anchor=(0.375,0.58,.3,.3), bbox_transform=ax1.transAxes) #posx, posy, width, height
axins14.plot(1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), bins, linewidth=1, color='k',linestyle='dashed', label='PDF')
axins14.patch.set_facecolor('red')
axins14.patch.set_alpha(0.1)
axins14.axis('off')



axins15 = inset_axes(ax1, width="10%", height=.5, loc=1, bbox_to_anchor=(0.42,0.6,.3,.3), bbox_transform=ax1.transAxes) #posx, posy, width, height
axins15.plot(1/(sigma1 * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu1)**2 / (2 * sigma1**2) ), bins, linewidth=1, color='k',linestyle='dashed', label='PDF')
axins15.patch.set_facecolor('red')
axins15.patch.set_alpha(0.1)
axins15.axis('off')



axins16 = inset_axes(ax1, width="10%", height=.5, loc=1, bbox_to_anchor=(0.465,0.65,.3,.3), bbox_transform=ax1.transAxes) #posx, posy, width, height
axins16.plot(1/(sigma3 * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu3)**2 / (2 * sigma3**2) ), bins, linewidth=1, color='k',linestyle='dashed', label='PDF')
axins16.patch.set_facecolor('red')
axins16.patch.set_alpha(0.1)
axins16.axis('off')


axins17 = inset_axes(ax1, width="10%", height=.5, loc=1, bbox_to_anchor=(0.52,0.68,.3,.3), bbox_transform=ax1.transAxes) #posx, posy, width, height
axins17.plot(1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), bins, linewidth=1, color='k',linestyle='dashed', label='PDF')
axins17.patch.set_facecolor('red')
axins17.patch.set_alpha(0.1)
axins17.axis('off')


axins18 = inset_axes(ax1, width="10%", height=.5, loc=1, bbox_to_anchor=(0.56,0.71,.3,.3), bbox_transform=ax1.transAxes) #posx, posy, width, height
axins18.plot(1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), bins, linewidth=1, color='k',linestyle='dashed', label='PDF')
axins18.patch.set_facecolor('red')
axins18.patch.set_alpha(0.1)
axins18.axis('off')


axins19 = inset_axes(ax1, width="10%", height=.5, loc=1, bbox_to_anchor=(0.6,0.71,.3,.3), bbox_transform=ax1.transAxes) #posx, posy, width, height
axins19.plot(1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), bins, linewidth=1, color='k',linestyle='dashed', label='PDF')
axins19.patch.set_facecolor('red')
axins19.patch.set_alpha(0.1)
axins19.axis('off')

axins20 = inset_axes(ax1, width="10%", height=.5, loc=1, bbox_to_anchor=(0.69,0.71,.3,.3), bbox_transform=ax1.transAxes) #posx, posy, width, height
axins20.plot(1/(sigma2 * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu2)**2 / (2 * sigma2**2) ), bins, linewidth=1, color='k',linestyle='dashed', label='PDF')
axins20.patch.set_facecolor('red')
axins20.patch.set_alpha(0.1)
axins20.axis('off')


ax1.annotate('Predictive posterior distribution \nat points of interest obtained\nfrom Gaussian process regression',xy=(14,6.0),  xycoords='data',
            xytext=(25, 3.5), textcoords='data',
            arrowprops=dict(facecolor='black', shrink=0.05,width=1.0,headwidth=5.0),
            horizontalalignment='right', verticalalignment='top')

plt.savefig('Methodology_UA.png',bbox_inches = 'tight',pad_inches = 0)
plt.show()