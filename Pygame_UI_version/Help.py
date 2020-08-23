#Home
import pygame
import pygame_gui

from home_and_help import  home_btn,help_btn
from pygame_gui.elements import UIButton as btn
from pygame_gui.elements.ui_label import UILabel as lbl
from pygame_gui.elements.ui_text_box import UITextBox as txt

HEIGHT = 480
WIDTH = 640

pygame.init()

def main():

  help_text='''1. Lorem ipsum dolor sit amet, consectetur adipiscing elit.<br>
2. Maecenas at quam nec nisi tempor malesuada sit amet eu justo.<br>
3. Duis in enim vel lorem tincidunt luctus.<br>
4. Maecenas quis urna vel lacus blandit maximus vel ut elit. <br>
5. Suspendisse ornare quam non tempor feugiat.<br>
6. Nullam ac enim at orci vestibulum venenatis sed maximus augue.<br>
7. Aenean lobortis velit sed gravida tempus.<br>
<br>
8. Cras a orci a leo blandit egestas nec eu ligula.<br>
9. Integer et turpis dapibus, eleifend sem ultricies, congue urna.<br>
10. Ut consequat massa nec erat molestie auctor.<br>
11. Sed egestas urna eget dapibus tristique.'''

  pygame.display.set_caption('Help')
  window_surface = pygame.display.set_mode((WIDTH, HEIGHT))

  background = pygame.Surface((WIDTH, HEIGHT))
  background.fill(pygame.Color('#5E6059'))

  manager = pygame_gui.UIManager((WIDTH, HEIGHT), 'theme.json')
  manager.add_font_paths('Mono', 'RobotoMono-Regular.ttf')
  
  clock = pygame.time.Clock()

  objects = {}

  objects['home_button'] = home_btn(manager)

  objects['heading'] = lbl(relative_rect = pygame.Rect((243, 58), (154, 75)),
                          text = 'Help',
                          manager = manager)

  objects['help_text'] = txt(relative_rect = pygame.Rect((27, 172), (585, 260)),
                          html_text = help_text,
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
          elif event.ui_element == objects['start_button']:
            print('start')
            return 'start'



      manager.process_events(event)
    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()

if __name__ == '__main__':
  main()
