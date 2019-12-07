import pygame, sys

pygame.init()
screen = pygame.display.set_mode((800,600))

done = False
is_groen = True

wit = (255,255,255)
zwart = (0,0,0)
rood = (255,0,0)
groen = (0,255,0)
blauw = (0,0,25)

x = 30
y = 30

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
      is_groen = not is_groen
  
  toets = pygame.key.get_pressed()
  if toets[pygame.K_UP]:
    y -= 3
  if toets[pygame.K_DOWN]:
    y += 3
  if toets[pygame.K_LEFT]:
    x -= 3
  if toets[pygame.K_RIGHT]:
    x +=3
  
  if is_groen:
    kleur = groen
  else:
    kleur = rood
  
  pygame.draw.rect(screen, kleur, pygame.Rect (x,y,50,45))

  pygame.display.update()

pygame.quit()
sys.exit(0)