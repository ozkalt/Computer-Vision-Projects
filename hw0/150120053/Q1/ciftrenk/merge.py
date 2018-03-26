import cv2

img = cv2.imread("Icolor.jpg")

#OpenCV kutuphanesi image'i Blue-Green-Red (BGR) olarak okudugu icin renkler BGR duzeninde degistirilmistir.

#b:blue, g:green, r:red
b,g,r = cv2.split(img)

#blue-green-blue
bgb = cv2.merge((b,g,b))
cv2.imwrite("bgb.jpg",bgb)

#blue-green-green
bgg = cv2.merge((b,g,g))
cv2.imwrite("bgg.jpg",bgg)

#green-green-red
ggr = cv2.merge((g,g,r))
cv2.imwrite("ggr.jpg",ggr)

#red-green-red
rgr = cv2.merge((r,g,r))
cv2.imwrite("rgr.jpg",rgr)

#blue-red-red
brr = cv2.merge((b,r,r))
cv2.imwrite("brr.jpg",brr)

#blue-blue-red
bbr = cv2.merge((b,b,r))
cv2.imwrite("bbr.jpg",bbr)