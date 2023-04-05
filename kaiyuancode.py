import sys
import pygame
import math
import os
import keyboard
import color

# 各種變數
screen_size = S_W, S_H = (500, 600)
FPS = 60
Radius = 40
RIGHT_TOP = (0, 0)
RIGHT_BOTTOM = (0, 500)
MIDDLE = (S_W // 2, S_H // 2)
BLACK = (0, 0, 0)

# 遊戲初始化 & 創建視窗
pygame.init()
pygame.display.set_caption("GameTest")
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
dfont = pygame.font.SysFont("Arial", 30)
dtopic = pygame.font.SysFont("Arial",46)

# 背景圖片讀取
background = pygame.Surface((500,500)).convert()
babackground = pygame.Surface((500,100)).convert()


class Player1(pygame.sprite.Sprite):
    # Sprite初始化、變數設定
    def __init__(self, x, y, velx, vely, color):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.velx = velx
        self.vely = vely
        self.color = color

        self.acl = int(0.2)
        self.backacl = int(0.05)
        self.maxv = int(2.0)
        self.aclx = int(0)
        self.acly = int(0)

    # Sprite刷新
    def update(self):
        key_pressed = pygame.key.get_pressed()
        self.aclx = int(0)
        self.acly = int(0)

        # 移動設定
        # 按鍵讀取、判斷移動加速度
        if key_pressed[pygame.K_LEFT] and self.x > 0:
            self.aclx = -acl
        if key_pressed[pygame.K_RIGHT] and self.x < S_W:
            self.aclx = acl
        if key_pressed[pygame.K_UP] and self.y > 0:
            self.acly = -acl
        if key_pressed[pygame.K_DOWN] and self.y < S_H:
            self.acly = acl

        # 單位向量
        if self.aclx ** 2 + self.acly ** 2 > acl * acl:
            self.aclx *= abs(acl / (math.sqrt(self.aclx ** 2 + self.acly ** 2)))
            self.acly *= abs(acl / (math.sqrt(self.aclx ** 2 + self.acly ** 2)))

        # 玩家邊界穿梭
        if self.x >= 500:
            pygame.draw.circle(background, color.blue, (self.x, self.y), Radius, Radius - 1)
            self.x -= 495
        if self.x <= 0:
            pygame.draw.circle(background, color.blue, (self.x, self.y), Radius, Radius - 1)
            self.x += 495
        if self.y >= 500:
            pygame.draw.circle(background, color.blue, (self.x, self.y), Radius, Radius - 1)
            self.y -= 495
        if self.y <= 0:
            pygame.draw.circle(background, color.blue, (self.x, self.y), Radius, Radius - 1)
            self.y += 495

        # 玩家速度變化、座標變化
        self.velx += self.aclx
        self.vely += self.acly

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

        if self.velx ** 2 + self.vely ** 2 > maxv ** 2:
            self.velx *= abs(maxv / (math.sqrt(self.velx ** 2 + self.vely ** 2)))
            self.vely *= abs(maxv / (math.sqrt(self.velx ** 2 + self.vely ** 2)))

        self.x += self.velx
        self.y += self.vely

        # 塗色
        # pygame.draw.rect(background, color.blue, (self.x, self.y, Radius, Radius))
        pygame.draw.circle(background, color.blue, (self.x, self.y), Radius, Radius - 1)

        # 玩家圖片


# --------------------------------------------------------------------------------------------------------------
class Player2(pygame.sprite.Sprite):
    # Sprite初始化、變數設定
    def __init__(self, x, y, velx, vely, color):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.velx = velx
        self.vely = vely
        self.color = color

        self.acl = 0.2
        self.backacl = 0.05
        self.maxv = 2.0

        self.aclx = 0
        self.acly = 0

    # Sprite刷新
    def update(self):
        key_pressed = pygame.key.get_pressed()
        self.aclx = 0
        self.acly = 0

        # 移動設定
        # 玩家邊界穿梭
        if self.x >= 500:
            pygame.draw.circle(background, color.blue, (self.x, self.y), Radius, Radius - 1)
            self.x -= 495
        if self.x <= 0:
            pygame.draw.circle(background, color.blue, (self.x, self.y), Radius, Radius - 1)
            self.x += 495
        if self.y >= 500:
            pygame.draw.circle(background, color.blue, (self.x, self.y), Radius, Radius - 1)
            self.y -= 495
        if self.y <= 0:
            pygame.draw.circle(background, color.blue, (self.x, self.y), Radius, Radius - 1)
            self.y += 495

        # 單位向量
        if self.aclx ** 2 + self.acly ** 2 > acl * acl:
            self.aclx *= abs(acl / (math.sqrt(self.aclx ** 2 + self.acly ** 2)))
            self.acly *= abs(acl / (math.sqrt(self.aclx ** 2 + self.acly ** 2)))

        # 按鍵讀取、判斷移動加速度
        if key_pressed[pygame.K_a] and self.x > 0:
            self.aclx = -acl
        if key_pressed[pygame.K_d] and self.x < S_W:
            self.aclx = acl
        if key_pressed[pygame.K_w] and self.y > 0:
            self.acly = -acl
        if key_pressed[pygame.K_s] and self.y < S_H:
            self.acly = acl

        # 玩家速度變化、座標變化
        self.velx += self.aclx
        self.vely += self.acly

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

        if self.velx ** 2 + self.vely ** 2 > maxv ** 2:
            self.velx *= abs(maxv / (math.sqrt(self.velx ** 2 + self.vely ** 2)))
            self.vely *= abs(maxv / (math.sqrt(self.velx ** 2 + self.vely ** 2)))

        self.x += self.velx
        self.y += self.vely

        # 塗色
        pygame.draw.circle(background, color.red, (self.x, self.y), Radius, Radius - 1)

        # 玩家圖片



###########################################################

Player1 = Player1(0, 50, 0, 0, color.blue)
Player2 = Player2(0, 50, 0, 0, color.red)
all_sprites = pygame.sprite.Group()
all_sprites.add(Player1)
all_sprites.add(Player2)


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
            if area_value[i * 5][j * 5] == cv.map_rgb(color.red):
                red_ar += 1
            if area_value[i * 5][j * 5] == cv.map_rgb(color.blue):
                blue_ar += 1

    return red_ar, blue_ar

def show_menu():
    message_topic = dtopic.render('michan v.s mafu', True, color.cyan)
    message_infor = dfont.render('1P:arrow key 2P:WASD', True, color.cyan)
    screen.blit(message_topic,(100,100))
    screen.blit(message_infor, (100, 300))
    message_infor = dfont.render('Press Space Key to Start', True, color.cyan)
    screen.blit(message_infor, (100, 400))
    pygame.display.update()
    waiting = True
    while waiting:
        clock.tick(FPS)
        # 取得輸入
        key_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif key_pressed[pygame.K_SPACE]:
                waiting=False

# -----------------------------------------------------------------------------------

counting_time = int(0)
frame_count = int(0)
R = 20  # the r of circle
maxv = int(2)
red_score, b_score = int(0), int(0)
acl = 0.2
backacl = 0.05

time = 0  # time of game

font = pygame.font.SysFont("Arial", 20)
running = True
start_menu=True
# 遊戲迴圈
while running:
    if start_menu:
        show_menu()
        pygame.display.update()
        start_menu=False
    if frame_count == 0:
        background.fill(color.white)

    counting_time += 1
    frame_count += 1
    pygame.time.Clock()
    pygame.time.delay(10)

    key_pressed = pygame.key.get_pressed()

    clock.tick(FPS)

    # 取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新遊戲
    all_sprites.update()
    x1, y1 = Player1.x, Player1.y
    x2, y2 = Player2.x, Player2.y
    # ColorCount
    if frame_count % 500 == 0:
        red_score, b_score = color_counting(background)
        counting_time = int(0)
    if key_pressed[pygame.K_SPACE]:
        print(b_score)
        print(f"{type(red_score)}")

    # 畫面顯示

    message_loc = font.render('P1_loc: {0},{1} | P2_loc: {2},{3}'.format(int(x1), int(y1), int(x2), int(y2)), True,
                              color.cyan)
    message_scores = font.render('P1_scores:{0} | P2_scores:{1}'.format((b_score/100), (red_score/100)), True,
                                 color.cyan)
    if frame_count % 500 != 0:
        screen.blit(babackground,(0,500))
        screen.blit(background, (0, 0))
        screen.blit(message_loc, (0, 470))
        screen.blit(message_scores, (0,520))

    # screen.blit(arrow,MIDDLE)
    pygame.display.update()

pygame.quit()
sys.exit()