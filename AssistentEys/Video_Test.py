import mediapipe as mp
import cv2
from math import sqrt
from time import time
import pyautogui
from threading import Thread

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

fingers = [0]*21
points_x_0 = [0]*21
points = [[0, 0]]*21

command1_flag = False
command2_flag = False
commandMouse_flag1 = False
commandMouse_flag2 = False
last_time = time()
last_update = [0, 0]
with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.6, max_num_hands=1) as hands:
    while cap.isOpened():
        ret, frame = cap.read()

        # BGR 2 RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Flip on horizontal
        image = cv2.flip(image, 1)

        # Set flag
        image.flags.writeable = False

        # Detections
        results = hands.process(image)

        # Set flag to true
        image.flags.writeable = True

        # RGB 2 BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Detections
        #print(results.multi_hand_landmarks)

        # Rendering results
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                          mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),)
                for id, point in enumerate(hand.landmark):
                    width, height, color = image.shape
                    width, height = (point.x * height), (point.y * width)
                    points[id] = [width, height]

                    if id == 8:
                        cv2.circle(image, (int(width), int(height)), 7, (0, 0, 255), cv2.FILLED)
                    if id == 6:
                        cv2.circle(image, (int(width), int(height)), 7, (0, 255, 255), cv2.FILLED)
                    if id == 0:
                        points_x_0[id] = 0
                    else:
                        points_x_0[id] = abs(sqrt(int(points[0][0]-width)**2 + int(points[0][1]-height)**2))


        #print(abs(points_x_0[0] - points_x_0[6]), abs(points_x_0[0] - points_x_0[8]), command1_flag)
        if (points_x_0[6] > points_x_0[8]) and (command1_flag == False) and (time() - last_time > 0.050):
            command1_flag = True
            last_time = time()
            pyautogui.click(button="left")

        if (points_x_0[6] < points_x_0[8]) and (command1_flag == True) and (time() - last_time > 0.050):
            command1_flag = False
            last_time = time()

        if (points_x_0[10] > points_x_0[12]) and (command2_flag == False) and (time() - last_time > 0.050):
            command2_flag = True
            last_time = time()
            pyautogui.click(button="right")

        if (points_x_0[10] < points_x_0[12]) and (command2_flag == True) and (time() - last_time > 0.050):
            command2_flag = False
            last_time = time()


        if (points_x_0[5] > points_x_0[4]) and (commandMouse_flag1 == False) and (time() - last_time > 0.050):
            commandMouse_flag1 = True
            commandMouse_flag2 = False
            last_time = time()

        if (points_x_0[5] < points_x_0[4]) and (commandMouse_flag2 == False) and (time() - last_time > 0.050):
            commandMouse_flag1 = False
            last_time = time()
            def mmove():
                    pyautogui.moveTo((points[9][0]*9)-2900, (points[9][1]*4)-300)

            if (abs(points[9][0] - last_update[0]) >= 0.5) and (abs(points[9][1] - last_update[1]) >= 0.5):
                last_update = points[9]
                Thread(target=mmove, daemon=False).start()




        cv2.imshow('Hand Tracking', image)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()

