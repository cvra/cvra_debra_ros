#!/bin/bash

# Create ROS Workspace
echo "Setting up a catkin workspace..."
mkdir -p ~/catkin_ws/src
sudo chown -R $USER catkin_ws/ # Transfer ownership to current user
cd ~/catkin_ws/src
catkin_init_workspace
cd ~/catkin_ws/
catkin_make
source devel/setup.bash

# Get CVRA ROS stack
echo "Installing CVRA ROS stack..."
cd ~/catkin_ws/src
git clone https://github.com/cvra/roscvra.git roscvra
cd ~/catkin_ws
catkin_make
source devel/setup.bash
cd ~/

echo "Finishing... Done."
