## Create 2D image using OpenGL/OpenCV for different objects

import cv2 as cv
import numpy as np

image = np.zeros((500, 500, 3), np.uint8)

cv.rectangle(image, (50, 50), (450, 450), (0, 255, 0), 2)

cv.line(image, (50, 50), (450, 450), (255, 255, 0), 2)

cv.circle(image, (250, 250), 150, (0, 255, 255), 2)

cv.ellipse(image, (250, 250), (100, 50), 45, 0, 360, (255, 255, 0), 2)

cv.imshow("Shapes", image)
cv.waitKey(0)
cv.destroyAllWindows()
