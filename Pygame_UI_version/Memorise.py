#Memorise
#imports
import pygame
import pygame_gui

from math import floor
from pygame_gui.elements import UIButton as btn
from pygame_gui.elements.ui_label import UILabel as lbl
#import my home and help buttons
from home_and_help import  home_btn,help_btn
#size
HEIGHT = 480
WIDTH = 640

pygame.init()

def Memorise(round_num=1,rand='*cH1;@'):
  #Setup
  pygame.display.set_caption('Memory')
  window_surface = pygame.display.set_mode((WIDTH, HEIGHT))

  background = pygame.Surface((WIDTH, HEIGHT))
  background.fill(pygame.Color('#5E6059'))

  manager = pygame_gui.UIManager((WIDTH, HEIGHT), 'theme.json')
  manager.add_font_paths('Mono', 'RobotoMono-Regular.ttf')
  
  clock = pygame.time.Clock()

  #dictionary for objects
  objects = {}

  #create my objects
  objects['home_button'] = home_btn(manager)
  objects['help_button'] = help_btn(manager)

  objects['round_num']=lbl(relative_rect = pygame.Rect((275, 73), (101, 28)),
                          text = 'Round '+str(round_num),
                          manager = manager,
                          object_id='small')
  objects['heading'] = lbl(relative_rect = pygame.Rect((147, 107), (346, 75)),
                          text = 'Memorise!',
                          manager = manager)
  #create the characters to display 'rand'
  objects['characters']=[]
  positions=[((119,193),(48,100)),((190,193),(48,100)),((261,193),(48,100)),((332,193),(48,100)),((403,193),(48,100)),((474,193),(48,100))]
  for p,c in enumerate(rand):
    objects['characters'].append(lbl(relative_rect = pygame.Rect(positions[p][0],positions[p][1]),
                          text = c,
                          manager = manager,
                          object_id='character_display'))

  objects['round_num']=lbl(relative_rect = pygame.Rect((219, 379), (202, 28)),
                          text = '# seconds left',
                          manager = manager,
                          object_id='small')

  #main loop
  end = False
  timer=-0.017
  while not end:
    time_delta = clock.tick(60) / 1000.0
    timer+=0.017
    #time the memorising
    if timer>=6:
      return 'cont'
    for event in pygame.event.get(): 
      #Check if the x was pressed
      if event.type == pygame.QUIT:
        pygame.quit()

      #check if one of my buttons was pressed
      elif event.type == pygame.USEREVENT:
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
          if event.ui_element == objects['home_button']:
            return 'home'
          if event.ui_element == objects['help_button']:
            return 'help'
      
      
      manager.process_events(event)
    
    #display the time left
    orig=objects['round_num'].text.split(' ',1)
    orig[0]=str(floor(6-timer))
    objects['round_num'].set_text(' '.join(orig))
    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()

if __name__ == '__main__':
  Memorise()