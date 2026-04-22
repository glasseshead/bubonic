import pygame

# initialize fps values
fps = 0
fpsClock = pygame.time.Clock()

# initialize canvas values
canvasX, canvasY = 400, 400
canvasBGColour = (66, 77, 79)

# initialize mouse values
mouseXraw, mouseYraw = 0, 0
mouseXheaded, mouseYheaded = 0, 0

# initialize robot position values
robotPosX, robotPosY, robotPosTheta = 0 + mouseXheaded, 0 + mouseYheaded, 0

poseData = []