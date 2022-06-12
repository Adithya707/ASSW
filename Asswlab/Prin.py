from Buffer import Buffer
from Lexical import Lexical

if __name__ == '__main__':
  Buffer = Buffer()
  Ana = Lexical()
  to = []
  lex = []
  ro  = []
  col = []
  for i in Buffer.load_buf():
    t,l,r,c = Ana.tokenize(i)
    to+=t
  print('Tokens',to)
