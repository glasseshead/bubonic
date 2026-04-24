# Bubonic by glasseshead (David Sun)
A solo-programmed VEX V5 program made with Python for Autonomous programming using a digital plottable field.
Made for use with Arson, Yaay! architectures and Plague? Where? by David

Thanks Zachary from 5776K; Kabir from 5776A; Jerry from CMAA

<img src="img/bubo_code.png" height="300">
<img src="img/bubo_path1.png" height="300">
<img src="img/bubo_path2.png" height="300">

## Features
- **Path and pose visualizer**
  - By plotting points, a line will appear tracing the path your robot theoretically takes

- **Field path plotting**  
  - Real time interactive path plotting using a Python-powered interface

- **Visual rendering**  
  - VEX V5 blank field rendered in high quality supporting:
    - Robot
      - Robot theta indicator
   - Field Perimeter
    - Checkerboarded tiles
    - Path rendering
      - Lines from point to point in red
      - Currently drawing line in cyan

- **Automated autonomous code programming**
  - Bubonic is capable of automatically writing autonomous code for PROS and LemLib

- **Rotational control**
  - Capability to rotate in 1 degree increments/decrements
  - Capability to rotate in 90 degree increments/decrements

- **High-frequency enhanced telemetry**
  - Optimized for low flicker and high refresh rate
  - Integrated telemetry in program
  - Non-terminal, graphical

- **Pose zeroing support**
  - Capability to zero the current pose and writing zeroing data to file

- **Data clearing support**
  - Capability to clear all contents of pose data and code

- **Arson, Yaay! and Plague? Where? compatability**
  - Designed to be compatible with Arson- and Plague-based structures and can be modifiable for other architectures

## Controls
- Add point = Left Mouse Click
- Rotate robot pose by 1° = A/D
- Rotate robot pose by 90° = Shift + A/D
- Reset origin/zero pose = E
- Zero current heading = S
- Clear pose data = Z
- Clear code poses = Q

## Notes
- inPerTick is already set, do not change it at all
- May require pygame dependencies