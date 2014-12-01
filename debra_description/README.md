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

### Urdf parsing & visualisation tools

You can parse the urdf file by running:
```sh
roscd debra_description/urdf/
check_urdf debra.urdf
```

And it should return something like this:
```sh
 robot name is: debra
 ---------- Successfully Parsed XML ---------------
 root Link: base_link has 4 child(ren)
     child(1):  b_l_wheel
     child(2):  b_r_wheel
     child(3):  f_l_wheel
     child(4):  f_r_wheel
```

You can also plot a graph tree of the robot's structure by running:
```sh
roscd debra_description/urdf/
urdf_to_graphiz debra.urdf
```

Dependencies
------------

This package uses the following ROS packages:
* robot_state_publisher
* urdf
* xacro

If you don't have these packages installed, install them using:
```sh
rosdep install robot_state_publisher urdf xacro
```

To do
-----

Fix issue #1: `rviz` fails to show the robot correctly when `roscore` is
running in parallel
