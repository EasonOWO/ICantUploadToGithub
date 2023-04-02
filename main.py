import sys
import pygame
import numpy as np
import math
import keyboard
import color
import player

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

    def move_input(self, keys):
        aclx = 0
        acly = 0
        if keys[self.go_left] and self.x > 0:
            aclx = -acl
    
        if keys[self.go_right] and self.x < 500:
            aclx = acl
    
        if keys[self.go_up] and self.y > 0:
            acly = -acl
    
        if keys[self.go_down] and self.y < 500:
            acly = acl
    
        if (aclx**2 + acly**2 > acl * acl):#單位向量
            aclx *= abs(acl / (math.sqrt(aclx**2 + acly**2)))
            acly *= abs(acl / (math.sqrt(aclx**2 + acly**2)))
        return aclx, acly
    
    def move_output(self, keys):
        aclx, acly = player.move_input(self, keys)
        self.velx += aclx
        self.vely += acly
        if self.velx != 0:
            if self.velx > 0:
                self.velx -= backacl
            else:
                self.velx += backacl
        
        if self.vely != 0:
            if self.vely > 0:
                self.vely -= backacl
            else:
                self.vely += backacl
        
        if (self.velx**2 + self.vely**2 > maxv**2):
            self.velx *= abs(maxv / (math.sqrt(self.velx**2 + self.vely**2)))
            self.vely *= abs(maxv / (math.sqrt(self.velx**2 + self.vely**2)))
        self.x += self.velx
        self.y += self.vely
        return (self.x, self.y)
###########################################################
player1 = player(0, 0, 0, 0, keyboard.UP, keyboard.DOWN, keyboard.LEFT, keyboard.RIGHT)
player2 = player(0, 0, 0, 0, keyboard.w, keyboard.s, keyboard.a, keyboard.d)
###########################################################

#settings
winScreen = pygame.display.set_mode((S_W, S_H))
pygame.display.set_caption("Keyboard Demo")
canvas = pygame.Surface(winScreen.get_size()).convert()
uiscreen = pygame.Surface((500, 50)).convert()
background = pygame.Surface(winScreen.get_size()).convert()


#count the score
def color_counting(cv):
    area_value = pygame.surfarray.pixels2d(cv)
    red_ar = int(0)
    blue_ar = int(0)
    print(area_value)
    for i in range(100):
        for j in range(100):
            if area_value[i*5][j*5] == 16777215:
              red_ar += 1
            if area_value[i*5][j*5]==16711680:
              blue_ar+=1

    return red_ar, blue_ar

counting_time=int(0)
frame_count=int(0)
R = 20  #the r of circle

maxv = int(2)
red_score, b_score =int(0),int(0)
acl = 0.2
backacl = 0.05
time = 0  #time of game
run = True  #run the game or not
dfont = pygame.font.SysFont("Arial", 30)
########################RUN##############################
while run:
    if frame_count==0:
        background.fill(color.white)
        canvas.fill(color.white)
    counting_time += 1
    frame_count+=1
    pygame.time.Clock()
    pygame.time.delay(10)
    uiscreen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #move
    
    keyInput=pygame.key.get_pressed()
    player1.x, player1.y = player1.move_output(keyInput)
    player2.x, player2.y = player2.move_output(keyInput)
    
    #ColorCount
    if frame_count%500==0:
        red_score, b_score = color_counting(canvas)
        counting_time = int(0)
    if(keyInput[pygame.K_SPACE]):
      print((b_score))
      print(f"{type(red_score)}")
    #Paint
    pygame.draw.circle(canvas, color.blue, (player1.x, player1.y), R, R - 1)
    pygame.draw.circle(canvas, color.red, (player2.x, player2.y), R, R - 1)
    #?
    b_point = int(0)

    #UI
    message = dfont.render('{0},{1},{2},{3}'.format(int(player1.x), int(player1.y),(red_score/100),(b_score/100)), 1, color.cyan)
    #text of location
    uiscreen.blit(message, (0, 0))

    if frame_count%500!=0:
      winScreen.blit(canvas, (0, 0))
    winScreen.blit(uiscreen, (0, 0))
     
    #winScreen.blit(michan, (x, y))

    pygame.display.update()
pygame.quit()
sys.exit()
##MICHAN DAISUKI