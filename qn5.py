import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)

kernel_size = 5
kernel = np.ones((kernel_size, kernel_size), np.uint8)

erosion = cv2.erode(image, kernel, iterations=1)

dilation = cv2.dilate(image, kernel, iterations=1)

cv2.imshow("Image",image)
cv2.imshow("Erosion", erosion)
cv2.imshow("Dilation", dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()