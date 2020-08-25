#Round

import Memorise
from random import choice as c

def randstr(length):
  characters = '1234567890-=qwertyuiop[]asdfghjkl;\'\\zxcvbnm,./!@#$%^&*()_+QWERTYUIOP{}ASDFGHJKL:"|ZXCVBNM<>?'
  out=''
  for i in range(length):
    out+=c(characters)
  return out

def main(round_num=1):
  rand=randstr(6)
  Memorise.main(round_num=round_num,rand=rand)