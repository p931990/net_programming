from socket import *
import socket
import random
port = 2500
BUFFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))
while True:
    msg, addr = sock.recvfrom(BUFFSIZE)
    if random.randint(1,10) <= 4:
        print('Packet from {} lost!'.format(addr))
        continue
    print('Packet is {} from {}'.format(msg.decode(),addr))
    #print('Received: ', msg.decode())
    sock.sendto('ack'.encode(), addr)