import pygame

import config

def renderData(posX, posY, data, canvas):
    # set up text variables
    font = pygame.font.Font(None, 14)
    text = font.render(data, True, (255, 255, 255), (0, 0, 0))

    # blit text to canvas
    canvas.blit(text, (posX, posY))

def renderTiles(canvas):
    # render field perimeter
    pygame.draw.rect(canvas, (200, 200, 200), (70, 30, 260, 260))

    # may not be the best way to do this but hey i need to do something
    for i in range(6):
        for j in range(6):
            # checkerboard
            if ((j % 2 == 0 and i % 2 != 0) or
                (j % 2 != 0 and i % 2 == 0)): 
                pygame.draw.rect(canvas, (95, 95, 95), (80 + 40 * j, 40 + 40 * i, 40, 40))
            else:  
                pygame.draw.rect(canvas, (100, 100, 100), (80 + 40 * j, 40 + 40 * i, 40, 40))

def renderBot(robotPosX, robotPosY, robotPosTheta, canvas):
    # set surface for robot
    botSurf = pygame.Surface((35, 35), pygame.SRCALPHA)

    # draw robot and rotator indication
    pygame.draw.rect(botSurf, (255, 90, 90), (0, 0, 35, 35))
    pygame.draw.line(botSurf, (0, 0, 0), (35 // 2, 35 // 2), (35, 35 // 2), 2)

    # rotate transform
    rotated = pygame.transform.rotate(botSurf, -robotPosTheta)
    rotatedrect = rotated.get_rect(center = (robotPosX, robotPosY))

    # blit to canvas
    canvas.blit(rotated, rotatedrect)

def renderPath(poses, canvas):
    # fetch points
    for i in range(1, len(poses)):
        # draw line from previous logged point to last logged point
        pygame.draw.line(canvas, (255, 0, 0), poses[i - 1][:2], poses[i][:2], 2)

        # draw point for visibility
        pygame.draw.circle(canvas, (255, 0, 0), poses[i - 1][:2], 4)

    # if within boundary
    if len(poses) > 0 and ((80 <= config.mouseXraw <= 320) and (40 <= config.mouseYraw <= 280)):
        # draw cyan line to represent mouse pointing path
        pygame.draw.line(canvas, (0, 255, 255), poses[-1][:2], (config.mouseXraw, config.mouseYraw), 2)

def renderField(canvas):
    # background
    canvas.fill(config.canvasBGColour)

    # render tiles, bot
    renderTiles(canvas)
    renderBot(config.robotPosX + 80, config.robotPosY + 40, config.robotPosTheta, canvas)

    # render path
    renderPath(config.poseData, canvas)