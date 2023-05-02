from socket import *
import sys
import random
import time 

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 9999))
sock.listen(6)
print('dev1 running...')

while True:
    c1, addr = sock.accept()
    msg = c1.recv(1024)
    msg = msg.decode()

    if msg == "1":
        Sender= random.randint(1, 100) 
        Receiver = random.randint(1, 100) 
        Temp = random.randint(1, 100) # Temperature
        Humi = random.randint(1, 100) 
        Lumi = random.randint(1, 100) 
        Air = random.randint(1, 100) 
        Seq  = random.randint(1, 100) 
        print(Temp)
        Temp = Temp.to_bytes(4, 'big')
        c1.send(Temp)
        Humid = Humid.to_bytes(4, 'big')
        c1.send(Humid)
        Lumi = Lumi.to_bytes(4, 'big')
        c1.send(Lumi)
        Air = Air.to_bytes(4, 'big')
        c1.send(Air)
        Seq = Seq.to_bytes(4, 'big')
        c1.send(Seq)
        data1 = Temp
        data2 = Humid
        data3 = Lumi

    elif msg == 'quit':
        break

    #c1.send(data1.encode(), data2.encode(), data3.encode())

    c1.close() 

    