import struct

class Udphdr:
    def __init__(self, src_port, dst_port, length, checksum):
        self.src_port = src_port
        self.dst_port = dst_port
        self.length = length
        self.checksum = checksum

    def pack_Udphdr(self):
        return struct.pack('!HHHH', self.src_port, self.dst_port, self.length, self.checksum)

    @classmethod
    def unpack_Udphdr(cls, packed_data):
        unpacked_data = struct.unpack('!HHHH', packed_data)
        return cls(*unpacked_data)

    def getSrcPort(self):
        return self.src_port

    def getDstPort(self):
        return self.dst_port

    def getLength(self):
        return self.length

    def getChecksum(self):
        return self.checksum


udp = Udphdr(5555, 80, 1000, 0xFFFF)
packed_data = udp.pack_Udphdr()
print("Packed UDP header:", packed_data)

unpacked_udp = Udphdr.unpack_Udphdr(packed_data)
print("Unpacked UDP header:")
print("  Src Port:", unpacked_udp.getSrcPort())
print("  Dst Port:", unpacked_udp.getDstPort())
print("  Length  :", unpacked_udp.getLength())
print("  Checksum:", unpacked_udp.getChecksum())
