import cv2
import imutils #importing imutils for image resizing 
image = cv2.imread("image/googlemap.png")
resized = imutils.resize(image, width=300) #resize image to width of 300 pixels
cv2.imshow('Resized Image', resized)
cv2.imwrite("resized_photo.jpg", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()