import cv2
import os

def capture_images(label):
    cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
    haar_eye = cv2.CascadeClassifier('haar cascade files/haarcascade_eye.xml')
    count = 0
    save_dir = f"dataset/{label}"
    os.makedirs(save_dir, exist_ok = True)

    while True:
        ret, frame = cap.read()

        if not ret or frame is None: 
            print("Failed to read frame from webcam")
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        eyes = haar_eye.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in eyes:
            eye = frame[y : y + h, x : x + w]
            eye = cv2.resize(eye, (24, 24))
            eye = cv2.cvtColor(eye, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(f"{save_dir}/{count}.jpg", eye)
            count += 1

        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q') or count > 1000:
            cap.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_images('Closed')