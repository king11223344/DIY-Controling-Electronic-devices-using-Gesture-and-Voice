import cv2
import time
import os
import mediapipe as mp
import asyncio
import pyfirmata2
import speech_recognition as sr
import pyttsx3
import asyncio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 200)



def speak(audio):
    engine.say(audio)
    # print(audio)
    engine.runAndWait()
mpHands=mp.solutions.hands
mpDraw = mp.solutions.drawing_utils
# PORT =  pyfirmata2.Arduino.AUTODETECT
# board = pyfirmata2.Arduino(PORT)
# board = pyfirmata2.Arduino('COM5')
wCam, hCam = 640, 480
def findHands(img):
    # print(results.multi_hand_landmarks)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    global results
    results = mpHands.Hands(False, 1,0,0.5,0.5).process(imgRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            if True:
                mpDraw.draw_landmarks(img, handLms,mpHands.HAND_CONNECTIONS)
    return img
def findPosition( img, handNo=0, draw=True):
    lmList = []
    if results.multi_hand_landmarks:
        myHand = results.multi_hand_landmarks[handNo]
        for id, lm in enumerate(myHand.landmark):
            # print(id, lm)
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            # print(id, cx, cy)
            lmList.append([id, cx, cy])
            if draw:
                cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

    return lmList
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
 
folderPath = "FingerImages"
myList = os.listdir(folderPath)
print(myList)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    # print(f'{folderPath}/{imPath}')
    overlayList.append(image)
print(len(overlayList))
pTime=0;
tipId=[4,8,12,16,20]
middlefinger=False
firstfinger=False
thirdfinger=False

while True:
    try:
        sucess,img=cap.read()
        img=findHands(img)
        lmList=findPosition(img,draw=False)
        # print(lmList)
        if len(lmList)!=0:
            fingers=[]
            if lmList[17][1]>lmList[4][1]:
                if lmList[tipId[0]][1]<lmList[tipId[0]-1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            else :
                if lmList[tipId[0]][1]>lmList[tipId[0]-1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
                

            for id in range(1,5):
                if lmList[tipId[id]][2]<lmList[tipId[id]-2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            # print(fingers)
            totalFingers=fingers.count(1)
            
        
            if(fingers==[0,1,0,0,0]):
                # board.digital[13].write(False)
                
                h,w,c=overlayList[0].shape
                img[0:h,0:w]=overlayList[0]
                cv2.rectangle(img, (20, 225), (170, 425), (255, 255, 255), cv2.FILLED)
                cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                            10, (0,0,0), 25)
            elif(fingers==[0,0,1,0,0]):
                # board.digital[10].write(False)
                
                h,w,c=overlayList[5].shape
                img[0:h,0:w]=overlayList[5]
                cv2.rectangle(img, (20, 225), (170, 425), (255, 255, 255), cv2.FILLED)
                cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                            10, (0,0,0), 25)
                    
            elif(fingers==[0,1,1,0,0]):
                # board.digital[13].write(True)
                h,w,c=overlayList[1].shape
                img[0:h,0:w]=overlayList[1]
                cv2.rectangle(img, (20, 225), (170, 425), (255, 255, 255), cv2.FILLED)
                cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                            10, (0,0,0), 25)   
            elif(fingers==[0,1,1,1,0]):
                # board.digital[12].write(False)
                
                h,w,c=overlayList[2].shape
                img[0:h,0:w]=overlayList[2]
                cv2.rectangle(img, (20, 225), (170, 425), (255, 255, 255), cv2.FILLED)
                cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                            10, (0,0,0), 25)   
            elif(fingers==[0,1,1,1,1]):
                # board.digital[12].write(True)
                h,w,c=overlayList[3].shape
                img[0:h,0:w]=overlayList[3]
                cv2.rectangle(img, (20, 225), (170, 425), (255, 255, 255), cv2.FILLED)
                cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                            10, (0,0,0), 25)  
            elif(fingers==[1,1,1,1,1]):
                # board.digital[10].write(True)
                h,w,c=overlayList[4].shape
                img[0:h,0:w]=overlayList[4]
                cv2.rectangle(img, (20, 225), (170, 425), (255, 255, 255), cv2.FILLED)
                cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                            10, (0,0,0), 25)  
            elif(fingers==[0,1,0,0,1]):
                # board.digital[9].write(False)
                h,w,c=overlayList[8].shape
                img[0:h,0:w]=overlayList[8]
                cv2.rectangle(img, (20, 225), (170, 425), (255, 255, 255), cv2.FILLED)
                cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                            10, (0,0,0), 25)
            elif(fingers==[0,0,1,1,1]):
                # board.digital[9].write(True)
                h,w,c=overlayList[7].shape
                img[0:h,0:w]=overlayList[7]
                cv2.rectangle(img, (20, 225), (170, 425), (255, 255, 255), cv2.FILLED)
                cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                            10, (0,0,0), 25)
            elif(fingers==[1,1,0,0,1]):
                h,w,c=overlayList[6].shape
                img[0:h,0:w]=overlayList[6]
                cv2.rectangle(img, (20, 225), (170, 425), (255, 255, 255), cv2.FILLED)
                cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                            10, (0,0,0), 25) 
                break                   
        ctime=time.time()
        fps=1/(ctime-pTime)
        pTime=ctime
        cv2.putText(img,f'FPS:{int(fps)}',(400,70),cv2.FONT_HERSHEY_PLAIN,3,(255, 0, 0),3)
        cv2.imshow("Image",img)
        cv2.waitKey(1)
    except:
        print("Something went wrong")


