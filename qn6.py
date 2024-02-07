import cv2
import numpy as np

# Read the input color image
image_bgr = cv2.imread("image.png")

# Check if the image is loaded successfully
if image_bgr is None:
    print("Error: Could not load the image.")
else:
    # Convert BGR to Grayscale
    image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)


    # Define a scale factor for resizing
    scale_factor = 0.5

    # Resize images for better visibility
    resized_original = cv2.resize(image_bgr, None, fx=scale_factor, fy=scale_factor)
    resized_gray = cv2.resize(image_gray, None, fx=scale_factor, fy=scale_factor)

    # Display the original, grayscale, and HSV images
    cv2.imshow("Original Image", image_bgr)
    cv2.imshow("Resized Image", resized_original)
    cv2.imshow("Grayscale Image", resized_gray)


    cv2.waitKey(0)
    cv2.destroyAllWindows()