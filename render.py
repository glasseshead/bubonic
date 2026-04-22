import pygame

import config

def renderData(posX, posY, data, canvas) :
    font = pygame.font.Font(None, 14)
    text = font.render(data, True, 
                       (255, 255, 255), 
                       (0, 0, 0))
    canvas.blit(text, (posX, posY))

def renderTiles(canvas):
    pygame.draw.rect(canvas, (200, 200, 200), (70, 30, 260, 260))

    for i in range(6):
        for j in range(6):
            if ((j % 2 == 0 and i % 2 != 0) or
                (j % 2 != 0 and i % 2 == 0)): 
                pygame.draw.rect(canvas, (95, 95, 95), (80 + 40 * j, 40 + 40 * i, 40, 40))
            else:  
                pygame.draw.rect(canvas, (100, 100, 100), (80 + 40 * j, 40 + 40 * i, 40, 40))

def renderBot(robotPosX, robotPosY, robotPosTheta, canvas):
    bot_surf = pygame.Surface((35, 35), pygame.SRCALPHA)
    pygame.draw.rect(bot_surf, (255, 90, 90), (0, 0, 35, 35))
    pygame.draw.line(bot_surf, (0, 0, 0), (35 // 2, 35 // 2), (35, 35 // 2), 2)
    rotated = pygame.transform.rotate(bot_surf, -robotPosTheta)
    rotatedrect = rotated.get_rect(center = (robotPosX, robotPosY))
    canvas.blit(rotated, rotatedrect)

def renderPath(poses, canvas):
    for i in range(1, len(poses)):
        pygame.draw.line(canvas, (255, 0, 0), poses[i - 1], poses[i], 2)

def renderField(canvas):
    canvas.fill(config.canvasBGColour)

    renderTiles(canvas)
    renderBot(config.robotPosX + 80, config.robotPosY + 40, config.robotPosTheta, canvas)
    renderPath(config.poseData, canvas)