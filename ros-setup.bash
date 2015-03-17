#!/bin/bash

# Install ROS
echo "Installing ROS..."
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu trusty main" > /etc/apt/sources.list.d/ros-latest.list'
wget https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -O - | sudo apt-key add -
sudo apt-get update
sudo apt-get install -y ros-indigo-desktop-full

# Setup ROS
echo "Setting up ROS..."
sudo rosdep init
rosdep update
echo "source /opt/ros/indigo/setup.bash" >> ~/.bashrc
source ~/.bashrc
sudo apt-get install -y python-rosinstall

# Install missing ROS packages
echo "Installing some missing ROS packages..."
sudo apt-get install -y ros-indigo-ros-control ros-indigo-ros-controllers ros-indigo-joystick-drivers ros-indigo-robot-state-publisher

# Install Gazebo
echo "Installing and setting up Gazebo..."
sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-latest.list'
wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
sudo apt-get update
sudo apt-get install -y ros-indigo-gazebo-ros-pkgs ros-indigo-gazebo-ros-control gazebo2 libsdformat1 ros-indigo-gazebo-plugins ros-indigo-gazebo-ros

# Setup ROS dependencies
echo "Setting up ROS dependencies..."
rosdep install robot_state_publisher urdf xacro controller_manager geometry_msgs joy ros_control ros_controllers sensor_msgs std_msgs gazebo_msgs gazebo_plugins gazebo_ros gazebo_ros_control joy

echo "Finishing... Done."
