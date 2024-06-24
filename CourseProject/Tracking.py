import time
import numpy as np
import cv2
from djitellopy import tello

tello = tello.Tello()
tello.connect()
print(tello.get_battery())

#w, h = 360, 240

tello.streamon()

# Define the codec and create VideoWriter object
# 'XVID' is a codec for the .avi file format, you can change it to others like 'MJPG'
#fourcc = cv2.VideoWriter.fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi', fourcc, 30.0, (960, 720))

while True:
    frame = tello.get_frame_read().frame
    #frame = cv2.resize(frame, (w, h))

    # Write the frame to the video file
    #out.write(frame)

    cv2.imshow('Video', frame)
    cv2.waitKey(1)