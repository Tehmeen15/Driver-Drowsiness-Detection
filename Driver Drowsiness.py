import cv2
import dlib
import numpy as np
from scipy.spatial import distance
import time
import pygame

# Initialize pygame mixer for sound alert
pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\tehme\Downloads\Ai Virtual projects\driver drowsiness\iphone_alarm.mp3")  # Ensure you have an alarm sound file

def play_alarm():
    pygame.mixer.music.play()

def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Load the face detector and facial landmarks predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(r"C:\Users\tehme\Downloads\Ai Virtual projects\driver drowsiness\shape_predictor_68_face_landmarks.dat")

(lStart, lEnd) = (42, 48)  # Left eye landmarks
(rStart, rEnd) = (36, 42)  # Right eye landmarks

EAR_THRESHOLD = 0.25  # Eye aspect ratio threshold
DROWSY_TIME = 1.5  # Time in seconds before triggering alarm

def draw_eye_contours(frame, eye):
    for (x, y) in eye:
        cv2.circle(frame, (x, y), 2, (0, 255, 255), -1)
    cv2.polylines(frame, [eye], True, (0, 255, 0), 1)

cap = cv2.VideoCapture(0)
drowsy_start_time = None

drowsy_alert_triggered = False

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    
    for face in faces:
        shape = predictor(gray, face)
        shape = np.array([(shape.part(i).x, shape.part(i).y) for i in range(68)])
        
        left_eye = shape[lStart:lEnd]
        right_eye = shape[rStart:rEnd]
        
        left_EAR = eye_aspect_ratio(left_eye)
        right_EAR = eye_aspect_ratio(right_eye)
        
        avg_EAR = (left_EAR + right_EAR) / 2.0
        
        # Draw eyes with better visualization
        draw_eye_contours(frame, left_eye)
        draw_eye_contours(frame, right_eye)
        
        if avg_EAR < EAR_THRESHOLD:
            if drowsy_start_time is None:
                drowsy_start_time = time.time()
            elif time.time() - drowsy_start_time >= DROWSY_TIME and not drowsy_alert_triggered:
                play_alarm()
                drowsy_alert_triggered = True
        else:
            drowsy_start_time = None
            drowsy_alert_triggered = False
        
        cv2.putText(frame, f"EAR: {avg_EAR:.2f}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    
    cv2.imshow("Driver Drowsiness Detection", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
