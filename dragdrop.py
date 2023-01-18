import cv2
import handtrack as ht

cap = cv2.VideoCapture(0)
cap.set(3, 1288)
cap.set(4, 720)
detector = ht.handDetector(detectionCon=0.8)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    cv2.imshow("Image", img)
    cv2.waitKey(1)

