from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()

    data = c.recv(1024)
    msg = data.decode()
    reg = msg.split('\r\n') # 요청 메시지 스플릿해서 list 형태로 저장 나는 첫번째 줄만 필요
    print(reg) # 확인용
    reg = reg[0].split() # 첫줄 가져와 공백으로 다시 split
    reg = reg[1] # 첫줄에서 두번째 /index.html 가져와
    reg = reg[1:] # 가져와서 / 이거 빼고 index.html만 남기기 
    ### 여기까지 index.html 파일 뽑음 ###

    print(reg) # 확인용
    if reg == "index.html":
        f = open('./index.html', 'r', encoding='utf-8')
        mimeType = 'text/html'
        # HTTP 헤더 전송
        c.send(b'HTTP/1.1 200 OK\r\n') 
        c.send(b'Content-Type: ' + mimeType.encode() + b'\r\n')
        c.send(b'\r\n')
        # HTTP 바디 전송
        data = f.read()
        c.send(data.encode('euc-kr'))
        
    
    elif reg == "iot.png":
        f = open('./iot-1.png', 'rb')
        mimeType = 'image/png'
        # HTTP 헤더 전송
        c.send(b'HTTP/1.1 200 OK\r\n') 
        c.send(b'Content-Type: ' + mimeType.encode() + b'\r\n')
        c.send(b'\r\n')
        # HTTP 바디 전송
        data = f.read()
        c.send(data)
        
    
    elif reg == "favicon.ico":
        f = open('./favicon.ico', 'rb')
        mimeType = 'image/x-icon'
        # HTTP 헤더 전송
        c.send(b'HTTP/1.1 200 OK\r\n') 
        c.send(b'Content-Type: ' + mimeType.encode() + b'\r\n')
        c.send(b'\r\n')
        # HTTP 바디 전송
        data = f.read()
        c.send(data)
        

    else:
        # HTTP 헤더 전송
        c.send(b'HTTP/1.1 404 Not Found\r\n')
        c.send(b'\r\n')
        # HTTP 바디 전송
        c.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
        c.send(b'<BODY>Not Found</BODY></HTML>')
        
    c.close()