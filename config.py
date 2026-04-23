import pygame

# initialize fps values
fps = 60
fpsClock = pygame.time.Clock()

# initialize canvas values
canvasX, canvasY = 800, 800
canvasBGColour = (66, 77, 79)

# initialize mouse values
mouseXraw, mouseYraw = 0, 0

# initialize robot position values
robotPosX, robotPosY, robotPosTheta = 0, 0, 0

# pose data storage
poseData = []

# turning toggle state
turning90Deg = False

# origin values
originX, originY, originT = 0, 0, 0

# relative values
relativeX, relativeY, relativeT = 0, 0, 0