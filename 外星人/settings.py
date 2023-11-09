import random
import pygame
class Settings:
    #一个储存在游戏里的设置类
    def __init__(self):
        #初始化设置
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        # self.bg_color = (random.randint(0,256),random.randint(0,256),random.randint(0,256))

        #飞船的设置
        self.ship_speed = 5
        self.ship_limit = 2

        #子弹的设置
        self.bullet_speed = 4.0
        self.bullet_width = 300
        self.bullet_height = 150
        self.bullet_color = (random.randint(0,256),random.randint(0,256),random.randint(0,256))
        self.bullets_allowed = 500

        #外星人的设置
        self.fleet_drop_speed=10

        #以什么速度加快游戏进度
        self.speedup_scale=1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        #初始化随游戏进行而变化的设置
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        # fleet_direction 为1时向右移动 -1向左移动
        self.fleet_direction=1

    def increase_speed(self):
        #提高游戏难度
        self.ship_speed*=self.speedup_scale
        self.bullet_speed*=self.speedup_scale
        self.alien_speed*=self.speedup_scale