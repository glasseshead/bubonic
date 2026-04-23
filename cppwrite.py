import config

def cppWrite():
    # if pose data is empty just don't write anything
    if not config.poseData:
        return

    with open("path.cpp", "a") as file:
        file.write(f"chassis.moveToPose({config.relativeX}, {config.relativeY}, {config.relativeT}, 700);\n")