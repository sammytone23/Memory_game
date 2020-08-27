#Home
#Imports
import pygame
import pygame_gui

from pygame_gui.elements import UIButton as btn
from pygame_gui.elements.ui_label import UILabel as lbl
from pygame_gui.elements.ui_horizontal_slider import UIHorizontalSlider as sld
#My help and home button
from home_and_help import  home_btn,help_btn

#Dimensions
HEIGHT = 480
WIDTH = 640

pygame.init()

def Home():
  #Set up the window
  pygame.display.set_caption('Home')
  window_surface = pygame.display.set_mode((WIDTH, HEIGHT))

  background = pygame.Surface((WIDTH, HEIGHT))
  background.fill(pygame.Color('#5E6059'))

  manager = pygame_gui.UIManager((WIDTH, HEIGHT), 'theme.json')
  manager.add_font_paths('Mono', 'RobotoMono-Regular.ttf')
  
  clock = pygame.time.Clock()


  #create the dictionary to store what's being shown
  objects = {}

  #create the objects
  objects['help_button'] = help_btn(manager)

  objects['heading'] = lbl(relative_rect = pygame.Rect((204, 91), (231, 75)),
                          text = 'Memory',
                          manager = manager)

  objects['start_button'] = btn(relative_rect = pygame.Rect((246, 299), (149, 48)),
                          text = 'Start',
                          manager = manager,
                          object_id='big_button')
  objects['diff_label'] = lbl(relative_rect = pygame.Rect((283,389),(73,14)),
                                text = 'Difficulty',
                                manager=manager,
                                object_id='tiny')
  objects['eas_label'] = lbl(relative_rect = pygame.Rect((241,412),(29,14)),
                                text = 'Easy',
                                manager=manager,
                                object_id='tiny')
  objects['har_label'] = lbl(relative_rect = pygame.Rect((370,412),(29,14)),
                                text = 'Hard',
                                manager=manager,
                                object_id='tiny')
  objects['diff_sld']= sld(relative_rect=pygame.Rect((270,410),(100,16)),
                            start_value=10,
                            value_range=(20,2),
                            manager=manager,
                            object_id='sld')

  #main loop
  end = False
  while not end:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get(): 
      #check if the x is pressed
      if event.type == pygame.QUIT:
        pygame.quit()
      #check if any of my buttons have been pressed
      elif event.type == pygame.USEREVENT:
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
          if event.ui_element == objects['help_button']:
            return 'help'
          elif event.ui_element == objects['start_button']:
            return ['start',int(objects['diff_sld'].get_current_value())]
      manager.process_events(event)
    
    #draw to screen
    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()

if __name__ == '__main__':
  Home()
#main()