#웹 서버

from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 80))
s.listen(10)
print('waiting...')

while True:
    c, addr = s.accept()
    #s.send(b'GET /index.html HTTP/1.1\r\n\r\n')
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')
    
    a= req[0].split()
    f = a[1][1:11]
    #print(f)

    b= req[2].split()
    print(req)
    

    if f != 'index.html':
        c.send(b'Not found')
 
    elif f == 'index.html':
        f= open("index.html", 'r', encoding='utf-8')
        mimeType = 'text/html'
        c.send(f)

    # elif f == 'iot.png':
    #     f = open(iot.png, 'rb')
    #     mimeType = 'image/png'

    # elif f == 'favicon.ico':
    #     f = open(favicon.ico, 'rb')
    #     mimeType = 'image/x-icon'

