# Autonomous Robot

![Lines of code](https://img.shields.io/tokei/lines/github/baduc1602/autonomous_robot)


Thanks to turtlebot3 with a huge and helpful library for me to use and in this project I implement the "WAFFLE_PI" model to practice SLAM and NAVIGATION. 

You can see how it works in this [links](https://drive.google.com/file/d/1yCYEjcg8byPkdRy354mxskaTIsZJ0wm7/view?usp=sharing).

## Walkthrough
Here's a walkthrough of implemented robot features:

<img src='demo.gif' title='Demo project final result'> <br>

## Installation

- Use Ubuntu 18.04 Melodic version. You can install it through [ROS](http://wiki.ros.org/melodic/Installation/Ubuntu) 
- Install some libraries which need for display and run. Using terminal:
```bash
$ sudo apt-get install ros-melodic-slam-gmapping
$ sudo apt-get install ros-meldoic-move-base
$ sudo apt-get install ros-melodic-teleop-twist-keyboard
$ sudo apt-get install ros-melodic-navigation
$ sudo apt-get install joint-state-publisher
$ sudo apt-get install rivz
$ sudo apt-get install ros-melodic turtlebot3
```
- Use the command line below to export "WAFFLE_PI" model through this project

```bash
echo "export TURTLEBOT3_MODEL="waffle_pi"">> ~/.bashrc
```
 #### For catkin_workspace: 
```bash
- mkdir -p ~/catkin_ws/src
- cd ~/catkin_ws && catkin_make
- git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
```

## Useage

I have four launch files here, each file contains some nodes to implement the different features.

- **f1_Robot.launch**: to implement the WAFFLE_PI model for the empty world and also display on Rviz. Besides, you can use the keyboard to control the robot. 
- **f2_SLAM.launch**: Inherit all features of **f1_Robot.launch** and it has the adding function, to track the map of the world I have created on Gazebo.
- **f3_Localization.launch**: Inherit all features of **f2_SLAM.launch** and this file aims to load map and detect the location of the robot through the AMCL algorithm.
- **f4_PathPlanning.launch**: Inherit all features of **f3_Localization** 

## License 
This is a project from Udemy course.Give a big thanks to **Muhammad Luqman** and his useful course. 
