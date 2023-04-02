import math

acl = 0.2
backacl = 0.05
maxv=2.0

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
    aclx, acly = move_input(self, keys)
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