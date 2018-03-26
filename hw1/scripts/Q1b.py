import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("underexposed.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#plt.imshow(img)
#plt.title('underexposed image')
#plt.show()

row, col, ch = img.shape
arr = np.array(img)

hist = [[0 for x in range(256)] for y in range(ch)]

for i in range(row):
    for j in range(col):
        for k in range(ch):
            hist[k][arr[i][j][k]] += 1

color = ['b', 'g', 'r']

for i in range(ch):
    plt.title('histograms of the underexposed image')
    plt.plot(hist[i], color[i])
plt.show()
