import os
import cv2
import numpy as np

cap = cv2.VideoCapture('example.mp4')

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Saves image of the current frame in jpg file
    name = './data/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1000

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

# from ultralytics import YOLO

# model = YOLO('yolov8n.pt')
# results = model.predict(source='dog.jpg', conf=0.25)
