#up_and_down

import pygame
import pygame_gui

from pygame_gui.elements import UIButton as btn
from pygame_gui.elements.ui_drop_down_menu import UIDropDownMenu as drpdn

def up_btn(manager,x):
  home_btn=btn(relative_rect = pygame.Rect((x,180),(20,20)),
                text = '/\\',
                manager=manager,
                object_id='arrow_btn')
  return home_btn

def dn_btn(manager,x):
  help_btn=btn(relative_rect = pygame.Rect((x,307),(20,20)),
                text = '\\/',
                manager=manager,
                object_id='arrow_btn')
  return help_btn

def type_drp(manager,x):
  dropdown=drpdn(options_list=['0-9','a-z','A-Z','Special'],
                  starting_option='0-9',
                  relative_rect=pygame.Rect(x,193,48,20),
                  manager=manager,
                  object_id='drop_down_menu')
  return dropdown