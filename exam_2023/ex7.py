#서버
#서버
from socket import *
import sys

# s1 = socket(AF_INET, SOCK_STREAM)
# s1.connect(('localhost', 6661))
# s2 = socket(AF_INET, SOCK_STREAM)
# s2.connect(('localhost', 6662))



while True:
    s1 = socket(AF_INET, SOCK_STREAM)
    s1.connect(('localhost', 9999))

    s1.send(b"Hello")
    msg1 = s1.recv(1024)
    msg1 =int.from_bytes(msg1,'big')
    msg2 = s1.recv(1024)
    msg2 = int.from_bytes(msg2,'big')
    msg3 = s1.recv(1024)
    msg3 = int.from_bytes(msg3,'big')
    Dev1Data = f'Temp:{msg1} Humid:{msg2} Lumi:{msg3}'
    print(Dev1Data)
       
    s1.close()


    
        
    print('s1 연결 종료')
    break
