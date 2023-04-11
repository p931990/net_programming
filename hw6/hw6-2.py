from socket import *
import sys
import random
import time 

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 6662))
sock.listen(6)
print('dev2 running...')

while True:
    c2, addr = sock.accept()
    msg = c2.recv(1024)
    msg = msg.decode()

    if msg == "Dev2_Request":
        HeartBeat = random.randint(40, 140) # HeartBeat
        Steps = random.randint(2000, 6000) # Steps
        Cal = random.randint(1000, 4000) # Cal

        data = f'HeartBeat={HeartBeat}, Steps={Steps}, Cal={Cal}'
        print(data)
        CurTime= time.ctime(time.time())
        print(CurTime)

        c2.send(CurTime.encode()) # 현재 시간
        c2.send(data.encode())

        c2.close() 
    

    elif msg == 'quit':
        break