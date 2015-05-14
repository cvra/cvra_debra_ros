cmake_minimum_required(VERSION 2.8.3)
project(cvra_operations)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  cvra_msgs
  master_bridge
  molly_base_motion_planner
  sick_tim
  webcam_stream
)

catkin_package(CATKIN_DEPENDS message_runtime)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

install(DIRECTORY launch/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
  PATTERN ".svn" EXCLUDE
)
