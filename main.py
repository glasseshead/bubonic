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

    if (config.mouseXheaded < 18): config.mouseXheaded = 18
    if (config.mouseXheaded > 223): config.mouseXheaded = 223

    if (config.mouseYheaded < 18): config.mouseYheaded = 18
    if (config.mouseYheaded > 223): config.mouseYheaded = 223

    canvas.fill(config.canvasBGColour)
    pygame.draw.rect(canvas, (40, 40, 40), (0, 320, 400, 400))

    render.renderTiles(canvas)
    render.renderBot(config.mouseXheaded + 80, config.mouseYheaded + 40, config.robotPosTheta, canvas)

    if len(config.poseData) > 1: 
        render.renderPath(config.poseData, canvas)

    render.renderData(10, 330, f"Raw Mouse Position      {config.mouseXraw}, {config.mouseYraw}", canvas)
    render.renderData(10, 342, f"Headed Mouse Position   {config.mouseXheaded}, {config.mouseYheaded}", canvas)
    render.renderData(10, 354, f"Robot Theta             {config.robotPosTheta}", canvas)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_z]:
        config.poseData = []

    if keys[pygame.K_a]:
        config.robotPosTheta -= 1
        
    if keys[pygame.K_d]:
        config.robotPosTheta += 1

    if keys[pygame.K_s]:
        config.robotPosTheta = 0

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                config.poseData.append((config.mouseXraw, config.mouseYraw))

    pygame.display.update()
    config.fpsClock.tick(config.fps)