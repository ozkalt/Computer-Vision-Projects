import numpy as np
import cv2
from matplotlib import pyplot as plt

def histeq(im,nbr_bins=256):
    
    #get image histogram
    imhist,bins = histogram(im.flatten(),nbr_bins,normed=True)
    cdf = imhist.cumsum() #cumulative distribution function
    cdf = 255 * cdf / cdf[-1] #normalize

    #use linear interpolation of cdf to find new pixel values
    im2 = interp(im.flatten(),bins[:-1],cdf)
        
    return im2.reshape(im.shape), cdf

imsrc = cv2.imread("Color1.png")
imtint = cv2.imread("Color2.png")

nbr_bins=255
if len(imsrc.shape) < 3:
    imsrc = imsrc[:,:,np.newaxis]
    imtint = imtint[:,:,np.newaxis]

imres = imsrc.copy()
for d in range(imsrc.shape[2]):
    imhist,bins = np.histogram(imsrc[:,:,d].flatten(),nbr_bins,normed=True)
    tinthist,bins = np.histogram(imtint[:,:,d].flatten(),nbr_bins,normed=True)
    
    cdfsrc = imhist.cumsum() #cumulative distribution function
    cdfsrc = (255 * cdfsrc / cdfsrc[-1]).astype(np.uint8) #normalize
    
    cdftint = tinthist.cumsum() #cumulative distribution function
    cdftint = (255 * cdftint / cdftint[-1]).astype(np.uint8) #normalize
    
    
    im2 = np.interp(imsrc[:,:,d].flatten(),bins[:-1],cdfsrc)
    
    
    
    im3 = np.interp(im2,cdftint, bins[:-1])
    
    imres[:,:,d] = im3.reshape((imsrc.shape[0],imsrc.shape[1] ))

try:
    cv2.imwrite("histogram matched image.jpg", imres)
except:
    cv2.imwrite("histogram matched image.jpg", imres.reshape((imsrc.shape[0],imsrc.shape[1] )))
