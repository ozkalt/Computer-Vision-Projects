import cv2
from matplotlib import pyplot as plt
import numpy as np

img1 = cv2.imread("color1.png")
img2 = cv2.imread("color2.png")

def histEQ(img, bins=256):
    hist, bins = histogram(img.flatten(), bins, normed=True)
    cdf = np.cumsum(img)
    cdf = 255 * cdf / cdf[-1]
    
    img2 = interp(im.flatten(), bins[:-1], cdf)
    
    return img2.reshape(img.shape), cdf


bins=255

if len(img1.shape) < 3:
    img1 = img1[:,:,np.newaxis]
    img2 = img2[:,:,np.newaxis]

newimg = img1.copy()
for d in range(img1.shape[2]):
    hist, bins = np.histogram(img1[:,:,d].flatten(), bins, normed=True)
    hist2, bins = np.histogram(img2[:,:,d].flatten(), bins, normed=True)
    
    cdf1 = np.cumsum(img1)
    cdf1 = 255 * cdf1 / cdf1[-1].astype(np.uint8)
    
    cdf2 = np.cumsum(img2)
    cdf2 = 255 * cdf2 / cdf2[-1].astype(np.uint8)
    
    img3 = np.interp(img1[:,:,d].flatten(),bins[:-1],cdf1)

    img4 = np.interp(img3,cdf2, bins[:-1])
    
    newimg[:,:,d] = img4.reshape((img1.shape[0],img1.shape[1] ))


cv2.imwrite("histogrammatchedimage.png", newimg)
