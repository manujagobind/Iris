import cv2
import numpy as np


img = cv2.imread('001/L/S1001L01.jpg', 0)
height, width = img.shape

n= 4
h=height/n
w=width/n
images = dict()

for i in range(n):
    for j in range(n):
        h_lb = i*h
        h_ub = (i+1)*h-1
        w_lb = j*w
        w_ub = (j+1)*w-1
        images[str(i)+str(j)] = temp = img[h_lb:h_ub, w_lb:w_ub]

        _, cell = cv2.threshold(temp, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        if j==0:
            row = cell
        else:
            row = np.hstack((row, cell))
    if i==0:
        merge = row
    else:
        merge = np.vstack((merge, row))

cv2.imshow('Original', img)
cv2.imshow('Merge', merge)
cv2.waitKey(0)
cv2.destroyAllWindows()
