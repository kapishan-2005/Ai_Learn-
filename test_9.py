import cv2, os
haar_file = 'haarcascade_frontalface_default.xml'
dataset = 'dataset'
sub_data = 'Trumb'
path = os.path.join(dataset, sub_data)
if not os.path.isdir(path):
    os.makedirs(path)
(width, height) = (130, 100)

face_cascade = cv2.CascadeClassifier(haar_file)

webcam = cv2.VideoCapture(0)
count = 1
while count<51 :
    