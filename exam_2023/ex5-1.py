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

    if msg == "1":
        Temp = random.randint(1, 50) # Temperature
        Humid = 0
        Lumi = 0
        print(Temp)
        Temp = Temp.to_bytes(4, 'big')
        c1.send(Temp)
        Humid = Humid.to_bytes(4, 'big')
        c1.send(Humid)
        Lumi = Lumi.to_bytes(4, 'big')
        c1.send(Lumi)
        data1 = Temp
        data2 = Humid
        data3 = Lumi
 

        
    elif msg == "2":
        Temp = 0
        Humid = random.randint(1, 100) # Humidity
        Lumi = 0
        Temp = Temp.to_bytes(4, 'big')
        c1.send(Temp)
        Humid = Humid.to_bytes(4, 'big')
        c1.send(Humid)
        Lumi = Lumi.to_bytes(4, 'big')
        c1.send(Lumi)
        data1 = Temp
        data2 = Humid
        data3 = Lumi


    elif msg == "3":
        Temp = 0
        Humid = 0
        Lumi = random.randint(1, 150) # Illuminance
        Temp = Temp.to_bytes(4, 'big')
        c1.send(Temp)
        Humid = Humid.to_bytes(4, 'big')
        c1.send(Humid)
        Lumi = Lumi.to_bytes(4, 'big')
        c1.send(Lumi)
        data1 = Temp
        data2 = Humid
        data3 = Lumi
       
        

    elif msg == 'quit':
        break

    #c1.send(data1.encode(), data2.encode(), data3.encode())

    c1.close() 

    