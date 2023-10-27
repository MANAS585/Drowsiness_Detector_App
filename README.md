# Drowsiness_Detector_App
1. Problem Statement:
Drowsy driving is a major cause of road accidents, and it's crucial to develop a system that can monitor a driver's alertness in real-time and issue warnings when signs of drowsiness are detected.
2. Components:
Camera: The project typically uses a camera (such as a webcam) to capture the driver's face in real-time.
OpenCV: OpenCV (Open Source Computer Vision Library) is used for image and video processing, enabling tasks like face detection and facial landmark detection.
3. Face Detection:
OpenCV is used for face detection to locate and track the driver's face within the camera feed.
4. Drowsiness Detection:
Sum of horizontal and vertical Euclidean distance is calculated,then EAR(Eye Aspect Ratio) is calculated.If EAR is less then threshould value then we alert the driver.
6. Alerting Mechanism:
When drowsiness is detected, an alert is issued to the driver to wake them up or prompt them to take a break. Alerts can also be in the form of visual warnings, or haptic feedback (vibrations in the steering wheel or seat).In this project we have used sound.
Benefits:
This project aims to improve road safety by reducing accidents caused by drowsy driving, potentially saving lives and reducing injuries.
The requirement for this Python project is a webcam through which we will capture images. You need to have Python (3.6 version recommended) installed on your system, then using pip, you can install the necessary packages.
1. OpenCV – pip install opencv-python (Face and eye detection).
2. Imutils – pip install imutils (To get landmarks of eye).
3. Scipy – pip install scipy (To calculate distance between eye landmarks).
4. Pygame – pip install pygame (To play alarm sound).
5. Dlib - pip install dlib
