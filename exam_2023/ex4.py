#220.69.189.125', 443
import socket
import struct
import sys
class DnsClient:
    def __init__(self, domainName):
        self.domainName = domainName
    # DNS Query Header
        self.TransactionId = 1
        self.Flag = 0x0100
        self.Questions = 1
        self.AnswerRRs = 0
        self.AuthorityRRs = 0
        self.AdditionalRRs = 0
    def response(self, packet): # processing dns response
        dnsHeader = packet[:12]
        dnsData = packet[12:].split(b'\x00', 1)

        ansRR = packet[12+len(dnsData[0])+5:12+len(dnsData[0])+21]
        rr_unpack = struct.unpack('!2sHHIH4s', ansRR)
        ip_addr = socket.inet_ntoa(rr_unpack[5])
        print(self.domainName, ip_addr)
