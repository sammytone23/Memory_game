#Repeat
#Imports
import pygame
import pygame_gui

from pygame_gui.elements import UIButton as btn
from pygame_gui.elements.ui_label import UILabel as lbl

#Import my buttons (and dropdown)
from home_and_help import  home_btn,help_btn
from up_and_down import up_btn,dn_btn,type_drp

#size
HEIGHT = 480
WIDTH = 640

pygame.init()

#change the character by one
def increment_character(ch,inc):
  if ch in '0123456789':
    return str((int(ch)+inc)%10)
  elif ch in 'abcdefghijklmnopqrstuvwxyz':
    pos='abcdefghijklmnopqrstuvwxyz'.find(ch)
    pos+=inc
    pos%=len('abcdefghijklmnopqrstuvwxyz')
    return 'abcdefghijklmnopqrstuvwxyz'[pos]
  elif ch in 'abcdefghijklmnopqrstuvwxyz'.upper():
    pos='abcdefghijklmnopqrstuvwxyz'.upper().find(ch)
    pos+=inc
    pos%=len('abcdefghijklmnopqrstuvwxyz')
    return 'abcdefghijklmnopqrstuvwxyz'.upper()[pos]
  elif ch in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
    pos='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'.find(ch)
    pos+=inc
    pos%=len('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    return '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'[pos]
#check if an arrow button as pressed
def arrow_pressed(event,objects):
  for pos in range(len(objects['characters'])):
    if event.ui_element==objects['characters'][pos]['up_button']:
      out_c=increment_character(objects['characters'][pos]['character'].text,-1)
      return [True,pos,out_c]
    elif event.ui_element==objects['characters'][pos]['down_button']:
      out_c=increment_character(objects['characters'][pos]['character'].text,1)
      return [True,pos,out_c]
  return [False]

#check which dropdown was changed, and then reset the displyed character
def dropdown_changed(event,objects):
  for pos in range(len(objects['characters'])):
    if event.ui_element==objects['characters'][pos]['type_dropdown']:
      typ=objects['characters'][pos]['type_dropdown'].selected_option
      if typ in ['0-9','a-z','A-Z']:
        out_c=typ[0]
      else:
        out_c='!'
      return [True,pos,out_c]
  return [False]

#score the input against the random string
def score(objects,rand):
  out=0
  for p,c in enumerate(rand):
    if c==objects['characters'][p]['character'].text:
      out+=1
  return out

#main function
def Repeat(round_num=1,rand='*cH1;@'):
  #setup
  pygame.display.set_caption('Memorise')
  window_surface = pygame.display.set_mode((WIDTH, HEIGHT))

  background = pygame.Surface((WIDTH, HEIGHT))
  background.fill(pygame.Color('#5E6059'))

  manager = pygame_gui.UIManager((WIDTH, HEIGHT), 'theme.json')
  manager.add_font_paths('Mono', 'RobotoMono-Regular.ttf')
  
  clock = pygame.time.Clock()

  #Dictionary for my objects
  objects = {}

  #create my objects
  objects['home_button'] = home_btn(manager)
  objects['help_button'] = help_btn(manager)

  objects['round_num']=lbl(relative_rect = pygame.Rect((275, 73), (101, 28)),
                          text = 'Round '+str(round_num),
                          manager = manager,
                          object_id='small')
  objects['heading'] = lbl(relative_rect = pygame.Rect((147, 107), (346, 75)),
                          text = 'Repeat!',
                          manager = manager)
  
  #make the editable characters
  objects['characters']=[]
  positions=[((119,193),(48,100)),((190,193),(48,100)),((261,193),(48,100)),((332,193),(48,100)),((403,193),(48,100)),((474,193),(48,100))]
  arrow_btn_pos=[132,203,274,345,416,487]
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

  objects['done_button']=btn(relative_rect = pygame.Rect((256, 330), (127, 48)),
                          text = 'Done',
                          manager = manager,
                          object_id='big_button')

  #Main loop
  end = False
  while not end:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get(): 
      #check if the x pressed
      if event.type == pygame.QUIT:
        pygame.quit()
      #Check if one of my objects was presed
      elif event.type == pygame.USEREVENT:
        #check if one of my buttons was pressed
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
          if event.ui_element == objects['home_button']:
            return 'home'
          if event.ui_element == objects['help_button']:
            return 'help'
          if event.ui_element == objects['done_button']:
            out=score(objects,rand)
            return out
          arp=arrow_pressed(event,objects)
          if arp[0]:
            #update the displayed character
            objects['characters'][arp[1]]['character'].set_text(arp[2])
        #checkl if one of my dropdowns was pressed
        elif event.user_type==pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
          drp=dropdown_changed(event,objects)
          if drp[0]:
            #update the displayed character
            objects['characters'][drp[1]]['character'].set_text(drp[2])
          
      manager.process_events(event)
    
    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()

if __name__ == '__main__':
  Repeat()