#test
#Main
import pygame
import pygame_gui

from pygame_gui.elements import UIButton as btn

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

  test_btn_dims=(200,100)
  test_btn=btn(relative_rect = pygame.Rect((WIDTH // 2 - test_btn_dims[0] // 2 , HEIGHT // 2 - test_btn_dims[1] // 2) , test_btn_dims),
                text = 'Test',
                manager=manager)

  end=False
  while not end:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get(): 
      if event.type==pygame.QUIT:
        end=True


      manager.process_events(event)

    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()

main()