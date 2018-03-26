from matplotlib import pyplot as plt
import cv2

img = cv2.imread('anka.jpg')

rows,cols,ch = img.shape
M = cv2.getRotationMatrix2D((cols/2, rows/2),330,1)
dst1 = cv2.warpAffine(img,M,(cols,rows))
cv2.imwrite('cenrotanka.jpg',dst1)

M = cv2.getRotationMatrix2D((0, 0),330,1)
dst2 = cv2.warpAffine(img,M,(cols,rows))
cv2.imwrite('toprotanka.jpg',dst2)

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
dst1 = cv2.cvtColor(dst1,cv2.COLOR_BGR2RGB)
dst2 = cv2.cvtColor(dst2,cv2.COLOR_BGR2RGB)

titles = ['ORIGINAL','CENTER','TOP LEFT']
images = [img, dst1, dst2]

for i in range(3): 
    plt.subplot(1,3,i+1),plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
