import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("2DScatterof3Ddata/data.txt", sep='\s+',header=0)
plotrownum = 2
#print(df.head())

x1 = 20.
y1 = 19.

x2 = 57.
y2 = 19.

x3 = 95.
y3 = 20.

x4 = 20.
y4 = 60.

x5 = 56.
y5 = 60.

x6 = 95.
y6 = 60.

x7 = 56.
y7 = 95.

x8 = 95.
y8 = 95.

x = [x1, x2, x3, x4, x5, x6, x7, x8]
y = [y1, y2, y3, y4, y5, y6, y7, y8]

z_data = df.iloc[:, lambda df: [i for i in range(0,8)]]

fig, ax = plt.subplots()
fig.set_figheight(11)
fig.set_figwidth(11)

z = z_data.iloc[plotrownum].values
print(len(z))
sc = ax.scatter(x, y, z, c=z, cmap='seismic')

ax.set_xlim(0,110)
ax.set_ylim(0,110)
ax.set_title("Plot 3D data in 2D scatter plot with the help of a colorbar",\
              fontdict={'fontsize': 16, 'fontweight': 'medium'})

ax.set_xlabel("X label")
ax.set_ylabel("Y label")

ax.tick_params(axis='both', which='major', labelsize=16)
ax.yaxis.get_label().set_fontsize(16)
ax.xaxis.get_label().set_fontsize(16)


cbar = plt.colorbar(sc)
cbar.ax.tick_params(labelsize=16) 
for count, (i, j) in enumerate(zip(x, y)):
    ax.text(i+1, j+1, count+1, fontsize=12)


plt.savefig("./2DScatterof3Ddata/2DScatterof3Ddata.png")