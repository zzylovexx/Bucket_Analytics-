import  numpy as np
import easyocr
import  cv2
import time
from datetime import datetime
import matplotlib.pyplot as plt
print(cv2.__version__)
cap = cv2.VideoCapture('demo2.mp4')  
reader = easyocr.Reader(['en','ch_tra'])
# fps = cap.get(5)
# print(fps)
# fps=1000/fps
# print(fps)
# if not cap.isOpened():
#     print("Cannot open camerqa")
#     exit() 
while (True):
    #time.sleep(0.03)
    ret,frame=cap.read()
    
    if not ret:
        print('cannot receive frame')
        break
    cv2.imshow('studio',frame)
    #print(frame.shape)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    
cap.release()
