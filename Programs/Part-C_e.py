import cv2

# Load an image
image = cv2.imread('D:\\Normie\\Final AI Practicals (2023-24)\\Programs\\Unclassified Trials\\Image.jpg')

# Define the new width and height
new_width = 100
new_height = 100

# Resize the image
resized_image = cv2.resize(image, (new_width, new_height))

# Save the resized image
cv2.imwrite('D:\\Normie\\Final AI Practicals (2023-24)\\Programs\\Unclassified Trials\\Resized_Image.jpg', resized_image)