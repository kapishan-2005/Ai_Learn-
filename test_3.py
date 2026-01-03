import cv2
img =cv2.imread("image/googlemap.png")
gaussianImg = cv2.GaussianBlur(img, (41, 41), 50)
gaussionImg2 = cv2.GaussianBlur(img, (21, 21), 0)
cv2.imshow('Original Image', img)
cv2.imshow('Gaussian Blurred Image', gaussianImg)
cv2.imshow('Gaussian Blurred Image 2', gaussionImg2)
waitkey = cv2.waitKey(0)
cv2.destroyAllWindows()

