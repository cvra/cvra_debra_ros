debra_control
=============

ROS package that handles the control of Debra


Usage
-----

### Gui control through `rqt`

For this part you will need rqt packages, please refer to the dependencies
section if you need to install them.

Run:
```sh
roslaunch debra_control debra_gazebo.launch
rqt
```

You should now be able to control the robot's linear and angular velocity
using the rqt gui.


### Keyboard control

Run:
```sh
roslaunch debra_control debra_gazebo.launch
rosrun debra_control key_teleop.py
```

You should now be able to control the robot's linear and angular velocity
using your keyboard. The keymap used is:
```
H:       Print this menu
Moving around:
  Q   W   E
  A   S   D
  Z   X   Z
T/B :   increase/decrease max speeds 10%
Y/N :   increase/decrease only linear speed 10%
U/M :   increase/decrease only angular speed 10%
anything else : stop

G :   Quit
```

Dependencies
------------

This package uses the following ROS packages:
* controller_manager
* geometry_msgs
* joy
* ros_control
* ros_controllers
* sensor_msgs
* std_msgs

If you don't have these packages installed, install them using:
```sh
rosdep install controller_manager geometry_msgs joy ros_control ros_controllers sensor_msgs std_msgs
```

For `rqt` usage, you will also need `rqt` packages that you can install with:
```sh
sudo apt-get install ros-indigo-rqt ros-indigo-rqt-common-plugins ros-indigo-rqt-robot-plugins
```


To do
-----

Fix `catkin_make` problem with `ros_control` & `ros_controllers` dependencies.
