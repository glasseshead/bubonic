import pygame

def renderData(posX, posY, data, canvas) :
    font = pygame.font.Font(None, 12)
    text = font.render(data, True, 
                       (255, 255, 255), 
                       (0, 0, 0))
    canvas.blit(text, (posX, posY))

def renderTiles(canvas):
    pygame.draw.rect(canvas, (200, 200, 200), (80, 80, 280, 280))

    for i in range(6):
        for j in range(6):
            if ((j % 2 == 0 and i % 2 != 0) or
                (j % 2 != 0 and i % 2 == 0)): 
                pygame.draw.rect(canvas, (90, 90, 90), (80 + 40 * j, 40 + 40 * i, 40, 40))
            else:  
                pygame.draw.rect(canvas, (100, 100, 100), (80 + 40 * j, 40 + 40 * i, 40, 40))

def renderBot(robotPosX, robotPosY, canvas):
    pygame.draw.rect(canvas, (255, 90, 90), (robotPosX, robotPosY, 35, 35))