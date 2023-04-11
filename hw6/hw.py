from socket import *
import sys

# s1 = socket(AF_INET, SOCK_STREAM)
# s1.connect(('localhost', 6661))
# s2 = socket(AF_INET, SOCK_STREAM)
# s2.connect(('localhost', 6662))

f = open("data.txt", "a")  # 파일 열기

while True:
    msg = input("What device number to connect to?: ")

    if msg == '1':
        s1 = socket(AF_INET, SOCK_STREAM)
        s1.connect(('localhost', 6661))

        s1.send(b"Dev1_Request")
        msg1 = s1.recv(1024)
        msg1 = msg1.decode()
        msg1_1 = s1.recv(1024)
        msg1_1 = msg1_1.decode()
        Dev1Data = f'{msg1}: Device1: {msg1_1}'
        print(Dev1Data)
        f.write(Dev1Data + "\n")  # 파일에 데이터 저장
        s1.close()

    
    elif msg == '2':
        s2 = socket(AF_INET, SOCK_STREAM)
        s2.connect(('localhost', 6662))

        s2.send(b"Dev2_Request")
        msg2 = s2.recv(1024)
        msg2 = msg2.decode()
        msg2_2 = s2.recv(1024)
        msg2_2 = msg2_2.decode()
        Dev2Data = f'{msg2}: Device2: {msg2_2}'
        print(Dev2Data)
        f.write(Dev2Data + "\n")  # 파일에 데이터 저장
        s2.close()

    elif msg == 'quit':
        s1 = socket(AF_INET, SOCK_STREAM)
        s1.connect(('localhost', 6661))

        s2 = socket(AF_INET, SOCK_STREAM)
        s2.connect(('localhost', 6662))

        s1.send(b'quit')
        s1.close()
        s2.send(b'quit')
        s2.close()
        print('s1, s2 연결 종료')
        f.close()  # 파일 닫기
        break
