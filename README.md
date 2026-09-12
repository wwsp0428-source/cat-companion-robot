# Cat Companion Robot

A ROS 2 based autonomous mobile robot designed to locate, approach, and safely interact with a cat.

The project is being developed as a practical robotics platform for learning and integrating mobile robot navigation, perception, control, SLAM, and human/pet-robot interaction.

## Project Goals

The final robot is expected to:

- Detect and track a cat using an onboard camera
- Navigate autonomously in an indoor environment
- Avoid obstacles in real time
- Build and use a map of the environment
- Approach a cat while maintaining a safe distance
- Perform simple interactive behaviours
- Return to a safe state when the cat is lost or the battery is low

## System Architecture

```text
Camera
  |
  v
Cat Detection
  |
  v
Behavior Controller
  |
  v
/cmd_vel
  |
  v
Base Controller
  |
  v
Differential Drive Motors


LiDAR --------> SLAM / Localization
                    |
                    v
                  Nav2
                    |
                    v
               Path Planning


Wheel Encoders + IMU
        |
        v
     Odometry
