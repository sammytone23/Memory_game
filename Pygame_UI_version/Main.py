#Main
difficulty = int(input('difficulty 2-20: '))

#Imports
import pygame
import pygame_gui
from pygame_gui.elements import UIButton as btn

#Import my pages
import Home,Help,Game

# Set Dimentions
HEIGHT=480
WIDTH=640

#Set up the window.
pygame.init()

pygame.display.set_caption('Memory')
window_surface = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.Surface((WIDTH, HEIGHT))
background.fill(pygame.Color('#5E6059'))

manager = pygame_gui.UIManager((WIDTH, HEIGHT),'theme.json')

#Main loop 
end=False
dest='home'
while not end:
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      end=True
  #Run the right screen
  if dest == 'home':
    dest = Home.Home()
    if dest == 'quit':
      break
  if dest == 'help':
    dest = Help.Help()
    if dest == 'quit':
      break
  if dest == 'start':
    dest = Game.Game(difficulty)
    if dest == 'quit':
      break
  if dest != 'home' and dest != 'help':
    break

#Kill the window
pygame.quit()