
class Buffer:
  def load_buf(self):
    arq = open('program.c','r')
    text = arq.readline()
    cont = 1
    buffer = []
    while text != "":
      buffer.append(text)
      cont +=1
      text = arq.readline()
      if cont == 10 or text=='':
        buf = ''.join(buffer)
        cont = 1
        yield buf
        buffer = []
    arq.close()
