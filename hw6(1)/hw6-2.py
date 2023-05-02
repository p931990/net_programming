#디바이스 2

from socket import *
import sys
import random
BUF_SIZE = 1024
LENGTH = 4

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 7777))

s.send(b'Hello I am device2')

msg = s.recv(BUF_SIZE)
print(msg.decode())

a=random.randint(40, 140)
b=random.randint(2000, 6000)
c=random.randint(1000, 4000)
s.send(a.encode(), b.encode(), c.encode())

s.close()