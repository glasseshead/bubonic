import pygame, sys, os
from pygame.locals import *
import config

import render
import telemetry
import control
import relativity
import boundary
import cppwrite

# initialize
pygame.init()

# set clock
config.fpsClock = pygame.time.Clock()

# set up canvas
canvas = pygame.display.set_mode((config.canvasX, config.canvasY))
pygame.display.set_caption('Bubonic')

# clear path.cpp to avoid appending to old data
with open("path.cpp", "w") as file:
    pass

while True:
    # getting raw mouse values
    config.mouseXraw, config.mouseYraw = pygame.mouse.get_pos()

    # to prevent theta getting too high
    config.robotPosTheta = config.robotPosTheta % 360
    
    # boundary and control checks
    boundary.bounds()
    control.control()

    if len(config.poseData) >= 1:
        relativity.relativity()

    # control loop
    for event in pygame.event.get():
        # exit control
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # plot point control
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and ((160 <= config.mouseXraw <= 640) and (80 <= config.mouseYraw <= 560)): 
                config.poseData.append((config.mouseXraw, config.mouseYraw, config.robotPosTheta))
                if len(config.poseData) == 1:
                    # ZERO comment for first point
                    absX = (config.mouseXraw - 200) / config.inPerTick
                    absY = (config.mouseYraw - 120) / config.inPerTick
                    absT = config.robotPosTheta
                    with open(cppwrite.getPath(), "a") as file:
                        file.write(f"// ZERO {absX} {absY} {absT}\n")

                elif len(config.poseData) == 2:
                    # setPose and first moveToPose
                    relativity.relativity()
                    with open(cppwrite.getPath(), "a") as file:
                        file.write(f"chassis.setPose(0, 0, 0, 700);\n")
                        # get first set of coords
                        x1, y1, t1 = config.poseData[0]
                        relX1 = (x1 - config.originX) / config.inPerTick
                        relY1 = (y1 - config.originY) / config.inPerTick
                        relT1 = t1 - config.originT
                        file.write(f"chassis.moveToPose({relX1}, {relY1}, {relT1}, 700);\n")
                        # Write second point
                        file.write(f"chassis.moveToPose({config.relativeX}, {config.relativeY}, {config.relativeT}, 700);\n")
                else:
                    cppwrite.cppWrite()

        # rotation controls (90deg)
        if event.type == pygame.KEYDOWN:
            mods = pygame.key.get_mods()

            if event.key == pygame.K_a and mods & pygame.KMOD_SHIFT:
                config.turning90Deg = True
                config.robotPosTheta -= 90

            if event.key == pygame.K_d and mods & pygame.KMOD_SHIFT:
                config.turning90Deg = True
                config.robotPosTheta += 90

            if event.key == pygame.K_e:
                with open(cppwrite.getPath(), "a") as file:
                    file.write(f"chassis.setPose(0.0, 0.0, 0.0);\n")
                config.resetOrigin = True

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_a, pygame.K_d):
                config.turning90Deg = False
            if event.key == pygame.K_e:
                config.resetOrigin = False
    
    # render field and telemetry
    render.renderField(canvas)
    telemetry.telemetry(canvas)

    # update ticks
    pygame.display.update()
    config.fpsClock.tick(config.fps)