cmake_minimum_required(VERSION 2.8.3)
project(summit_xls_ur5_description)

find_package(catkin REQUIRED COMPONENTS
  roslaunch
  urdf 
  xacro
  robotnik_sensors
  summit_xl_description
  ur_description
)

catkin_package(
  CATKIN_DEPENDS urdf xacro
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

install(
  DIRECTORY launch robots
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

