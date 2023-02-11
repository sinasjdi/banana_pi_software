import serial
ser = serial.Serial(baudrate=9600)
ser.port='/dev/ttyS3'
ser.open() 
ser.write(b'hello from Pi!\n')
data = ser.readline()
print(data)
