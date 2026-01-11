import cv2

alg = "haarcascade_frontalface_default.xml"
haar = cv2.CascadeClassifier(alg)

# Verify cascade
if haar.empty():
    print("Error: Haar cascade file not loaded")
    exit()

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Error: Camera not accessible")
    exit()

while True:
    ret, img = cam.read()
    if not ret:
        print("Failed to grab frame")
        break

    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = haar.detectMultiScale(grayImg, 1.3, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)

    cv2.imshow("FaceDetection", img)

    if cv2.waitKey(10) & 0xFF == 27:
        break

cam.release()
cv2.destroyAllWindows()
