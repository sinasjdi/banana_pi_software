#!/usr/bin/env python3
import serial
import time

def beep_motorts():
	'''
	doc string
	'''

	serial1.write(b"#MV30,30,30,30,30,30\n")
	time.sleep(1)
	serial1.write(b"\n")
	serial1.write(b"#MV-1,-1,-1,-1,-1,-1\n")
	serial1.write(b"#MSTOP\n")
	serial1.write(b"#MSTOP\n")
	serial1.write(b"#MSTOP\n")
	serial1.write(b"#MSTOP\n")
	time.sleep(2)

	



if __name__ == '__main__':
	serial1 = serial.Serial('/dev/ttyS3', 115200, timeout=1)
	#print("Connection to device established!")
	serial1.reset_input_buffer()
	time.sleep(1)
	#serial1.write(b"#0,0,0,0,0,0\n#")
	beep_motorts()
	time.sleep(3)
	#print("beeping motors done!")
	#time.sleep(5000)
	
	#serial1.write(b"#0,0,0,0,0,0\n#")
	
	serial1.write(b"#HANDSHAKE#\n")
	if serial1.in_waiting > 0:
			line = serial1.readline().decode()
			print(line)	
	
	while True:
		if serial1.in_waiting > 0:
			serial1.write(b"#DATA\n")
			line = serial1.readline().decode()
			print(line)
			#serial1.write(b"#30,30,30,30,30,30\r\n#")


