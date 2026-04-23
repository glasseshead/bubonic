import pygame, sys
from pygame.locals import *
import config

import render
import telemetry
import control
import boundary
import cppwrite

# initialize
pygame.init()

# set clock
config.fpsClock = pygame.time.Clock()

# set up canvas
canvas = pygame.display.set_mode((config.canvasX, config.canvasY))
pygame.display.set_caption('Bubonic')

while True:
    # getting raw mouse values
    config.mouseXraw, config.mouseYraw = pygame.mouse.get_pos()

    # to prevent theta getting too high
    config.robotPosTheta = config.robotPosTheta % 360
    
    # boundary and control checks
    boundary.bounds()
    control.control()

    for event in pygame.event.get():
        # exit control
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # plot point control
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and ((80 <= config.mouseXraw <= 320) and (40 <= config.mouseYraw <= 280)): 
                config.poseData.append((config.mouseXraw, config.mouseYraw, config.robotPosTheta))
                cppwrite.cppWrite()

        # rotation controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    config.robotPosTheta -= 90
                else:
                    config.robotPosTheta -= 1

            if event.key == pygame.K_d:
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    config.robotPosTheta += 90
                else:
                    config.robotPosTheta += 1
    
    # render field and telemetry
    render.renderField(canvas)
    telemetry.telemetry(canvas)

    pygame.display.update()
    config.fpsClock.tick(config.fps)