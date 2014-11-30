debra_description
=================

ROS package containing description files of Debra


Usage
-----

To view the robot model in rviz, run one of the following:
```sh
roslaunch debra_description debra_display.launch
roslaunch debra_description debra_rviz.launch
```

Dependencies
------------

This package uses the following ROS packages:
* robot_state_publisher
* urdf
* xacro

If you don't have these packages installed, install them using:
```sh
rosdep install robot_state_publisher
rosdep install urdf
rosdep install xacro
```
