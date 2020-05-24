import pygame as pg
import random as r
from settings import *
from sprites import *
import re


class Game:
    def __init__(self):
        pg.init()
        self.playing = True
        self.running = True
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.font_name = pg.font.match_font(FONT)

    def game_loop(self):
        #  always start playing when game loop starts:
        self.playing = True
        while self.playing:
            #  time passes
            self.clock.tick(FPS)

            #  user input
            self.events()

            #  update sprites
            self.update()

            #  draw to the screen
            self.draw()

    def new_game(self):

        #  set up the level
        self.setup()

        #  play the game loop
        self.game_loop()

        #  gameover screen
        self.show_go_screen()

    def setup(self):
        self.all_sprites = pg.sprite.Group()
        self.all_targets = pg.sprite.Group()
        self.all_bullets = pg.sprite.Group()
        self.player = Player(self, WIDTH // 2, HEIGHT - 30)
        self.windx = r.uniform(-W_X_LIMIT * MpS / SECOND, W_X_LIMIT * MpS / SECOND)
        self.windy = r.uniform(-W_Y_LIMIT * MpS / SECOND, W_Y_LIMIT * MpS / SECOND)
        self.fun_points = self.get_fun_points()

    def show_go_screen(self):
        pass

    def events(self):
        events = pg.event.get()
        for e in events:
            if e.type == pg.QUIT:
                self.playing = False
                self.running = False
            elif e.type == pg.KEYDOWN and e.key == pg.K_SPACE:
                self.player.shoot()

        #  check to change the wind:
        if pg.time.get_ticks() % WIND_CHANGE_RATE == 0:
            self.windx = r.uniform(-W_X_LIMIT * MpS / SECOND, W_X_LIMIT * MpS / SECOND)
            self.windy = r.uniform(-W_Y_LIMIT * MpS / SECOND, W_Y_LIMIT * MpS / SECOND)

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.draw_text("Winds vector: [" + str(self.windx * SECOND / MpS) + ", " + str(self.windy * SECOND / MpS) + "]", 16, CYAN, WIDTH / 2,
                       HEIGHT / 8)
        pg.display.flip()

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.centerx = x
        text_rect.centery = y
        self.screen.blit(text_surface, text_rect)

    def get_fun_points(self):
        points = []
        coef = self.find_fun()  # returns a table of polynomial coefficients
        coef_len = len(coef)
        for i in range(WIDTH):  # for each point on X axis
            y = HEIGHT
            for j in range(coef_len):
                y -= coef[j] * i**j
            point = (i, y)
            points.append(point)
        return points

    def find_fun(self):  # finds coefficients of polynomial function using regex
        coef = []

        return coef



g = Game()
while g.running:
    g.new_game()
