#Main
import pygame
import pygame_gui

from pygame_gui.elements import UIButton as btn

HEIGHT=480
WIDTH=640

pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((640, 480))

background = pygame.Surface((640, 480))
background.fill(pygame.Color('#5E6059'))

manager = pygame_gui.UIManager((640, 480),'theme.json')





end=False
while not end:
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      end=True

    if event.type == pygame.USEREVENT:
      if event.user_type == pygame_gui.UI_BUTTON_PRESSED: