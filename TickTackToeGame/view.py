import pygame as pg
#from pygame.locals import *
import settings
import time
import sys

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

def draw_status(screen,message):
    font = pg.font.Font(None, 30)

    # setting the font properties like
    # color and width of the text
    text = font.render(message, 1, (255, 255, 255))

    # copy the rendered message onto the board
    # creating a small block at the bottom of the main display
    screen.fill((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(settings.screen_width / 2, 500 - 50))
    screen.blit(text, text_rect)
    pg.display.update()

def my_question(screen,question,text1,text2):
    font = pg.font.Font(None, 30)

    # setting the font properties like
    # color and width of the text
    text = font.render(question, 1, (255, 255, 255))

    # copy the rendered message onto the board
    # creating a small block at the bottom of the main display
    screen.fill((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(settings.screen_width / 2, 500 - 75))
    screen.blit(text, text_rect)

    text = font.render(text1, 1, (255, 255, 255))
    text_rect = text.get_rect(center=(settings.screen_width / 4, 500 - 30))
    screen.blit(text, text_rect)

    text = font.render(text2, 1, (255, 255, 255))
    text_rect = text.get_rect(center=(settings.screen_width * 3 / 4, 500 - 30))
    screen.blit(text, text_rect)

    pg.draw.line(screen,(255, 255, 255), [0, 400 + 40],[600, 400 + 40], 2)
    pg.draw.line(screen,(255, 255, 255), [settings.screen_width / 2, 400 + 40],[settings.screen_width / 2, 500], 2)

    pg.display.update()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                print(pos)
                if pos[1]>400:
                    if pos[0]<(settings.screen_width / 2):
                        return 1
                    else: return 2

def PrintField(local_field):
    pass

# https://www.geeksforgeeks.org/tic-tac-toe-gui-in-python-using-pygame/

