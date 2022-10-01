import pygame as pg
from pygame.locals import *
import settings
import time

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

