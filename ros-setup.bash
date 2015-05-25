#!/bin/bash

# Install ROS
echo "Installing ROS..."
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu trusty main" > /etc/apt/sources.list.d/ros-latest.list'
wget https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -O - | sudo apt-key add -
sudo aptitude update
sudo aptitude install -y ros-jade-desktop-full

# If using elementary OS uncomment the following two lines or if using another distro, replace according to this structure: export ROS_OS_OVERRIDE="DISTRIB_ID:DISTRIB_RELEASE:DISTRIB_CODENAME"
# export ROS_OS_OVERRIDE="elementary OS:0.3:freya" >> ~/.bashrc
# bash

# Setup ROS
echo "Setting up ROS..."
sudo rosdep init
rosdep update
echo "source /opt/ros/jade/setup.bash" >> ~/.bashrc
source ~/.bashrc
sudo aptitude install -y python-rosinstall

# Install missing ROS packages
echo "Installing some missing ROS packages..."
sudo aptitude install -y ros-jade-ros-control ros-jade-ros-controllers ros-jade-joystick-drivers ros-jade-robot-state-publisher

# Install Gazebo
# echo "Installing and setting up Gazebo..."
# sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu trusty main" > /etc/apt/sources.list.d/gazebo-latest.list'
# wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
# sudo aptitude update
# sudo aptitude install -y ros-jade-gazebo-ros-pkgs ros-jade-gazebo-ros-control gazebo2 libsdformat1 ros-jade-gazebo-plugins ros-jade-gazebo-ros

# Setup ROS dependencies
echo "Setting up ROS dependencies..."
bash
rosdep install robot_state_publisher urdf xacro controller_manager geometry_msgs joy ros_control ros_controllers sensor_msgs std_msgs #gazebo_msgs gazebo_plugins gazebo_ros gazebo_ros_control joy

echo "Finishing... Done."
