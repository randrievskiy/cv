import cv2
from djitellopy import tello
import HUD

tello = tello.Tello()
tello.connect()

w, h = 400, 280

tello.streamon()

# Define the codec and create VideoWriter object
# 'XVID' is a codec for the .avi file format, you can change it to others like 'MJPG'
# fourcc = cv2.VideoWriter.fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi', fourcc, 30.0, (960, 720))

while True:
    frame = tello.get_frame_read().frame
    # frame = cv2.resize(frame, (w, h))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Write the frame to the video file
    # out.write(frame)

    battery_level = tello.get_battery()
    height, width, channels = frame.shape

    HUD.draw_battery_info(frame, battery_level, width)

    cv2.imshow('Video', frame)
    cv2.waitKey(1)