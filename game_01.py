import pygame, sys

pygame.init()
screen = pygame.display.set_mode((800,600))

done = False

wit = (255,255,255)
zwart = (0,0,0)
rood = (255,0,0)
groen = (0,255,0)
blauw = (0,0,255)

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
  
  pygame.draw.rect(screen, (groen), pygame.Rect(30,30,50,45))

  pygame.display.update()

pygame.quit()
sys.exit(0)