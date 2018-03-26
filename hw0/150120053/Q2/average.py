import cv2
import numpy as np

img = cv2.imread('Icolor.jpg')


togray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('Igray.jpg', togray)

avg_color_per_row = np.average(togray, axis=0)
avg_color = np.average(avg_color_per_row, axis=0)
print("avarage color: ", avg_color)


smallest = np.amin(img)
print ("image min: ", smallest)
smallest0 = np.amin(avg_color_per_row)
print ("avg_color_per_row min: ", smallest0)
smallest1 = np.amin(avg_color)
print ("avg_color min: ", smallest1)


biggest = np.amax(img)
print ("image max: ", biggest)
biggest0 = np.amax(avg_color_per_row)
print ("avg_color_per_row max: ", biggest0)
biggest1 = np.amax(avg_color)
print ("avg_color max: ", biggest1)