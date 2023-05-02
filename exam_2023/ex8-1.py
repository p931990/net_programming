#클라이언트

from socket import *

port = 3333
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

for i in range(10):
    time = 0.1
    while True:
        data = {}
        msg = input('Enter the message("send mboxId message" or "receive mboxId"):')
        if msg == 'quit':
            sock.close()

        sock.sendto(msg.encode(), ('localhost', port))
        sock.settimeout(time)
        try:
            data, addr = sock.recvfrom(BUFFSIZE)
        except timeout:
            time +=2            #2초 최대 3회
            if time > 6.0:
                break
        else:
            print('Response ', data.decode())
            break
