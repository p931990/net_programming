from socket import *

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('', 80))
sock.send(b'GET /index.html HTTP/1.1\r\n\r\n')
data = sock.recv(10000)
a= data.decode()
b=a.split('\r\n')[1];
print(b)
sock.close()