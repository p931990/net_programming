import socket       #서버
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    client.send(b'Hello '+ addr[0].encode())
    #학생의 이름 수신한후 출력
    msg = client.recv(1024)
    print(msg.decode())
    #학생의 학번을 전송
    #정수형으로 전송
    b = 20201499
    client.send(b.to_bytes(4, 'little'))
    client.close()

    