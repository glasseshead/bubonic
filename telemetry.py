import pygame, os, math

import render
import config

def telemetry(canvas):
    # draw telemetry box
    pygame.draw.rect(canvas, (40, 40, 40), (0, 640, 800, 800))

    # render telemetry data
    render.renderData(10, 660 + 0 * 20, f"Raw Mouse Position             {config.mouseXraw}, {config.mouseYraw}", canvas)
    render.renderData(10, 660 + 1 * 20, f"Robot Pose (Nonrelative)       {config.robotPosX}, {config.robotPosY}, {config.robotPosTheta}", canvas)
    render.renderData(10, 660 + 2 * 20, f"Robot Theta Reset              {config.robotPosTheta == 0}", canvas)
    render.renderData(10, 660 + 3 * 20, f"Pose Data Reset                {config.poseData == []}             path.cpp Reset             {os.path.exists('./path.cpp') and os.path.getsize('./path.cpp') == 0}", canvas)
    render.renderData(10, 660 + 4 * 20, f"Turning 90 Deg                 {config.turning90Deg}", canvas)
    render.renderData(10, 660 + 5 * 20, f"Origin Reset                   {math.isclose(config.originX, 0.0) and math.isclose(config.originY, 0.0) and math.isclose(config.originT, 0.0)}", canvas)