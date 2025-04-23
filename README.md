# Driver Drowsiness Detection System

This project uses computer vision and facial landmarks to detect driver drowsiness in real time using a webcam. If drowsiness is detected based on eye aspect ratio (EAR), an alarm is triggered to alert the driver.

## 🧠 Features

- Real-time video stream analysis
- Eye aspect ratio (EAR) calculation for both eyes
- Automatic drowsiness detection and sound alert
- Face and eye landmarks using dlib
- Visual feedback with EAR display and eye contour overlays

## 📁 Folder Structure

Make sure to set up the paths to the following files correctly in the script:

Add your folder path/ ├── iphone_alarm.mp3 # Alarm sound file └── shape_predictor_68_face_landmarks.dat # Dlib facial landmark model

## 🛠️ Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone https://github.com/yourusername/driver-drowsiness-detection.git
   cd driver-drowsiness-detection
   ```

2. **Install dependencies:**
```bash
pip install opencv-python dlib scipy pygame numpy
```

3. Download Dlib's landmark predictor: Download shape_predictor_68_face_landmarks.dat
Extract the file and place it in your working directory.

4. **Replace path placeholders in the script:**

-```"Add your folder path/iphone_alarm.mp3"```
-```"Add your folder path/shape_predictor_68_face_landmarks.dat"```

## 🚀 Usage
*Run the script:*
```bash
python drowsiness_detection.py
```
Press Q to quit the application.

## 🔔 Notes
-Make sure your webcam is connected.
-Adjust the ```EAR_THRESHOLD``` and ```DROWSY_TIME``` values if needed based on testing.
-Alarm won't replay until the user opens their eyes.

## 🧑‍💻 Author
Tehmeen - GitHub

Feel free to fork or contribute to this project!

Let me know if you'd like a GitHub-style project structure or logo too!