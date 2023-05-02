#서버

import socket
import random
BUFF_SIZE = 1024
port = 2500

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))
print('Listening...')


while True:
    msg, addr = sock.recvfrom(BUFF_SIZE)
    if random.randint(1, 10) <= 4:
        print('Packet from {} lost!'.format(addr))
        continue
    print('Packet is {} from {}'.format(msg.decode(), addr))

    sock.sendto('ack'.encode(), addr)