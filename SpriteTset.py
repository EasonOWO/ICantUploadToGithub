import sys
import pygame
import numpy as np
import math
import os
import keyboard
import color
import player

# 遊戲初始化 & 創建視窗
pygame.init()
pygame.display.set_caption("GameTest")

# the width and height of screen
screen_size = S_W, S_H = (500, 500)
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
Radius = 20
RIGHT_TOP = (0, 0)
MIDDLE = (S_W // 2, S_H // 2)

screen = pygame.display.set_mode(screen_size)
canvas = pygame.Surface(screen.get_size()).convert()
uiscreen = pygame.Surface((500, 50)).convert()
background = pygame.Surface(screen.get_size()).convert()

michan = pygame.image.load(os.path.join('img', 'michan 500x500.jpg')).convert()
arrow = pygame.image.load(os.path.join('img', 'arrow.png')).convert()
#background = michan
clock = pygame.time.Clock()


class Player1(pygame.sprite.Sprite):
    acl = 0.2
    backacl = 0.05
    maxv = 2.0

    def __init__(self, x, y, velx, vely, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(MIDDLE)

        self.x1 = x
        self.y1 = y
        self.velx1 = velx
        self.vely1 = vely
        self.color1 = color

        self.image.fill(BLUE)
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()

    def move_output(self):
        key_pressed = pygame.key.get_pressed()
        aclx = 0
        acly = 0
        if key_pressed[pygame.K_LEFT] and self.x1 > 0:
            aclx = -acl

        if key_pressed[pygame.K_RIGHT] and self.x1 < 500:
            aclx = acl

        if key_pressed[pygame.K_UP] and self.y1 > 0:
            acly = -acl

        if key_pressed[pygame.K_DOWN] and self.y1 < 500:
            acly = acl

        if aclx ** 2 + acly ** 2 > acl * acl:  # 單位向量
            aclx *= abs(acl / (math.sqrt(aclx ** 2 + acly ** 2)))
            acly *= abs(acl / (math.sqrt(aclx ** 2 + acly ** 2)))

        self.rect.x += self.velx1
        self.rect.y += self.vely1
        return aclx, acly

    def move_input(self):
        aclx, acly = Player2.move_output(self, key_pressed)
        self.velx1 += aclx
        self.vely1 += acly

        if self.velx1 != 0:
            if self.velx1 > 0:
                self.velx1 -= backacl
            else:
                self.velx1 += backacl

        if self.vely1 != 0:
            if self.vely1 > 0:
                self.vely1 -= backacl
            else:
                self.vely1 += backacl

        if (self.velx1 ** 2 + self.vely1 ** 2 > maxv ** 2):
            self.velx1 *= abs(maxv / (math.sqrt(self.velx1 ** 2 + self.vely1 ** 2)))
            self.vely1 *= abs(maxv / (math.sqrt(self.velx1 ** 2 + self.vely1 ** 2)))
        self.x1 += self.velx1
        self.y1 += self.vely1
        return (self.x1, self.y1)


class Player2(pygame.sprite.Sprite):
    acl = 0.2
    backacl = 0.05
    maxv = 2.0

    def __init__(self,x, y, velx, vely, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(MIDDLE)

        self.x2 = x
        self.y2= y
        self.velx2 = velx
        self.vely2 = vely
        self.color2 = color

        self.image.fill(BLUE)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

        self.rect = self.image.get_rect()

    def move_input(self):
        key_pressed = pygame.key.get_pressed()
        aclx = 0
        acly = 0
        if key_pressed[pygame.K_a] and self.x2 > 0:
            aclx = -acl

        if key_pressed[pygame.K_d] and self.x2 < 500:
            aclx = acl

        if key_pressed[pygame.K_w] and self.y2 > 0:
            acly = -acl

        if key_pressed[pygame.K_s] and self.y2 < 500:
            acly = acl

        if aclx ** 2 + acly ** 2 > acl * acl:  # 單位向量
            aclx *= abs(acl / (math.sqrt(aclx ** 2 + acly ** 2)))
            acly *= abs(acl / (math.sqrt(aclx ** 2 + acly ** 2)))

        self.x2 += self.velx2
        self.y2 += self.vely2
        return aclx, acly

    def move_output(self, keys):
        aclx, acly = Player2.move_input(self, key_pressed)
        self.velx2 += aclx
        self.vely2 += acly
        if self.velx2 != 0:
            if self.velx2 > 0:
                self.velx2 -= backacl
            else:
                self.velx2 += backacl

        if self.vely2 != 0:
            if self.vely2 > 0:
                self.vely2 -= backacl
            else:
                self.vely2 += backacl

        if self.velx2 ** 2 + self.vely2 ** 2 > maxv ** 2:
            self.velx2 *= abs(maxv / (math.sqrt(self.velx2 ** 2 + self.vely2 ** 2)))
            self.vely2 *= abs(maxv / (math.sqrt(self.velx2 ** 2 + self.vely2 ** 2)))
        self.x2 += self.velx2
        self.y2 += self.vely2
        return self.x2, self.y2


###########################################################

###########################################################
player1 = Player1(0, 0, 0, 0,  color.blue)
player2 = Player2(0, 0, 0, 0,  color.red)
###########################################################


# count the score
def color_counting(cv):
    red_area_intcode = 16777215
    blue_area_intcode = 16711680
    area_value = pygame.surfarray.pixels2d(cv)
    red_ar = int(0)
    blue_ar = int(0)
    print(area_value)
    for i in range(100):
        for j in range(100):
            if area_value[i * 5][j * 5] == red_area_intcode:
                red_ar += 1
            if area_value[i * 5][j * 5] == blue_area_intcode:
                blue_ar += 1

    return red_ar, blue_ar


# -----------------------------------------------------------------------------------
all_sprites = pygame.sprite.Group()

counting_time = int(0)
frame_count = int(0)
R = 20  # the r of circle
x = int(S_W / 2)  # position x
y = int(S_H / 2)  # position y
velx = int(0)
vely = int(0)
maxv = int(2)
red_score, b_score = int(0), int(0)
acl = 0.2
backacl = 0.05
time = 0  # time of game
dfont = pygame.font.SysFont("Arial", 30)
running = True

# 遊戲迴圈
while running:
    counting_time += 1
    frame_count += 1
    pygame.time.Clock()
    pygame.time.delay(10)
    uiscreen.blit(background, (0, 0))
    key_pressed = pygame.key.get_pressed()

    clock.tick(FPS)
    if frame_count==0:
        background.fill(color.white)
    # 取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新遊戲
    all_sprites.update()
    pygame.draw.circle(michan, BLUE, (player1.x1,player1.y1), Radius)
    pygame.draw.circle(michan, RED, (player2.x2,player2.y2), Radius)

    # ColorCount
    if frame_count % 500 == 0:
        red_score, b_score = color_counting(canvas)
        counting_time = int(0)
    if (key_pressed[pygame.K_SPACE]):
        print((b_score))
        print(f"{type(red_score)}")

    # 畫面顯示
    '''
    # UI
    p1_location_font = dfont.render(
        'blue_loc : {0}, {1}'.format(int(Player1.x1), int(Player1.y1)), 1, color.cyan)
    p2_location_font = dfont.render(
        'red_loc : {0}, {1}'.format(int(Player2.x2), int(Player2.y2)), 1, color.cyan)
                               
    message = dfont.render('{0},{1},{2},{3}'.format(int(player1.x), int(player1.y),(red_score/100),(b_score/100)), 1, color.cyan)
    '''

    # text of location
    '''uiscreen.blit(message, (0, 0))
    uiscreen.blit(p1_location_font, (0, 0))
    uiscreen.blit(p2_location_font, (275, 0))
    '''

    if frame_count % 500 != 0:
        screen.blit(background, (0, 0))
    screen.blit(uiscreen, (0, 0))

    pygame.display.flip()
    pygame.display.update()

pygame.quit()
sys.exit()
