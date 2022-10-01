import settings
import time

import sys
import pygame as pg
from pygame.locals import *
import model
import botAI
import view


def user_click():
    # get coordinates of mouse click
    x, y = pg.mouse.get_pos()
    # get column of mouse click (1-3)
    if (x < settings.screen_width / 3):
        col = 1
    elif (x < settings.screen_width / 3 * 2):
        col = 2
    elif (x < settings.screen_width):
        col = 3
    else:
        col = 0
    # get row of mouse click (1-3)
    if (y < settings.screen_height / 3):
        row = 0
    elif (y < settings.screen_height / 3 * 2):
        row = 1
    elif (y < settings.screen_height):
        row = 2
    else:
        row = 0
    if (col + row) == 0:
        return 0
    else: return row * 3 + col

def run():
    pg.init()
    screen = pg.display.set_mode((settings.screen_width, settings.screen_height + 100), 0, 32)
    pg.display.set_caption('Tic Tac Toe GAME')
    CLOCK = pg.time.Clock()

    x_img = pg.image.load("img/X.png")
    y_img = pg.image.load("img/0.png")

    # resizing images
    x_img = pg.transform.scale(x_img, (80, 80))
    o_img = pg.transform.scale(y_img, (80, 80))

    view.game_initiating_window(screen)
    game_result = 'None'
    x_turn = settings.x_turn
    bot_play_X = settings.bot_play_X
    model.init()



    while game_result == 'None':
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type is MOUSEBUTTONDOWN:
                user_click()
        ###############PrintField(field)
        if x_turn:
            view.draw_status(screen, 'Ходят X')
            if bot_play_X:
                field = field.replace(botAI.get_bot_turn(field, 'X', settings.bot_algorithm), 'X')  # бот сходил за X
            else:
                field = field.replace(MyInput(field), 'X')  # чел сходил за X
        else:
            view.draw_status(screen, 'Ходят 0')
            if not bot_play_X:
                field = field.replace(botAI.get_bot_turn(field, 'O', settings.bot_algorithm), 'O')  # бот сходил за O
            else:
                field = field.replace(MyInput(field), 'O')  # чел сходил за O    game_result = MyCheckGame(field)
        game_result = botAI.MyCheckGame(field)  # проверяем, чего там с результатом игры
        x_turn = not x_turn

        pg.display.update()
        CLOCK.tick(settings.fps)
