import os, sys

import config
import relativity

def getPath():
    if getattr(sys, "frozen", False):
        base = os.path.expanduser("~")
        outDirectory = os.path.join(base, "bubonicOutput")
    else:
        outDirectory = os.path.dirname(os.path.abspath(__file__))

    os.makedirs(outDirectory, exist_ok=True)
    return os.path.join(outDirectory, "path.cpp")

def cppWrite():
    # Recalculate relative coordinates based on latest poseData
    relativity.relativity()

    with open(getPath(), "a") as file:
        file.write(f"chassis.moveToPose({config.relativeX}, {config.relativeY}, {config.relativeT}, 700);\n")