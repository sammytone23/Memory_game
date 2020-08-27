#Game manager
#Imports
import pygame
import pygame_gui

from home_and_help import  home_btn,help_btn
from pygame_gui.elements import UIButton as btn
from pygame_gui.elements.ui_label import UILabel as lbl
#import my screens
import Round,Display

#main funcction
def Game(length=10):
  #gameplay loop
  tot_score=0
  for round_num in range(6):
    #run the round
    rnd=Round.Round(round_num=round_num,length=length)
    #make sure it's supposed to continue
    if rnd in ['home','help']:
      return rnd
    tot_score+=rnd
  #Go to the display screen
  disp=Display.Display(score)
  return disp

if __name__ == '__main__':
  Game()