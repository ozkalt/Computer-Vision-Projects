import cv2
from matplotlib import pyplot as plt
import numpy as np

img1 = cv2.imread("color1.png")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

img2 = cv2.imread("color2.png")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

#plt.imshow(img1)
#plt.show()
#plt.imshow(img2)
#plt.show()

row1, col1, ch1 = img1.shape
arr1 = np.array(img1)

hist1 = [[0 for x in range(256)] for y in range(ch1)]

for i in range(row1):
    for j in range(col1):
        for k in range(ch1):
            hist1[k][arr1[i][j][k]] += 1

row2, col2, ch2 = img2.shape
arr2 = np.array(img2)

hist2 = [[0 for x in range(256)] for y in range(ch2)]

for i in range(row1):
    for j in range(col1):
        for k in range(ch1):
            hist2[k][arr2[i][j][k]] += 1

hists = [hist1, hist2]
titles = ['color1', 'color2']
color = ['b', 'g', 'r']

for i in range(2):
    plt.subplot(1,2,i+1)
    plt.title(titles[i])
    for j in range(ch2):
        plt.plot(hists[i][j], color[j])
    plt.xticks([]),plt.yticks([])

plt.show()
