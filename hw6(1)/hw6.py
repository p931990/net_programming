#파일 서버

from socket import *
import os
import random

BUF_SIZE = 1024
LENGTH = 4

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 7777))
sock.listen(10)
print('File server is running...')

while True:
    conn, addr = sock.accept()

    msg = conn.recv(BUF_SIZE)
    if not msg:
        conn.close()
        continue
    res= input()
    if res == '1' :
        a=random.randrange(1, 40)
        b=random.randrange(1, 100)
        c=random.randint(70, 150)
        conn.send(a.encode(), b.encode(), c.encode())
        continue

    elif res == '2' :
        a=random.randint(40, 140)
        b=random.randint(2000, 6000)
        c=random.randint(1000, 4000)
        conn.send(a.encode(), b.encode(), c.encode())
        continue
    elif res == 'quit' :
        conn.close()

       