import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.ndimage.filters import gaussian_filter
from PIL import Image
from scipy import ndimage


def canny(I, sig, tau):
   
    M = gaussian_filter(I, sigma=sig)   ## Firstly, gaussian filter is applied.

    I = I.astype('int32')
    sobelx = ndimage.sobel(I, 0)
    sobely = ndimage.sobel(I, 1)
    mag = np.hypot(sobelx, sobely)
    mag *= 255.0 / np.max(mag)
    
    
    row, col = I.shape
    
    E = np.zeros(shape=(row, col))
    A = np.zeros(shape=(row, col))
    
    for i in range(row):
        for j in range(col):
            E[i][j] = ((sobelx[i][j]**2) + (sobely[i][j]**2))**(1/2)
            if E[i][j] <= tau:
                E[i][j] = 0
            
            if sobelx[i][j] != 0:
                A[i][j] = np.arctan(sobely[i][j]/sobelx[i][j])
                
                if A[i][j] < 22.5 and A[i][j] >= 0:
                    A[i][j] = 0
                elif A[i][j] < 67.5 and A[i][j] >= 22.5:
                    A[i][j] = 45
                elif A[i][j] < 112.5 and A[i][j] >= 67.5:
                    A[i][j] = 90
                elif A[i][j] < 157.5 and A[i][j] >= 112.5:
                    A[i][j] = 135
                elif A[i][j] <= 180 and A[i][j] >= 157.5:
                    A[i][j] = 0

    for i in range(1, row-1):
        for j in range(1, col-1):
            if A[i][j] == 0:
                if E[i][j] <= E[i-1][j] or E[i][j] <= E[i+1][j]:
                    E[i][j] = 0
            elif A[i][j] == 45:
                if E[i][j] <= E[i+1][j+1] or E[i][j] <= E[i-1][j-1]:
                    E[i][j] = 0
            elif A[i][j] == 90:
                if E[i][j] <= E[i][j-1] or E[i][j] <= E[i][j+1]:
                    E[i][j] = 0
            elif A[i][j] == 135:
                if E[i][j] <= E[i-1][j+1] or E[i][j] <= E[i+1][j-1]:
                    E[i][j] = 0
    
    return E, M, A;


img = cv2.imread('Fig2wirebond_mask.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


e05, m05, a05 = canny(img, 0.5, 5)
e1, m1, a1 = canny(img, 1, 5)
e3, m3, a3 = canny(img, 3, 5)


e05 = np.array(e05, dtype=np.uint8)
e05 = Image.fromarray(e05, "L")
e05.save('first05.jpg')

e1 = np.array(e1, dtype=np.uint8)
e1 = Image.fromarray(e1, "L")
e1.save('first1.jpg')

e3 = np.array(e3, dtype=np.uint8)
e3 = Image.fromarray(e3, "L")
e3.save('first3.jpg')


fig3 = cv2.imread('Fig3bottles.jpg')
fig3 = cv2.cvtColor(fig3, cv2.COLOR_BGR2GRAY)

fig3E, fig3M, fig3A = canny(fig3, 7.5, 200)

fig3E = np.array(fig3E, dtype=np.uint8)
fig3E = Image.fromarray(fig3E, "L")
fig3E.save('fig3.jpg')


builtin = cv2.Canny(fig3,100,200)
builtin = np.array(builtin, dtype=np.uint8)
builtin = Image.fromarray(builtin, "L")
builtin.save('builtin.jpg')



