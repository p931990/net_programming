from socket import *

#계산기의 조건 함수 추가
def calculator(a,b,k):
    a = int(a)
    b = int(b)
    if k=='+':
        return a+b
    elif k== '-':
        return a-b
    elif k== '*':
        return a*b
    elif k== '/':
        return round(a/b, 1)    #소수점 첫째자리까지

s= socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('waiting...')

while True:
    client, addr = s.accept()
    print('connection from ', addr)
    while True:
        data = client.recv(1024)     
        
        if not data:
            break
        try:
            res = data.decode()
            a,c,b = res.split()             #파싱
            res = str(calculator(a,b,c))    #계산
        except:
            client.send(b'Try again')
        else:
            client.send(res.encode())

    client.close()