#Home
#imports
import pygame
import pygame_gui

from pygame_gui.elements import UIButton as btn
from pygame_gui.elements.ui_label import UILabel as lbl
from pygame_gui.elements.ui_text_box import UITextBox as txt
#home and help button
from home_and_help import  home_btn,help_btn

HEIGHT = 480
WIDTH = 640

pygame.init()

def Help():
  #get the text for the help page
  help_text=open('help_text.txt','r').read()

  #set up window
  pygame.display.set_caption('Help')
  window_surface = pygame.display.set_mode((WIDTH, HEIGHT))

  background = pygame.Surface((WIDTH, HEIGHT))
  background.fill(pygame.Color('#5E6059'))

  manager = pygame_gui.UIManager((WIDTH, HEIGHT), 'theme.json')
  manager.add_font_paths('Mono', 'RobotoMono-Regular.ttf')
  
  clock = pygame.time.Clock()

  #dictionary of my opbjects
  objects = {}
  #create object
  objects['home_button'] = home_btn(manager)

  objects['heading'] = lbl(relative_rect = pygame.Rect((243, 58), (154, 75)),
                          text = 'Help',
                          manager = manager)

  objects['help_text'] = txt(relative_rect = pygame.Rect((27, 172), (585, 260)),
                          html_text = help_text,
                          manager = manager)

  #main loop
  end = False
  while not end:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get(): 
      #check if the x was pressed
      if event.type == pygame.QUIT:
        pygame.quit()

      #check if the home button was pressed
      elif event.type == pygame.USEREVENT:
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
          if event.ui_element == objects['home_button']:
            return 'home'
          



      manager.process_events(event)
    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()

if __name__ == '__main__':
  Help()
