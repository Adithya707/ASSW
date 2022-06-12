import socket 
import datetime
import time

ms = "i am god"
bys = str.encode(ms)
buff = 1024
localip = '127.0.0.1'
port = 2002

udps = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
udps.bind((localip,port))
print('Listening')
while True:
  time.sleep(5)
  msg = udps.recvfrom(buff)
  cf = datetime.datetime.now()
  ts = cf.timestamp()
  ms = msg[0]
  addr = msg[1]
  print('Message ',ms,' at time stamp ',ts )
  udps.sendto(ms,addr)
  
