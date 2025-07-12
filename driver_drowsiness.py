import cv2
import numpy as np
from tensorflow.keras.models import load_model
from pygame import mixer
import time
import os
from datetime import datetime
import pandas as pd
import csv

mixer.init()
sound = mixer.Sound('alarm.wav')  

face_cascade = cv2.CascadeClassifier('haar cascade files/haarcascade_frontalface_alt.xml')
left_eye_cascade = cv2.CascadeClassifier('haar cascade files/haarcascade_lefteye_2splits.xml')
right_eye_cascade = cv2.CascadeClassifier('haar cascade files/haarcascade_righteye_2splits.xml')


model = load_model('models/cnnCat2.h5')

cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION) 

score = 0
thresh = 15  

log_file = "session_log.csv"

if not os.path.exists(log_file):
    with open(log_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "event"])  

drowsy_event_active = False

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to read frame from webcam.")
        continue

    height, width = frame.shape[:2]
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    left_eye = left_eye_cascade.detectMultiScale(gray)
    right_eye = right_eye_cascade.detectMultiScale(gray)

    eyes_closed = 0

    for (x, y, w, h) in right_eye:
        eye_img = frame[y:y+h, x:x+w]
        eye_img = cv2.cvtColor(eye_img, cv2.COLOR_BGR2GRAY)
        eye_img = cv2.resize(eye_img, (24, 24)) / 255.0
        eye_img = eye_img.reshape(1, 24, 24, 1)

        pred = model.predict(eye_img)
        rpred = np.argmax(pred, axis=1)[0]

        if rpred == 0:
            eyes_closed += 1
        break  

    for (x, y, w, h) in left_eye:
        eye_img = frame[y:y+h, x:x+w]
        eye_img = cv2.cvtColor(eye_img, cv2.COLOR_BGR2GRAY)
        eye_img = cv2.resize(eye_img, (24, 24)) / 255.0
        eye_img = eye_img.reshape(1, 24, 24, 1)

        pred = model.predict(eye_img)
        lpred = np.argmax(pred, axis=1)[0]

        if lpred == 0:
            eyes_closed += 1
        break  

    if eyes_closed == 2:
        if score < thresh:
            score += 1  # score builds up until threshold
        cv2.putText(frame, "Closed", (10, height - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    else:
        if score > 0:
            score -= 1  # score decreases only when eyes are open
        cv2.putText(frame, "Open", (10, height - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.putText(frame, f"Score: {score}", (150, height - 20),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    if score == thresh:
        if not drowsy_event_active:
            drowsy_event_active = True
            with open(log_file, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Drowsiness Starts"])

        if sound.get_num_channels() == 0:
            sound.play()

        cv2.rectangle(frame, (0, 0), (width, height), (0, 0, 255), 4)
        cv2.putText(frame, "DROWSY!", (width // 2 - 100, height // 2),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

    else:
        if drowsy_event_active:
            drowsy_event_active = False
            with open(log_file, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Drowsiness Ends"])




    cv2.imshow("Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
