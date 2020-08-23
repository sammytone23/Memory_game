#home and help button

import pygame
import pygame_gui

from pygame_gui.elements import UIButton as btn

def home_btn(manager):
  test_btn=btn(relative_rect = pygame.Rect((10,10),(48,48)),
                text = 'Home',
                manager=manager)

def help_btn(manager):
  test_btn=btn(relative_rect = pygame.Rect((10,10),(48,48)),
                text = 'Help',
                manager=manager)