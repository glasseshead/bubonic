import pygame, sys
from pygame.locals import *
import config

import render
import telemetry
import control
import boundary

pygame.init()

config.fpsClock = pygame.time.Clock()

canvas = pygame.display.set_mode((config.canvasX, config.canvasY))
pygame.display.set_caption('Bubonic')

while True:
    config.mouseXraw, config.mouseYraw = pygame.mouse.get_pos()
    
    boundary.bounds()
    control.control()

    if len(config.poseData) > 1: 
        render.renderPath(config.poseData, canvas)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                config.poseData.append((config.mouseXraw, config.mouseYraw))
    
    print(config.poseData)
    
    render.renderField(canvas)
    telemetry.telemetry(canvas)

    pygame.display.update()
    config.fpsClock.tick(config.fps)