global s
pro = input("Input program")
s = list(pro)
global i
i = 0

def match(a):
  global i
  global s
  if i>=len(s):
    return False
  j = "".join(s[i:i+len(a)])
  if j == a:
    print(a," is matched")
    i = i+len(a)
    return True
  else:
    return False

def S():
  if match('b'):
    if(SX()):
      return True
    else:
      return False
  else:
    return False

def SX():
  if match('a'):
    if(S()):
      if(SX()):
        return True
      else:
        return False
    else:
      return False
  else:
    return True
    
if(S()):
  if(i==len(s)):
    print('Accepted')
  else:
    print('Inner not accepted')
else:
  print('Outer not accpeted')
