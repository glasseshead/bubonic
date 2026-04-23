import pygame, os

import render
import config

def telemetry(canvas):
    # draw telemetry box
    pygame.draw.rect(canvas, (40, 40, 40), (0, 320, 400, 400))

    # render telemetry data
    render.renderData(10, 330 + 0 * 12, f"Raw Mouse Position      {config.mouseXraw}, {config.mouseYraw}", canvas)
    render.renderData(10, 330 + 1 * 12, f"Robot Pose              {config.robotPosX}, {config.robotPosY}, {config.robotPosTheta}", canvas)
    render.renderData(10, 330 + 2 * 12, f"Robot Theta Reset       {config.robotPosTheta == 0}", canvas)
    render.renderData(10, 330 + 3 * 12, f"Pose Data Reset         {config.poseData == []}", canvas)
    render.renderData(10, 330 + 4 * 12, f"path.cpp Reset          {os.path.exists('./path.cpp') and os.path.getsize('./path.cpp') == 0}", canvas)