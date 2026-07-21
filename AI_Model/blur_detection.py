import cv2

# Load image
image = cv2.imread("images/test.jpg")

if image is None:
    print("Image not found!")

else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Create a blurred version of the same image
    blurred = cv2.GaussianBlur(gray, (15, 15), 0)

    # Blur score of original image
    original_score = cv2.Laplacian(gray, cv2.CV_64F).var()

    # Blur score of blurred image
    blurred_score = cv2.Laplacian(blurred, cv2.CV_64F).var()

    print("Original Image Score:", original_score)
    print("Blurred Image Score:", blurred_score)