import sys
import socket

#Membuat TCP/IP Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Menyambungkan Socket dengan Port
server_address = ('localhost', 20001)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)


try:
    #Mengirim data
    message = 'INI ADALAH DATA YANG DIKIRIM ABCDEFGHIJKLMNOPQ'
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)

    #Melihat Respon
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print >>sys.stderr, 'received "%s"' % data
finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
