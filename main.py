# import libraries
import cv2

# Load trained cascade classifier
eye_detect = cv2.CascadeClassifier('haarcascade_eye.xml')

# start camera / read video
cam = cv2.VideoCapture('Face.mp4')