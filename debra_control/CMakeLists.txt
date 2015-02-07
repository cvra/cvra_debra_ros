cmake_minimum_required(VERSION 2.8.3)
project(debra_control)

find_package(catkin REQUIRED COMPONENTS
  controller_manager
  geometry_msgs
  joy
#  ros_control
#  ros_controllers
  sensor_msgs
  std_msgs
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)
