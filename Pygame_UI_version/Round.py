#Round

import Memorise,Repeat,Display
import random

#random string generator
def randstr(length):
  characters = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
  out=''
  for i in range(length):
    #add a random character
    out+=random.choice(characters)
  return out

def Round(round_num=1,length=10):
  rand=randstr(6)
  #run the memorise screen
  mem=Memorise.Memorise(round_num=round_num,rand=rand,length=length)
  #make sure it's supposed to continue
  if mem!='cont':
    return mem
  #run the repeat screen
  rep=Repeat.Repeat(round_num=round_num,rand=rand)
  #make sure it's supposed to continue
  if rep in ['home','help', 'quit']:
    return rep
  return rep

