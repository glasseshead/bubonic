import pygame

import config

def renderData(posX, posY, data, canvas):
    # set up text variables
    font = pygame.font.Font(None, 20)
    text = font.render(data, True, (255, 255, 255), (0, 0, 0))

    # blit text to canvas
    canvas.blit(text, (posX, posY))

def renderTiles(canvas):
    # render field perimeter
    pygame.draw.rect(canvas, (200, 200, 200), (140, 60, 520, 520))

    # may not be the best way to do this but hey i need to do something
    for i in range(6):
        for j in range(6):
            # checkerboard
            if ((j % 2 == 0 and i % 2 != 0) or
                (j % 2 != 0 and i % 2 == 0)): 
                pygame.draw.rect(canvas, (95, 95, 95), (160 + 80 * j, 80 + 80 * i, 80, 80))
            else:  
                pygame.draw.rect(canvas, (100, 100, 100), (160 + 80 * j, 80 + 80 * i, 80, 80))

def renderBot(robotPosX, robotPosY, robotPosTheta, canvas):
    # set surface for robot
    botSurf = pygame.Surface((70, 70), pygame.SRCALPHA)

    # draw robot and rotator indication
    pygame.draw.rect(botSurf, (255, 90, 90), (0, 0, 70, 70))
    pygame.draw.line(botSurf, (0, 0, 0), (70 // 2, 70 // 2), (70, 70 // 2), 4)

    # rotate transform
    rotated = pygame.transform.rotate(botSurf, -robotPosTheta)
    rotatedrect = rotated.get_rect(center = (robotPosX, robotPosY))

    # blit to canvas
    canvas.blit(rotated, rotatedrect)

def renderPath(poses, canvas):
    # fetch points
    for i in range(1, len(poses)):
        # draw line from previous logged point to last logged point
        pygame.draw.line(canvas, (255, 0, 0), poses[i - 1][:2], poses[i][:2], 3)

        # draw point for visibility
        pygame.draw.circle(canvas, (255, 0, 0), poses[i - 1][:2], 5)

    # if within boundary
    if len(poses) > 0 and ((160 <= config.mouseXraw <= 640) and (80 <= config.mouseYraw <= 560)):
        # draw cyan line to represent mouse pointing path
        pygame.draw.line(canvas, (0, 255, 255), poses[-1][:2], (config.mouseXraw, config.mouseYraw), 3)

def renderField(canvas):
    # background
    canvas.fill(config.canvasBGColour)

    # render tiles, bot
    renderTiles(canvas)
    renderBot(config.robotPosX + 160, config.robotPosY + 80, config.robotPosTheta, canvas)

    # render path
    renderPath(config.poseData, canvas)