import cv2
import numpy
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
print("Initializing Camera")
camera = PiCamera()
camera.resolution = (640, 480)
rawCapture = PiRGBArray(camera, size=(640,480))
cap = cv2.VideoCapture(0)
#print("Which colour do you want to display?")
#colour = int(input("1 = red \n2:blue\n3: green\n4:yellow\n5:orange \n6:colour mask"))

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    key = cv2.waitKey(1)
    frame = frame.array
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame,(480,320))
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # green
    low_green = np.array([50, 52, 50])
    high_green = np.array([85, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    kernel = np.ones((3, 3), np.uint8)
    green_mask = cv2.erode(green_mask, kernel)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    box = np.zeros(frame.shape[:2], dtype="uint8")
    cv2.circle(box, (320, 175), 10, 255, -1)
    frame2 = cv2.bitwise_and(hsv_frame, hsv_frame, mask = box)
    gm2 = cv2.inRange(frame2, low_green, high_green)
    green_det = cv2.medianBlur(gm2, 3)
    frame_gaussian = cv2.GaussianBlur(green_det, (5, 5), 2, 2)
    circles = cv2.HoughCircles(frame_gaussian, cv2.HOUGH_GRADIENT, 1, frame_gaussian.shape[0] / 8, param1=150, param2=20, minRadius=0, maxRadius=30)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        print("GREEN DETECTEDDD MKCCCCCCCCCCCCCCCCCCCCCCCCC")
        green_zone = True
    #     """cv2.circle(frame, center=(circles[0, 0], circles[0, 1]), radius=circles[0, 2], color=(0, 0, 0), thickness=2)
    #     cv2.putText(output_frame, 'Diameter : ' + str(2 * circles[0, 2]), (0, 20), cv2.FONT_HERSHEY_COMPLEX, 0.5,
    #                 (0, 0, 0))"""
    # contours, heirarchy = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # if len(contours) != 0:
    #     for contour in contours:
    #         if cv2.contourArea(contour) > 500:
    #             x, y, w, h = cv2.boundingRect(contour)
    #             cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
    cv2.imshow("Frame", frame)
    # cv2.imshow("green mask", green)
    # cv2.imshow("meow", box)
    cv2.imshow("meow2", gm2)

    if key == 27:
        break