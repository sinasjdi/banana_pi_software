import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.2.196', 8487)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

while(1):
# Send data
	message = b'This is our message. It is very long but will only be transmitted in chunks of 16 at a time'
	print('sending {!r}'.format(message))
	sock.sendall(message)

    	 # Look for the response
	amount_received = 0
	amount_expected = len(message)
	while amount_received < amount_expected:
        	data = sock.recv(1024)
       		amount_received += len(data)
        	print('received {!r}'.format(data))

