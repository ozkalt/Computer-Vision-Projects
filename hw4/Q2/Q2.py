import cv2
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
from scipy import ndimage

img = cv2.imread("mr.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

row, col = img.shape
arr = np.array(img)
skull = np.array(img)
hist = np.zeros(256)

for i in range(row):
    for j in range(col):
        hist[arr[i][j]] += 1


plt.title('histogram of the mr image')
plt.plot(hist)
plt.show()

"""
print ("Enter threshold value:"),
thresh = input()
thresh = int(thresh)
"""
thresh = 100

for i in range(row):
    for j in range(col):
        if(arr[i][j] < thresh):
            arr[i][j] = 0
        else:
            arr[i][j] = 255

arr = np.array(arr, dtype=np.uint8)
t = Image.fromarray(arr)
t.save('mrthresh.jpg')

kernel = np.ones((12,12),np.uint8)

erosion = cv2.erode(arr,kernel,iterations = 1)
erosion = np.array(erosion, dtype=np.uint8)
t = Image.fromarray(erosion)
t.save('skull.jpg')

"""
print ("Enter threshold value for skull:"),
thresh_skull = input()
thresh_skull = int(thresh_skull)
"""
thresh_skull = 220
for i in range(row):
    for j in range(col):
        if(skull[i][j] < thresh):
            skull[i][j] = 0
        elif(skull[i][j] > thresh and skull[i][j] < thresh_skull):
            skull[i][j] = 127
        else:
            skull[i][j] = 255

        if(skull[i][j] > erosion[i][j]):
            skull[i][j] = 0


tumor = np.array(skull, dtype=np.uint8)
s = Image.fromarray(tumor)
s.save('tumor.jpg')

for i in range(row):
    for j in range(col):
        if(tumor[i][j] < 255):
            tumor[i][j] = 0
        else:
            tumor[i][j] = 255

boundary = cv2.morphologyEx(tumor, cv2.MORPH_GRADIENT, kernel)
boundary = np.array(boundary, dtype=np.uint8)
s = Image.fromarray(boundary)
s.save('boundary.jpg')

newImg = img.copy()
color_img = cv2.cvtColor(newImg, cv2.COLOR_GRAY2RGB)
for i in range(row):
    for j in range(col):
        if(boundary[i][j] == 255):
            color_img[i][j][0] = 0
            color_img[i][j][0] = 0
            color_img[i][j][0] = 255


final = np.array(color_img, dtype=np.uint8)
s = Image.fromarray(final)
s.save('final.jpg')


