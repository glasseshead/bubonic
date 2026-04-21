import pygame

def renderData(posX, posY, data, canvas) :
    font = pygame.font.Font(None, 12)
    text = font.render(data, True, 
                       (255, 255, 255), 
                       (0, 0, 0))
    canvas.blit(text, (posX, posY))