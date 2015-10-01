# Debra description

ROS package containing description files of Debra


# Usage

## Rviz

To view the robot model in rviz, run:
```sh
roslaunch debra_description display.launch
```

## Gazebo

To launch the simulation of the robot on the Eurobot table with rviz, run:
```sh
roslaunch debra_description gazebo.launch
```

To place the robot at runtime, you can run the following command:
```sh
rosrun debra_description set_robot_pose debra x y heading
```
Don't forget to replace x, y and heading by the values you want (floating point).

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


# ROS Jade

When running the simulation on ROS Jade, you'll need to install Gazebo 5 as the gazebo_ros packages depend on the dev branch of the simulator:
```sh
apt-get install libgazebo5-dev
```
