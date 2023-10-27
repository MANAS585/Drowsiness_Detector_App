import cv2
import imutils
from imutils import face_utils
import dlib
from pygame import mixer
from scipy.spatial import distance
mixer.init()
mixer.music.load("music.wav")
def eye_aspect_ratio(eye):
	A = distance.euclidean(eye[1], eye[5])
	B = distance.euclidean(eye[2], eye[4])
	C = distance.euclidean(eye[0], eye[3])
	ear = (A+B)/(2*C)
	return ear
thresh=0.25
frame_check=20
detect=dlib.get_frontal_face_detector()
predict=dlib.shape_predictor("models\shape_predictor_68_face_landmarks.dat")
(lstart,lend)=face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
(rstart,rend)=face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]
cap = cv2.VideoCapture(0)
while True:
	ret, frame = cap.read()
	frame=imutils.resize(frame, width=450)
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	subjects=detect(gray,0)
	for subject in subjects:
		shape=predict(gray,subjects)
		shape=face_utils.shape_to_np(shape)
		lefteye=shape[lstart:lend]
		righteye = shape[rstart:rend]
		leftEAR=eye_aspect_ratio(lefteye)
		rightEAR = eye_aspect_ratio(lefteye)
		ear=(leftEAR+rightEAR)/2.0
		leftEyeHull=cv2.convexHull(lefteye)
		rightEyeHull = cv2.convexHull(righteye)
		cv2.drawContours(frame,[leftEyeHull],-1,(0,255,0),1)
		cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
cv2.destroyAllWindows()
cap.release()
	