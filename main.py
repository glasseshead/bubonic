import pygame, sys
from pygame.locals import *
import config

import render

pygame.init()

config.fps = 60
config.fpsClock = pygame.time.Clock()

canvas = pygame.display.set_mode((config.canvasX, config.canvasY))
pygame.display.set_caption('Bubonic')

while True:
    config.mouseXraw, config.mouseYraw = pygame.mouse.get_pos()

    if ((80 <= config.mouseXraw <= 320) and (40 <= config.mouseYraw <= 280)):
        config.mouseXheaded, config.mouseYheaded = config.mouseXraw - 80, config.mouseYraw - 40
    else:
        config.mouseXheaded, config.mouseYheaded = -1, -1

    canvas.fill(config.canvasBGColour)

    render.renderTiles(canvas)
    render.renderBot(config.mouseXheaded + 62.5, config.mouseYheaded + 22.5, canvas)

    render.renderData(40, 340, f"Raw Mouse Position      {config.mouseXraw}, {config.mouseYraw}", canvas)
    render.renderData(40, 352, f"Headed Mouse Position   {config.mouseXheaded}, {config.mouseYheaded}", canvas)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    config.fpsClock.tick(config.fps)