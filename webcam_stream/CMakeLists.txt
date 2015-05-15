cmake_minimum_required(VERSION 2.8.3)
project(webcam_stream)

find_package(catkin REQUIRED COMPONENTS
  sensor_msgs
  cv_bridge
  rospy
  std_msgs
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

install(DIRECTORY launch/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
  PATTERN ".svn" EXCLUDE
)
