import os
import cv2
import numpy as np
from math import ceil
from matplotlib import pyplot as plt


workspace_dir = os.getcwd()
image_dir = workspace_dir + '/001/L'
os.chdir(image_dir)
files = [string for string in os.listdir(image_dir) if string.endswith('.jpg')]
files.sort()
num_files = len(files)
morphKernel = np.ones((7, 7), np.uint8)

images = list()
pupils = list()
irises = list()
for item in files:
	images.append(cv2.imread(item, cv2.IMREAD_GRAYSCALE))

for img in images:
	target = cv2.cvtColor(img.copy(), cv2.COLOR_GRAY2BGR)
	temp = target.copy()
	target2 = target.copy()
	ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
	morph = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, morphKernel)
	_, contours, hierarchy = cv2.findContours(morph.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(temp, contours, -1, (0, 0, 255), 3)
	(x, y), radius = cv2.minEnclosingCircle(contours[0])
	centre = (int(x), int(y))
	radius = int(radius)
	cv2.circle(target, centre, radius, (255, 0, 0), 2)
	pupils.append(target)

	temp = cv2.medianBlur(img.copy(), 5)
	temp = cv2.equalizeHist(temp)
	circles = cv2.HoughCircles(temp, cv2.HOUGH_GRADIENT, 1, 20, param1=160, param2=30, minRadius=radius, maxRadius=2*radius)
	circles = np.uint16(np.around(circles))

	for i in circles[0, :]:
		cv2.circle(target2, (i[0], i[1]), i[2], (0, 255, 0), 2)
	irises.append(target2)

plt.figure('Original')
for i, img in enumerate(images):
	plt.subplot(int(ceil(num_files/2)), 2, i), plt.imshow(img, cmap='gray')
	plt.xticks([]), plt.yticks([])

plt.figure('Pupil')
for i, pupil in enumerate(pupils):
	plt.subplot(int(ceil(num_files/2)), 2, i), plt.imshow(pupil, cmap='gray')
	plt.xticks([]), plt.yticks([])

plt.figure('Iris')
for i, iris in enumerate(irises):
	plt.subplot(int(ceil(num_files/2)), 2, i), plt.imshow(iris, cmap='gray')
	plt.xticks([]), plt.yticks([])

plt.show()
