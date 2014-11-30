cmake_minimum_required(VERSION 2.8.3)
project(debra_description)

find_package(catkin REQUIRED COMPONENTS
  robot_state_publisher
  urdf
  xacro
)

###################################
## catkin specific configuration ##
###################################

catkin_package()

###########
## Build ##
###########

include_directories(
  ${catkin_INCLUDE_DIRS}
)
