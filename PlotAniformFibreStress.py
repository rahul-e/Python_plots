#!/usr/bin/env python
# coding: utf-8

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from mpl_toolkits import mplot3d
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib import cm
from matplotlib.pyplot import figure

def main(args):
    
    filename=args[-1]
    print("Read filename", filename)
    df = pd.read_csv(filename+'.txt', header=None, sep='\s+', error_bad_lines=False)
    df.head()

    NodenumIndex = df[df[1].str.fullmatch('nodes')].index
    NodeNum = df[2].iloc[NodenumIndex[0]]
    ResultIndex = df[df[1].str.fullmatch('results')].index
    nodecoords = pd.DataFrame(df.iloc[NodenumIndex[0]+1:int(NodeNum)+1+NodenumIndex[0],:].dropna(axis=1)).reset_index(drop=True).astype('float64')
    nodecoords.head()
    nodecoords.tail()
    
    df = pd.read_csv(filename+'.txt', header=None, sep='\s+', error_bad_lines=False)
    Fs2 = pd.DataFrame(df.iloc[ResultIndex[0]+1:ResultIndex[0]+1+int(NodeNum),:].dropna(axis=1)).reset_index(drop=True).astype('float64')

 
    df1 = pd.concat([nodecoords,Fs2[1]],axis=1,ignore_index=True)
    x=df1[1].values
    y=df1[2].values
    z=df1[4].values
    
    
    fig = plt.figure(figsize=(10,8))
    ax = plt.axes(projection='3d')
    sc=ax.scatter3D(x, y, z, c=z, cmap='seismic', vmin=-20, vmax=20)
    ax.set_xlim3d(0, 600)
    ax.set_ylim3d(-180, 180)
    ax.set_zlim3d(-20, 20)
    ax.set_xlabel('Length',fontsize=12)
    ax.set_ylabel('Width',fontsize=12)
    ax.set_zlabel('Stress (MPa)',fontsize=12)
    ax.view_init(-11, 114)
    fig.set_tight_layout(True)
    ax.tick_params(axis='both', which='major', labelsize=10)
    plt.colorbar(sc,shrink=0.46,pad=-0.08,orientation='horizontal')
    plt.tight_layout()
    plt.savefig(filename+'.png',dpi=300,pad_inches=0.1)
    plt.show()


if __name__ == '__main__':
    main(sys.argv)  

