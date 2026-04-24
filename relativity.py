import config

def relativity():
    if len(config.poseData) == 1 or config.resetOrigin == True:
        config.originX, config.originY, config.originT = config.poseData[-1]
        # First point is the origin, so relative coordinates are (0, 0, 0)
        config.relativeX = 0
        config.relativeY = 0
        config.relativeT = 0
        config.resetOrigin = False
    else:
        x, y, t = config.poseData[-1]
        # Divide by inPerTick to convert pixels to inches, then subtract origin
        config.relativeX = (x - config.originX) / config.inPerTick
        config.relativeY = (y - config.originY) / config.inPerTick
        config.relativeT = t - config.originT