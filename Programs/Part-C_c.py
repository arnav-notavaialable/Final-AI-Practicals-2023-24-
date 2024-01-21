import cv2

# Read an image from file
image = cv2.imread('D:\\Normie\\Final AI Practicals (2023-24)\\Programs\\Unclassified Trials\\Image.jpg')


# Display the gray scale image
dimensions = image.shape

height = image.shape[0]
width = image.shape[1]
channels = image.shape[2]
 
print('Image Dimension    : ',dimensions)
print('Image Height       : ',height)
print('Image Width        : ',width)
print('Number of Channels : ',channels)