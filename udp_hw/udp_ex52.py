#서버

from socket import *

port = 3333
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))
list1 = list()
while True:
    data, addr = sock.recvfrom(BUFFSIZE)
    print('<- ', data.decode())
    d = data.decode().split(' ',2)      # send 1 message 두칸 띄움
    print(d)

    if data.decode() == "":
        resp = 'No messages'
    elif data.decode() == "quit":
        break
    
    elif d[0]== 'send':
        print('hahah')
        list1.append(d[2])
        print(list1)
        resp = 'Ok'
        
    elif d[0]=='receive':
        print('nonono')
        mboxID = int(d[1]) -1
        print(mboxID)
        resp = list1[mboxID]   

    else:
        resp = '다시입력해.'
        print(resp)     
        
    

    sock.sendto(resp.encode(), addr)
sock.close()
