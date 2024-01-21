import cv2

# Loading an image using 'imread'
image = cv2.imread('D:\\Normie\\Final AI Practicals (2023-24)\\Programs\\Unclassified Trials\\Image.jpg')

# Checking if the image was loaded successfully
if image is not None:
   # Display the image using 'imshow'
   cv2.imshow('Image', image)

   # Wait for a key press and close the window
   cv2.waitKey(0)
   cv2.destroyAllWindows()
else:
   print("Image not found.")