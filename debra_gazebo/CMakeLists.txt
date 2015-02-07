cmake_minimum_required(VERSION 2.8.3)
project(debra_gazebo)

find_package(catkin REQUIRED COMPONENTS
  debra_description
  gazebo_msgs
  gazebo_plugins
  gazebo_ros
  gazebo_ros_control
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)
