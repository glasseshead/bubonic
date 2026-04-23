import config

def bounds():
    # if within a current boundary set robot position in that boundary
    if ((160 <= config.mouseXraw <= 640) and (80 <= config.mouseYraw <= 560)):
        config.robotPosX, config.robotPosY = config.mouseXraw - 160, config.mouseYraw - 80

    # set bounds for robot to fallback to
    if (config.robotPosX < 36): config.robotPosX = 36
    if (config.robotPosX > 444): config.robotPosX = 444

    if (config.robotPosY < 36): config.robotPosY = 36
    if (config.robotPosY > 444): config.robotPosY = 444