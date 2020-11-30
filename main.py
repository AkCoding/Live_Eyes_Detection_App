# import libraries
import cv2

# Load trained cascade classifier
eye_detect = cv2.CascadeClassifier('haarcascade_eye.xml')

# start camera / read video
cam = cv2.VideoCapture('Face.mp4')

while True:

    # read frame/image from camera
    resp, frame = cam.read()

    # no frame then brak loop
    if resp == 0:
        break

    # Convert color image into grayscale
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces ROI
    # Syntax: Classifier.detectMultiScale(input image, Scale Factor , Min Neighbors)
    eyes = eye_detect.detectMultiScale(gray_img, 1.3, 7)

    # Draw rectangle around the faces
    for (x, y, w, h) in eyes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)



