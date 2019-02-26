import sys
import socket

#Membuat TCP/IP Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind Socket ke Port
server_address = ('localhost', 20001)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)


sock.listen(1)
while True:
    	#Menunggu koneksi
    	print >>sys.stderr, 'waiting for a connection'
    	connection, client_address = sock.accept()
    	print >>sys.stderr, 'connection from', client_address

    	#Menerima data
    	while True:
        	data = connection.recv(32)
        	print >>sys.stderr, 'received "%s"' % data
            	if data:
                	print >>sys.stderr, 'sending data back to the client'
                	connection.sendall('-->'+data)
            	else:
                	print >>sys.stderr, 'no more data from', client_address
                	break
        #Membersihkan koneksi
	connection.close()
