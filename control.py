import pygame

import config

def control():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_z]:
        config.poseData = []

    if keys[pygame.K_a]:
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            config.robotPosTheta -= 90
        else:
            config.robotPosTheta -= 1

    if keys[pygame.K_d]:
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            config.robotPosTheta += 90
        else:
            config.robotPosTheta += 1

    if keys[pygame.K_s]:
        config.robotPosTheta = 0

    if keys[pygame.K_q]:
        with open("path.cpp", "w") as file:
            pass