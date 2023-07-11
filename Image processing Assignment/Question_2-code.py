import cv2
import numpy as np

# Load image
img = cv2.imread('image.jpg')

# Add noise
noise = np.random.normal(loc=0, scale=25, size=img.shape)
noisy_img = np.clip(img + noise, 0, 255).astype(np.uint8)

# Implement non-local means algorithm
denoised_img = cv2.fastNlMeansDenoisingColored(noisy_img, None, 10, 10, 7, 21)

# Display images
cv2.imshow('Original', img)
cv2.imshow('Noisy', noisy_img)
cv2.imshow('Denoised', denoised_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

