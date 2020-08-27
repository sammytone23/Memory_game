#home and help button

import pygame
import pygame_gui

from pygame_gui.elements import UIButton as btn

#the home button
def home_btn(manager):
  home_btn=btn(relative_rect = pygame.Rect((10,10),(127,48)),
                text = 'Home',
                manager=manager,
                object_id='big_button')
  return home_btn

#the help button
def help_btn(manager):
  help_btn=btn(relative_rect = pygame.Rect((582,10),(48,48)),
                text = '?',
                manager=manager,
                object_id='big_button')
  return help_btn