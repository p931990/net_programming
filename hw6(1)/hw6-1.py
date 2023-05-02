from socket import *
import sys
import random
BUF_SIZE = 1024
LENGTH = 4 # '파일 크기': 4바이트
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 7777))


s.send("Hello I am device1")
msg = s.recv(BUF_SIZE) # 'Filename' 메시지 수신

a=random.randrange(1, 40)
b=random.randrange(1, 100)
c=random.randint(70, 150)
s.send(a.encode(), b.encode(), c.encode())
        
while rx_size < LENGTH:
    msg = s.recv(BUF_SIZE)
    if not msg:
        s.close()
        sys.exit()
    data = data + msg
    rx_size += len(msg)
if rx_size < LENGTH:
    s.close()
    sys.exit()

filesize = int.from_bytes(data, 'big')
print('server:', filesize)





if not msg:
    s.close()
    sys.exit()
elif msg != b'Filename':
    print('server:', msg.decode())
    s.close()
    sys.exit()
else:
    print('server:', msg.decode())