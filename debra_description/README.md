# Debra description

ROS package containing description files of Debra


# Usage

To view the robot model in rviz, run:
```sh
roslaunch debra_description display.launch
```

To launch the simulation of the robot on the Eurobot table with rviz, run:
```sh
roslaunch debra_description gazebo.launch
```

## Urdf parsing & visualisation tools

You can parse the urdf file by running:
```sh
roscd debra_description/urdf/
check_urdf debra.urdf
```

You can also plot a graph tree of the robot's structure by running:
```sh
roscd debra_description/urdf/
urdf_to_graphiz debra.urdf
```


# Dependencies

This package uses the following ROS packages:
* robot_state_publisher
* urdf
* xacro

If you don't have these packages installed, install them using:
```sh
rosdep install robot_state_publisher urdf xacro
```
