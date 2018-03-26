import cv2
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
from scipy import ndimage
import os
import glob
import pickle

imlist = []
files = glob.glob ("*.png")
images = np.array([np.array(cv2.imread(fname, cv2.IMREAD_GRAYSCALE)) for fname in files])


def pca(img):
    row, col = img.shape
    toplam = 0

    for i in range(row):
        for j in range(col):
            if img[i][j] != 0:
                toplam++;

    T = np.zeros((2, toplam), dtype=float)
    index = 0
    for i in range(row):
        for j in range(col):
            if img[i][j] != 0:
                T[0][index] = i
                T[1][index] = j
                index++



    mean_T = np.mean(T)

    for i in range(2):
        for j in range(toplam):
            T[i][j] -= mean_T

    avg = toplam / pixel
    index = 0
    

    P, D, Q = np.linalg.svd(sub_arr, full_matrices=False)
    X_a = np.dot(np.dot(P, np.diag(D)), Q)


pca(images[0])
