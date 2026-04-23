import pygame

import config

def control():
    # get keys pressed currently
    keys = pygame.key.get_pressed()

    # clear pose data
    if keys[pygame.K_z]:
        config.poseData = []

    # set robot theta to current theta
    # aka zero theta
    if keys[pygame.K_s]:
        config.robotPosTheta = 0

    # clear cpp output
    if keys[pygame.K_q]:
        with open("path.cpp", "w") as file:
            pass