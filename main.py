import sys
import pygame
import numpy as np
import math
import classes

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

#########################################################player
class player:
    def __init__(self, x, y, velx, vely, go_up, go_down, go_left, go_right):
        self.x = x
        self.y = y
        self.velx = velx
        self.vely = vely
        self.go_up = go_up
        self.go_down = go_down
        self.go_left = go_left
        self.go_right = go_right
    def move_input(keys):
        aclx = 0
        acly = 0
        if keys[self.go_left] and x > 0:
            aclx = -acl
    
        if keys[self.go_right] and x < 500:
            aclx = acl
    
        if keys[self.go_up] and y > 0:
            acly = -acl
    
        if keys[pygame.go_down] and y < 500:
            acly = acl
    
        if (aclx**2 + acly**2 > acl * acl):#單位向量
            aclx *= abs(acl / (math.sqrt(aclx**2 + acly**2)))
            acly *= abs(acl / (math.sqrt(aclx**2 + acly**2)))
        return aclx, acly
    #def move_position():
        

########################################################################        
player1 = player(0, 0, 0, 0, classes.UP, classes.DOWN, classes.LEFT, classes.RIGHT)
player2 = player(0, 0, 0, 0, classes.w, classes.s, classes.a, classes.d)
##############################################################################
#move
def move_input(keys):
    aclx = 0
    acly = 0
    if keys[1073741904] and x > 0:#[1073741904]
        aclx = -acl

    if keys[1073741903] and x < 500:#[1073741903]
        aclx = acl

    if keys[pygame.K_UP] and y > 0:#[1073741906]
        acly = -acl

    if keys[pygame.K_DOWN] and y < 500:#[1073741905]
        acly = acl

    if (aclx**2 + acly**2 > acl * acl):#單位向量
        aclx *= abs(acl / (math.sqrt(aclx**2 + acly**2)))
        acly *= abs(acl / (math.sqrt(aclx**2 + acly**2)))
    return aclx, acly

#settings
winScreen = pygame.display.set_mode((S_W, S_H))
pygame.display.set_caption("Keyboard Demo")
canvas = pygame.Surface(winScreen.get_size()).convert()
uiscreen = pygame.Surface((500, 50)).convert()
background = pygame.Surface(winScreen.get_size()).convert()


#count the score
def color_counting(cv):
  area_value=pygame.surfarray.array2d(cv)
  red_ar=int(0)
  blue_ar=int(0)
  for i in range(500):
    for j in range(500):
      if area_value[i][j]==16776960:
        red_ar+=1
      
  return red_ar,blue_ar

counting_time=int(0)
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
    counting_time+=1
    pygame.time.Clock()
    pygame.time.delay(10)
    uiscreen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #move
    
    keyInput=pygame.key.get_pressed()
    aclx, acly = move_input(keyInput)
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
    #prevent from going out
    '''
    if(x>500 or x<0):
        #x -= velx
        #velx=-velx
        #x=500-x
    
    if(y>500 or y<0):
        #y -= vely
        #vely=-vely
        #y=500-y
    '''
    #ColorCount
    if counting_time>500:
      red_score,b_score=color_counting(canvas)
      counting_time=int(0)
    if(keyInput[pygame.K_SPACE]):
      print((red_score))
      print(f"{type(red_score)}  and  {type(classes.a)}")
    #Paint
    pygame.draw.circle(canvas, color.yellow, (x, y), R, R - 1)

    #?
    b_point = int(0)

    #UI
    message = dfont.render('{0},{1}'.format(int(x), int(y)), 1, color.cyan)  
    #text of location
    uiscreen.blit(message, (0, 0))

    winScreen.blit(canvas, (0, 0))
    winScreen.blit(uiscreen, (0, 0))
     
    #winScreen.blit(michan, (x, y))

    pygame.display.update()
pygame.quit()
sys.exit()
##MICHAN DAISUKI