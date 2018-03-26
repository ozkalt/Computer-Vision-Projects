import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("underexposed.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.title('underexposed image')
plt.show()

row, col, ch = img.shape
arr = np.array(img)

pixel = row*col

## CALCULATING MEAN VALUE ##
sum = [0 for x in range(ch)]

for i in range(row):
	for j in range(col):
		for k in range(ch):
			sum[k] += arr[i][j][k]

mean = [0 for x in range(ch)]
for i in range(ch):
	mean[i] = sum[i] / pixel

print('mean =', mean)

## CALCULATING STANDART DEVIATION VALUE ##
distance = [[[0 for x in range(ch)] for y in range(col)] for z in range(row)]
distsqr = [[[0 for x in range(ch)] for y in range(col)] for z in range(row)]

for i in range(row):
	for j in range(col):
		for k in range(ch):
			distance[i][j][k] = arr[i][j][k] - mean[k]
			distsqr[i][j][k] = distance[i][j][k] ** 2

sumsd = [0 for x in range(ch)]

for i in range(row):
	for j in range(col):
		for k in range(ch):
			sumsd[k] += distsqr[i][j][k]

sd = [0 for x in range(ch)]
for i in range(ch):
	sd[i] = sumsd[i] / pixel
	sd[i] = sd[i] ** 0.5

print('standart deviation =', sd)


