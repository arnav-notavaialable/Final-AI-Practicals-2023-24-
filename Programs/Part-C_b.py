import cv2

# Read an image from file
image = cv2.imread('D:\\Normie\\Final AI Practicals (2023-24)\\Programs\\Unclassified Trials\\Image.jpg')

# Convert the image to gray scale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

# Display the gray scale image
cv2.imshow('Gray Image', gray_image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('D:\\Normie\\Final AI Practicals (2023-24)\\Programs\\Unclassified Trials\\greyscale_Image.jpg', gray_image)
