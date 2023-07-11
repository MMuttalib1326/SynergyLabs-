import numpy as np
import cv2

# Load an example image
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Add some noise to the image
noise = np.random.normal(0, 25, img.shape)
noisy_img = img + noise

# Define the Point Spread Function (PSF)
psf_size = 15
psf_sigma = 5
psf = cv2.getGaussianKernel(psf_size, psf_sigma)
psf = psf @ psf.T

# Compute the Power Spectral Density (PSD)
img_fft = np.fft.fft2(img)
noise_fft = np.fft.fft2(noise)
img_psd = np.abs(img_fft) ** 2 / np.prod(img.shape)
noise_psd = np.abs(noise_fft) ** 2 / np.prod(noise.shape)

# Compute the Wiener filter
wiener_filter = np.conj(img_fft) * img_psd / (img_psd + noise_psd)

# Apply the Wiener filter to the noisy image
noisy_img_fft = np.fft.fft2(noisy_img)
restored_img_fft = noisy_img_fft * wiener_filter
restored_img = np.real(np.fft.ifft2(restored_img_fft))

# Show the original image, the noisy image, and the restored image
cv2.imshow('Original image', img)
cv2.imshow('Noisy image', noisy_img.astype(np.uint8))
cv2.imshow('Restored image', restored_img.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
