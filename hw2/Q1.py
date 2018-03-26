import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image


imgN1 = cv2.imread('cameramanN1.jpg')
imgN1_gray = cv2.cvtColor(imgN1, cv2.COLOR_BGR2GRAY)

imgN2 = cv2.imread('cameramanN2.jpg')
imgN2_gray = cv2.cvtColor(imgN2, cv2.COLOR_BGR2GRAY)

imgN3 = cv2.imread('cameramanN3.jpg')
imgN3_gray = cv2.cvtColor(imgN3, cv2.COLOR_BGR2GRAY)


rowN1, colN1 = imgN1_gray.shape
imgN1_arr = np.array(imgN1_gray)

rowN2, colN2 = imgN2_gray.shape
imgN2_arr = np.array(imgN2_gray)

rowN3, colN3 = imgN3_gray.shape
imgN3_arr = np.array(imgN3_gray)

def riseRowCol(img_arr, row, col):
    array = [[0 for y in range(col+2)] for z in range(row+2)]
    for i in range(row):
        for j in range(col):
            array[i+1][j+1] = img_arr[i][j]

    return array


def mean(A, B, row, col):
    arr = [[0 for y in range(col)] for z in range(row)]
    total = 0;
    for i in range(1,row+1):
        for j in range(1,col+1):
            total = A[i-1][j-1] * B[0][0]
            total += A[i-1][j] * B[0][1]
            total += A[i-1][j+1] * B[0][2]
            total += A[i][j-1] * B[1][0]
            total += A[i][j] * B[1][1]
            total += A[i][j+1] * B[1][2]
            total += A[i+1][j-1] * B[2][0]
            total += A[i+1][j] * B[2][1]
            total += A[i+1][j+1] * B[2][2]
            arr[i-1][j-1] = total
    return arr

def median(A, row, col):
    arr = [[0 for y in range(col)] for z in range(row)]
    kernel = [[0 for y in range(3)] for z in range(3)]
    for i in range(1,row+1):
        for j in range(1,col+1):
            kernel[0][0] = A[i-1][j-1]
            kernel[0][1] = A[i-1][j]
            kernel[0][2] = A[i-1][j+1]
            kernel[1][0] = A[i][j-1]
            kernel[1][1] = A[i][j]
            kernel[1][2] = A[i][j+1]
            kernel[2][0] = A[i+1][j-1]
            kernel[2][1] = A[i+1][j]
            kernel[2][2] = A[i+1][j+1]
            arr[i-1][j-1] = np.median(kernel)
    return arr

def MeanMedian(A, B, row, col, alfa):
    arr = [[0 for y in range(col)] for z in range(row)]
    for i in range(row):
        for j in range(col):
            arr[i][j] = (alfa * A[i][j]) + ((1 - alfa) * B[i][j])
    return arr

kernel = [[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]]

tN1 = riseRowCol(imgN1_arr, rowN1, colN1)
tN2 = riseRowCol(imgN2_arr, rowN2, colN2)
tN3 = riseRowCol(imgN3_arr, rowN3, colN3)


ftN1 = mean(tN1, kernel, rowN1, colN1)
ftN1 = np.array(ftN1, dtype=np.uint8)
tfN1 = Image.fromarray(ftN1, "L")
tfN1.save('meanN1.png')

ftN2 = mean(tN2, kernel, rowN2, colN2)
ftN2 = np.array(ftN2, dtype=np.uint8)
tfN2 = Image.fromarray(ftN2, "L")
tfN2.save('meanN2.png')

ftN3 = mean(tN3, kernel, rowN3, colN3)
ftN3 = np.array(ftN3, dtype=np.uint8)
tfN3 = Image.fromarray(ftN3, "L")
tfN3.save('meanN3.png')


iN1 = median(tN1, rowN1, colN1)
iN1 = np.array(iN1, dtype=np.uint8)
uN1 = Image.fromarray(iN1, "L")
uN1.save('medianN1.png')

iN2 = median(tN2, rowN2, colN2)
iN2 = np.array(iN2, dtype=np.uint8)
uN2 = Image.fromarray(iN2, "L")
uN2.save('medianN2.png')

iN3 = median(tN3, rowN3, colN3)
iN3 = np.array(iN3, dtype=np.uint8)
uN3 = Image.fromarray(iN3, "L")
uN3.save('medianN3.png')



alfa = 0.8

mmN1 = MeanMedian(ftN1, iN1, rowN1, colN1, alfa)
mmN1 = np.array(mmN1, dtype=np.uint8)
mmN1 = Image.fromarray(mmN1, "L")
mmN1.save('MeanMedianN1.png')

mmN2 = MeanMedian(ftN2, iN2, rowN2, colN2, alfa)
mmN2 = np.array(mmN2, dtype=np.uint8)
mmN2 = Image.fromarray(mmN2, "L")
mmN2.save('MeanMedianN2.png')

mmN3 = MeanMedian(ftN3, iN3, rowN3, colN3, alfa)
mmN3 = np.array(mmN3, dtype=np.uint8)
mmN3 = Image.fromarray(mmN3, "L")
mmN3.save('MeanMedianN3.png')




