#home and help button

import pygame
import pygame_gui

from pygame_gui.elements import UIButton as btn

def home_btn(manager):
  home_btn=btn(relative_rect = pygame.Rect((10,10),(48,48)),
                text = '⌂',
                manager=manager)
  return home_btn

def help_btn(manager):
  help_btn=btn(relative_rect = pygame.Rect((582,10),(48,48)),
                text = '?',
                manager=manager)
  return help_btn