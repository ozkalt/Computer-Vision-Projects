import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.ndimage.filters import gaussian_filter
from PIL import Image
from scipy import ndimage


def harris(I):
    row, col = I.shape
    
    sig = 0.3
    M = gaussian_filter(I, sigma=sig)
    dy, dx = np.gradient(M)
    Ixx = dx**2
    Ixy = dy*dx
    Iyy = dy**2

    thresh = 50000000000
    newImg = I.copy()
    color_img = cv2.cvtColor(newImg, cv2.COLOR_GRAY2RGB)
    window = 3
    k = 0.06
    for y in range(window, row-window):
        for x in range(window, col-window):
            windowIxx = Ixx[y-window:y+window+1, x-window:x+window+1]
            windowIxy = Ixy[y-window:y+window+1, x-window:x+window+1]
            windowIyy = Iyy[y-window:y+window+1, x-window:x+window+1]
            Gxx = windowIxx.sum()
            Gxy = windowIxy.sum()
            Gyy = windowIyy.sum()

            det = (Gxx * Gyy) - (Gxy**2)
            trace = Gxx + Gyy
            r = det - k*(trace**2)

            if r > thresh:
                color_img.itemset((y, x, 0), 255)
                color_img.itemset((y, x, 1), 0)
                color_img.itemset((y, x, 2), 0)
    return color_img


I = cv2.imread("blocks.jpg")
I = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

img = harris(I)
img = np.array(img, dtype=np.uint8)
img = Image.fromarray(img)
img.save('corners.jpg')



