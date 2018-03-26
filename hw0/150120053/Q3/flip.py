import numpy as np
import cv2

img = cv2.imread("Icolor.jpg")

width = img.shape[1]
height = img.shape[0]

halfw = int(width/2)
halfh = int(height/2)

crop_img1 = img[0:height, 0:halfw]
crop_img2 = img[0:height, halfw:width]

vis=np.concatenate((crop_img2, crop_img1), axis=1)
cv2.imwrite("croppedw.jpg", vis)

img2= cv2.imread("croppedw.jpg")

crop_img3 = img2[0:halfh, 0:width]
crop_img4 = img2[halfh:height, 0:width]

vis2=np.concatenate((crop_img4, crop_img3), axis=0)
cv2.imwrite("croppedh.jpg", vis2)

mimg=cv2.flip(img,1)
cv2.imwrite('mirror.jpg', mimg)