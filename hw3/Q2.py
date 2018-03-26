import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('cameraman1.jpg')
gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

img2 = cv2.imread('cameraman2.jpg')
gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(gray1,None)
kp2, des2 = sift.detectAndCompute(gray2,None)

bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good, None, flags=2)


img1=cv2.drawKeypoints(gray1,kp1, img1)
img2=cv2.drawKeypoints(gray2,kp2, img2)


plt.subplot(121),plt.imshow(img1), plt.title('cameraman1')
plt.subplot(122),plt.imshow(img2), plt.title('cameraman2')
plt.show()

plt.imshow(img3)
plt.title('matched points')
plt.show()

cv2.imwrite('sift_keypoints1.jpg',img1)
cv2.imwrite('sift_keypoints2.jpg',img2)
cv2.imwrite('matchedpoint.jpg', img3)


row, col = gray1.shape

pts1 = np.float32([[0,0],[100,50],[50,200]])
pts2 = np.float32([[0,0],[100,50],[130,200]])

M = cv2.getAffineTransform(pts1,pts2)
dst = cv2.warpAffine(gray1,M,(col+143,row))

plt.subplot(121),plt.imshow(gray1),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

