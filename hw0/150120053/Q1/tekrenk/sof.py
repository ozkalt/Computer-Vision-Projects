import cv2
import numpy as np
from matplotlib import pyplot as plt

#OPENCV FOTOGRAFLARI RGB OLARAK DEGIL DE BGR (blue-green-red) OLARAK OKUDUGU ICIN RENKLENDIRMEDE FARKLILIK OLUYOR.
#0:0:255 -> RED
#0:255:0 -> GREEN
#255:0:0 -> BLUE

img = cv2.imread('Icolor.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

red=[[[0,0,255%j] for j in i] for i in img_gray]
dt = np.dtype('f8')
red = np.array(red, dtype=dt)

green=[[[0,255%j,0] for j in i] for i in img_gray]
dt = np.dtype('f8')
green = np.array(green, dtype=dt)

blue=[[[255%j,0,0] for j in i] for i in img_gray]
dt = np.dtype('f8')
blue = np.array(blue, dtype=dt)

titles = ['RED','GREEN','BLUE']
images = [red, green, blue]

#RESMI PLOT EDERKEN RGB CINSINDEN YAZDIRIYOR. ANCAK OPENCV KUTUPHANESI KULLANILDIGINDA BGR CINSINDEN YAZIYOR.

for i in range(3): 
    plt.subplot(1,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

cv2.imwrite('00255.jpg',red)
cv2.imwrite('02550.jpg',green)
cv2.imwrite('25500.jpg',blue)