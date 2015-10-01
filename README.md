# ROSCVRA

ROS stack of nodes that run on our robots

# Setup

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


# Build

When updating nodes, you need to rebuild the packages:
```bash
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```


# Simulation

To launch the robot model in simulation run:
```bash
roslaunch debra_description gazebo.launch
```


# Operations

To launch the ROS stack on Debra (similarly for Caprica, use `caprica.launch` instead), do the following:
```bash
roslaunch cvra_operations debra.launch
```


# Packages

Here is a list of the packages contained in this repository that are actively used/supported:

- **debra_description**: URDF model of debra, also handles the simulation for now
- **master_bridge**: acts as a bridge between the master board and the PC that runs ROS using the simpleRPC interface
- **sick_tim**: driver and parser for the measurements coming from the laser range finder sensor, we use a Sick Tim561 on our robot


# Dependencies

You will need
- [simplerpc](https://github.com/cvra/simplerpc)
(to be able to use them along with python 3, you may want to install them using pip3.
