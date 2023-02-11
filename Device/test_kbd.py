
import struct 
f = open( "/dev/input/by-id/usb-0513_0318-event-kbd", "rb" ); # Open the file in the read-binary mode
while 1:
  data = f.read(24)
  data2=struct.unpack('4IHHI',data)
  print (struct.unpack('4IHHI',data))
  
  ###### PRINT FORMAL = ( Time Stamp_INT , 0 , Time Stamp_DEC , 0 , 
  ######   type , code ( key pressed ) , value (press/release) )