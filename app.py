import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8,maxHands=1)

def slope(x1, y1, x2, y2):
    m = 0
    b = (x2 - x1)
    d = (y2 - y1)
    if b != 0:
        m = (d)/(b) 

    return m



while True:
    success, img = cap.read()
    hands,img = detector.findHands(img)
    
    if hands:
        fingers =detector.fingersUp(hands[0])
        hand1 = hands[0]
        lmList = hand1["lmList"]
        # print(fingers)
        # print(lmList)
        # length, info, img = detector.findDistance(lmList[8], lmList[12], img)
        # length, info, img = detector.findDistance(lmList[8], lmList[5], img)
        length, info, img = detector.findDistance(lmList[12], lmList[9], img)
        n1 = slope(lmList[8][0], lmList[8][1], lmList[5][0], lmList[5][1])
        n2 = slope(lmList[12][0], lmList[12][1], lmList[9][0], lmList[9][1])
        # print("n1",n1)
        # print("n2",n2)

        if (0.95>n1>0.65) and (0.75>n2>0.45):
            pyautogui.keyDown("ctrl")
            pyautogui.press("right")    
            pyautogui.keyUp("ctrl")
        elif (-0.15>n1>-0.35) and (-0.05>n2>-0.35):
            pyautogui.keyDown("ctrl")
            pyautogui.press("left")
            pyautogui.keyUp("ctrl")


    cv2.imshow("img", img)
    cv2.waitKey(1)
