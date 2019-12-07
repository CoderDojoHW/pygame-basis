import pygame
import sys
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))

done = False

# laad de twee images
bg = pygame.image.load("achtergrond.jpg").convert()
kop = pygame.image.load("lkop.png").convert_alpha()
# mouse pointer onzichtbaar maken
pygame.mouse.set_visible(0)
# bepaal de grootte van de kop
kopx,kopy = (kop.get_rect().size)
pygame.display.set_caption('test')
x1 = 0
left = 1

while not done:
  # teken de achtergrond
  screen.blit(bg, (0,0))
  # bepaal de muis positie
  x,y = pygame.mouse.get_pos()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

  # bepaal de grens het speelveld
  if x >= 800+(kopx/2):
    x = 800+(kopx/2)
  if y >= 600+(kopy/2):
     y = 600+(kopy/2)

  # laat de kop naar links of rechts kijken
  if x1 > x and left == 0:
    kop = pygame.transform.flip(kop,True,False)
    left = 1
  if x1 < x and left == 1:
    kop = pygame.transform.flip(kop,True,False)
    left = 0

  # schrijf de kop op de achtergrond
  x1 = x
  screen.blit(kop, (x-(kopx/2),y-(kopy/2)))

  pygame.display.update()
  clock.tick(30)

pygame.quit()
sys.exit(0)