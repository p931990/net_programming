from  socket import *
import socket
port = 2500
BUFFSIZE = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(('localhost',port))

for i in range(10):
    time = 0.1
    data='IOT'
    while True:
        
        sock.send(data.encode())
        print('Packet({}): Waiting up to {} secs for ack'.format(i, time))
        sock.settimeout(time)
        try:
            data = sock.recv(BUFFSIZE)
        except timeout:
            time *=2
            if time > 1.0:
                break
        else:
            print('Response', data.decode())
            break

