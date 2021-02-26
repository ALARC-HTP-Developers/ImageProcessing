# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 12:11:17 2021

@author: ibkpu
"""
#date = sys.argv[0]
from PIL import Image
import PIL.Image
import numpy as np
from skimage import io, color
import matplotlib 
import rasterio
from rasterio import plot

path = r'D:\T2020 F13B4 Timothy\DOY181\odm_orthophoto'
RGBA = Image.open(r'D:\T2020 F13B4 Timothy\DOY181\odm_orthophoto\odm_orthophoto_sub.tif')
R = rasterio.open(r'D:\T2020 F13B4 Timothy\DOY181\odm_orthophoto\S2red.tif') # A one channel image (in this case Red channel) is needed to create individual LAB color channels


#Converting RGBA to RGB (Removing the fourth channel from RGBA)
RGB = RGBA.convert('RGB')

#Converting RGB to LAB color space
LAB = color.rgb2lab(RGB)

#splitting LAB into L, A, B channels
L_array= np.array(LAB[:,:,0])
A_array= np.array(LAB[:,:,1])
B_array = np.array(LAB[:,:,2])

#Plotting L channel from L_array
L_image = rasterio.open(path +'\\' + 'span2L.tif', 'w', driver = 'Gtiff',
                         width=R.width, height=R.height,
                         count = 1,
                         crs=R.crs,
                         transform=R.transform,
                         dtype='float64'
                         )
                         

L_image.write(L_array, 1)
L_image.close()

L = rasterio.open (path  +'\\' + 'span2L.tif')
plot.show(L)

#Plotting A channel from A_array
A_image = rasterio.open(path +'\\' + 'span2A.tif', 'w', driver = 'Gtiff',
                         width=R.width, height=R.height,
                         count = 1,
                         crs=R.crs,
                         transform=R.transform,
                         dtype='float64'
                         )
                         

A_image.write(A_array, 1)
A_image.close()

A = rasterio.open (path  +'\\' + 'span2A.tif')
plot.show(A)

#Plotting B channel from A_array
B_image = rasterio.open(path +'\\' + 'span2B.tif', 'w', driver = 'Gtiff',
                         width=R.width, height=R.height,
                         count = 1,
                         crs=R.crs,
                         transform=R.transform,
                         dtype='float64'
                         )
                         

B_image.write(B_array, 1)
B_image.close()

B = rasterio.open (path  +'\\' + 'span2B.tif')
plot.show(B)




