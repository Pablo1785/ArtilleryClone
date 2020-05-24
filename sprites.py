import pygame as pg
import math as m
from settings import *
import random as r


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((P_SIZE, P_SIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def update(self):
        pass

    def shoot(self):
        b = Bullet(self.game, 4 * MpS, -10 * MpS)


class Bullet(pg.sprite.Sprite):
    def __init__(self, game, vx, vy):
        self.groups = game.all_sprites, game.all_bullets
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((B_SIZE, B_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.game.player.rect.centerx
        self.rect.centery = self.game.player.rect.centery
        self.accx = 0
        self.accy = GRAVITY
        self.vx = vx
        self.vy = vy

    def update(self):
        self.accx = self.game.windx
        self.accy = GRAVITY + self.game.windy
        self.vx += self.accx
        self.vy += self.accy
        self.rect.centerx += self.vx
        self.rect.centery += self.vy

        if self.rect.bottom >= HEIGHT or self.rect.top <= 0 or self.rect.right >= WIDTH or self.rect.left <= 0:
            self.kill()



