#Home
import pygame
import pygame_gui

from home_and_help import  home_btn,help_btn
from pygame_gui.elements import UIButton as btn
from pygame_gui.elements.ui_label import UILabel as lbl

HEIGHT = 480
WIDTH = 640

pygame.init()

def main():
  pygame.display.set_caption('Test')
  window_surface = pygame.display.set_mode((WIDTH, HEIGHT))

  background = pygame.Surface((WIDTH, HEIGHT))
  background.fill(pygame.Color('#5E6059'))

  manager = pygame_gui.UIManager((WIDTH, HEIGHT), 'theme.json')
  manager.add_font_paths('Mono', 'mono.ttf')
  
  clock = pygame.time.Clock()

  objects = {}

  objects['home_button'] = home_btn(manager)

  objects['heading'] = lbl(relative_rect = pygame.Rect((243, 58), (154, 75)),
                          text = 'Help',
                          manager = manager)

  objects['help_text'] = lbl(relative_rect = pygame.Rect((27, 172), (585, 260)),
                          text = 'Start',
                          manager = manager,
                          object_id='help_text')

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
          elif event.ui_element == objects['start_button']:
            print('start')
            return 'start'



      manager.process_events(event)
    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()

main()