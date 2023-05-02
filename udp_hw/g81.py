import socket

def main():
    host = '127.0.0.1'
    port = 9000
    external_host = 'www.daum.net'
    external_port = 80

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("릴레이 서버가 시작되었습니다. 브라우저를 기다리는 중입니다...")

    conn, addr = server_socket.accept()
    print(f"{addr}에서 브라우저가 연결되었습니다.")

    request_data = conn.recv(1024).decode().split('\r\n')
    request_line = request_data[0]

    # 외부 웹 서버로 요청을 보내는 클라이언트 소켓
    external_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    external_socket.connect((external_host, external_port))

    # HTTP 메시지의 요청 라인과 'Host: www.daum.net'만 전송
    external_socket.send((request_line + '\r\n' + 'Host: ' + external_host + '\r\n\r\n').encode())

    # 외부 웹 서버로부터 응답을 받아 브라우저로 전송
    while True:
        response_data = external_socket.recv(1024)
        if not response_data:
            break
        conn.send(response_data)

    conn.close()
    external_socket.close()
    server_socket.close()

if __name__ == '__main__':
    main()
