from socket import *
import os
BUF_SIZE = 1024
LENGTH = 4 # '파일 크기': 4바이트
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 7777))
sock.listen(10)
print('File server is running...')
while True:
    conn, addr = sock.accept()
    msg = conn.recv(BUF_SIZE)
    a=str(input())
    conn.send(a.encode())

    if a == '1':
        b = conn.recv(BUF_SIZE)
        print('client:', addr, "device1.txt")
        #내용 파일에 넣기 -> 송신
        x,y,z = conn.recv(BUF_SIZE)
        res = "날짜 Device1: Temp={x.decode()}, Humid={y.decode()}, lilum={z.decode()}"
        f = open("device2.txt", 'w')
        data = f.write(res)
        conn.sendall(data)


    elif a == '2':
        c = conn.recv(BUF_SIZE)
        print('client:', addr, "device2.txt")
        #내용 파일에 넣기 -> 송신
        x,y,z = conn.recv(BUF_SIZE)
        res = "날짜 Device2: Temp={x.decode()}, Humid={y.decode()}, lilum={z.decode()}"
        f = open("device2.txt", 'w')
        data = f.write(res)
        conn.sendall(data)




    conn.close()
