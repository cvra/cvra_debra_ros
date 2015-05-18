cmake_minimum_required(VERSION 2.8.3)
project(beacons_interface)

find_package(catkin REQUIRED COMPONENTS
  cvra_msgs
  roscpp
  rospy
  std_msgs
)

catkin_package(CATKIN_DEPENDS message_runtime)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(
  PROGRAMS scripts/ennemy_position_publisher.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
  PATTERN ".svn" EXCLUDE
)
