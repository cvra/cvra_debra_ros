cmake_minimum_required(VERSION 2.8.3)
project(molly_base_motion_planner)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  cvra_msgs
)

catkin_package(CATKIN_DEPENDS message_runtime)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(
  PROGRAMS scripts/get_base_trajectory_client.py
           scripts/get_base_trajectory_server.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
