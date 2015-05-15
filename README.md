roscvra
=======
ROS stack of nodes that run on our robots

Setup
-----
It is assumed you have not installed ROS and configured your ROS workspace yet.
To setup ROS and everything, simply run:
```bash
bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
git clone https://github.com/cvra/roscvra.git
chmod +x setup.bash
sudo ./setup.bash
cd ..
catkin_make
source devel/setup.bash
```

Remember to run these last two lines everything you tweak or change something in the package as they will build the package and ensure ROS commands detect newly installed packages.

Operations
----------
To launch the ROS stack on Debra (similarly for Caprica, use `caprica.launch` instead), do the following:
```bash
cd ~/catkin_ws
catkin_make
roslaunch cvra_operations debra.launch
```
This will rebuild all the packages in the stack, then it will launch each of the nodes:
- the **master bridge publisher** which relays odometry data from the master board
- the **molly base motion planner server** to which trajectories for the differential base can be requested
- the **sick tim561 launcher** which publishes measurements from the lidar in a LaserScan topic
- the **raw stream launcher** which publishes raw video footage from the onboard camera

Packages
--------
Here is a list of the packages contained in this repository that are actively used/supported:
- **cvra_msgs**: which includes all our custome message structures
- **master_bridge**: acts as a bridge between the master board and the PC that runs ROS using the simpleRPC interface
- **molly_base_motion_planner**: ROS bindings to molly
- **sick_tim**: driver and parser for the measurements coming from the laser range finder sensor, we use a Sick Tim561 on our robot
- **webcam_stream**: allows you to stream raw video footage from a standard USB webcam, we use a Logitech C310 webcam on our robot

Dependencies
------------
You will need
- [simplerpc](https://github.com/cvra/simplerpc)
- [serial-datagram](https://github.com/cvra/serial-datagram)
- [molly-the-motion-planner](https://github.com/cvra/molly-the-motion-planner)
(to be able to use them along with python 3, you may want to install them using pip3.
