import cv2

# Read an image from any folder
image = cv2.imread('D:\\Normie\\Final AI Practicals (2023-24)\\Programs\\Unclassified Trials\\Image.jpg')

# Save the image in the drive 
cv2.imwrite('D:\\saved_image.jpg', image)

#to save to a specific folder:
cv2.imwrite('D:\\Normie\\Final AI Practicals (2023-24)\\Programs\\Unclassified Trials\\saved_image.jpg', image)