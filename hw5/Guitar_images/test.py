from PIL import Image
import numpy as np
import os
import cv2
from pylab import *

def pca(X):
	row, col = X.shape
	mean_X = X.mean(axis=0)
	X = X - mean_X
	
	if col>row:
		M = np.dot(X, X.T)
		e, EV = np.linalg.eigh(M)
		tmp = np.dot(X.T, EV).T
		V = tmp[::-1]
		for i in range(V.shape[1]):
			V[:i] /= S
	else:
		U, S, V = np.linalg.svd(X)
		U = V[:row]

	return V, S, mean_X

allfiles=os.listdir(os.getcwd())
imlist=[filename for filename in allfiles if filename.endswith(".png")]
im = np.array(Image.open(imlist[0]))
m, n = im.shape[0:2]
imnbr = list(imlist)

immatrix = np.asarray([np.array(Image.open(im)).flatten() for im in imlist], 'f')

V, S, immean = pca(immatrix)

figure()
gray()
imshow(immean.reshape(m,n))	









