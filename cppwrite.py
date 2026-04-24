import config
import relativity

def cppWrite():
    # if pose data is empty just don't write anything
    if not config.poseData:
        return

    # Recalculate relative coordinates based on latest poseData
    relativity.relativity()

    with open("path.cpp", "a") as file:
        file.write(f"chassis.moveToPose({config.relativeX}, {config.relativeY}, {config.relativeT}, 700);\n")

        '''
        if config.robotPosTheta % 180 != 0:
            file.write(f"chassis.moveToPose({config.relativeX}, {config.relativeY}, {config.relativeT}, 700);\n")
        if config.robotPosTheta % 180 == 0:
            file.write(f"chassis.moveToPose({config.relativeY}, {config.relativeX}, {config.relativeT}, 700);\n")
        '''