#implemented pySaliencyMap developed by  Akisato Kimura

import cv2
import pySaliencyMap
import matplotlib.pyplot as plt

img = cv2.imread('S1001L01.jpg', cv2.IMREAD_COLOR)

height, width, channels = img.shape

sm = pySaliencyMap.pySaliencyMap(width, height)

saliency_map = sm.SMGetSM(img)
binarized_map = sm.SMGetBinarizedSM(img)
salient_region = sm.SMGetSalientRegion(img)

plt.subplot(221)
plt.imshow(img)
plt.xticks([]), plt.yticks([])
plt.title('Input Image')

plt.subplot(222)
plt.imshow(saliency_map, 'gray')
plt.xticks([]), plt.yticks([])
plt.title('Saliency Map')

plt.subplot(223)
plt.imshow(binarized_map, 'gray')
plt.xticks([]), plt.yticks([])
plt.title('Binarized Saliency Map')

plt.subplot(224)
plt.imshow(salient_region)
plt.xticks([]), plt.yticks([])
plt.title('Salient Region')

plt.show()
