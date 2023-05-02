#서버
# server.py
import socket
import random

def main():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print("서버가 시작되었습니다. 클라이언트를 기다리는 중입니다...")

    while True:
        data, addr = server_socket.recvfrom(1024)
        if not data:
            break

        # 40% 확률로 응답하지 않음
        if random.random() < 0.6:
            server_socket.sendto(b'ack', addr)
        else:
            print("서버에서 ack 손실 발생")

    server_socket.close()

if __name__ == '__main__':
    main()