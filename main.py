
import sys
import pygame
import math
import random
import os
import keyboard
import color

# 各種變數
screen_size = S_W, S_H = (750, 800)
game_screen_size = (750, 750)
UI_screen_size = (750, 100)
Chracter_size = (50, 50)

FPS = 60
Radius = 40
RIGHT_TOP = (0, 0)
RIGHT_BOTTOM = (0, 500)
MIDDLE = (S_W // 2, S_H // 2)

gametime=0
deltatime=1/60
frame_count = int(0)
R = 20  # the r of circle
maxv = int(2)
red_score, b_score = int(0), int(0)
acl = 0.2
backacl = 0.05
# 遊戲初始化 & 創建視窗
pygame.init()
pygame.display.set_caption("GameTest")
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
dfont = pygame.font.SysFont("Arial", 30)
dtopic = pygame.font.SysFont("Arial", 46)

# 圖片網址
'''
michan_raw : https://www.pixiv.net/en/artworks/97929808
michan_raw2 : https://www.pixiv.net/en/artworks/104207003
michan_raw3 :https://www.pixiv.net/en/artworks/99080799
michan_raw4 : https://www.pixiv.net/en/artworks/98452870
'''
# 背景圖片讀取
background = pygame.Surface(screen_size).convert()
uiscreen = pygame.Surface((750, 50)).convert()

michan_raw = pygame.image.load(os.path.join('img', 'michan_raw.jpg')).convert()
michan_raw2 = pygame.image.load(os.path.join('img', 'michan_raw2.jpg')).convert()
michan_raw3 = pygame.image.load(os.path.join('img', 'michan_raw3.jpg')).convert()
michan_raw4 = pygame.image.load(os.path.join('img', 'michan_raw4.jpg')).convert()
start_background = pygame.transform.scale(michan_raw2, screen_size)
michan_background = pygame.transform.scale(michan_raw3, game_screen_size)
michan_chracter = pygame.transform.scale(michan_raw, Chracter_size)
michan_item = pygame.transform.scale(michan_raw4, Chracter_size)

# michan_chracter = pygame.image.load(os.path.join('img', 'michan.jpg')).convert()
mafu_chracter = pygame.image.load(os.path.join('img', 'mafu.jpg')).convert()
icons_grid = pygame.image.load(os.path.join('img', 'icons_grid.png')).convert()
'''
classmate = pygame.image.load(os.path.join('img', 'classmate.jpg')).convert()
arrow = pygame.image.load(os.path.join('img', 'Arrow.jpg')).convert()
circle = pygame.image.load(os.path.join('img', 'circle.png')).convert()

'''
background = michan_background


class Player(pygame.sprite.Sprite):
    # Sprite初始化、變數設定
    def __init__(self, x, y, velx, vely, go_up, go_down, go_left, go_right, color, photo):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.velx = velx
        self.vely = vely
        self.go_up = go_up
        self.go_down = go_down
        self.go_left = go_left
        self.go_right = go_right
        self.color = color
        self.photo = photo

        self.acl = int(0.2)
        self.backacl = int(0.5)
        self.maxv = int(2.0)
        self.aclx = int(0)
        self.acly = int(0)

    # Sprite刷新
    def update(self):
        global key_pressed, backacl
        key_pressed = pygame.key.get_pressed()
        self.aclx = int(0)
        self.acly = int(0)

        # 移動設定
        # 按鍵讀取、判斷移動加速度
        if key_pressed[self.go_left] and self.x > 0:
            self.aclx = -acl
        if key_pressed[self.go_right] and self.x < S_W:
            self.aclx = acl
        if key_pressed[self.go_up] and self.y > 0:
            self.acly = -acl
        if key_pressed[self.go_down] and self.y < S_H:
            self.acly = acl

        # 單位向量
        if self.aclx ** 2 + self.acly ** 2 > acl * acl:
            self.aclx *= abs(acl / (math.sqrt(self.aclx ** 2 + self.acly ** 2)))
            self.acly *= abs(acl / (math.sqrt(self.aclx ** 2 + self.acly ** 2)))

        # 玩家邊界穿梭
        if self.x >= 750:
            pygame.draw.circle(background, self.color, (self.x, self.y), Radius, Radius - 1)
            self.x -= 745
        if self.x <= 0:
            pygame.draw.circle(background, self.color, (self.x, self.y), Radius, Radius - 1)
            self.x += 745
        if self.y >= 750:
            pygame.draw.circle(background, self.color, (self.x, self.y), Radius, Radius - 1)
            self.y -= 745
        if self.y <= 0:
            pygame.draw.circle(background, self.color, (self.x, self.y), Radius, Radius - 1)
            self.y += 745
          
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
        
      # 玩家靜止判斷
        if -backacl < self.velx < backacl:
            self.velx = 0
        elif -backacl < self.vely < backacl:
            self.vely = 0
        self.x += self.velx
        self.y += self.vely



        # 塗色
        # pygame.draw.rect(background, color.blue, (self.x, self.y, Radius, Radius))
        pygame.draw.circle(background, self.color, (self.x, self.y), Radius, Radius - 1)

        # 玩家圖片
        self.image = pygame.image.load(os.path.join('img', self.photo)).convert()
        background.blit(self.image, (self.x - 25, self.y - 25))

class item(pygame.sprite.Sprite):
    # Sprite初始化、變數設定
    def __init__(self, x, y, photo, p1, p2):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.photo = photo
        self.site = (self.x, self.y)
        self.p1 = p1
        self.p2 = p2
        self.alreadyTrigger = False
        self.triggerDistance = 80

    def update(self):
        if(self.alreadyTrigger == False):
            distance1 = ((self.x - self.p1.x)**2 + (self.y - self.p1.y)**2)**0.5
            distance2 =((self.x - self.p2.x)**2 + (self.y - self.p2.y)**2)**0.5
            if (distance1 >= self.triggerDistance and distance2 >= self.triggerDistance): 
              background.blit(self.photo, self.site)
            if (distance1 < self.triggerDistance):
                pygame.draw.circle(background, self.p1.color, (self.x, self.y), Radius*3, Radius*3 - 1)
                self.alreadyTrigger = True
                
            if(distance2 < self.triggerDistance):
                pygame.draw.circle(background, self.p2.color, (self.x, self.y), Radius*3, Radius*3 - 1)
                self.alreadyTrigger = True
            


# 玩家設定、Sprite整合

Player1 = Player(187, 375, 0, 0, keyboard.UP, keyboard.DOWN, keyboard.LEFT, keyboard.RIGHT, color.FFE2E2, 'michan.jpg')
Player2 = Player(563, 375, 0, 0, keyboard.w, keyboard.s, keyboard.a, keyboard.d, color.A5D7E8, 'mafu.jpg')
item = item(random.randint(0, 700), random.randint(0, 700), michan_item, Player1, Player2)
all_sprites = pygame.sprite.Group()
all_sprites.add(Player1)
all_sprites.add(Player2)


# 計分
def color_counting(cv):
    area_value = pygame.surfarray.pixels2d(cv)
    red_ar = int(0)
    blue_ar = int(0)
    print(area_value)
    for i in range(100):
        for j in range(100):
            if area_value[i * 5][j * 5] == cv.map_rgb(color.A5D7E8):
                red_ar += 1
            if area_value[i * 5][j * 5] == cv.map_rgb(color.FFE2E2):
                blue_ar += 1

    return red_ar, blue_ar

#遊戲準備介面
def show_menu(photoname):
    screen.blit(photoname, RIGHT_TOP)
    message_topic = dtopic.render('michan v.s mafu', True, color.color_002B5B)
    message_infor = dfont.render('1P:arrow key/2P:WASD', True, color.color_002B5B)
    screen.blit(message_topic, (200, 0))
    screen.blit(message_infor, (200, 50))
    message_infor = dfont.render('Press Space Key to Start', True, color.color_002B5B)
    screen.blit(message_infor, (200, 770))
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
                waiting = False


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
start_menu = True
while running:
    #Timer
    gametime += 1/60
    
    #game item collision
    if((20<gametime<20.2 or 40<gametime<40.2) and item.alreadyTrigger == True):
        item.alreadyTrigger = False
        item.x, item.y = random.randint(0,700), random.randint(0,700)
        item.site = item.x , item.y
    # 遊戲準備介面
    if start_menu:
        show_menu(start_background)
        pygame.display.update()
        start_menu = False
    # 遊戲準備介面
    if frame_count == 0:
        uiscreen.fill(color.deepgray)
        background.blit(michan_background, RIGHT_TOP)
        
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



  
    item.update()
    all_sprites.update()
    x1, y1 = Player1.x, Player1.y
    x2, y2 = Player2.x, Player2.y

    # 分數判定
    if frame_count % 500 == 0:
        red_score, b_score = color_counting(background)
        counting_time = int(0)
    if key_pressed[pygame.K_SPACE]:
        print(b_score)
        print(f"{type(red_score)}")

# 畫面顯示

    message_loc = font.render('P1_loc: ({0},{1}) | P2_loc: ({2},{3})'.format(int(x1), int(y1), int(x2), int(y2)), True,
                              color.color_002B5B)
    message_scores = font.render('P1_scores: {0} | P2_scores: {1}'.format(int(b_score), int(red_score)), True,
                                 color.color_002B5B)
    message_time = font.render('time : {0:.2f}'.format(gametime), True, color.color_002B5B)
    if frame_count % 500 != 0:
        screen.blit(uiscreen, (0, 750))
        screen.blit(background, (0, 0))

        screen.blit(message_loc, (0, 750))
        screen.blit(message_scores, (0, 775))
        screen.blit(message_time, (500, 775))
    pygame.display.update()

pygame.quit()
sys.exit()

'''

                   ___====-_  _-====___
             _--^^^     //      \\     ^^^--_
          _-^          // (    ) \\          ^-_
         -            //  |\^^/|  \\            -
       _/            //   (@  @)   \\            \_
      /             ((     \\//     ))             \
     -               \\    (oo)    //               -
    -                 \\  / VV \  //                 -
   -                   \\/      \//                   -
  _ /|          /\      (   /\   )      /\          |\ _
  |/ | /\ /\ /\/  \ /\  \  |  |  /  /\ /  \/\ /\ /\ | \|
  `  |/  V  V  `   V  \ \| |  | |/ /  V   '  V  V  \|  '
     `   `  `      `   / | |  | | \   '      '  '   '
                      (  | |  | |  )
                     __\ | |  | | /__
                    (vvv(VVV)(VVV)vvv)
                    神獸保佑，程式碼沒Bug!
'''
