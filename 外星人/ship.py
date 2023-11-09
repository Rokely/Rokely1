import pygame


class Ship:
    #一个飞船的类

    def __init__(self, ai_game):
        #初始化飞船并设置飞船的初始位置
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #加载飞船图像和获取外接矩形
        self.image = pygame.image.load(r'images\小飞机.png')
        self.rect = self.image.get_rect()

        #每艘飞船都放在屏幕中央
        self.rect.midbottom = self.screen_rect.midbottom

        #在飞船的属性X中储存一个浮点数
        self.x = float(self.rect.x)

        # 移动标志 （飞船一开始不移动）
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        #将飞船放在屏幕中央
        self.rect.midbottom=self.screen_rect.midbottom
        self.x=float(self.rect.x)
        
    def update(self):
        #更新飞船而不是rect对象的x值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
        #根据self.x更新rect对象
        self.rect.x = self.x

    def blitme(self):
        #指定位置绘制飞船
        self.screen.blit(self.image, self.rect)
