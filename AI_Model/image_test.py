import cv2

image = cv2.imread("images/test.jpg")

# Get original dimensions
height, width = image.shape[:2]

# Set maximum display size
max_width = 800
max_height = 600

# Calculate scaling factor
scale = min(max_width / width, max_height / height)

# Resize while maintaining aspect ratio
new_width = int(width * scale)
new_height = int(height * scale)

resized_image = cv2.resize(image, (new_width, new_height))

cv2.imshow("My First Image", resized_image)

cv2.waitKey(0)

cv2.destroyAllWindows()