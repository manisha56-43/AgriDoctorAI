import cv2

image = cv2.imread("images/test.jpg")

height, width, channels = image.shape

print("Height:", height)
print("Width:", width)
print("Channels:", channels)

print("Image loaded successfully")