cmake_minimum_required(VERSION 2.8.3)
project(robot_odometry)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  cvra_msgs
  message_generation
)

catkin_package(CATKIN_DEPENDS message_runtime)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
