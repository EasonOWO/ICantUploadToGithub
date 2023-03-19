import sys
import pygame
import numpy
import math

#the start of pygame
pygame.init()

#the width and height of screen
S_W = 500
S_H = 500
'''
#咪醬
michan = pygame.image.load('Picture/channels4_profile.jpg')
'''
#michan.convert()


#usage: color.<the_color_you_want>
class color:
  red = (255, 0, 0)
  green = (0, 255, 0)
  blue = (0, 0, 255)
  yellow = (255, 255, 0)
  cyan = (0, 255, 255)
  magenta = (255, 0, 255)
  white = (255, 255, 255)
  black = (0, 0, 0)


#move
def move_input(keys):
  aclx = 0
  acly = 0
  if keys[pygame.K_LEFT] and x > 0:
    aclx = -acl

  if keys[pygame.K_RIGHT] and x < 500:
    aclx = acl

  if keys[pygame.K_UP] and y > 0:
    acly = -acl

  if keys[pygame.K_DOWN] and y < 500:
    acly = acl
  return aclx, acly


#settings
winScreen = pygame.display.set_mode((S_W, S_H))
pygame.display.set_caption("Keyboard Demo")
canvas = pygame.Surface(winScreen.get_size()).convert()
uiscreen = pygame.Surface((500, 50)).convert()
background = pygame.Surface(winScreen.get_size()).convert()


#get the color of certain pixle
def getcolor(x, y):
  pixleColor = pygame.Surface.get_at((x, y))
  return pixleColor


#count the score
def countScore(color_of_the_team):
  Territory = 0
  for i in range(500):
    for j in range(500):
      color = getcolor(i, j)
      if (color == color_of_the_team):
        Territory += 1
  return Territory


R = 20  #the r of circle
x = int((S_W) / 2)  #position x
y = int((S_H) / 2)  #position y
velx = int(0)
vely = int(0)
maxv = int(2)
acl = 0.2
backacl = 0.05
time = 0  #time of game
run = True  #run the game or not
dfont = pygame.font.SysFont("Arial", 30)

while run:
  pygame.time.delay(10)
  uiscreen.blit(background, (0, 0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  #move
  aclx, acly = move_input(pygame.key.get_pressed())

  if (aclx * aclx + acly * acly > acl * acl):
    aclx = aclx * abs(acl / (math.sqrt(aclx * aclx + acly * acly)))
    acly = acly * abs(acl / (math.sqrt(aclx**2 + acly**2)))
  velx += aclx
  vely += acly
  if velx != 0:
    if velx > 0:
      velx -= backacl
    else:
      velx += backacl
  if vely != 0:
    if vely > 0:
      vely -= backacl
    else:
      vely += backacl
  if (velx**2 + vely**2 > maxv**2):
    velx = velx * abs(maxv / (math.sqrt(velx**2 + vely**2)))
    vely = vely * abs(maxv / (math.sqrt(velx**2 + vely**2)))
  x += velx
  y += vely

  #paint
  pygame.draw.circle(canvas, color.yellow, (x, y), R, R - 1)

  #?
  b_point = int(0)

  #UI
  message = dfont.render('{0},{1}'.format(int(x - 250), int(-y + 250)), 1, color.cyan)  #text of location
  uiscreen.blit(message, (0, 0))
  winScreen.blit(canvas, (0, 0))
  winScreen.blit(uiscreen, (0, 0))

  #winScreen.blit(michan, (x, y))

  pygame.display.update()
pygame.quit()
sys.exit()
##MICHAN DAISUKI