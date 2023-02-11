import cv2 
cap = cv2.VideoCapture(1,cv2.CAP_V4L2) # video capture source camera (Here webcam 
cap.set(3,640)
cap.set(4,480)
#print(width, height)

ret,frame = cap.read() # return a single frame in variable `frame` 
    #cv2.imshow('img1',frame) #display the captured image
   #save on pressing 'y'

cv2.imwrite('./c12.png',frame)

cap.release()

