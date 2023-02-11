import cv2
cap0 = cv2.VideoCapture(1,cv2.CAP_V4L2)
cap0.set(3,320)
cap0.set(4,240)
cap1 = cv2.VideoCapture(3,cv2.CAP_V4L2)
cap1.set(cv2.CAP_PROP_FPS,10)

cap1.set(3,320)
cap1.set(4,240)
#cap1.set(3,)
cap1.set(cv2.CAP_PROP_FPS,10)
#cap1.set(4,720)
ret0, frame0 = cap0.read()
#assert ret0 # succeeds
ret1, frame1 = cap1.read()
#print(ret0)
cv2.imwrite('./c13.png',frame0)
cv2.imwrite('./c14.png',frame1)


print(ret1)
print(ret0)
cap0.release()
cap1.release()
