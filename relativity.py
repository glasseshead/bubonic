import config

def relativity():
    '''
    if len(config.poseData) == 1:
        config.originX, config.originY, config.originT = config.poseData[0]
        x, y, t = config.poseData[-1]
    else:
        # if has multiple objects, relative values at whatever origin you have set
        config.relativeX = x - config.originX
        config.relativeY = y - config.originY
        config.relativeT = t - config.originT
    '''

    if len(config.poseData) == 1:
        config.originX, config.originY, config.originT = config.poseData[0]
    else:
        x, y, t = config.poseData[-1]
        config.relativeX = x - config.originX
        config.relativeY = y - config.originY
        config.relativeT = t - config.originT