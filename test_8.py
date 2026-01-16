import cv2
import imutils
import numpy as np

# Replace these with the HSV range from your calibration
lower_hsv = np.array([0, 30, 60])
upper_hsv = np.array([20, 255, 255])

# Initialize camera
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("ERROR: Camera not accessible")
    exit()

while True:
    grabbed, frame = camera.read()
    if not grabbed:
        print("ERROR: Frame not captured")
        break

    # Resize for better visibility but not too small
    frame = imutils.resize(frame, width=640)
    
    # Blur lightly to remove noise
    blurred = cv2.GaussianBlur(frame, (5, 5), 0)
    
    # Convert to HSV
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    
    # Create mask for your object color
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    
    # Find contours
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None
    
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        if M["m00"] > 0:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        
        if radius > 10:
            # Draw circle and center
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
            print("Center:", center, "Radius:", radius)
            
            # Directions based on horizontal position
            frame_width = frame.shape[1]
            if center[0] < frame_width // 3:
                print("left")
            elif center[0] > 2 * frame_width // 3:
                print("right")
            else:
                print("center")
            
            # Stop if object is too close
            if radius > 250:
                print("stop")
    
    # Show frames
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC to exit
        break

camera.release()
cv2.destroyAllWindows()
