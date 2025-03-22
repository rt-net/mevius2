cmake_minimum_required(VERSION 2.8.3)

project(mevius2)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  std_msgs
)

add_message_files(
  FILES
  Mevius2Log.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package()

