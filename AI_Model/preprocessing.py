import cv2
import numpy as np

# Load the image
image = cv2.imread("images/test.jpg")

# Check that the image loaded successfully
if image is None:
    print("Error: Image not found!")
else:
    print("Original Shape:", image.shape)

    # Resize for AI
    resized_image = cv2.resize(image, (224, 224))
    print("Resized Shape:", resized_image.shape)
        # Normalize pixel values
    normalized_image = resized_image / 255.0

    print("\nNormalization Complete!")
    print("Data Type:", normalized_image.dtype)
    print("Minimum Pixel Value:", normalized_image.min())
    print("Maximum Pixel Value:", normalized_image.max())
    # Convert BGR to RGB
rgb_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

print("\nColor space converted successfully!")
print("\nFirst Pixel (BGR):", resized_image[0, 0])
print("First Pixel (RGB):", rgb_image[0, 0])