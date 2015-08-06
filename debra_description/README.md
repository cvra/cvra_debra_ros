Debra description
=================
ROS package containing description files of Debra


Usage
-----
To view the robot model in rviz, run one of the following:
```sh
roslaunch debra_description debra_display.launch
roslaunch debra_description debra_rviz.launch
```

### Updating the model
When changing the model of Debra,
you can regenerate the urdf file from the xacro file by running:
```sh
rosrun xacro xacro --inorder debra.xacro > debra.urdf
```
Make sure you are in the correct tree `debra_descriptìon/urdf`

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
root Link: base_footprint has 1 child(ren)
    child(1):  base_link
        child(1):  base_link_left_wheel
        child(2):  base_link_right_wheel
        child(3):  body
            child(1):  left_arm_slider
                child(1):  left_arm_arm
                    child(1):  left_arm_forearm
            child(2):  right_arm_slider
                child(1):  right_arm_arm
                    child(1):  right_arm_forearm
            child(3):  hokuyo_link
```

You can also plot a graph tree of the robot's structure by running:
```sh
roscd debra_description/urdf/
urdf_to_graphiz debra.urdf
```
Or simply look at the [output](urdf/debra.pdf)

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
