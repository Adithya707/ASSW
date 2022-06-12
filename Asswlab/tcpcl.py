import socket
import threading
import sys

def receive(socket,signal):
  while signal:
    try:
      data = socket.recv(5)
      print('Data received: ',str(data.decode("utf-8")))
    except:
      print('Connection is disconnected')
      signal = False
      break

host = input("Enter host")
port = int(input("Enter port number"))

try:
  tcpc = socket.socket(family = socket.AF_INET,type=socket.SOCK_STREAM)
  tcpc.connect((host,port))
except:
  print("Disconnected")
  sys.exit(0)

newThread = threading.Thread(target=receive,args=(tcpc,True))
newThread.start()

while True:
  msg = input()
  tcpc.sendall(str.encode(msg))
