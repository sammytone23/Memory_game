#Repeat

import pygame
import pygame_gui

from home_and_help import  home_btn,help_btn
from up_and_down import up_btn,dn_btn,type_drp
from pygame_gui.elements import UIButton as btn
from pygame_gui.elements.ui_label import UILabel as lbl

HEIGHT = 480
WIDTH = 640

pygame.init()

def increment_character(c,inc):
  if c in '0123456789':
    return str((int(c)+inc)%10)
  elif c in 'abcdefghijklmnopqrstuvwxyz':
    return chr((ord(c)-(ord('a')-1)+inc%26)+ord('a')-1)
  elif c in 'abcdefghijklmnopqrstuvwxyz'.upper():
    return chr((ord(c)-(ord('A')-1)+inc%26)+ord('A')-1)
  elif c in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
    pos='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'.find(c)
    pos+=inc
    pos%=len('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    return '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'[pos]
def arrow_pressed(event,objects):
  for pos in objects['characters']:
    if objects['characters'][pos]['up_button']:
      out_c=increment_character(objects['characters'][pos]['character'].text,1)
      return [True,pos,out_c]
    elif objects['characters'][pos]['down_button']:
      out_c=increment_character(objects['characters'][pos]['character'].text,-1)
      return [True,pos,out_c]
  return [False]





def Repeat(round_num=1,rand='*cH1;@'):
  pygame.display.set_caption('Memorise')
  window_surface = pygame.display.set_mode((WIDTH, HEIGHT))

  background = pygame.Surface((WIDTH, HEIGHT))
  background.fill(pygame.Color('#5E6059'))

  manager = pygame_gui.UIManager((WIDTH, HEIGHT), 'theme.json')
  manager.add_font_paths('Mono', 'RobotoMono-Regular.ttf')
  
  clock = pygame.time.Clock()

  objects = {}

  objects['home_button'] = home_btn(manager)
  objects['help_button'] = help_btn(manager)

  objects['round_num']=lbl(relative_rect = pygame.Rect((275, 73), (101, 28)),
                          text = 'Round '+str(round_num),
                          manager = manager,
                          object_id='small')
  objects['heading'] = lbl(relative_rect = pygame.Rect((147, 107), (346, 75)),
                          text = 'Repeat!',
                          manager = manager)
  objects['characters']=[]
  positions=[((119,193),(48,100)),((190,193),(48,100)),((261,193),(48,100)),((332,193),(48,100)),((403,193),(48,100)),((474,193),(48,100))]
  arrow_btn_pos=[132,223,294,365,416,507]
  drpdn_pos=[118,189,260,331,402,473]
  

  for p,c in enumerate('000000'):
    group={}
    group['up_button']=up_btn(manager,arrow_btn_pos[p])
    group['down_button']=dn_btn(manager,arrow_btn_pos[p])
    group['type_dropdown']=type_drp(manager,drpdn_pos[p])
    group['character']=lbl(relative_rect = pygame.Rect(positions[p][0],positions[p][1]),
                          text = c,
                          manager = manager,
                          object_id='character_display')
    objects['characters'].append(group)

  objects['round_num']=lbl(relative_rect = pygame.Rect((219, 379), (202, 28)),
                          text = '# seconds left',
                          manager = manager,
                          object_id='small')

  end = False
  while not end:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get(): 
      if event.type == pygame.QUIT:
        pygame.quit()

      elif event.type == pygame.USEREVENT:
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
          if event.ui_element == objects['home_button']:
            print('home')
            return 'home'
          if event.ui_element == objects['help_button']:
            print('help')
            return 'help'
          arp=arrow_pressed(event,objects)
          if arp[0]:
            objects['characters'][arp[1]].set_text(arp[2])
          
      manager.process_events(event)
    
    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()

if __name__ == '__main__':
  Repeat()