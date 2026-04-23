import config

def bounds():
    # if within a current boundary set robot position in that boundary
    if ((80 <= config.mouseXraw <= 320) and (40 <= config.mouseYraw <= 280)):
        config.robotPosX, config.robotPosY = config.mouseXraw - 80, config.mouseYraw - 40

    # set bounds for robot to fallback to
    if (config.robotPosX < 18): config.robotPosX = 18
    if (config.robotPosX > 222): config.robotPosX = 222

    if (config.robotPosY < 18): config.robotPosY = 18
    if (config.robotPosY > 222): config.robotPosY = 222