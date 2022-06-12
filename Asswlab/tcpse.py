import socket
import threading

total_con = 0
connection = []

class Client(threading.Thread):
  def __init__(self,socket,address,id,name,signal):
    threading.Thread.__init__(self)
    self.socket = socket
    self.address = address
    self.id = id
    self.name = name
    self.signal = signal
  
  def __str__(self):
    return(str(self.id) + " " + str(self.address))
  
  def run(self):
    while self.signal:
      try:
        data = self.socket.recv(5)
      except:
        print('Disconnected with id',str(self.id))
        self.signal = False
        break
      if data != "":
        print("Data from ",str(self.id),' Data ',str(data.decode("utf-8")))
        for client in connection:
          if client.id != self.id:
            client.socket.sendall(data)
            

def newcon(socket):
  while True:
    sock,addr = socket.accept()
    global total_con
    connection.append(Client(sock,addr,total_con,"Name",True))
    connection[len(connection)-1].start()
    print("New connection established",connection[len(connection)-1])
    total_con+=1

def main():
  host = input("Host: ")
  port = int(input("Port: "))
  tcps = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
  tcps.bind((host,port))
  tcps.listen(5)
  newThread = threading.Thread(target=newcon,args=(tcps,))
  newThread.start()
  
main()
