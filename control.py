import pygame

import config

def control():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_z]:
        config.poseData = []

    if keys[pygame.K_a]:
        config.robotPosTheta -= 1
        
    if keys[pygame.K_d]:
        config.robotPosTheta += 1

    if keys[pygame.K_s]:
        config.robotPosTheta = 0