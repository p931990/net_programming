#클라이언트


import socket

BUFF_SIZE = 1024
port = 2500

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


for i in range(10):
    time = 0.1
    data = 'Hello, IoT'
    while True:
        sock.sendto(data.encode(), ('localhost', port))
        print('Packet({}): Waiting up to {} secs for ack'.format(i,time))
        sock.settimeout(time)
        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except timeout:
            time += 1
            if time > 3.0:
                break
        else:
            print('Response', data.decode())
            break

