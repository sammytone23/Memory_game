#Home
import pygame
import pygame_gui


from home_and_help import  home_btn,help_btn
from pygame_gui.elements import UIButton as btn
from pygame_gui.elements.ui_label import UILabel as lbl

HEIGHT=480
WIDTH=640

pygame.init()

def main():
  pygame.display.set_caption('Test')
  window_surface = pygame.display.set_mode((WIDTH, HEIGHT))

  background = pygame.Surface((WIDTH, HEIGHT))
  background.fill(pygame.Color('#5E6059'))

  manager = pygame_gui.UIManager((WIDTH, HEIGHT), 'theme.json')
  manager.add_font_paths('Mono','mono.ttf')
  
  clock = pygame.time.Clock()

  objects={}

  objects['help_button']=help_btn(manager)

  objects['Heading']=lbl(relative_rect=pygame.Rect((204,91),(231,75)),
                          text='Memory',
                          manager=manager)
  

  end=False
  while not end:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get(): 
      if event.type==pygame.QUIT:
        print('quit')
        return 'quit'

      if event.type == pygame.USEREVENT:
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
          if event.ui_element == objects['help_button']:
            print('help')
            return 'help'


      manager.process_events(event)
    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()

main()