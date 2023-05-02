#서버
from socket import *
import sys


while True:
    msg = input("number(1~3): ")
    s1 = socket(AF_INET, SOCK_STREAM)
    s1.connect(('localhost', 6661))
    if msg == '1':
        s1.send(b"1")
        msg1 = s1.recv(1024)
        msg1 =int.from_bytes(msg1,'big')
        msg2 = s1.recv(1024)
        msg2 = int.from_bytes(msg2,'big')
        msg3 = s1.recv(1024)
        msg3 = int.from_bytes(msg3,'big')
        Dev1Data = f'Temp:{msg1} Humid:{msg2} Lumi:{msg3}'
        print(Dev1Data)
        #f.write(Dev1Data + "\n")  # 파일에 데이터 저장
        s1.close()

    
    elif msg == '2':
        s1.send(b"2")
        msg1 = s1.recv(1024)
        msg1 =int.from_bytes(msg1,'big')
        msg2 = s1.recv(1024)
        msg2 = int.from_bytes(msg2,'big')
        msg3 = s1.recv(1024)
        msg3 = int.from_bytes(msg3,'big')
        Dev1Data = f'Temp:{msg1} Humid:{msg2} Lumi:{msg3}'
        print(Dev1Data)
        #f.write(Dev1Data + "\n")  # 파일에 데이터 저장
        s1.close()

    elif msg == '3':
        s1.send(b"3")
        msg1 = s1.recv(1024)
        msg1 =int.from_bytes(msg1,'big')
        msg2 = s1.recv(1024)
        msg2 = int.from_bytes(msg2,'big')
        msg3 = s1.recv(1024)
        msg3 = int.from_bytes(msg3,'big')
        Dev1Data = f'Temp:{msg1} Humid:{msg2} Lumi:{msg3}'
        print(Dev1Data)
        #f.write(Dev1Data + "\n")  # 파일에 데이터 저장
        s1.close()

    elif msg == 'quit':
        
        s1.send(b'quit')
        s1.close()
        
        print('s1 연결 종료')
        #f.close()  # 파일 닫기
        break
