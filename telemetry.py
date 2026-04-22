import pygame

import render
import config

def telemetry(canvas):
    pygame.draw.rect(canvas, (40, 40, 40), (0, 320, 400, 400))
    render.renderData(10, 330 + 0 * 12, f"Raw Mouse Position      {config.mouseXraw}, {config.mouseYraw}", canvas)
    render.renderData(10, 330 + 1 * 12, f"Robot Pose              {config.robotPosX}, {config.robotPosY}, {config.robotPosTheta}", canvas)