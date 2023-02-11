#!/usr/bin/env python3
import serial
if __name__ == '__main__':
	ser = serial.Serial('/dev/ttyS3', 115200, timeout=3) 
	ser.reset_input_buffer()
	ser.write(b'hello from stm!\n')
	while True:
		if ser.in_waiting > 0: 
			line = ser.readline()
			print(line)
