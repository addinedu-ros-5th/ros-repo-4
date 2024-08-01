cmake_minimum_required(VERSION 3.5)
project(main_server_gui)

# Find dependencies
find_package(task_manager REQUIRED)
find_package(ament_cmake REQUIRED)
find_package(network_manager REQUIRED)    # new
find_package(robot_state REQUIRED)        # new
find_package(rclpy REQUIRED)              # new
find_package(std_msgs REQUIRED)           # new
find_package(geometry_msgs REQUIRED)      # new

# Install UI files
install(
  DIRECTORY ui map
  DESTINATION share/${PROJECT_NAME}
)

# Install Python scripts
install(
  PROGRAMS src/main_server_gui.py
  PROGRAMS ../network_manager/src/communication_robot_node.py  # new
  PROGRAMS ../network_manager/src/communication_MFC_arduino.py # new
  DESTINATION lib/${PROJECT_NAME}
  PERMISSIONS OWNER_EXECUTE OWNER_WRITE OWNER_READ
              GROUP_EXECUTE GROUP_READ
              WORLD_EXECUTE WORLD_READ
)

# Install Python modules
install(
  DIRECTORY src/modules
  DESTINATION lib/${PROJECT_NAME}
  FILES_MATCHING PATTERN "*.py"
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
