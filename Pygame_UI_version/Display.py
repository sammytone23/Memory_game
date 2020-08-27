#display
import pygame
import pygame_gui

from home_and_help import  home_btn,help_btn
from pygame_gui.elements import UIButton as btn
from pygame_gui.elements.ui_label import UILabel as lbl

HEIGHT = 480
WIDTH = 640

pygame.init()

def high_score(score):
  hs=open('high_score.txt','r').read()
  f=open('high_score.txt','w')
  if score>int(hs):
    f.write(score)
    f.close()
    return score
  else:
    f.write(hs)
    f.close()
    return hs




def Display(score):
  pygame.display.set_caption('Home')
  window_surface = pygame.display.set_mode((WIDTH, HEIGHT))

  background = pygame.Surface((WIDTH, HEIGHT))
  background.fill(pygame.Color('#5E6059'))

  manager = pygame_gui.UIManager((WIDTH, HEIGHT), 'theme.json')
  manager.add_font_paths('Mono', 'RobotoMono-Regular.ttf')
  
  clock = pygame.time.Clock()

  objects = {}

  objects['help_button'] = help_btn(manager)
  objects['home_button'] = home_btn(manager)

  objects['score'] = lbl(relative_rect = pygame.Rect((74, 98), (491, 56)),
                          text = 'Your score was: '+str(score),
                          manager = manager,
                          object_id='med')

  objects['high_score'] = lbl(relative_rect = pygame.Rect((219, 169), (202, 28)),
                          text = 'High score: '+high_score(score),
                          manager = manager,
                          object_id='small')

  objects['cong']= lbl(relative_rect = pygame.Rect((190, 212), (260, 56)),
                          text = 'Good job!',
                          manager = manager,
                          object_id='med')

  objects['start_button'] = btn(relative_rect = pygame.Rect((162, 326), (315, 48)),
                          text = 'Play again?',
                          manager = manager,
                          object_id='big_button')
  
  end = False
  while not end:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get(): 
      if event.type == pygame.QUIT:
        print('quit')
        pygame.quit()

      elif event.type == pygame.USEREVENT:
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
          if event.ui_element == objects['help_button']:
            print('help')
            return 'help'
          elif event.ui_element == objects['home_button']:
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

if __name__ == '__main__':
  Display(0)