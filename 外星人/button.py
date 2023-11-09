import pygame.font
import random

class   Button:
    #为游戏创建按钮的类
    def __init__(self,ai_game,msg): 
        self.screen =ai_game.screen
        self.screen_rect=self.screen.get_rect()

        #设置按钮的尺寸
        self.width,self.height=200,50
        self.button_color=(random.randint(0,256),random.randint(0,256),random.randint(0,256))
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,48)

        #创建按钮的rect 的对象 使其居中
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center

        #按钮的标签只用创建一次
        self._prep_msg(msg)

    def _prep_msg(self,msg):
        #将msg 渲染成为图像，并且使其居中
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center

    def draw_button(self):
        #绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)