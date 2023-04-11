from socket import *
import sys
import random
import time 

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 6661))
sock.listen(6)
print('dev1 running...')

while True:
    c1, addr = sock.accept()
    msg = c1.recv(1024)
    msg = msg.decode()

    if msg == "Dev1_Request":
        Temp = random.randint(0, 40) # Temperature
        Humid = random.randint(0, 100) # Humidity
        Illum = random.randint(70, 150) # Illuminance

        data = f'Temp={Temp}, Humid={Humid}, Illum={Illum}'
        print(data)
        CurTime= time.ctime(time.time())
        print(CurTime)

        c1.send(CurTime.encode()) # 현재 시간
        c1.send(data.encode())

        c1.close() 
    

    elif msg == 'quit':
        break