import settings
import time
import sys
import pygame as pg
from pygame.locals import *

def game_initiating_window(screen):
    # displaying over the screen
    #screen.blit(initiating_window, (0, 0))

    # updating the display
    pg.display.update()
    time.sleep(3)
    screen.fill(settings.bg_color)

    # drawing vertical lines
    pg.draw.line(screen, settings.line_color, (settings.screen_width / 3, 0), (settings.screen_width / 3, settings.screen_height), 7)
    pg.draw.line(screen, settings.line_color, (settings.screen_width / 3 * 2, 0), (settings.screen_width / 3 * 2, settings.screen_height), 7)

    # drawing horizontal lines
    pg.draw.line(screen, settings.line_color, (0, settings.screen_height / 3), (settings.screen_width, settings.screen_height / 3), 7)
    pg.draw.line(screen, settings.line_color, (0, settings.screen_height / 3 * 2), (settings.screen_width, settings.screen_height / 3 * 2), 7)
#    draw_status()

def run():
    pg.init()
    screen = pg.display.set_mode((settings.screen_width, settings.screen_height), 0, 32)
    pg.display.set_caption('Tic Tac Toe GAME')
    CLOCK = pg.time.Clock()

    x_img = pg.image.load("img/X.png")
    y_img = pg.image.load("img/0.png")

    # resizing images
    x_img = pg.transform.scale(x_img, (80, 80))
    o_img = pg.transform.scale(y_img, (80, 80))

    game_initiating_window(screen)

    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
        pg.display.update()
        CLOCK.tick(settings.fps)
    #pg.display.flip()