#Main
import pygame
import pygame_gui
import Home,Help,Game

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
dest='home'
while not end:
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      end=True
  
  if dest == 'home':
    dest = Home.Home()
    if dest == 'quit':
      break
  if dest == 'help':
    dest = Help.Help()
    if dest == 'quit':
      break
  if dest == 'start':
    dest = Game.Game()
    if dest == 'quit':
      break
  if dest != 'home' and dest != 'help':
    break
pygame.quit()