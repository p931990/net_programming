#서버
import socket
import time
clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)f
s.bind(('', 2500))
s.listen(1)



print('Server Started')
while True:
    conn, addr = s.accept()
    data = conn.recv(1024)
    if 'quit' in data.decode():
        if addr in clients:
            print(addr, 'exited')
            clients.remove(addr)
            continue

    if addr not in clients:
        print('new client', addr)
        clients.append(addr)

    print(time.asctime() + str(addr) + ':' + data.decode())

    for client in clients:
        if client != addr:
            conn.send(data, client)
