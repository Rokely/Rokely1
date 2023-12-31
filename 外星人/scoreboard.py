import pygame.font
import random

class  Scoreboard:
    #显示得分的类

    def __init__(self,ai_game):
        
        #初始化得分和属性
        self.ai_game=ai_game
        self.screen=ai_game.screen
        self.screen_rect=self.screen.get_rect()
        self.settings=ai_game.settings
        self.stats=ai_game.stats
        #显示得分信息的字体
        self.text_color=(random.randint(0,256),random.randint(0,256),random.randint(0,256))
        self.font=pygame.font.SysFont(None,48)
        #准备初始化得分图像
        self.prep_score()

    def prep_score(self):
        #将得分渲染为图像
        score_str=str(self.stats.score)
        self.score_image=self.font.render(score_str,True,self.text_color,self.settings.bullet_color)

        #在屏幕右上角显示得分
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20

    def show_score(self):
        #显示得分
        self.screen.blit(self.score_image,self.score_rect)