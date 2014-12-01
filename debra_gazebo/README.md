debra_gazebo
============

ROS package that handles the gazebo interactions with Debra model


Usage
-----

To use this package, you can run:
```sh
roslaunch debra_gazebo debra_gazebo.launch
```

It should launch gazebo and display a mode of the robot that you can control
using the gui controller. Or you can use the package *debra_control*.


Dependencies
------------

This package uses the following ROS packages:
* debra_description
* gazebo_msgs
* gazebo_plugins
* gazebo_ros
* gazebo_ros_control

If you don't have these packages installed, install them using:
```sh
rosdep install debra_description gazebo_msgs gazebo_plugins gazebo_ros gazebo_ros_control
```
