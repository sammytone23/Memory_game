#Game manager

import pygame
import pygame_gui
import Round

from home_and_help import  home_btn,help_btn
from pygame_gui.elements import UIButton as btn
from pygame_gui.elements.ui_label import UILabel as lbl

HEIGHT = 480
WIDTH = 640

pygame.init()

def Game():
  # stage='mem'
  round_num=1

  # end = False
  # while not end:
  #   if stage=='mem':
  #     stage=Round.main()
  #   else:
  #     return stage
  for round_num in range(6):
    score=Round.Round(round_num=round_num)

if __name__ == '__main__':
  Game()