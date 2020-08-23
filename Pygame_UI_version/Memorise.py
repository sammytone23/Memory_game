#Memorise

import pygame
import pygame_gui

from home_and_help import  home_btn,help_btn
from pygame_gui.elements import UIButton as btn
from pygame_gui.elements.ui_label import UILabel as lbl

HEIGHT = 480
WIDTH = 640

pygame.init()

def main(round_num=1):
  pygame.display.set_caption('Memorise')
  window_surface = pygame.display.set_mode((WIDTH, HEIGHT))

  background = pygame.Surface((WIDTH, HEIGHT))
  background.fill(pygame.Color('#5E6059'))

  manager = pygame_gui.UIManager((WIDTH, HEIGHT), 'theme.json')
  manager.add_font_paths('Mono', 'RobotoMono-Regular.ttf')
  
  clock = pygame.time.Clock()

  objects = {}

  objects['home_btn'] = home_btn(manager)
  objects['help_button'] = help_btn(manager)

  objects['round_num']=lbl(relative_rect = pygame.Rect((275, 73), (101, 28)),
                          text = 'Round '+str(round_num),
                          manager = manager,
                          object_id=('small','round_num'))
  objects['heading'] = lbl(relative_rect = pygame.Rect((147, 107), (346, 75)),
                          text = 'Memorise!',
                          manager = manager)
  
  end = False
  while not end:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get(): 
      if event.type == pygame.QUIT:
        print('quit')
        return 'quit'

      elif event.type == pygame.USEREVENT:
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
          if event.ui_element == objects['home_button']:
            print('home')
            return 'home'
          if event.ui_element == objects['help_button']:
            print('help')
            return 'help'
          
      manager.process_events(event)
    
    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()

if __name__ == '__main__':
  main()