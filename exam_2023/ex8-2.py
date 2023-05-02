#서버

from socket import *
import random

port = 3333
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))
list1 = list()
while True:
    data, addr = sock.recvfrom(BUFFSIZE)
    if random.randint(1,10) <= 1:               #10%확률
        print('Packet from {} lost!'.format(addr))
        continue
    else:
        print('<- ', data.decode(),addr)
        d = data.decode().split(' ',2)      # send 1 message 두칸 띄움
        #print(d)

        if data.decode() == "":
            resp = 'No messages'
        elif data.decode() == "quit":
            break
    
        elif d[0]== 'send':
            list1.append(d[2])
            print(list1)
            resp = 'Ok'
        
        elif d[0]=='receive':  
            mboxID = int(d[1]) -1
            resp = list1[mboxID]   

        else:
            resp = '다시입력해.'    #send 1 message or receive 1 형태가 아닐시
            #print(resp)     
            
        sock.sendto(resp.encode(), addr)
    
sock.close()
