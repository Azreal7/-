import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, ai_settings, screen, ship):
        """在飞船的位置创建子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen

        # 在（0，0）处创建子弹，再赋予其位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.top = ship.rect.top
        self.rect.centerx = ship.rect.centerx
        # 用小数存储子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

        self.shooting = False

    def update(self):
        """向上移动子弹"""
        self.y -=self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)