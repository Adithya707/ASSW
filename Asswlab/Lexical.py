import re

class Lexical:
  lin_num =1
  def tokenize(self,code):
    rules =[
      ('MAIN',r'main'),
      ('INT',r'int'),
      ('FLOAT',r'float'),
      ('IF',r'if'),
      ('ELSE',r'else'),
      ('WHILE',r'while'),
      ('COMMA',r','),
      ('PCOMMA',r';'),
      ('READ',r'read'),
      ('PRINT',r'print'),
      ('LBRACKET',r'\{'),
      ('RBRACKET',r'\}'),
      ('LCIR',r'\('),
      ('RCIR',r'\)'),
      ('EQ',r'\='),
      ('GE','>='),
      ('ADD','\+'),
      ('ID',r'[a-zA-Z]\w*'),
      ('INTCONST',r'\d(\d)*'),
      ('NEWLINE',r'\n'),
      ('SKIP',r'[ \t]+'),
      ('MISMATCH',r'.'),
    ]
    
    token_join = '|'.join('(?P<%s>%s)' % x for x in rules)
    lin_start = 0
    token = []
    lex = []
    row = []
    col = []
    li = []
    
    for m in re.finditer(token_join,code):
      token_type = m.lastgroup
      token_lex = m.group(token_type)
      
      if token_type == 'NEWLINE':
        lin_start = m.end()
        self.lin_num += 1
      elif token_type == 'SKIP' or token_type=='MISMATCH':
        continue
      else:
        co = m.start()-lin_start
        col.append(co)
        row.append(self.lin_num)
        token.append(token_type)
        lex.append(token_lex)
        if token_lex not in li and token_type == 'ID':
          li.append(token_lex)
        elif token_lex in li and token_type == 'ID':
          print('ID: ',li.index(token_lex)) 
        print('Token: ',token_type,' Lexeme: ',token_lex,' row number: ',self.lin_num,' col number: ',co)
    return token,lex,row,col
