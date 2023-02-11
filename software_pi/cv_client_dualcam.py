import cv2
import io
import socket
import struct
import time
import pickle
import zlib


client_socket0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket0.connect(('192.168.2.196', 8485))
connection0 = client_socket0.makefile('wb')

time.sleep(2)
print("conn1 established")
client_socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket1.connect(('192.168.2.196', 8486))
connection1 = client_socket1.makefile('wb')
time.sleep(2)
print("conn2 established")

cap0 = cv2.VideoCapture(1)
cap0.set(3,640)
cap0.set(4,480)
cap1 = cv2.VideoCapture(3)
cap1.set(cv2.CAP_PROP_FPS,10)
cap1.set(3,320)
cap1.set(4,240)
cap1.set(cv2.CAP_PROP_FPS,10)



img_counter = 0

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 70]

while True:
    ret0, frame0 = cap0.read()
    ret1, frame1 = cap1.read()
    result0, frame0 = cv2.imencode('.jpg', frame0, encode_param)
    result1, frame1 = cv2.imencode('.jpg', frame1, encode_param)
#    data = zlib.compress(pickle.dumps(frame, 0))
    data0 = pickle.dumps(frame0, 0)
    size0 = len(data0)
    
    data1 = pickle.dumps(frame1, 0)
    size1 = len(data1)


    #print("{}: {}".format(img_counter, size))
    client_socket0.sendall(struct.pack(">L", size0) + data0)
    client_socket1.sendall(struct.pack(">L", size1) + data1)
    img_counter += 1

cam0.release()
cam1.release()
