import cv2

# Read an image from file
image = cv2.imread('D:\\Normie\\Final AI Practicals (2023-24)\\Programs\\Unclassified Trials\\Image.jpg')

# Define the coordinates of the region of interest
start_point = (500, 500)
end_point = (1500, 1500)

# Crop the original image to obtain the region of interest
cropped_image = image[start_point[1]:end_point[1], start_point[0]:end_point[0]]

# Save the cropped image to a file
cv2.imwrite('D:\\Normie\\Final AI Practicals (2023-24)\\Programs\\Unclassified Trials\\Cropped_Image.jpg', cropped_image)