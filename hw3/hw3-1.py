import socket       #클라이언트
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())    #수신 후 문자열처리
#본인의 이름을 문자열로 전송
a = "Jihye Park"
sock.send(a.encode())

#본인의 학번을 수신 후 출력
a = sock.recv(1024)       #정수로 받음
print(int.from_bytes(a, 'little'))     #엔디언 변환 출력
sock.close()

