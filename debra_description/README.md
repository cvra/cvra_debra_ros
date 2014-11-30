debra_description
=================

ROS package containing description files of Debra


Usage
-----

To view the robot model in rviz, run:
```sh
roslaunch urdf_tutorial display.launch model:=debra_description/urdf/debra.urdf
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
