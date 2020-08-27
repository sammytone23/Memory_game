#up_and_down

import pygame
import pygame_gui

from pygame_gui.elements import UIButton as btn
from pygame_gui.elements.ui_drop_down_menu import UIDropDownMenu as drpdn

# the up button used in 'Repeat.py'
def up_btn(manager,x):
  home_btn=btn(relative_rect = pygame.Rect((x,173),(20,20)),
                text = '/\\',
                manager=manager,
                object_id='up_arrow_btn')
  return home_btn

# the down button used in 'Repeat.py'
def dn_btn(manager,x):
  help_btn=btn(relative_rect = pygame.Rect((x,293),(20,20)),
                text = '\\/',
                manager=manager,
                object_id='dn_arrow_btn')
  return help_btn

# the dropdown used in 'Repeat.py'
def type_drp(manager,x):
  dropdown=drpdn(options_list=['0-9','a-z','A-Z','Spc.'],
                  starting_option='0-9',
                  relative_rect=pygame.Rect(x,193,48,20),
                  manager=manager,
                  object_id='choice')
  return dropdown