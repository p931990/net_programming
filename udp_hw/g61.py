#클라이언트

# client.py
import socket
import time

def main():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(1)  # 타임아웃 설정

    while True:
        message = input("메시지를 입력하세요 (빈 문자열이면 종료): ")
        if not message:
            break

        retries = 3
        while retries > 0:
            client_socket.sendto(message.encode(), (host, port))
            print("메시지 전송: ", message)

            try:
                data, _ = client_socket.recvfrom(1024)
                if data.decode() == 'ack':
                    print("서버로부터 ack 수신")
                    break
                else:
                    print("예상치 못한 응답")
            except socket.timeout:
                retries -= 1
                print("ack를 받지 못함. 재전송 시도:", 3 - retries)

    client_socket.close()

if __name__ == '__main__':
    main()
