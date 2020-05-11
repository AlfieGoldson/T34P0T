import socket
import struct
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("lsis.univ-tln.fr", 37))
t = struct.unpack('I', s.recv(4))
print(t[0])
t = socket.ntohl(t[0])
print(t)
print(time.ctime(t - 2208988800))
s.close()
