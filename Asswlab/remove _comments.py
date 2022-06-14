import re
import sys
if __name__ == "__main__":
  next_str = ""
  with open('abc.c',"r") as f:
    next_str = re.sub('(?<!\")(\/\/[\s\S]*?[\s])(?!\")', '',f.read(),flags=re.S)
  with open('abc.c','w') as f:
    f.write(next_str)
