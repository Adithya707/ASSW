import socket
import datetime

msg = "I am not god"
bys = str.encode(msg)

server = ('127.0.0.1',2002)
buffer = 1024
cf = datetime.datetime.now()
ts = cf.timestamp()
print('Before time',ts)
udps = socket.socket(family = socket.AF_INET,type=socket.SOCK_DGRAM)
udps.sendto(bys,server)
ms = udps.recvfrom(buffer)
ts = cf.timestamp()
print('After time',ts)
print('msg from server',ms[0])
