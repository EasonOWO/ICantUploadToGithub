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
RIGHT_BOTTOM = (0, 700)
MIDDLE = (S_W // 2, S_H // 2)

#遊戲初始化 & 創建視窗
pygame.init()
pygame.display.set_caption("GameTest")
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
dfont = pygame.font.SysFont("Arial", 30)
dtopic = pygame.font.SysFont("Arial",46)

#背景圖片讀取
background = pygame.Surface((500,500)).convert()
uiscreen = pygame.Surface((screen.get_size())).convert()

michan_background = pygame.image.load(os.path.join('img', 'michan 500x500.jpg')).convert()
michan_chracter = pygame.image.load(os.path.join('img', 'michan.jpg')).convert()
mafu_chracter = pygame.image.load(os.path.join('img', 'mafu.jpg')).convert()
classmate = pygame.image.load(os.path.join('img', 'classmate.jpg')).convert()
start_background = pygame.image.load(os.path.join('img','start_background.jpg'))
arrow = pygame.image.load(os.path.join('img', 'arrow.png')).convert()
circle = pygame.image.load(os.path.join('img', 'circle.png')).convert()
icons_grid = pygame.image.load(os.path.join('img', 'icons_grid.png')).convert()

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
        if key_pressed[self.go_left] and self.x > 0:
            self.aclx = -acl
        if key_pressed[self.go_right] and self.x < S_W:
            self.aclx = acl
        if key_pressed[self.go_up] and self.y > 0:
            self.acly = -acl
        if key_pressed[self.go_down] and self.y < S_H:
            self.acly = acl

        # 單位向量
        if self.aclx ** 2 + self.acly ** 2 > acl ** 2:
            self.aclx *= abs(acl / (math.sqrt(self.aclx ** 2 + self.acly ** 2)))
            self.acly *= abs(acl / (math.sqrt(self.aclx ** 2 + self.acly ** 2)))

        # 玩家邊界穿梭
        if self.x >= 500:
            pygame.draw.circle(background, self.color, (self.x, self.y), Radius, Radius - 1)
            self.x -= 495
        if self.x <= 0:
            pygame.draw.circle(background, self.color, (self.x, self.y), Radius, Radius - 1)
            self.x += 495
        if self.y >= 500:
            pygame.draw.circle(background, self.color, (self.x, self.y), Radius, Radius - 1)
            self.y -= 495
        if self.y <= 0:
            pygame.draw.circle(background, self.color, (self.x, self.y), Radius, Radius - 1)
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

        if(-backacl < self.vely < backacl):
            self.vely=0
        if(-backacl < self.velx < backacl):
            self.velx=0

        if self.velx ** 2 + self.vely ** 2 > maxv ** 2:
            self.velx *= abs(maxv / (math.sqrt(self.velx ** 2 + self.vely ** 2)))
            self.vely *= abs(maxv / (math.sqrt(self.velx ** 2 + self.vely ** 2)))

        self.x += self.velx
        self.y += self.vely

        # 塗色
        # pygame.draw.rect(background, color.blue, (self.x, self.y, Radius, Radius))
        pygame.draw.circle(background, self.color, (self.x, self.y), Radius, Radius-1)

        # 玩家圖片
        self.image = pygame.image.load(os.path.join('img',self.photo)).convert()
        self.image.set_colorkey((0, 0, 0))
        background.blit(self.image, (self.x - 25, self.y - 25))


###########################################################

Player1 = Player(115, 250, 0, 0, keyboard.UP, keyboard.DOWN, keyboard.LEFT, keyboard.RIGHT, color.blue, 'michan.jpg')
Player2 = Player(395, 250, 0, 0, keyboard.w, keyboard.s, keyboard.a, keyboard.d, color.red, 'mafu.jpg')
all_sprites = pygame.sprite.Group()
all_sprites.add(Player1)
all_sprites.add(Player2)

###########################################################

# count the score
def color_counting(cv):
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
    message_infor = dfont.render('1P:arrow key/2P:WASD', True, color.cyan)
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
        uiscreen.fill(color.F6F6F6)
        background.blit(michan_background,RIGHT_TOP)
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

    message_loc = font.render('P1_loc: {0},{1} | P2_loc: {2},{3}'.format(int(x1), int(y1), int(x2), int(y2)), True,color.cyan)
    message_scores = font.render('P1_scores:{0} | P2_scores:{1}'.format(int(b_score), int(red_score)), True,color.cyan)
    if frame_count % 500 != 0:

        screen.blit(uiscreen,(0,500))
        screen.blit(background, (0, 0))
        #background.blit(michan_background, (0, 0))

        screen.blit(message_loc, (0, 500))
        screen.blit(message_scores, (0,550))


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