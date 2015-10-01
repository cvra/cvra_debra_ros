cmake_minimum_required(VERSION 2.8.3)
project(debra_description)

find_package(catkin REQUIRED COMPONENTS
  robot_state_publisher
  urdf
  xacro
  roscpp
  sensor_msgs
  nav_msgs
  tf
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

install(DIRECTORY launch/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
  PATTERN ".svn" EXCLUDE
)
