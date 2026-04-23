import config

def cppWrite():
    # open file
    with open("path.cpp", "a") as file:
        # write data
        file.write(f"chassis.moveToPose({config.poseData[-1][0]}, {config.poseData[-1][1]}, {config.poseData[-1][2]}, 700);\n")
        
        # save changes
        file.close()