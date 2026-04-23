import config

def cppWrite():
    with open("path.cpp", "a") as file:
        file.write(f"chassis.moveToPose({config.poseData[-1][0]}, {config.poseData[-1][1]}, {config.poseData[-1][2]}, 700);\n")
        file.close()