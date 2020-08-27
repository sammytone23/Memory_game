#Round

import Memorise,Repeat,Display
from random import choice as c

def randstr(length):
  characters = r'''~`1234567890-=qwertyuiop[]asdfghjkl;'\zxcvbnm,./!@#$%^&*()_+QWERTYUIOP{}ASDFGHJKL:"|ZXCVBNM<>?'''
  out=''
  for i in range(length):
    out+=c(characters)
  return out

def Round(round_num=1):
  rand=randstr(6)
  mem=Memorise.Memorise(round_num=round_num,rand=rand)
  if mem!='cont':
    return mem
  rep=Repeat.Repeat(round_num=round_num,rand=rand)
  if rep in ['home','help', 'quit']:
    return rep
  return rep

