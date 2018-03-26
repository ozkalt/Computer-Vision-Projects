import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

I = cv2.imread('StairsBuildingsN.png')
I = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)


row, col = I.shape
img_arr = np.array(I)

arr = [[0 for y in range(col+2)] for z in range(row+2)]
for i in range(row):
    for j in range(col):
        arr[i+1][j+1] = img_arr[i][j]

def convolution(A, kernel, row, col):
    arr = [[0 for y in range(col)] for z in range(row)]
    total = 0;
    for i in range(1,row+1):
        for j in range(1,col+1):
            total = A[i-1][j-1] * kernel[2][2]
            total += (A[i-1][j] * kernel[2][1])
            total += (A[i-1][j+1] * kernel[2][0])
            total += (A[i][j-1] * kernel[1][2])
            total += (A[i][j] * kernel[1][1])
            total += (A[i][j+1] * kernel[1][0])
            total += (A[i+1][j-1] * kernel[0][2])
            total += (A[i+1][j] * kernel[0][1])
            total += (A[i+1][j+1] * kernel[0][0])
            if total >= 255:
                arr[i-1][j-1] = 255
            elif total < 0:
                arr[i-1][j-1] = 0
            else:
                arr[i-1][j-1] = total

    return arr

#kernels#
N = [[-3,-3,-3],[-3,0,-3],[5,5,5]]
S = [[5,5,5],[-3,0,-3],[-3,-3,-3]]
E = [[5,-3,-3],[5,0,-3],[-5,-3,-3]]
W = [[-3,-3,5],[-3,0,5],[-3,-3,5]]
NW = [[-3,-3,-3],[-3,0,5],[-3,5,5]]
NE = [[-3,-3,-3],[5,0,-3],[5,5,-3]]
SW = [[-3,5,5],[-3,0,5],[-3,-3,-3]]
SE = [[5,5,-3],[5,0,-3],[-3,-3,-3]]

Nedge = convolution(arr, N, row, col)
Nedge = np.array(Nedge, dtype=np.uint8)
N = Image.fromarray(Nedge, "L")
N.save('N.png')

Sedge = convolution(arr, S, row, col)
Sedge = np.array(Sedge, dtype=np.uint8)
S = Image.fromarray(Sedge, "L")
S.save('S.png')

Eedge = convolution(arr, E, row, col)
Eedge = np.array(Eedge, dtype=np.uint8)
E = Image.fromarray(Eedge, "L")
E.save('E.png')

Wedge = convolution(arr, W, row, col)
Wedge = np.array(Wedge, dtype=np.uint8)
W = Image.fromarray(Wedge, "L")
W.save('W.png')

NEedge = convolution(arr, NE, row, col)
NEedge = np.array(NEedge, dtype=np.uint8)
NE = Image.fromarray(NEedge, "L")
NE.save('NE.png')

SWedge = convolution(arr, SW, row, col)
SWedge = np.array(SWedge, dtype=np.uint8)
SW = Image.fromarray(SWedge, "L")
SW.save('SW.png')

SEedge = convolution(arr, SE, row, col)
SEedge = np.array(SEedge, dtype=np.uint8)
SE = Image.fromarray(SEedge, "L")
SE.save('SE.png')

NWedge = convolution(arr, NW, row, col)
NWedge = np.array(NWedge, dtype=np.uint8)
NW = Image.fromarray(NWedge, "L")
NW.save('NW.png')

