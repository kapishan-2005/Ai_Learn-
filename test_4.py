import cv2
img = cv2.imread("image/googlemap.png")
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
threshImg = cv2.threshold(grayImg, 100, 255, cv2.THRESH_BINARY)[1]
cv2.imshow('Original Image', img)
cv2.imshow("threshold.jpg", threshImg)
cv2.waitKey(0)
cv2.destroyAllWindows()